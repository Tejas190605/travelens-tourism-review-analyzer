from typing import List, Dict, Union, Any
from collections import Counter
from sqlalchemy.orm import Session
from sklearn.feature_extraction.text import TfidfVectorizer

from app.ml.preprocessing import preprocess_for_tfidf, tokenize_words
from app.db.models import Review

# Domain stopword blacklist to avoid generic travel filler
GENERIC_STOPWORDS = {
    "hotel", "place", "day", "days", "stay", "stayed", "time", "one", "also", "would",
    "get", "went", "got", "night", "nights", "first", "back", "area", "visit", "trip",
    "thing", "things", "really", "very", "even", "nice", "good", "great", "well", "much",
    "many", "made", "make", "took", "take", "lot", "lots", "way", "found", "find",
    "see", "saw", "sure", "need", "needed", "come", "came", "going", "just", "bit",
    "quite", "little", "definitely", "always", "every", "say", "said", "two", "three",
    "overall", "visiting", "experience", "around", "like", "us", "our", "we", "traveler",
    "travelers", "vacation", "holiday", "destination"
}

def extract_keywords(
    text_or_texts: Union[str, List[str]],
    top_n: int = 8,
    min_word_len: int = 3
) -> List[Dict[str, Any]]:
    """
    Extract top ranked keywords with TF-IDF scores and token frequency from text or collection of texts.
    Returns: [{'keyword': 'architecture', 'score': 0.45, 'frequency': 3}, ...]
    """
    if isinstance(text_or_texts, str):
        texts = [text_or_texts]
    else:
        texts = [t for t in text_or_texts if t and t.strip()]

    if not texts:
        return []

    # Preprocess
    preprocessed_texts = [preprocess_for_tfidf(t) for t in texts]
    preprocessed_texts = [t for t in preprocessed_texts if t.strip()]

    if not preprocessed_texts:
        return []

    # Frequency counter
    all_tokens = []
    for t in preprocessed_texts:
        all_tokens.extend([w for w in t.split() if len(w) >= min_word_len and w not in GENERIC_STOPWORDS])
    freq_counts = Counter(all_tokens)

    try:
        vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            max_features=1000,
            sublinear_tf=True
        )
        tfidf_matrix = vectorizer.fit_transform(preprocessed_texts)
        feature_names = vectorizer.get_feature_names_out()

        # Mean tfidf score across the provided documents
        mean_scores = tfidf_matrix.mean(axis=0).A1
        scored_words = []
        for word, score in zip(feature_names, mean_scores):
            # Check if any constituent token is in generic stopwords
            tokens = word.split()
            if any(t in GENERIC_STOPWORDS for t in tokens):
                continue
            if len(word) >= min_word_len:
                freq = freq_counts.get(word, sum(freq_counts.get(t, 1) for t in tokens))
                scored_words.append({
                    "keyword": word,
                    "score": round(float(score), 4),
                    "frequency": freq
                })

        scored_words.sort(key=lambda x: x["score"], reverse=True)
        return scored_words[:top_n]
    except Exception:
        total = sum(freq_counts.values()) or 1
        return [
            {
                "keyword": word,
                "score": round(count / total, 4),
                "frequency": count
            }
            for word, count in freq_counts.most_common(top_n)
        ]

def extract_review_keywords(text: str, top_n: int = 6) -> List[Dict[str, Any]]:
    """Review-level keyword extraction helper."""
    return extract_keywords(text, top_n=top_n)

def extract_destination_keywords(destination_id: int, db: Session, top_n: int = 10) -> List[Dict[str, Any]]:
    """
    Extracts top empirical keywords across all recorded reviews for a destination in the database.
    """
    reviews = db.query(Review.review_text).filter(Review.destination_id == destination_id).all()
    if not reviews:
        return []

    texts = [r[0] for r in reviews if r[0]]
    return extract_keywords(texts, top_n=top_n)
