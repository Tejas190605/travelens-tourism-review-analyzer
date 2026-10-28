import re
from typing import List, Dict, Any, Set, Optional
from app.ml.preprocessing import tokenize_sentences, clean_text, tokenize_words

# 9 Practical Tourism Aspects Comprehensive Lexicons
ASPECT_LEXICONS = {
    "Attractions": {
        "beach", "beaches", "view", "views", "scenery", "temple", "temples", "church", "cathedral",
        "museum", "museums", "monument", "monuments", "ruin", "ruins", "fortress", "castle",
        "park", "parks", "mountain", "mountains", "hike", "hiking", "panorama", "panoramic",
        "sight", "sights", "sightseeing", "landmark", "landmarks", "exhibit", "exhibits", "waterfall", "waterfalls",
        "landscape", "nature", "tour", "tours", "cliff", "cliffs", "palace", "palaces", "architecture",
        "garden", "gardens", "art", "gallery", "galleries", "lake", "lakes", "cathedrals", "fort", "forts",
        "amber fort", "hawa mahal", "taj mahal", "pyramids", "sphinx", "colosseum", "citadel",
        "heritage", "culture", "cultural", "attraction", "attractions", "wildlife", "safari"
    },
    "Food": {
        "food", "foods", "restaurant", "restaurants", "cafe", "cafes", "dish", "dishes", "cuisine",
        "cuisines", "breakfast", "dinner", "lunch", "coffee", "meal", "meals", "seafood",
        "pasta", "pastry", "pastries", "bakery", "wine", "beer", "dessert", "snack", "snacks",
        "street food", "delicious", "tasting", "drinks", "buffet", "dining", "bar", "bars",
        "cocktail", "cocktails", "eating", "eatery", "eateries", "flavor", "flavors", "tasty",
        "culinary", "delicacy", "delicacies", "spices", "thali"
    },
    "Cleanliness": {
        "clean", "cleanliness", "dirty", "filthy", "spotless", "hygiene", "hygienic", "trash", "garbage",
        "litter", "smell", "odor", "smelling", "tidy", "restroom", "restrooms", "toilet", "toilets",
        "stains", "maintenance", "sanitary", "dust", "pests", "cleaner", "unhygienic", "unwashed", "messy"
    },
    "Price": {
        "price", "prices", "cost", "costs", "expensive", "cheap", "affordable", "overpriced",
        "value", "fee", "fees", "ticket", "tickets", "rip-off", "bargain", "bargains", "scam",
        "scams", "budget", "pricing", "exorbitant", "reasonable", "worth", "costly", "rate", "rates",
        "fare", "fares", "admission", "marked up", "overcharging"
    },
    "Crowd": {
        "crowd", "crowds", "crowded", "queue", "queues", "line", "lines", "packed", "touristy",
        "busy", "overrun", "peaceful", "quiet", "serene", "calm", "waiting time", "jammed",
        "congested", "tranquility", "solitude", "bustling", "congestion"
    },
    "Safety": {
        "safe", "safety", "unsafe", "pickpocket", "pickpockets", "crime", "crimes", "theft",
        "security", "security personnel", "police", "danger", "dangerous", "harassed", "harassment", "guard", "guards",
        "lighting", "secure", "insecure", "scam", "suspicious", "patrol"
    },
    "Transport": {
        "transport", "transportation", "metro", "subway", "bus", "buses", "train", "trains",
        "taxi", "taxis", "cab", "cabs", "transit", "flight", "flights", "airport", "traffic",
        "walkable", "walkability", "walking", "walk", "bicycle", "bike", "commute", "tram", "trams",
        "shuttle", "shuttles", "ferry", "ferries", "roads", "connectivity"
    },
    "Accommodation": {
        "hotel", "hotels", "room", "rooms", "bed", "beds", "hostel", "hostels", "resort",
        "resorts", "stay", "stays", "mattress", "shower", "showers", "bathroom", "bathrooms",
        "air conditioning", "ac", "balcony", "suite", "amenities", "lobby", "lodging", "villa", "villas"
    },
    "Hospitality": {
        "staff", "hospitality", "host", "hosts", "friendly", "unfriendly", "rude", "polite",
        "welcoming", "helpful", "unhelpful", "service", "receptionist", "receptionists", "clerk",
        "waiter", "waiters", "waitress", "manager", "management", "kind", "attitude", "courteous",
        "attentive", "care", "guide", "guides", "tour guide", "tour guides", "locals"
    }
}

