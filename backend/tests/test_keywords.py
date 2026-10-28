from app.services.keywords import extract_keywords

def test_extract_keywords_single_text():
    text = "The ancient cathedral and historic museum offered spectacular architectural views."
    keywords = extract_keywords(text, top_n=5)
    assert isinstance(keywords, list)
    assert len(keywords) > 0
    first = keywords[0]
    assert "keyword" in first
    assert "score" in first
    assert isinstance(first["score"], float)

def test_extract_keywords_multi_text():
    texts = [
        "Kyoto temples and peaceful traditional gardens.",
        "Delicious matcha tea and authentic Japanese culinary experience.",
        "Beautiful bamboo grove with scenic walking paths."
    ]
    keywords = extract_keywords(texts, top_n=5)
    assert len(keywords) > 0
