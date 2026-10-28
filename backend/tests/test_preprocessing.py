from app.ml.preprocessing import (
    clean_text,
    tokenize_sentences,
    tokenize_words,
    preprocess_for_tfidf,
    expand_contractions
)

def test_clean_text_removes_html_and_urls():
    raw = "<p>Visit our website at http://example.com! Amazing sights!</p>"
    cleaned = clean_text(raw)
    assert "<p>" not in cleaned
    assert "http" not in cleaned
    assert "amazing sights" in cleaned

def test_expand_contractions():
    raw = "The hotel room wasn't clean and couldn't be locked."
    expanded = expand_contractions(raw)
    assert "not" in expanded
    assert "n't" not in expanded

def test_tokenize_sentences_splits_properly():
    text = "The temple was magnificent. However, the crowd was enormous! We enjoyed the food."
    sentences = tokenize_sentences(text)
    assert len(sentences) >= 3

def test_preprocess_for_tfidf_preserves_negation():
    text = "The room was not clean and very noisy."
    processed = preprocess_for_tfidf(text)
    # Ensure negation 'not' is preserved in token output
    assert "not" in processed
    # Ensure stopword 'was' is removed
    assert "was" not in processed.split()
