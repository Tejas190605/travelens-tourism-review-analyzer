import re
from typing import List

# Essential negation words to preserve for sentiment analysis
NEGATION_WORDS = {
    "not", "no", "never", "none", "neither", "nor", "barely", "hardly", "scarcely",
    "cannot", "without", "rarely"
}

# Standard English stopwords (excluding negations)
STANDARD_STOPWORDS = {
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any",
    "are", "aren", "as", "at", "be", "because", "been", "before", "being", "below",
    "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down",
    "during", "each", "few", "for", "from", "further", "had", "has", "have", "having",
    "he", "her", "here", "hers", "herself", "him", "himself", "his", "how", "i", "if",
    "in", "into", "is", "it", "its", "itself", "just", "me", "more", "most", "my",
    "myself", "of", "off", "on", "once", "only", "or", "other", "our", "ours", "ourselves",
    "out", "over", "own", "s", "same", "she", "should", "so", "some", "such", "t", "than",
    "that", "the", "their", "theirs", "them", "themselves", "then", "there", "these",
    "they", "this", "those", "through", "to", "too", "under", "until", "up", "very",
    "was", "we", "were", "what", "when", "where", "which", "while", "who", "whom",
    "why", "will", "with", "you", "your", "yours", "yourself", "yourselves"
} - NEGATION_WORDS

# Contraction mapping
CONTRACTIONS = {
    r"can\'t": "cannot",
    r"won\'t": "will not",
    r"n\'t": " not",
    r"\'re": " are",
    r"\'s": " is",
    r"\'d": " would",
    r"\'ll": " will",
    r"\'ve": " have",
    r"\'m": " am",
}

# Simple lemmatization rules for common tourism inflections
IRREGULAR_LEMMAS = {
    "went": "go",
    "gone": "go",
    "saw": "see",
    "seen": "see",
    "ate": "eat",
    "eaten": "eat",
    "felt": "feel",
    "took": "take",
    "taken": "take",
    "crowded": "crowd",
    "crowding": "crowd",
    "toured": "tour",
    "touring": "tour",
    "tours": "tour",
    "cleaner": "clean",
    "cleanest": "clean",
    "cleaning": "clean",
    "dirtier": "dirty",
    "dirtiest": "dirty",
    "visited": "visit",
    "visiting": "visit",
    "visits": "visit",
    "walked": "walk",
    "walking": "walk",
    "walks": "walk",
    "stayed": "stay",
    "staying": "stay",
    "stays": "stay",
    "rooms": "room",
    "hotels": "hotel",
    "beaches": "beach",
    "restaurants": "restaurant",
    "cafes": "cafe",
    "prices": "price",
    "taxis": "taxi",
    "buses": "bus",
    "trains": "train",
}

def expand_contractions(text: str) -> str:
    """Expand short-form English contractions."""
    for pattern, replacement in CONTRACTIONS.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text

def clean_text(text: str) -> str:
    """
    Remove HTML tags, URLs, special punctuation while keeping semantic text.
    Preserves alphanumeric characters, essential spaces, and basic sentiment tokens.
    """
    if not text:
        return ""
    # Strip HTML tags
    text = re.sub(r"<[^>]+>", " ", text)
    # Strip URLs
    text = re.sub(r"http\S+|www\.\S+", " ", text)
    # Expand contractions
    text = expand_contractions(text)
    # Lowercase
    text = text.lower()
    # Normalize multiple whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text

def tokenize_sentences(text: str) -> List[str]:
    """
    Split a review into discrete sentences by sentence-ending punctuation or conjunctions.
    Useful for aspect-level sentiment scoping.
    """
    if not text:
        return []
    # Replace common abbreviations that might trigger false splits
    cleaned = re.sub(r"\b(e\.g\.|i\.e\.|mr\.|mrs\.|ms\.|dr\.)\s*", "", text, flags=re.IGNORECASE)
    # Split on punctuation (. ! ?) or strong contrasting conjunctions (but, however, although)
    parts = re.split(r"(?:[.!?;]+|\b(?:but|however|although|whereas|though)\b)", cleaned, flags=re.IGNORECASE)
    sentences = [p.strip() for p in parts if p.strip() and len(p.strip()) > 2]
    return sentences

def simple_lemmatize(token: str) -> str:
    """Lemmatize common plurals and past tenses."""
    if token in IRREGULAR_LEMMAS:
        return IRREGULAR_LEMMAS[token]
    if token.endswith("ies") and len(token) > 4:
        return token[:-3] + "y"
    if token.endswith("es") and len(token) > 4 and token[-3] in ("s", "x", "z", "ch", "sh"):
        return token[:-2]
    if token.endswith("s") and not token.endswith("ss") and len(token) > 3:
        return token[:-1]
    if token.endswith("ing") and len(token) > 5:
        return token[:-3]
    if token.endswith("ed") and len(token) > 4:
        return token[:-2]
    return token

def tokenize_words(text: str) -> List[str]:
    """Extract individual word tokens from text."""
    words = re.findall(r"\b[a-zA-Z]{2,}\b", text.lower())
    return words

def remove_stopwords_and_lemmatize(tokens: List[str]) -> List[str]:
    """Filter non-negation stopwords and lemmatize tokens."""
    processed = []
    for token in tokens:
        if token in STANDARD_STOPWORDS:
            continue
        lemma = simple_lemmatize(token)
        processed.append(lemma)
    return processed

def preprocess_for_tfidf(text: str) -> str:
    """
    Full ASTMA preprocessing pipeline:
    Raw Text -> Clean -> Lowercase -> Word Tokenize -> Stopwords/Lemmatization -> Normalized Text
    """
    cleaned = clean_text(text)
    tokens = tokenize_words(cleaned)
    lemmatized = remove_stopwords_and_lemmatize(tokens)
    return " ".join(lemmatized)
