from app.services.aspects import extract_aspects_from_text

def test_extract_aspects_user_example_1():
    text = "The beach was beautiful but the area was extremely crowded."
    aspects = extract_aspects_from_text(text)
    aspect_dict = {item["aspect"]: item["sentiment"] for item in aspects}

    assert "Attractions" in aspect_dict
    assert aspect_dict["Attractions"] == "positive"

    assert "Crowd" in aspect_dict
    assert aspect_dict["Crowd"] == "negative"

def test_extract_aspects_user_example_2():
    text = "The food was excellent but the hotel room was dirty."
    aspects = extract_aspects_from_text(text)
    aspect_dict = {item["aspect"]: item["sentiment"] for item in aspects}

    assert "Food" in aspect_dict
    assert aspect_dict["Food"] == "positive"

    # Both Cleanliness (dirty) and Accommodation (hotel room) detected negative
    assert "Cleanliness" in aspect_dict or "Accommodation" in aspect_dict
    if "Cleanliness" in aspect_dict:
        assert aspect_dict["Cleanliness"] == "negative"
    if "Accommodation" in aspect_dict:
        assert aspect_dict["Accommodation"] == "negative"

def test_extract_multiple_aspects_food_and_cleanliness():
    text = "The seafood dinner was delicious, but the public restroom was filthy and dirty."
    aspects = extract_aspects_from_text(text)
    aspect_dict = {item["aspect"]: item["sentiment"] for item in aspects}

    assert "Food" in aspect_dict
    assert aspect_dict["Food"] == "positive"

    assert "Cleanliness" in aspect_dict
    assert aspect_dict["Cleanliness"] == "negative"

def test_aspect_negation_handling():
    text = "The hotel room was not clean."
    aspects = extract_aspects_from_text(text)
    aspect_dict = {item["aspect"]: item["sentiment"] for item in aspects}

    assert "Cleanliness" in aspect_dict
    assert aspect_dict["Cleanliness"] == "negative"

def test_aspect_inherent_crowd_serene():
    text = "The garden was serene and quiet."
    aspects = extract_aspects_from_text(text)
    aspect_dict = {item["aspect"]: item["sentiment"] for item in aspects}

    assert "Crowd" in aspect_dict
    assert aspect_dict["Crowd"] == "positive"