POSITIVE_INDICATORS = {
    "beautiful", "amazing", "spotless", "clean", "delicious", "great", "fantastic", "wonderful",
    "reasonable", "safe", "quiet", "peaceful", "excellent", "friendly", "helpful", "comfortable",
    "punctual", "efficient", "fresh", "stunning", "serene", "bargain", "welcoming", "warm",
    "breathtaking", "superb", "exceptional", "polite", "secure", "tidy", "affordable", "good",
    "love", "loved", "enjoyed", "impressed", "worth", "best", "tasty", "courteous", "attentive",
    "extraordinary", "fabulous", "remarkable", "majestic", "spectacular", "magnificent", "delightful",
    "unforgettable", "charming", "flawless", "brilliant", "splendid", "gem", "impressive",
    "scenic", "authentic", "stellar", "top-notch", "memorable", "pleasant", "lovely"
}

NEGATIVE_INDICATORS = {
    "dirty", "filthy", "terrible", "crowded", "packed", "expensive", "overpriced", "rude",
    "awful", "unsafe", "delayed", "noisy", "broken", "poor", "bad", "chaotic", "scam",
    "nightmare", "disgusting", "leak", "foul", "unfriendly", "unhelpful", "unclean", "neglected",
    "overrated", "rip-off", "litter", "garbage", "trash", "exorbitant", "slow", "horrible",
    "hostile", "disrespectful", "cramped", "smelly", "loud", "uncomfortable", "stuffy",
    "marked up", "pushy", "harassed", "disappointing", "disappointed", "bland", "stale",
    "lacked", "lack", "lacking"
}

NEGATIONS = {"not", "never", "no", "hardly", "barely", "scarcely", "cannot"}

