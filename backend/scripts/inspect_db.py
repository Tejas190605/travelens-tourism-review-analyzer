import sqlite3
import os

db_path = os.path.abspath("backend/travelens.db")
print("Opening database at:", db_path, "Size:", os.path.getsize(db_path))

conn = sqlite3.connect(db_path)
c = conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [row[0] for row in c.fetchall()]
print("Tables found:", tables)

for tbl in tables:
    if not tbl.startswith("sqlite_"):
        c.execute(f"SELECT count(*) FROM {tbl}")
        print(f"Table '{tbl}': {c.fetchone()[0]} rows")

if "destinations" in tables:
    c.execute("SELECT count(*) FROM destinations")
    dest_count = c.fetchone()[0]
    
    c.execute("SELECT count(*) FROM reviews")
    rev_count = c.fetchone()[0]

    c.execute("SELECT count(*) FROM review_aspects")
    aspect_count = c.fetchone()[0]

    c.execute("SELECT sentiment, count(*) FROM reviews GROUP BY sentiment")
    sent_dist = c.fetchall()

    c.execute("SELECT predicted_sentiment, count(*) FROM reviews GROUP BY predicted_sentiment")
    pred_dist = c.fetchall()

    c.execute("SELECT count(*) FROM reviews WHERE rating >= 4 AND sentiment = 'Negative'")
    high_star_neg = c.fetchone()[0]

    c.execute("SELECT count(*) FROM reviews WHERE rating <= 2 AND sentiment = 'Positive'")
    low_star_pos = c.fetchone()[0]

    c.execute("SELECT count(*) FROM reviews WHERE is_mixed = 1")
    mixed_count = c.fetchone()[0]

    c.execute("SELECT count(image_url), count(DISTINCT image_url) FROM destinations")
    img_total, img_distinct = c.fetchone()

    c.execute("SELECT count(*) FROM users")
    user_count = c.fetchone()[0]

    c.execute("SELECT count(*) FROM saved_destinations")
    saved_count = c.fetchone()[0]

    print("\n=== DETAILED METRICS ===")
    print(f"Destinations: {dest_count}")
    print(f"Reviews: {rev_count}")
    print(f"Review Aspects: {aspect_count}")
    print(f"Rating Sentiment Distribution: {sent_dist}")
    print(f"Predicted Sentiment Distribution: {pred_dist}")
    print(f"High-star (>=4) labeled Negative: {high_star_neg}")
    print(f"Low-star (<=2) labeled Positive: {low_star_pos}")
    print(f"Mixed reviews flagged: {mixed_count}")
    print(f"Image URLs total: {img_total}, distinct: {img_distinct}")
    print(f"Users: {user_count}, Saved destinations: {saved_count}")

    # Check sample destination
    c.execute("SELECT id, name, country, region, category, budget_tier, image_url FROM destinations LIMIT 3")
    print("\nSample Destinations:")
    for row in c.fetchall():
        print(row)

conn.close()
