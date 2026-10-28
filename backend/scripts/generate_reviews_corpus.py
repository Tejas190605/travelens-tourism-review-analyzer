"""
Generates rich, high-fidelity reviews for all 54 curated destinations.
Every destination receives a realistic, distinct review count (7 to 13 reviews)
across differentiated rating profiles based on destination character:
- 5 stars: Highly positive reviews celebrating attractions, food, hospitality, scenery
- 4 stars: Strong experiences with minor concessions (e.g. minor price caveats, weather)
- 3 stars: Balanced/mixed reviews praising attractions/food but remarking on crowds, tricky transit, or prices
- 1-2 stars: Critical reviews highlighting real tourist pain points (peak-season queues, aggressive vendors)

All reviews are explicitly labeled data_source="curated_demonstration_corpus" with preserved provenance.
All dates fall within 2024-01-15 to 2026-05-15 (strictly preceding the 10 October 2026 reference date).
"""
import json
import random
from datetime import datetime, timedelta
from pathlib import Path

from curated_destinations_data import DESTINATIONS

def generate_reviews():
    # Deterministic generation
    random.seed(101)
    reviews = []
    
    start_date = datetime(2024, 1, 15)
    end_date = datetime(2026, 5, 15)
    total_days = (end_date - start_date).days

    # Destination-specific rating and volume profile weights
    # High-praise destinations (avg 4.5 - 4.8, 8 - 12 reviews)
    stellar_dests = {"Kyoto", "Zermatt", "Udaipur", "Queenstown", "Banff", "Florence", "Santorini", "Amalfi Coast", "Maui"}
    # Historic bustling hubs (avg 3.9 - 4.3, 10 - 13 reviews with mixed crowd/price reviews)
    bustling_dests = {"Jaipur", "Agra", "Paris", "Rome", "Cairo", "Bangkok", "Istanbul", "Barcelona", "New York"}
    # Coastal & nature retreats (avg 4.1 - 4.5, 8 - 11 reviews)
    coastal_nature = {"Goa", "Munnar", "Varkala", "Gokarna", "Bali", "Reykjavik", "Andaman Islands", "Coorg", "Ooty"}

    for idx, dest in enumerate(DESTINATIONS):
        d_name = dest["name"]
        cat = dest["category"]
        country = dest["country"]
        region = dest.get("region", "International")
        attractions_list = json.loads(dest.get("attractions", "[]"))
        primary_attraction = attractions_list[0] if attractions_list else d_name
        secondary_attraction = attractions_list[1] if len(attractions_list) > 1 else "the historic city centre"

        # Determine target review volume and rating distribution
        if d_name in stellar_dests:
            # 8 to 11 reviews, heavily 5 and 4 stars
            ratings_pool = [5, 5, 5, 4, 5, 4, 4, 5, 3, 5, 4]
            count = 8 + (idx % 4)  # 8, 9, 10, or 11
        elif d_name in bustling_dests:
            # 10 to 13 reviews, mixture of 5, 4, 3 and one 2 star
            ratings_pool = [5, 4, 5, 4, 3, 4, 3, 2, 5, 4, 3, 5, 4]
            count = 10 + (idx % 4)  # 10, 11, 12, or 13
        elif d_name in coastal_nature:
            # 8 to 11 reviews
            ratings_pool = [5, 5, 4, 4, 5, 3, 4, 5, 4, 3, 5]
            count = 8 + (idx % 4)
        else:
            # Standard destination profile: 7 to 10 reviews
            ratings_pool = [5, 4, 5, 4, 3, 4, 5, 3, 4, 2, 5]
            count = 7 + (idx % 4)

        chosen_ratings = ratings_pool[:count]

        # Template generators for each rating type
        for r_idx, rating in enumerate(chosen_ratings):
            days_offset = (hash(f"{d_name}_{r_idx}_{rating}") % total_days)
            rev_date = (start_date + timedelta(days=days_offset)).strftime("%Y-%m-%d")

            if rating == 5:
                variant = r_idx % 4
                if variant == 0:
                    text = (
                        f"Visiting {d_name} was an unforgettable journey! {primary_attraction} completely "
                        f"took our breath away with its stunning architecture and majestic views. The local food "
                        f"was delicious and every meal was a delight. The local residents and tour guides showed "
                        f"extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods "
                        f"made walking everywhere a joy."
                    )
                elif variant == 1:
                    text = (
                        f"Our stay in {d_name} exceeded all expectations. The room was spacious, comfortable, "
                        f"and maintained spotless cleanliness by attentive staff. Public transport and shuttle "
                        f"connectivity to {secondary_attraction} were remarkably punctual and efficient. "
                        f"Highly recommend this destination for both families and solo travellers!"
                    )
                elif variant == 2:
                    text = (
                        f"An absolute gem of a destination! Exploring {primary_attraction} in the early morning "
                        f"provided glorious, uninterrupted views and peaceful serenity. The culinary culture in "
                        f"{d_name} is top-notch, with fresh regional delicacies at welcoming bistros. "
                        f"Felt completely safe and well looked after at all hours."
                    )
                else:
                    text = (
                        f"Magnificent atmosphere in {d_name}. From the breathtaking panorama at {secondary_attraction} "
                        f"to the warm, courteous service from every guide, everything was exceptional. "
                        f"Transport was seamless and the vibrant heritage left a lasting impression on our entire family."
                    )
            elif rating == 4:
                variant = r_idx % 3
                if variant == 0:
                    text = (
                        f"Wonderful holiday in {d_name}! The sightseeing at {primary_attraction} was fabulous "
                        f"and we captured spectacular panoramic photos. Street cafes and traditional eateries "
                        f"served flavourful dishes at reasonable rates. The only minor inconvenience was finding "
                        f"metered taxis during evening hours, but overall the trip offered fantastic value for money."
                    )
                elif variant == 1:
                    text = (
                        f"The cultural depth of {d_name} is truly remarkable. Exploring {secondary_attraction} "
                        f"in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of "
                        f"security personnel around major landmarks. Food was tasty and authentic, though some "
                        f"tourist menus were slightly marked up in price."
                    )
                else:
                    text = (
                        f"Really enjoyed our time discovering {d_name}. {primary_attraction} is an impressive site "
                        f"with well-maintained facilities and informative plaques. Hotel accommodation was clean "
                        f"and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes."
                    )
            elif rating == 3:
                variant = r_idx % 2
                if variant == 0:
                    text = (
                        f"While {primary_attraction} is undeniably iconic and magnificent, the overwhelming crowds "
                        f"and endless queues tested our patience. Entry tickets and nearby restaurants were quite "
                        f"expensive and felt slightly overpriced. Food quality was decent, but you must reserve "
                        f"tables well in advance to avoid long waits."
                    )
                else:
                    text = (
                        f"A mixed experience in {d_name}. Natural beauty and historical sites like {secondary_attraction} "
                        f"are top-tier, but local transport was congested and confusing to navigate. Our hotel room "
                        f"was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit "
                        f"rather than an extended holiday."
                    )
            else: # rating 2 or 1
                text = (
                    f"Disappointed by our visit to {d_name} during peak season. Mass tourism has made "
                    f"{primary_attraction} overly crowded and chaotic with noisy tour groups. Several public "
                    f"restrooms lacked basic cleanliness and prices for bottled water and snacks were exorbitant. "
                    f"Local vendors were quite pushy."
                )

            reviews.append({
                "destination_name": d_name,
                "rating": rating,
                "review_text": text,
                "review_date": rev_date,
                "data_source": "curated_demonstration_corpus"
            })

    return reviews

if __name__ == "__main__":
    revs = generate_reviews()
    out_file = Path(__file__).resolve().parent / "curated_reviews_data.py"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write('"""\nCurated review corpus containing multi-aspect reviews for 54 destinations.\n')
        f.write('Provenance: Curated demonstration corpus for TRAVELENS tourism analytics.\n')
        f.write('Preserves ground-truth star ratings, dates, and explicit aspect cues.\n"""\n\n')
        f.write(f"REVIEWS = {json.dumps(revs, indent=4, ensure_ascii=False)}\n\n")
        f.write('print(f"Loaded {len(REVIEWS)} curated reviews across 54 destinations.")\n')
    print(f"Successfully wrote {len(revs)} reviews to {out_file}")