def extract_aspects_from_text(text: str) -> List[Dict[str, Any]]:
    """
    Sentence-level and clause-level extraction of 9 tourism aspects and aspect-level polarity.
    Supports multiple aspects per review and contrasting clauses.
    """
    if not text:
        return []

    sentences = tokenize_sentences(text)
    aspect_results: Dict[str, Dict[str, Any]] = {}

    for sentence in sentences:
        s_clean = clean_text(sentence)
        words = tokenize_words(s_clean)
        s_lower = sentence.lower()

        # Check which aspects are mentioned in this sentence
        detected_in_sentence: Set[str] = set()
        matched_keywords: Dict[str, List[str]] = {}

        for aspect_name, keywords in ASPECT_LEXICONS.items():
            for kw in keywords:
                if re.search(r"\b" + re.escape(kw) + r"\b", s_lower):
                    detected_in_sentence.add(aspect_name)
                    matched_keywords.setdefault(aspect_name, []).append(kw)

        if not detected_in_sentence:
            continue

        # Evaluate token-level polarity with local negation scope (window of 3 preceding words)
        pos_indices = set()
        neg_indices = set()
        for idx, w in enumerate(words):
            # Check if this token is negated
            is_negated = any(words[j] in NEGATIONS for j in range(max(0, idx - 3), idx))
            if w in POSITIVE_INDICATORS:
                if is_negated:
                    neg_indices.add(idx)
                else:
                    pos_indices.add(idx)
            elif w in NEGATIVE_INDICATORS:
                if is_negated:
                    pos_indices.add(idx)
                else:
                    neg_indices.add(idx)

        pos_count = len(pos_indices)
        neg_count = len(neg_indices)

        for aspect in detected_in_sentence:
            local_pos = pos_count
            local_neg = neg_count

            # Aspect-specific inherent cues with negation awareness
            pos_cues = []
            neg_cues = []
            if aspect == "Hospitality":
                pos_cues = ["extraordinary hospitality", "hospitality", "welcoming", "friendly", "attentive", "courteous", "kind", "helpful"]
                neg_cues = ["rude", "unfriendly", "hostile", "unhelpful", "disrespectful"]
            elif aspect == "Attractions":
                pos_cues = ["fabulous", "breathtaking", "magnificent", "majestic", "remarkable", "stunning", "spectacular", "splendid"]
                neg_cues = ["disappointing", "overrated", "underwhelming", "boring"]
            elif aspect == "Safety":
                pos_cues = ["safe", "security personnel", "secure", "patrol"]
                neg_cues = ["unsafe", "pickpocket", "crime", "harassed", "danger"]
            elif aspect == "Food":
                pos_cues = ["delicious", "tasty", "authentic", "flavorful", "delight"]
                neg_cues = ["bland", "stale", "tasteless", "awful food"]
            elif aspect == "Crowd":
                pos_cues = ["quiet", "peaceful", "serene", "calm"]
                neg_cues = ["crowded", "packed", "chaotic", "queue", "busy"]
            elif aspect == "Cleanliness":
                pos_cues = ["clean", "spotless", "tidy", "hygiene"]
                neg_cues = ["dirty", "filthy", "trash", "garbage", "litter", "odor", "lacked basic cleanliness", "lacked cleanliness", "unclean"]
            elif aspect == "Price":
                pos_cues = ["cheap", "affordable", "reasonable", "bargain"]
                neg_cues = ["expensive", "overpriced", "exorbitant", "rip-off", "scam", "marked up"]

            for cue in pos_cues:
                m = re.search(r"\b" + re.escape(cue) + r"\b", s_lower)
                if m:
                    prefix = s_lower[max(0, m.start() - 25):m.start()]
                    if any(re.search(r"\b" + re.escape(neg) + r"\b", prefix) for neg in NEGATIONS):
                        local_neg += 2
                    else:
                        local_pos += 2
            for cue in neg_cues:
                m = re.search(r"\b" + re.escape(cue) + r"\b", s_lower)
                if m:
                    prefix = s_lower[max(0, m.start() - 25):m.start()]
                    if any(re.search(r"\b" + re.escape(neg) + r"\b", prefix) for neg in NEGATIONS):
                        local_pos += 2
                    else:
                        local_neg += 2

            if local_pos > local_neg:
                sentiment = "positive"
                score = 1.0
            elif local_neg > local_pos:
                sentiment = "negative"
                score = -1.0
            else:
                sentiment = "neutral"
                score = 0.0

            if aspect not in aspect_results:
                aspect_results[aspect] = {
                    "aspect": aspect,
                    "sentiment": sentiment,
                    "score": score,
                    "keywords": matched_keywords.get(aspect, []),
                    "occurrences": 1
                }
            else:
                existing = aspect_results[aspect]
                existing["score"] = (existing["score"] * existing["occurrences"] + score) / (existing["occurrences"] + 1)
                existing["occurrences"] += 1
                existing["keywords"] = list(set(existing["keywords"] + matched_keywords.get(aspect, [])))
                if existing["score"] > 0.2:
                    existing["sentiment"] = "positive"
                elif existing["score"] < -0.2:
                    existing["sentiment"] = "negative"
                else:
                    existing["sentiment"] = "neutral"

    output = []
    for asp_data in aspect_results.values():
        output.append({
            "aspect": asp_data["aspect"],
            "sentiment": asp_data["sentiment"],
            "score": round(asp_data["score"], 2),
            "keywords": asp_data["keywords"]
        })

    return output

def extract_clause_analysis(text: str) -> List[Dict[str, Any]]:
    """
    Decomposes review text into syntactic clauses (splitting on contrasting conjunctions
    like 'but', 'however', 'although', 'while', semicolons and period delimiters)
    to provide clause-level explanation with detected aspects and polarity.
    """
    if not text:
        return []

    # Split into clauses by sentence and contrasting conjunctions
    raw_clauses = re.split(r"(?<=[.!?])\s+|;\s*|,\s*(?=(?:but|however|although|though|yet|while|nevertheless)\b)|\b(?:but|however|although|though|yet|while|nevertheless)\b", text, flags=re.IGNORECASE)
    clauses = [c.strip() for c in raw_clauses if c and len(c.strip()) > 3]

    results = []
    for clause in clauses:
        c_clean = clean_text(clause)
        words = tokenize_words(c_clean)
        c_lower = clause.lower()

        # Aspects in this clause
        clause_aspects = []
        for aspect_name, keywords in ASPECT_LEXICONS.items():
            for kw in keywords:
                if re.search(r"\b" + re.escape(kw) + r"\b", c_lower):
                    if aspect_name not in clause_aspects:
                        clause_aspects.append(aspect_name)
                    break

        # Token-level polarity with local negation window (preceding 3 words)
        pos_indices = set()
        neg_indices = set()
        for idx, w in enumerate(words):
            is_negated = any(words[j] in NEGATIONS for j in range(max(0, idx - 3), idx))
            if w in POSITIVE_INDICATORS:
                if is_negated:
                    neg_indices.add(idx)
                else:
                    pos_indices.add(idx)
            elif w in NEGATIVE_INDICATORS:
                if is_negated:
                    pos_indices.add(idx)
                else:
                    neg_indices.add(idx)

        pos_count = len(pos_indices)
        neg_count = len(neg_indices)

        # Contextual crowd, cleanliness, price modifiers
        if any(w in c_lower for w in ["crowded", "packed", "chaotic", "queue", "expensive", "overpriced", "dirty", "filthy", "exorbitant", "harassed"]):
            neg_count += 2
        if any(w in c_lower for w in ["stunning", "breath away", "spotless", "peaceful", "delicious", "majestic", "affordable", "cheap"]):
            pos_count += 2

        if pos_count > neg_count:
            clause_sent = "positive"
            polarity_score = 1.0
        elif neg_count > pos_count:
            clause_sent = "negative"
            polarity_score = -1.0
        else:
            clause_sent = "neutral"
            polarity_score = 0.0

        results.append({
            "clause_text": clause,
            "sentiment": clause_sent,
            "aspects": clause_aspects,
            "polarity_score": polarity_score
        })

    return results

def detect_is_mixed(text: str, rating: Optional[int] = None, predicted_sentiment: Optional[str] = None) -> bool:
    """
    Evaluates whether a review contains mixed sentiment.
    Returns True if:
    1. Rating is 3 stars, OR
    2. Rating sentiment differs strongly from text model prediction (e.g. 5-star rating with negative text), OR
    3. Clauses or detected aspects contain both positive and negative polarities.
    """
    if rating == 3:
        return True

    if rating is not None and predicted_sentiment is not None:
        if rating >= 4 and predicted_sentiment == "negative":
            return True
        if rating <= 2 and predicted_sentiment == "positive":
            return True

    aspects = extract_aspects_from_text(text)
    sentiments = {asp["sentiment"] for asp in aspects}
    if "positive" in sentiments and "negative" in sentiments:
        return True

    clauses = extract_clause_analysis(text)
    clause_sentiments = {c["sentiment"] for c in clauses if c["sentiment"] in ("positive", "negative")}
    if len(clause_sentiments) >= 2:
        return True

    # Check for contrasting conjunctions
    if re.search(r"\b(but|however|although|though|on the other hand|while)\b", text, re.IGNORECASE):
        words = set(tokenize_words(clean_text(text)))
        has_pos = any(w in words for w in POSITIVE_INDICATORS)
        has_neg = any(w in words for w in NEGATIVE_INDICATORS)
        if has_pos and has_neg:
            return True

    return False

