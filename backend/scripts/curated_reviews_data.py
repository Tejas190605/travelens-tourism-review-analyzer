"""
Curated review corpus containing multi-aspect reviews for 54 destinations.
Provenance: Curated demonstration corpus for TRAVELENS tourism analytics.
Preserves ground-truth star ratings, dates, and explicit aspect cues.
"""

REVIEWS = [
    {
        "destination_name": "Jaipur",
        "rating": 5,
        "review_text": "Visiting Jaipur was an unforgettable journey! Amber Fort completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-07-22",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Jaipur",
        "rating": 4,
        "review_text": "The cultural depth of Jaipur is truly remarkable. Exploring Hawa Mahal (Palace of Winds) in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2025-08-03",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Jaipur",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Amber Fort in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Jaipur is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-04-25",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Jaipur",
        "rating": 4,
        "review_text": "Wonderful holiday in Jaipur! The sightseeing at Amber Fort was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-12-11",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Jaipur",
        "rating": 3,
        "review_text": "While Amber Fort is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-12-09",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Jaipur",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Jaipur. Amber Fort is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-12-11",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Jaipur",
        "rating": 3,
        "review_text": "While Amber Fort is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-06-26",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Jaipur",
        "rating": 2,
        "review_text": "Disappointed by our visit to Jaipur during peak season. Mass tourism has made Amber Fort overly crowded and chaotic with noisy tour groups. Several public restrooms lacked basic cleanliness and prices for bottled water and snacks were exorbitant. Local vendors were quite pushy.",
        "review_date": "2025-05-07",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Jaipur",
        "rating": 5,
        "review_text": "Visiting Jaipur was an unforgettable journey! Amber Fort completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-08-15",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Jaipur",
        "rating": 4,
        "review_text": "Wonderful holiday in Jaipur! The sightseeing at Amber Fort was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-09-12",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Varanasi",
        "rating": 5,
        "review_text": "Visiting Varanasi was an unforgettable journey! Dashashwamedh Ghat completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-10-04",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Varanasi",
        "rating": 4,
        "review_text": "The cultural depth of Varanasi is truly remarkable. Exploring Kashi Vishwanath Golden Temple in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2024-07-08",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Varanasi",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Dashashwamedh Ghat in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Varanasi is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2026-02-22",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Varanasi",
        "rating": 4,
        "review_text": "Wonderful holiday in Varanasi! The sightseeing at Dashashwamedh Ghat was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-06-09",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Varanasi",
        "rating": 3,
        "review_text": "While Dashashwamedh Ghat is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2026-02-25",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Varanasi",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Varanasi. Dashashwamedh Ghat is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-11-26",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Varanasi",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Dashashwamedh Ghat in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Varanasi is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-07-15",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Varanasi",
        "rating": 3,
        "review_text": "A mixed experience in Varanasi. Natural beauty and historical sites like Kashi Vishwanath Golden Temple are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2025-07-20",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Agra",
        "rating": 5,
        "review_text": "Visiting Agra was an unforgettable journey! Taj Mahal completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-07-13",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Agra",
        "rating": 4,
        "review_text": "The cultural depth of Agra is truly remarkable. Exploring Agra Fort in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2024-03-15",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Agra",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Taj Mahal in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Agra is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-03-24",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Agra",
        "rating": 4,
        "review_text": "Wonderful holiday in Agra! The sightseeing at Taj Mahal was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-08-18",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Agra",
        "rating": 3,
        "review_text": "While Taj Mahal is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-07-29",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Agra",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Agra. Taj Mahal is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-06-22",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Agra",
        "rating": 3,
        "review_text": "While Taj Mahal is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-03-13",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Agra",
        "rating": 2,
        "review_text": "Disappointed by our visit to Agra during peak season. Mass tourism has made Taj Mahal overly crowded and chaotic with noisy tour groups. Several public restrooms lacked basic cleanliness and prices for bottled water and snacks were exorbitant. Local vendors were quite pushy.",
        "review_date": "2024-02-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Agra",
        "rating": 5,
        "review_text": "Visiting Agra was an unforgettable journey! Taj Mahal completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-12-05",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Agra",
        "rating": 4,
        "review_text": "Wonderful holiday in Agra! The sightseeing at Taj Mahal was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-12-01",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Agra",
        "rating": 3,
        "review_text": "While Taj Mahal is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-12-01",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Agra",
        "rating": 5,
        "review_text": "Magnificent atmosphere in Agra. From the breathtaking panorama at Agra Fort to the warm, courteous service from every guide, everything was exceptional. Transport was seamless and the vibrant heritage left a lasting impression on our entire family.",
        "review_date": "2024-08-26",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Hampi",
        "rating": 5,
        "review_text": "Visiting Hampi was an unforgettable journey! Virupaksha Temple completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-12-07",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Hampi",
        "rating": 4,
        "review_text": "The cultural depth of Hampi is truly remarkable. Exploring Vijaya Vittala Temple & Stone Chariot in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2025-12-29",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Hampi",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Virupaksha Temple in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Hampi is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-08-05",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Hampi",
        "rating": 4,
        "review_text": "Wonderful holiday in Hampi! The sightseeing at Virupaksha Temple was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-06-04",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Hampi",
        "rating": 3,
        "review_text": "While Virupaksha Temple is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-11-21",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Hampi",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Hampi. Virupaksha Temple is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-07-08",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Hampi",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Virupaksha Temple in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Hampi is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2026-04-06",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Hampi",
        "rating": 3,
        "review_text": "A mixed experience in Hampi. Natural beauty and historical sites like Vijaya Vittala Temple & Stone Chariot are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2025-02-17",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Hampi",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Hampi. Virupaksha Temple is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-04-30",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Hampi",
        "rating": 2,
        "review_text": "Disappointed by our visit to Hampi during peak season. Mass tourism has made Virupaksha Temple overly crowded and chaotic with noisy tour groups. Several public restrooms lacked basic cleanliness and prices for bottled water and snacks were exorbitant. Local vendors were quite pushy.",
        "review_date": "2025-04-12",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Udaipur",
        "rating": 5,
        "review_text": "Visiting Udaipur was an unforgettable journey! City Palace Complex completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-09-16",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Udaipur",
        "rating": 5,
        "review_text": "Our stay in Udaipur exceeded all expectations. The room was spacious, comfortable, and maintained spotless cleanliness by attentive staff. Public transport and shuttle connectivity to Lake Pichola & Jag Mandir were remarkably punctual and efficient. Highly recommend this destination for both families and solo travellers!",
        "review_date": "2024-12-11",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Udaipur",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring City Palace Complex in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Udaipur is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-09-04",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Udaipur",
        "rating": 4,
        "review_text": "Wonderful holiday in Udaipur! The sightseeing at City Palace Complex was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-04-08",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Udaipur",
        "rating": 5,
        "review_text": "Visiting Udaipur was an unforgettable journey! City Palace Complex completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-09-27",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Udaipur",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Udaipur. City Palace Complex is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2026-04-01",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Udaipur",
        "rating": 4,
        "review_text": "Wonderful holiday in Udaipur! The sightseeing at City Palace Complex was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-08-04",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Udaipur",
        "rating": 5,
        "review_text": "Magnificent atmosphere in Udaipur. From the breathtaking panorama at Lake Pichola & Jag Mandir to the warm, courteous service from every guide, everything was exceptional. Transport was seamless and the vibrant heritage left a lasting impression on our entire family.",
        "review_date": "2026-01-02",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Leh-Ladakh",
        "rating": 5,
        "review_text": "Visiting Leh-Ladakh was an unforgettable journey! Pangong Tso Lake completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-03-20",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Leh-Ladakh",
        "rating": 4,
        "review_text": "The cultural depth of Leh-Ladakh is truly remarkable. Exploring Nubra Valley & Hunder Sand Dunes in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2024-05-12",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Leh-Ladakh",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Pangong Tso Lake in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Leh-Ladakh is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-10-02",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Leh-Ladakh",
        "rating": 4,
        "review_text": "Wonderful holiday in Leh-Ladakh! The sightseeing at Pangong Tso Lake was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2026-01-24",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Leh-Ladakh",
        "rating": 3,
        "review_text": "While Pangong Tso Lake is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2026-04-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Leh-Ladakh",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Leh-Ladakh. Pangong Tso Lake is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-03-15",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Leh-Ladakh",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Pangong Tso Lake in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Leh-Ladakh is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2026-01-22",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Leh-Ladakh",
        "rating": 3,
        "review_text": "A mixed experience in Leh-Ladakh. Natural beauty and historical sites like Nubra Valley & Hunder Sand Dunes are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2025-07-16",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Manali",
        "rating": 5,
        "review_text": "Visiting Manali was an unforgettable journey! Solang Valley completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-03-16",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Manali",
        "rating": 4,
        "review_text": "The cultural depth of Manali is truly remarkable. Exploring Atal Tunnel & Sissu in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2024-07-20",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Manali",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Solang Valley in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Manali is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-07-05",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Manali",
        "rating": 4,
        "review_text": "Wonderful holiday in Manali! The sightseeing at Solang Valley was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-01-24",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Manali",
        "rating": 3,
        "review_text": "While Solang Valley is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-05-07",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Manali",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Manali. Solang Valley is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-12-11",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Manali",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Solang Valley in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Manali is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2026-01-19",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Manali",
        "rating": 3,
        "review_text": "A mixed experience in Manali. Natural beauty and historical sites like Atal Tunnel & Sissu are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2025-09-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Manali",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Manali. Solang Valley is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-08-31",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Munnar",
        "rating": 5,
        "review_text": "Visiting Munnar was an unforgettable journey! Eravikulam National Park completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-04-07",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Munnar",
        "rating": 5,
        "review_text": "Our stay in Munnar exceeded all expectations. The room was spacious, comfortable, and maintained spotless cleanliness by attentive staff. Public transport and shuttle connectivity to Mattupetty Dam were remarkably punctual and efficient. Highly recommend this destination for both families and solo travellers!",
        "review_date": "2024-01-20",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Munnar",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Munnar. Eravikulam National Park is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-01-18",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Munnar",
        "rating": 4,
        "review_text": "Wonderful holiday in Munnar! The sightseeing at Eravikulam National Park was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-02-23",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Munnar",
        "rating": 5,
        "review_text": "Visiting Munnar was an unforgettable journey! Eravikulam National Park completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-08-25",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Munnar",
        "rating": 3,
        "review_text": "A mixed experience in Munnar. Natural beauty and historical sites like Mattupetty Dam are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2024-05-07",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Munnar",
        "rating": 4,
        "review_text": "Wonderful holiday in Munnar! The sightseeing at Eravikulam National Park was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-04-23",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Munnar",
        "rating": 5,
        "review_text": "Magnificent atmosphere in Munnar. From the breathtaking panorama at Mattupetty Dam to the warm, courteous service from every guide, everything was exceptional. Transport was seamless and the vibrant heritage left a lasting impression on our entire family.",
        "review_date": "2025-03-19",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Munnar",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Munnar. Eravikulam National Park is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-12-02",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Munnar",
        "rating": 3,
        "review_text": "A mixed experience in Munnar. Natural beauty and historical sites like Mattupetty Dam are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2026-03-03",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Munnar",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Eravikulam National Park in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Munnar is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-10-29",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Goa",
        "rating": 5,
        "review_text": "Visiting Goa was an unforgettable journey! Basilica of Bom Jesus completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-01-30",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Goa",
        "rating": 5,
        "review_text": "Our stay in Goa exceeded all expectations. The room was spacious, comfortable, and maintained spotless cleanliness by attentive staff. Public transport and shuttle connectivity to Palolem Beach were remarkably punctual and efficient. Highly recommend this destination for both families and solo travellers!",
        "review_date": "2025-01-12",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Goa",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Goa. Basilica of Bom Jesus is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-10-21",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Goa",
        "rating": 4,
        "review_text": "Wonderful holiday in Goa! The sightseeing at Basilica of Bom Jesus was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-10-23",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Goa",
        "rating": 5,
        "review_text": "Visiting Goa was an unforgettable journey! Basilica of Bom Jesus completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-12-15",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Goa",
        "rating": 3,
        "review_text": "A mixed experience in Goa. Natural beauty and historical sites like Palolem Beach are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2025-01-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Goa",
        "rating": 4,
        "review_text": "Wonderful holiday in Goa! The sightseeing at Basilica of Bom Jesus was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-10-14",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Goa",
        "rating": 5,
        "review_text": "Magnificent atmosphere in Goa. From the breathtaking panorama at Palolem Beach to the warm, courteous service from every guide, everything was exceptional. Transport was seamless and the vibrant heritage left a lasting impression on our entire family.",
        "review_date": "2025-05-03",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Darjeeling",
        "rating": 5,
        "review_text": "Visiting Darjeeling was an unforgettable journey! Tiger Hill Sunrise completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-09-13",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Darjeeling",
        "rating": 4,
        "review_text": "The cultural depth of Darjeeling is truly remarkable. Exploring Darjeeling Himalayan Railway (Toy Train) in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2024-08-14",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Darjeeling",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Tiger Hill Sunrise in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Darjeeling is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-07-16",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Darjeeling",
        "rating": 4,
        "review_text": "Wonderful holiday in Darjeeling! The sightseeing at Tiger Hill Sunrise was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-08-18",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Darjeeling",
        "rating": 3,
        "review_text": "While Tiger Hill Sunrise is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-02-03",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Darjeeling",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Darjeeling. Tiger Hill Sunrise is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-03-30",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Darjeeling",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Tiger Hill Sunrise in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Darjeeling is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2026-01-16",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Darjeeling",
        "rating": 3,
        "review_text": "A mixed experience in Darjeeling. Natural beauty and historical sites like Darjeeling Himalayan Railway (Toy Train) are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2025-04-23",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rishikesh",
        "rating": 5,
        "review_text": "Visiting Rishikesh was an unforgettable journey! Triveni Ghat completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-09-05",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rishikesh",
        "rating": 4,
        "review_text": "The cultural depth of Rishikesh is truly remarkable. Exploring Beatles Ashram (Chaurasi Kutia) in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2025-02-26",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rishikesh",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Triveni Ghat in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Rishikesh is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-04-03",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rishikesh",
        "rating": 4,
        "review_text": "Wonderful holiday in Rishikesh! The sightseeing at Triveni Ghat was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-03-19",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rishikesh",
        "rating": 3,
        "review_text": "While Triveni Ghat is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2024-07-29",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rishikesh",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Rishikesh. Triveni Ghat is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-08-05",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rishikesh",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Triveni Ghat in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Rishikesh is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-12-22",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rishikesh",
        "rating": 3,
        "review_text": "A mixed experience in Rishikesh. Natural beauty and historical sites like Beatles Ashram (Chaurasi Kutia) are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2024-03-03",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rishikesh",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Rishikesh. Triveni Ghat is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-05-23",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Andaman Islands",
        "rating": 5,
        "review_text": "Visiting Andaman Islands was an unforgettable journey! Radhanagar Beach (Havelock) completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-02-03",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Andaman Islands",
        "rating": 5,
        "review_text": "Our stay in Andaman Islands exceeded all expectations. The room was spacious, comfortable, and maintained spotless cleanliness by attentive staff. Public transport and shuttle connectivity to Elephant Beach Coral Reef were remarkably punctual and efficient. Highly recommend this destination for both families and solo travellers!",
        "review_date": "2024-02-23",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Andaman Islands",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Andaman Islands. Radhanagar Beach (Havelock) is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-12-17",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Andaman Islands",
        "rating": 4,
        "review_text": "Wonderful holiday in Andaman Islands! The sightseeing at Radhanagar Beach (Havelock) was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-06-06",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Andaman Islands",
        "rating": 5,
        "review_text": "Visiting Andaman Islands was an unforgettable journey! Radhanagar Beach (Havelock) completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-06-21",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Andaman Islands",
        "rating": 3,
        "review_text": "A mixed experience in Andaman Islands. Natural beauty and historical sites like Elephant Beach Coral Reef are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2025-08-12",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Andaman Islands",
        "rating": 4,
        "review_text": "Wonderful holiday in Andaman Islands! The sightseeing at Radhanagar Beach (Havelock) was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-07-01",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Andaman Islands",
        "rating": 5,
        "review_text": "Magnificent atmosphere in Andaman Islands. From the breathtaking panorama at Elephant Beach Coral Reef to the warm, courteous service from every guide, everything was exceptional. Transport was seamless and the vibrant heritage left a lasting impression on our entire family.",
        "review_date": "2025-02-20",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Andaman Islands",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Andaman Islands. Radhanagar Beach (Havelock) is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-12-23",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Andaman Islands",
        "rating": 3,
        "review_text": "A mixed experience in Andaman Islands. Natural beauty and historical sites like Elephant Beach Coral Reef are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2024-09-13",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Andaman Islands",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Radhanagar Beach (Havelock) in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Andaman Islands is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-12-19",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Ooty",
        "rating": 5,
        "review_text": "Visiting Ooty was an unforgettable journey! Nilgiri Mountain Railway completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-01-22",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Ooty",
        "rating": 5,
        "review_text": "Our stay in Ooty exceeded all expectations. The room was spacious, comfortable, and maintained spotless cleanliness by attentive staff. Public transport and shuttle connectivity to Ooty Lake & Boathouse were remarkably punctual and efficient. Highly recommend this destination for both families and solo travellers!",
        "review_date": "2024-10-25",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Ooty",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Ooty. Nilgiri Mountain Railway is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-07-30",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Ooty",
        "rating": 4,
        "review_text": "Wonderful holiday in Ooty! The sightseeing at Nilgiri Mountain Railway was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2026-02-25",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Ooty",
        "rating": 5,
        "review_text": "Visiting Ooty was an unforgettable journey! Nilgiri Mountain Railway completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-03-12",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Ooty",
        "rating": 3,
        "review_text": "A mixed experience in Ooty. Natural beauty and historical sites like Ooty Lake & Boathouse are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2024-05-12",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Ooty",
        "rating": 4,
        "review_text": "Wonderful holiday in Ooty! The sightseeing at Nilgiri Mountain Railway was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-04-26",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Ooty",
        "rating": 5,
        "review_text": "Magnificent atmosphere in Ooty. From the breathtaking panorama at Ooty Lake & Boathouse to the warm, courteous service from every guide, everything was exceptional. Transport was seamless and the vibrant heritage left a lasting impression on our entire family.",
        "review_date": "2026-03-06",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Coorg",
        "rating": 5,
        "review_text": "Visiting Coorg was an unforgettable journey! Abbey Falls completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-07-27",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Coorg",
        "rating": 5,
        "review_text": "Our stay in Coorg exceeded all expectations. The room was spacious, comfortable, and maintained spotless cleanliness by attentive staff. Public transport and shuttle connectivity to Raja's Seat Sunset Point were remarkably punctual and efficient. Highly recommend this destination for both families and solo travellers!",
        "review_date": "2024-04-23",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Coorg",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Coorg. Abbey Falls is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-12-05",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Coorg",
        "rating": 4,
        "review_text": "Wonderful holiday in Coorg! The sightseeing at Abbey Falls was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-07-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Coorg",
        "rating": 5,
        "review_text": "Visiting Coorg was an unforgettable journey! Abbey Falls completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-08-19",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Coorg",
        "rating": 3,
        "review_text": "A mixed experience in Coorg. Natural beauty and historical sites like Raja's Seat Sunset Point are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2025-10-07",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Coorg",
        "rating": 4,
        "review_text": "Wonderful holiday in Coorg! The sightseeing at Abbey Falls was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-10-31",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Coorg",
        "rating": 5,
        "review_text": "Magnificent atmosphere in Coorg. From the breathtaking panorama at Raja's Seat Sunset Point to the warm, courteous service from every guide, everything was exceptional. Transport was seamless and the vibrant heritage left a lasting impression on our entire family.",
        "review_date": "2024-09-11",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Coorg",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Coorg. Abbey Falls is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2026-01-16",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Amritsar",
        "rating": 5,
        "review_text": "Visiting Amritsar was an unforgettable journey! Golden Temple (Sri Harmandir Sahib) completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-12-22",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Amritsar",
        "rating": 4,
        "review_text": "The cultural depth of Amritsar is truly remarkable. Exploring Wagah Border Beating Retreat in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2024-09-24",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Amritsar",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Golden Temple (Sri Harmandir Sahib) in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Amritsar is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-09-12",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Amritsar",
        "rating": 4,
        "review_text": "Wonderful holiday in Amritsar! The sightseeing at Golden Temple (Sri Harmandir Sahib) was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-01-04",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Amritsar",
        "rating": 3,
        "review_text": "While Golden Temple (Sri Harmandir Sahib) is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-07-19",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Amritsar",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Amritsar. Golden Temple (Sri Harmandir Sahib) is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-06-27",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Amritsar",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Golden Temple (Sri Harmandir Sahib) in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Amritsar is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2026-03-26",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Amritsar",
        "rating": 3,
        "review_text": "A mixed experience in Amritsar. Natural beauty and historical sites like Wagah Border Beating Retreat are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2025-08-17",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Amritsar",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Amritsar. Golden Temple (Sri Harmandir Sahib) is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-01-06",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Khajuraho",
        "rating": 5,
        "review_text": "Visiting Khajuraho was an unforgettable journey! Kandariya Mahadeva Temple completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-09-23",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Khajuraho",
        "rating": 4,
        "review_text": "The cultural depth of Khajuraho is truly remarkable. Exploring Lakshmana Temple in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2024-11-14",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Khajuraho",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Kandariya Mahadeva Temple in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Khajuraho is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-02-21",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Khajuraho",
        "rating": 4,
        "review_text": "Wonderful holiday in Khajuraho! The sightseeing at Kandariya Mahadeva Temple was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2026-03-14",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Khajuraho",
        "rating": 3,
        "review_text": "While Kandariya Mahadeva Temple is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2024-05-15",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Khajuraho",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Khajuraho. Kandariya Mahadeva Temple is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-09-14",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Khajuraho",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Kandariya Mahadeva Temple in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Khajuraho is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-12-11",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Khajuraho",
        "rating": 3,
        "review_text": "A mixed experience in Khajuraho. Natural beauty and historical sites like Lakshmana Temple are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2026-01-14",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Khajuraho",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Khajuraho. Kandariya Mahadeva Temple is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-01-04",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Khajuraho",
        "rating": 2,
        "review_text": "Disappointed by our visit to Khajuraho during peak season. Mass tourism has made Kandariya Mahadeva Temple overly crowded and chaotic with noisy tour groups. Several public restrooms lacked basic cleanliness and prices for bottled water and snacks were exorbitant. Local vendors were quite pushy.",
        "review_date": "2025-12-04",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Mysore",
        "rating": 5,
        "review_text": "Visiting Mysore was an unforgettable journey! Mysore Palace (Amba Vilas) completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-04-29",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Mysore",
        "rating": 4,
        "review_text": "The cultural depth of Mysore is truly remarkable. Exploring Chamundi Hill & Temple in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2024-10-20",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Mysore",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Mysore Palace (Amba Vilas) in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Mysore is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2026-01-01",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Mysore",
        "rating": 4,
        "review_text": "Wonderful holiday in Mysore! The sightseeing at Mysore Palace (Amba Vilas) was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-04-18",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Mysore",
        "rating": 3,
        "review_text": "While Mysore Palace (Amba Vilas) is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2026-03-29",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Mysore",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Mysore. Mysore Palace (Amba Vilas) is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2026-01-01",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Mysore",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Mysore Palace (Amba Vilas) in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Mysore is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-07-13",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Pondicherry",
        "rating": 5,
        "review_text": "Visiting Pondicherry was an unforgettable journey! White Town (French Quarter) completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-11-14",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Pondicherry",
        "rating": 4,
        "review_text": "The cultural depth of Pondicherry is truly remarkable. Exploring Promenade Beach in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2025-09-02",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Pondicherry",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring White Town (French Quarter) in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Pondicherry is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-04-25",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Pondicherry",
        "rating": 4,
        "review_text": "Wonderful holiday in Pondicherry! The sightseeing at White Town (French Quarter) was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-04-30",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Pondicherry",
        "rating": 3,
        "review_text": "While White Town (French Quarter) is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-07-01",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Pondicherry",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Pondicherry. White Town (French Quarter) is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-03-10",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Pondicherry",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring White Town (French Quarter) in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Pondicherry is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-06-22",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Pondicherry",
        "rating": 3,
        "review_text": "A mixed experience in Pondicherry. Natural beauty and historical sites like Promenade Beach are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2026-02-08",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Shillong",
        "rating": 5,
        "review_text": "Visiting Shillong was an unforgettable journey! Umiam Lake completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-08-27",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Shillong",
        "rating": 4,
        "review_text": "The cultural depth of Shillong is truly remarkable. Exploring Elephant Falls in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2025-05-07",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Shillong",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Umiam Lake in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Shillong is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-06-09",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Shillong",
        "rating": 4,
        "review_text": "Wonderful holiday in Shillong! The sightseeing at Umiam Lake was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-10-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Shillong",
        "rating": 3,
        "review_text": "While Umiam Lake is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-08-13",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Shillong",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Shillong. Umiam Lake is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-08-13",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Shillong",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Umiam Lake in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Shillong is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-10-01",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Shillong",
        "rating": 3,
        "review_text": "A mixed experience in Shillong. Natural beauty and historical sites like Elephant Falls are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2025-01-01",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Shillong",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Shillong. Umiam Lake is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-03-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Gokarna",
        "rating": 5,
        "review_text": "Visiting Gokarna was an unforgettable journey! Om Beach completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-12-30",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Gokarna",
        "rating": 5,
        "review_text": "Our stay in Gokarna exceeded all expectations. The room was spacious, comfortable, and maintained spotless cleanliness by attentive staff. Public transport and shuttle connectivity to Kudle Beach were remarkably punctual and efficient. Highly recommend this destination for both families and solo travellers!",
        "review_date": "2026-01-17",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Gokarna",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Gokarna. Om Beach is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2026-01-02",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Gokarna",
        "rating": 4,
        "review_text": "Wonderful holiday in Gokarna! The sightseeing at Om Beach was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-07-15",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Gokarna",
        "rating": 5,
        "review_text": "Visiting Gokarna was an unforgettable journey! Om Beach completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-02-23",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Gokarna",
        "rating": 3,
        "review_text": "A mixed experience in Gokarna. Natural beauty and historical sites like Kudle Beach are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2025-01-12",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Gokarna",
        "rating": 4,
        "review_text": "Wonderful holiday in Gokarna! The sightseeing at Om Beach was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-06-17",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Gokarna",
        "rating": 5,
        "review_text": "Magnificent atmosphere in Gokarna. From the breathtaking panorama at Kudle Beach to the warm, courteous service from every guide, everything was exceptional. Transport was seamless and the vibrant heritage left a lasting impression on our entire family.",
        "review_date": "2024-10-25",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Gokarna",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Gokarna. Om Beach is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-08-25",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Gokarna",
        "rating": 3,
        "review_text": "A mixed experience in Gokarna. Natural beauty and historical sites like Kudle Beach are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2024-08-03",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Gokarna",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Om Beach in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Gokarna is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-01-24",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Varkala",
        "rating": 5,
        "review_text": "Visiting Varkala was an unforgettable journey! Varkala North Cliff completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-05-11",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Varkala",
        "rating": 5,
        "review_text": "Our stay in Varkala exceeded all expectations. The room was spacious, comfortable, and maintained spotless cleanliness by attentive staff. Public transport and shuttle connectivity to Papanasam Beach (Holy Waters) were remarkably punctual and efficient. Highly recommend this destination for both families and solo travellers!",
        "review_date": "2025-07-04",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Varkala",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Varkala. Varkala North Cliff is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-09-06",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Varkala",
        "rating": 4,
        "review_text": "Wonderful holiday in Varkala! The sightseeing at Varkala North Cliff was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-11-23",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Varkala",
        "rating": 5,
        "review_text": "Visiting Varkala was an unforgettable journey! Varkala North Cliff completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-04-05",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Varkala",
        "rating": 3,
        "review_text": "A mixed experience in Varkala. Natural beauty and historical sites like Papanasam Beach (Holy Waters) are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2025-11-03",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Varkala",
        "rating": 4,
        "review_text": "Wonderful holiday in Varkala! The sightseeing at Varkala North Cliff was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-02-15",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Varkala",
        "rating": 5,
        "review_text": "Magnificent atmosphere in Varkala. From the breathtaking panorama at Papanasam Beach (Holy Waters) to the warm, courteous service from every guide, everything was exceptional. Transport was seamless and the vibrant heritage left a lasting impression on our entire family.",
        "review_date": "2025-05-29",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Shimla",
        "rating": 5,
        "review_text": "Visiting Shimla was an unforgettable journey! The Ridge & Christ Church completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-08-15",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Shimla",
        "rating": 4,
        "review_text": "The cultural depth of Shimla is truly remarkable. Exploring Mall Road in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2024-03-04",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Shimla",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring The Ridge & Christ Church in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Shimla is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-06-07",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Shimla",
        "rating": 4,
        "review_text": "Wonderful holiday in Shimla! The sightseeing at The Ridge & Christ Church was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-04-14",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Shimla",
        "rating": 3,
        "review_text": "While The Ridge & Christ Church is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-09-10",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Shimla",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Shimla. The Ridge & Christ Church is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-05-09",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Shimla",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring The Ridge & Christ Church in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Shimla is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-02-03",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Shimla",
        "rating": 3,
        "review_text": "A mixed experience in Shimla. Natural beauty and historical sites like Mall Road are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2024-03-07",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Jaisalmer",
        "rating": 5,
        "review_text": "Visiting Jaisalmer was an unforgettable journey! Jaisalmer Fort (Sonar Qila) completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-12-23",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Jaisalmer",
        "rating": 4,
        "review_text": "The cultural depth of Jaisalmer is truly remarkable. Exploring Patwon Ki Haveli in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2026-02-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Jaisalmer",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Jaisalmer Fort (Sonar Qila) in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Jaisalmer is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-05-15",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Jaisalmer",
        "rating": 4,
        "review_text": "Wonderful holiday in Jaisalmer! The sightseeing at Jaisalmer Fort (Sonar Qila) was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-04-19",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Jaisalmer",
        "rating": 3,
        "review_text": "While Jaisalmer Fort (Sonar Qila) is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2026-01-03",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Jaisalmer",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Jaisalmer. Jaisalmer Fort (Sonar Qila) is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-04-13",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Jaisalmer",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Jaisalmer Fort (Sonar Qila) in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Jaisalmer is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-07-30",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Jaisalmer",
        "rating": 3,
        "review_text": "A mixed experience in Jaisalmer. Natural beauty and historical sites like Patwon Ki Haveli are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2026-04-01",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Jaisalmer",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Jaisalmer. Jaisalmer Fort (Sonar Qila) is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-06-08",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Kaziranga",
        "rating": 5,
        "review_text": "Visiting Kaziranga was an unforgettable journey! Central (Kohora) Safari Range completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-02-26",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Kaziranga",
        "rating": 4,
        "review_text": "The cultural depth of Kaziranga is truly remarkable. Exploring Western (Bagori) Range in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2024-11-24",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Kaziranga",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Central (Kohora) Safari Range in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Kaziranga is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-10-07",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Kaziranga",
        "rating": 4,
        "review_text": "Wonderful holiday in Kaziranga! The sightseeing at Central (Kohora) Safari Range was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-09-05",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Kaziranga",
        "rating": 3,
        "review_text": "While Central (Kohora) Safari Range is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2024-05-07",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Kaziranga",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Kaziranga. Central (Kohora) Safari Range is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-04-05",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Kaziranga",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Central (Kohora) Safari Range in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Kaziranga is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-01-21",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Kaziranga",
        "rating": 3,
        "review_text": "A mixed experience in Kaziranga. Natural beauty and historical sites like Western (Bagori) Range are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2024-08-31",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Kaziranga",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Kaziranga. Central (Kohora) Safari Range is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-09-01",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Kaziranga",
        "rating": 2,
        "review_text": "Disappointed by our visit to Kaziranga during peak season. Mass tourism has made Central (Kohora) Safari Range overly crowded and chaotic with noisy tour groups. Several public restrooms lacked basic cleanliness and prices for bottled water and snacks were exorbitant. Local vendors were quite pushy.",
        "review_date": "2026-03-15",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Madurai",
        "rating": 5,
        "review_text": "Visiting Madurai was an unforgettable journey! Meenakshi Amman Temple completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-01-21",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Madurai",
        "rating": 4,
        "review_text": "The cultural depth of Madurai is truly remarkable. Exploring Thirumalai Nayakkar Palace in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2025-06-01",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Madurai",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Meenakshi Amman Temple in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Madurai is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-02-08",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Madurai",
        "rating": 4,
        "review_text": "Wonderful holiday in Madurai! The sightseeing at Meenakshi Amman Temple was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-02-10",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Madurai",
        "rating": 3,
        "review_text": "While Meenakshi Amman Temple is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-09-21",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Madurai",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Madurai. Meenakshi Amman Temple is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-01-30",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Madurai",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Meenakshi Amman Temple in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Madurai is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-05-21",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rann of Kutch",
        "rating": 5,
        "review_text": "Visiting Rann of Kutch was an unforgettable journey! White Desert (Dhordo) completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-12-17",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rann of Kutch",
        "rating": 4,
        "review_text": "The cultural depth of Rann of Kutch is truly remarkable. Exploring Kalo Dungar (Black Hill) in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2024-01-18",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rann of Kutch",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring White Desert (Dhordo) in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Rann of Kutch is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-09-14",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rann of Kutch",
        "rating": 4,
        "review_text": "Wonderful holiday in Rann of Kutch! The sightseeing at White Desert (Dhordo) was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2026-03-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rann of Kutch",
        "rating": 3,
        "review_text": "While White Desert (Dhordo) is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-06-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rann of Kutch",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Rann of Kutch. White Desert (Dhordo) is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-12-04",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rann of Kutch",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring White Desert (Dhordo) in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Rann of Kutch is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2026-04-18",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rann of Kutch",
        "rating": 3,
        "review_text": "A mixed experience in Rann of Kutch. Natural beauty and historical sites like Kalo Dungar (Black Hill) are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2025-06-04",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Kyoto",
        "rating": 5,
        "review_text": "Visiting Kyoto was an unforgettable journey! Fushimi Inari Shrine Torii Gates completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-08-30",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Kyoto",
        "rating": 5,
        "review_text": "Our stay in Kyoto exceeded all expectations. The room was spacious, comfortable, and maintained spotless cleanliness by attentive staff. Public transport and shuttle connectivity to Kinkaku-ji (Golden Pavilion) were remarkably punctual and efficient. Highly recommend this destination for both families and solo travellers!",
        "review_date": "2024-05-21",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Kyoto",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Fushimi Inari Shrine Torii Gates in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Kyoto is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-11-05",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Kyoto",
        "rating": 4,
        "review_text": "Wonderful holiday in Kyoto! The sightseeing at Fushimi Inari Shrine Torii Gates was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-01-09",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Kyoto",
        "rating": 5,
        "review_text": "Visiting Kyoto was an unforgettable journey! Fushimi Inari Shrine Torii Gates completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-07-14",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Kyoto",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Kyoto. Fushimi Inari Shrine Torii Gates is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2026-04-30",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Kyoto",
        "rating": 4,
        "review_text": "Wonderful holiday in Kyoto! The sightseeing at Fushimi Inari Shrine Torii Gates was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2026-05-07",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Kyoto",
        "rating": 5,
        "review_text": "Magnificent atmosphere in Kyoto. From the breathtaking panorama at Kinkaku-ji (Golden Pavilion) to the warm, courteous service from every guide, everything was exceptional. Transport was seamless and the vibrant heritage left a lasting impression on our entire family.",
        "review_date": "2025-07-03",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Kyoto",
        "rating": 3,
        "review_text": "While Fushimi Inari Shrine Torii Gates is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2024-07-11",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Kyoto",
        "rating": 5,
        "review_text": "Our stay in Kyoto exceeded all expectations. The room was spacious, comfortable, and maintained spotless cleanliness by attentive staff. Public transport and shuttle connectivity to Kinkaku-ji (Golden Pavilion) were remarkably punctual and efficient. Highly recommend this destination for both families and solo travellers!",
        "review_date": "2026-02-06",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Florence",
        "rating": 5,
        "review_text": "Visiting Florence was an unforgettable journey! Florence Cathedral (Duomo) completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-09-08",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Florence",
        "rating": 5,
        "review_text": "Our stay in Florence exceeded all expectations. The room was spacious, comfortable, and maintained spotless cleanliness by attentive staff. Public transport and shuttle connectivity to Uffizi Gallery were remarkably punctual and efficient. Highly recommend this destination for both families and solo travellers!",
        "review_date": "2025-01-19",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Florence",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Florence Cathedral (Duomo) in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Florence is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2026-03-06",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Florence",
        "rating": 4,
        "review_text": "Wonderful holiday in Florence! The sightseeing at Florence Cathedral (Duomo) was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-11-27",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Florence",
        "rating": 5,
        "review_text": "Visiting Florence was an unforgettable journey! Florence Cathedral (Duomo) completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-11-21",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Florence",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Florence. Florence Cathedral (Duomo) is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-07-05",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Florence",
        "rating": 4,
        "review_text": "Wonderful holiday in Florence! The sightseeing at Florence Cathedral (Duomo) was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-06-30",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Florence",
        "rating": 5,
        "review_text": "Magnificent atmosphere in Florence. From the breathtaking panorama at Uffizi Gallery to the warm, courteous service from every guide, everything was exceptional. Transport was seamless and the vibrant heritage left a lasting impression on our entire family.",
        "review_date": "2026-04-05",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Florence",
        "rating": 3,
        "review_text": "While Florence Cathedral (Duomo) is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-04-09",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Florence",
        "rating": 5,
        "review_text": "Our stay in Florence exceeded all expectations. The room was spacious, comfortable, and maintained spotless cleanliness by attentive staff. Public transport and shuttle connectivity to Uffizi Gallery were remarkably punctual and efficient. Highly recommend this destination for both families and solo travellers!",
        "review_date": "2025-03-19",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Florence",
        "rating": 4,
        "review_text": "The cultural depth of Florence is truly remarkable. Exploring Uffizi Gallery in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2025-05-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Banff",
        "rating": 5,
        "review_text": "Visiting Banff was an unforgettable journey! Lake Louise completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2026-01-16",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Banff",
        "rating": 5,
        "review_text": "Our stay in Banff exceeded all expectations. The room was spacious, comfortable, and maintained spotless cleanliness by attentive staff. Public transport and shuttle connectivity to Moraine Lake & Valley of the Ten Peaks were remarkably punctual and efficient. Highly recommend this destination for both families and solo travellers!",
        "review_date": "2026-02-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Banff",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Lake Louise in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Banff is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-04-17",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Banff",
        "rating": 4,
        "review_text": "Wonderful holiday in Banff! The sightseeing at Lake Louise was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-06-03",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Banff",
        "rating": 5,
        "review_text": "Visiting Banff was an unforgettable journey! Lake Louise completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-07-20",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Banff",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Banff. Lake Louise is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-06-25",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Banff",
        "rating": 4,
        "review_text": "Wonderful holiday in Banff! The sightseeing at Lake Louise was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-04-17",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Banff",
        "rating": 5,
        "review_text": "Magnificent atmosphere in Banff. From the breathtaking panorama at Moraine Lake & Valley of the Ten Peaks to the warm, courteous service from every guide, everything was exceptional. Transport was seamless and the vibrant heritage left a lasting impression on our entire family.",
        "review_date": "2024-08-13",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Santorini",
        "rating": 5,
        "review_text": "Visiting Santorini was an unforgettable journey! Oia Village Sunset Castle completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2026-04-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Santorini",
        "rating": 5,
        "review_text": "Our stay in Santorini exceeded all expectations. The room was spacious, comfortable, and maintained spotless cleanliness by attentive staff. Public transport and shuttle connectivity to Fira to Oia Caldera Cliff Trail were remarkably punctual and efficient. Highly recommend this destination for both families and solo travellers!",
        "review_date": "2025-03-11",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Santorini",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Oia Village Sunset Castle in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Santorini is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-01-21",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Santorini",
        "rating": 4,
        "review_text": "Wonderful holiday in Santorini! The sightseeing at Oia Village Sunset Castle was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2026-01-12",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Santorini",
        "rating": 5,
        "review_text": "Visiting Santorini was an unforgettable journey! Oia Village Sunset Castle completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-09-09",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Santorini",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Santorini. Oia Village Sunset Castle is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-09-29",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Santorini",
        "rating": 4,
        "review_text": "Wonderful holiday in Santorini! The sightseeing at Oia Village Sunset Castle was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-03-04",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Santorini",
        "rating": 5,
        "review_text": "Magnificent atmosphere in Santorini. From the breathtaking panorama at Fira to Oia Caldera Cliff Trail to the warm, courteous service from every guide, everything was exceptional. Transport was seamless and the vibrant heritage left a lasting impression on our entire family.",
        "review_date": "2026-03-12",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Santorini",
        "rating": 3,
        "review_text": "While Oia Village Sunset Castle is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2024-08-02",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cape Town",
        "rating": 5,
        "review_text": "Visiting Cape Town was an unforgettable journey! Table Mountain Cableway completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2026-01-19",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cape Town",
        "rating": 4,
        "review_text": "The cultural depth of Cape Town is truly remarkable. Exploring Boulders Beach African Penguin Colony in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2025-09-25",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cape Town",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Table Mountain Cableway in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Cape Town is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-04-01",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cape Town",
        "rating": 4,
        "review_text": "Wonderful holiday in Cape Town! The sightseeing at Table Mountain Cableway was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-02-11",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cape Town",
        "rating": 3,
        "review_text": "While Table Mountain Cableway is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-06-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cape Town",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Cape Town. Table Mountain Cableway is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2026-05-09",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cape Town",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Table Mountain Cableway in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Cape Town is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-04-13",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cape Town",
        "rating": 3,
        "review_text": "A mixed experience in Cape Town. Natural beauty and historical sites like Boulders Beach African Penguin Colony are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2024-09-30",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cape Town",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Cape Town. Table Mountain Cableway is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2026-03-12",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Queenstown",
        "rating": 5,
        "review_text": "Visiting Queenstown was an unforgettable journey! Milford Sound & Fiordland completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-12-14",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Queenstown",
        "rating": 5,
        "review_text": "Our stay in Queenstown exceeded all expectations. The room was spacious, comfortable, and maintained spotless cleanliness by attentive staff. Public transport and shuttle connectivity to Kawarau Gorge Bungee Bridge were remarkably punctual and efficient. Highly recommend this destination for both families and solo travellers!",
        "review_date": "2024-02-20",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Queenstown",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Milford Sound & Fiordland in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Queenstown is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-06-30",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Queenstown",
        "rating": 4,
        "review_text": "Wonderful holiday in Queenstown! The sightseeing at Milford Sound & Fiordland was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2026-02-01",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Queenstown",
        "rating": 5,
        "review_text": "Visiting Queenstown was an unforgettable journey! Milford Sound & Fiordland completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-05-16",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Queenstown",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Queenstown. Milford Sound & Fiordland is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2026-01-05",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Queenstown",
        "rating": 4,
        "review_text": "Wonderful holiday in Queenstown! The sightseeing at Milford Sound & Fiordland was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2026-03-04",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Queenstown",
        "rating": 5,
        "review_text": "Magnificent atmosphere in Queenstown. From the breathtaking panorama at Kawarau Gorge Bungee Bridge to the warm, courteous service from every guide, everything was exceptional. Transport was seamless and the vibrant heritage left a lasting impression on our entire family.",
        "review_date": "2025-11-20",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Queenstown",
        "rating": 3,
        "review_text": "While Milford Sound & Fiordland is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2024-02-27",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Queenstown",
        "rating": 5,
        "review_text": "Our stay in Queenstown exceeded all expectations. The room was spacious, comfortable, and maintained spotless cleanliness by attentive staff. Public transport and shuttle connectivity to Kawarau Gorge Bungee Bridge were remarkably punctual and efficient. Highly recommend this destination for both families and solo travellers!",
        "review_date": "2026-04-14",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Queenstown",
        "rating": 4,
        "review_text": "The cultural depth of Queenstown is truly remarkable. Exploring Kawarau Gorge Bungee Bridge in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2025-10-05",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Oaxaca",
        "rating": 5,
        "review_text": "Visiting Oaxaca was an unforgettable journey! Monte Alban Zapotec Ruins completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-01-25",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Oaxaca",
        "rating": 4,
        "review_text": "The cultural depth of Oaxaca is truly remarkable. Exploring Santo Domingo Church in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2025-01-20",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Oaxaca",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Monte Alban Zapotec Ruins in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Oaxaca is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-02-22",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Oaxaca",
        "rating": 4,
        "review_text": "Wonderful holiday in Oaxaca! The sightseeing at Monte Alban Zapotec Ruins was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-04-11",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Oaxaca",
        "rating": 3,
        "review_text": "While Monte Alban Zapotec Ruins is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-03-25",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Oaxaca",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Oaxaca. Monte Alban Zapotec Ruins is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-09-24",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Oaxaca",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Monte Alban Zapotec Ruins in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Oaxaca is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-12-26",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Dubrovnik",
        "rating": 5,
        "review_text": "Visiting Dubrovnik was an unforgettable journey! Old Town City Walls completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-03-18",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Dubrovnik",
        "rating": 4,
        "review_text": "The cultural depth of Dubrovnik is truly remarkable. Exploring Stradun Limestone Promenade in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2025-06-01",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Dubrovnik",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Old Town City Walls in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Dubrovnik is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-10-07",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Dubrovnik",
        "rating": 4,
        "review_text": "Wonderful holiday in Dubrovnik! The sightseeing at Old Town City Walls was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-08-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Dubrovnik",
        "rating": 3,
        "review_text": "While Old Town City Walls is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2024-11-12",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Dubrovnik",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Dubrovnik. Old Town City Walls is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-09-15",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Dubrovnik",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Old Town City Walls in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Dubrovnik is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-09-06",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Dubrovnik",
        "rating": 3,
        "review_text": "A mixed experience in Dubrovnik. Natural beauty and historical sites like Stradun Limestone Promenade are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2024-03-27",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Bali",
        "rating": 5,
        "review_text": "Visiting Bali was an unforgettable journey! Tegallalang Rice Terraces completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-01-21",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Bali",
        "rating": 5,
        "review_text": "Our stay in Bali exceeded all expectations. The room was spacious, comfortable, and maintained spotless cleanliness by attentive staff. Public transport and shuttle connectivity to Uluwatu Clifftop Temple were remarkably punctual and efficient. Highly recommend this destination for both families and solo travellers!",
        "review_date": "2025-11-13",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Bali",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Bali. Tegallalang Rice Terraces is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-09-20",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Bali",
        "rating": 4,
        "review_text": "Wonderful holiday in Bali! The sightseeing at Tegallalang Rice Terraces was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-08-23",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Bali",
        "rating": 5,
        "review_text": "Visiting Bali was an unforgettable journey! Tegallalang Rice Terraces completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-10-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Bali",
        "rating": 3,
        "review_text": "A mixed experience in Bali. Natural beauty and historical sites like Uluwatu Clifftop Temple are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2026-01-15",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Bali",
        "rating": 4,
        "review_text": "Wonderful holiday in Bali! The sightseeing at Tegallalang Rice Terraces was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-11-30",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Bali",
        "rating": 5,
        "review_text": "Magnificent atmosphere in Bali. From the breathtaking panorama at Uluwatu Clifftop Temple to the warm, courteous service from every guide, everything was exceptional. Transport was seamless and the vibrant heritage left a lasting impression on our entire family.",
        "review_date": "2024-09-17",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Bali",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Bali. Tegallalang Rice Terraces is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-04-27",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Bali",
        "rating": 3,
        "review_text": "A mixed experience in Bali. Natural beauty and historical sites like Uluwatu Clifftop Temple are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2025-03-05",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Prague",
        "rating": 5,
        "review_text": "Visiting Prague was an unforgettable journey! Prague Castle & St. Vitus Cathedral completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-09-29",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Prague",
        "rating": 4,
        "review_text": "The cultural depth of Prague is truly remarkable. Exploring Charles Bridge in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2026-01-17",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Prague",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Prague Castle & St. Vitus Cathedral in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Prague is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-10-23",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Prague",
        "rating": 4,
        "review_text": "Wonderful holiday in Prague! The sightseeing at Prague Castle & St. Vitus Cathedral was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2026-03-04",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Prague",
        "rating": 3,
        "review_text": "While Prague Castle & St. Vitus Cathedral is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2024-12-12",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Prague",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Prague. Prague Castle & St. Vitus Cathedral is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-01-15",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Prague",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Prague Castle & St. Vitus Cathedral in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Prague is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-07-14",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Prague",
        "rating": 3,
        "review_text": "A mixed experience in Prague. Natural beauty and historical sites like Charles Bridge are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2024-12-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Prague",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Prague. Prague Castle & St. Vitus Cathedral is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-11-17",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Prague",
        "rating": 2,
        "review_text": "Disappointed by our visit to Prague during peak season. Mass tourism has made Prague Castle & St. Vitus Cathedral overly crowded and chaotic with noisy tour groups. Several public restrooms lacked basic cleanliness and prices for bottled water and snacks were exorbitant. Local vendors were quite pushy.",
        "review_date": "2026-04-26",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Petra",
        "rating": 5,
        "review_text": "Visiting Petra was an unforgettable journey! The Treasury (Al-Khazneh) completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-09-22",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Petra",
        "rating": 4,
        "review_text": "The cultural depth of Petra is truly remarkable. Exploring The Siq Canyon Entrance in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2025-04-08",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Petra",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring The Treasury (Al-Khazneh) in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Petra is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-10-14",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Petra",
        "rating": 4,
        "review_text": "Wonderful holiday in Petra! The sightseeing at The Treasury (Al-Khazneh) was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2026-02-12",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Petra",
        "rating": 3,
        "review_text": "While The Treasury (Al-Khazneh) is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2024-10-22",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Petra",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Petra. The Treasury (Al-Khazneh) is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-07-05",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Petra",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring The Treasury (Al-Khazneh) in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Petra is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2026-01-18",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Reykjavik",
        "rating": 5,
        "review_text": "Visiting Reykjavik was an unforgettable journey! Hallgrimskirkja Church completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-06-30",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Reykjavik",
        "rating": 5,
        "review_text": "Our stay in Reykjavik exceeded all expectations. The room was spacious, comfortable, and maintained spotless cleanliness by attentive staff. Public transport and shuttle connectivity to Blue Lagoon & Sky Lagoon were remarkably punctual and efficient. Highly recommend this destination for both families and solo travellers!",
        "review_date": "2026-03-01",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Reykjavik",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Reykjavik. Hallgrimskirkja Church is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-10-30",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Reykjavik",
        "rating": 4,
        "review_text": "Wonderful holiday in Reykjavik! The sightseeing at Hallgrimskirkja Church was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-09-11",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Reykjavik",
        "rating": 5,
        "review_text": "Visiting Reykjavik was an unforgettable journey! Hallgrimskirkja Church completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-01-08",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Reykjavik",
        "rating": 3,
        "review_text": "A mixed experience in Reykjavik. Natural beauty and historical sites like Blue Lagoon & Sky Lagoon are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2024-03-13",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Reykjavik",
        "rating": 4,
        "review_text": "Wonderful holiday in Reykjavik! The sightseeing at Hallgrimskirkja Church was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-02-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Reykjavik",
        "rating": 5,
        "review_text": "Magnificent atmosphere in Reykjavik. From the breathtaking panorama at Blue Lagoon & Sky Lagoon to the warm, courteous service from every guide, everything was exceptional. Transport was seamless and the vibrant heritage left a lasting impression on our entire family.",
        "review_date": "2025-08-18",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Reykjavik",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Reykjavik. Hallgrimskirkja Church is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-12-29",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rome",
        "rating": 5,
        "review_text": "Visiting Rome was an unforgettable journey! The Colosseum completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-01-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rome",
        "rating": 4,
        "review_text": "The cultural depth of Rome is truly remarkable. Exploring Vatican Museums & Sistine Chapel in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2024-05-05",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rome",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring The Colosseum in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Rome is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-07-26",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rome",
        "rating": 4,
        "review_text": "Wonderful holiday in Rome! The sightseeing at The Colosseum was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2026-01-29",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rome",
        "rating": 3,
        "review_text": "While The Colosseum is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2026-01-12",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rome",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Rome. The Colosseum is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-04-12",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rome",
        "rating": 3,
        "review_text": "While The Colosseum is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2024-07-30",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rome",
        "rating": 2,
        "review_text": "Disappointed by our visit to Rome during peak season. Mass tourism has made The Colosseum overly crowded and chaotic with noisy tour groups. Several public restrooms lacked basic cleanliness and prices for bottled water and snacks were exorbitant. Local vendors were quite pushy.",
        "review_date": "2024-08-26",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rome",
        "rating": 5,
        "review_text": "Visiting Rome was an unforgettable journey! The Colosseum completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-08-30",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rome",
        "rating": 4,
        "review_text": "Wonderful holiday in Rome! The sightseeing at The Colosseum was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-11-25",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rome",
        "rating": 3,
        "review_text": "While The Colosseum is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2026-01-24",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rome",
        "rating": 5,
        "review_text": "Magnificent atmosphere in Rome. From the breathtaking panorama at Vatican Museums & Sistine Chapel to the warm, courteous service from every guide, everything was exceptional. Transport was seamless and the vibrant heritage left a lasting impression on our entire family.",
        "review_date": "2026-01-29",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Paris",
        "rating": 5,
        "review_text": "Visiting Paris was an unforgettable journey! Eiffel Tower completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-02-22",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Paris",
        "rating": 4,
        "review_text": "The cultural depth of Paris is truly remarkable. Exploring The Louvre Museum in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2024-07-02",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Paris",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Eiffel Tower in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Paris is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-10-30",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Paris",
        "rating": 4,
        "review_text": "Wonderful holiday in Paris! The sightseeing at Eiffel Tower was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-02-26",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Paris",
        "rating": 3,
        "review_text": "While Eiffel Tower is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2026-01-22",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Paris",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Paris. Eiffel Tower is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-08-19",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Paris",
        "rating": 3,
        "review_text": "While Eiffel Tower is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-06-22",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Paris",
        "rating": 2,
        "review_text": "Disappointed by our visit to Paris during peak season. Mass tourism has made Eiffel Tower overly crowded and chaotic with noisy tour groups. Several public restrooms lacked basic cleanliness and prices for bottled water and snacks were exorbitant. Local vendors were quite pushy.",
        "review_date": "2025-09-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Paris",
        "rating": 5,
        "review_text": "Visiting Paris was an unforgettable journey! Eiffel Tower completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2026-03-15",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Paris",
        "rating": 4,
        "review_text": "Wonderful holiday in Paris! The sightseeing at Eiffel Tower was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-09-07",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Paris",
        "rating": 3,
        "review_text": "While Eiffel Tower is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2024-08-26",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Paris",
        "rating": 5,
        "review_text": "Magnificent atmosphere in Paris. From the breathtaking panorama at The Louvre Museum to the warm, courteous service from every guide, everything was exceptional. Transport was seamless and the vibrant heritage left a lasting impression on our entire family.",
        "review_date": "2025-04-22",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Paris",
        "rating": 4,
        "review_text": "Wonderful holiday in Paris! The sightseeing at Eiffel Tower was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-02-08",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Tokyo",
        "rating": 5,
        "review_text": "Visiting Tokyo was an unforgettable journey! Shibuya Crossing & Hachiko completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-01-03",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Tokyo",
        "rating": 4,
        "review_text": "The cultural depth of Tokyo is truly remarkable. Exploring Senso-ji Temple (Asakusa) in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2024-02-22",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Tokyo",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Shibuya Crossing & Hachiko in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Tokyo is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-06-29",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Tokyo",
        "rating": 4,
        "review_text": "Wonderful holiday in Tokyo! The sightseeing at Shibuya Crossing & Hachiko was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-01-29",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Tokyo",
        "rating": 3,
        "review_text": "While Shibuya Crossing & Hachiko is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-01-18",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Tokyo",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Tokyo. Shibuya Crossing & Hachiko is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-07-11",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Tokyo",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Shibuya Crossing & Hachiko in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Tokyo is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-03-30",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Barcelona",
        "rating": 5,
        "review_text": "Visiting Barcelona was an unforgettable journey! Sagrada Familia Basilica completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-01-21",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Barcelona",
        "rating": 4,
        "review_text": "The cultural depth of Barcelona is truly remarkable. Exploring Park Guell in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2024-05-20",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Barcelona",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Sagrada Familia Basilica in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Barcelona is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-06-09",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Barcelona",
        "rating": 4,
        "review_text": "Wonderful holiday in Barcelona! The sightseeing at Sagrada Familia Basilica was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2026-02-02",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Barcelona",
        "rating": 3,
        "review_text": "While Sagrada Familia Basilica is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-08-05",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Barcelona",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Barcelona. Sagrada Familia Basilica is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-10-02",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Barcelona",
        "rating": 3,
        "review_text": "While Sagrada Familia Basilica is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2026-02-26",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Barcelona",
        "rating": 2,
        "review_text": "Disappointed by our visit to Barcelona during peak season. Mass tourism has made Sagrada Familia Basilica overly crowded and chaotic with noisy tour groups. Several public restrooms lacked basic cleanliness and prices for bottled water and snacks were exorbitant. Local vendors were quite pushy.",
        "review_date": "2025-07-17",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Barcelona",
        "rating": 5,
        "review_text": "Visiting Barcelona was an unforgettable journey! Sagrada Familia Basilica completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-02-02",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Barcelona",
        "rating": 4,
        "review_text": "Wonderful holiday in Barcelona! The sightseeing at Sagrada Familia Basilica was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-07-27",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Barcelona",
        "rating": 3,
        "review_text": "While Sagrada Familia Basilica is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2024-09-18",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Zermatt",
        "rating": 5,
        "review_text": "Visiting Zermatt was an unforgettable journey! The Matterhorn Peak completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-02-20",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Zermatt",
        "rating": 5,
        "review_text": "Our stay in Zermatt exceeded all expectations. The room was spacious, comfortable, and maintained spotless cleanliness by attentive staff. Public transport and shuttle connectivity to Gornergrat Railway & Viewpoint were remarkably punctual and efficient. Highly recommend this destination for both families and solo travellers!",
        "review_date": "2024-02-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Zermatt",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring The Matterhorn Peak in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Zermatt is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-07-15",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Zermatt",
        "rating": 4,
        "review_text": "Wonderful holiday in Zermatt! The sightseeing at The Matterhorn Peak was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-11-10",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Zermatt",
        "rating": 5,
        "review_text": "Visiting Zermatt was an unforgettable journey! The Matterhorn Peak completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-05-18",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Zermatt",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Zermatt. The Matterhorn Peak is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-03-30",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Zermatt",
        "rating": 4,
        "review_text": "Wonderful holiday in Zermatt! The sightseeing at The Matterhorn Peak was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-11-20",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Zermatt",
        "rating": 5,
        "review_text": "Magnificent atmosphere in Zermatt. From the breathtaking panorama at Gornergrat Railway & Viewpoint to the warm, courteous service from every guide, everything was exceptional. Transport was seamless and the vibrant heritage left a lasting impression on our entire family.",
        "review_date": "2025-07-14",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Zermatt",
        "rating": 3,
        "review_text": "While The Matterhorn Peak is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-06-24",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Zermatt",
        "rating": 5,
        "review_text": "Our stay in Zermatt exceeded all expectations. The room was spacious, comfortable, and maintained spotless cleanliness by attentive staff. Public transport and shuttle connectivity to Gornergrat Railway & Viewpoint were remarkably punctual and efficient. Highly recommend this destination for both families and solo travellers!",
        "review_date": "2024-12-02",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cairo",
        "rating": 5,
        "review_text": "Visiting Cairo was an unforgettable journey! Great Pyramids of Giza completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-11-01",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cairo",
        "rating": 4,
        "review_text": "The cultural depth of Cairo is truly remarkable. Exploring The Great Sphinx in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2024-09-08",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cairo",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Great Pyramids of Giza in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Cairo is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-06-17",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cairo",
        "rating": 4,
        "review_text": "Wonderful holiday in Cairo! The sightseeing at Great Pyramids of Giza was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-07-09",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cairo",
        "rating": 3,
        "review_text": "While Great Pyramids of Giza is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2026-02-05",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cairo",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Cairo. Great Pyramids of Giza is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-10-31",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cairo",
        "rating": 3,
        "review_text": "While Great Pyramids of Giza is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-11-26",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cairo",
        "rating": 2,
        "review_text": "Disappointed by our visit to Cairo during peak season. Mass tourism has made Great Pyramids of Giza overly crowded and chaotic with noisy tour groups. Several public restrooms lacked basic cleanliness and prices for bottled water and snacks were exorbitant. Local vendors were quite pushy.",
        "review_date": "2025-06-04",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cairo",
        "rating": 5,
        "review_text": "Visiting Cairo was an unforgettable journey! Great Pyramids of Giza completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-10-04",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cairo",
        "rating": 4,
        "review_text": "Wonderful holiday in Cairo! The sightseeing at Great Pyramids of Giza was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-08-06",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cairo",
        "rating": 3,
        "review_text": "While Great Pyramids of Giza is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2026-02-10",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cairo",
        "rating": 5,
        "review_text": "Magnificent atmosphere in Cairo. From the breathtaking panorama at The Great Sphinx to the warm, courteous service from every guide, everything was exceptional. Transport was seamless and the vibrant heritage left a lasting impression on our entire family.",
        "review_date": "2025-11-09",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cairo",
        "rating": 4,
        "review_text": "Wonderful holiday in Cairo! The sightseeing at Great Pyramids of Giza was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-05-04",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cusco",
        "rating": 5,
        "review_text": "Visiting Cusco was an unforgettable journey! Machu Picchu Sanctuary completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2026-04-21",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cusco",
        "rating": 4,
        "review_text": "The cultural depth of Cusco is truly remarkable. Exploring Sacsayhuaman Fortress in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2025-05-22",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cusco",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Machu Picchu Sanctuary in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Cusco is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-11-03",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cusco",
        "rating": 4,
        "review_text": "Wonderful holiday in Cusco! The sightseeing at Machu Picchu Sanctuary was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-11-05",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cusco",
        "rating": 3,
        "review_text": "While Machu Picchu Sanctuary is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-09-18",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cusco",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Cusco. Machu Picchu Sanctuary is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2026-02-13",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Cusco",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Machu Picchu Sanctuary in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Cusco is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-03-11",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Istanbul",
        "rating": 5,
        "review_text": "Visiting Istanbul was an unforgettable journey! Hagia Sophia Grand Mosque completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-06-04",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Istanbul",
        "rating": 4,
        "review_text": "The cultural depth of Istanbul is truly remarkable. Exploring Blue Mosque (Sultanahmet) in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2025-01-13",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Istanbul",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Hagia Sophia Grand Mosque in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Istanbul is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-01-03",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Istanbul",
        "rating": 4,
        "review_text": "Wonderful holiday in Istanbul! The sightseeing at Hagia Sophia Grand Mosque was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-12-22",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Istanbul",
        "rating": 3,
        "review_text": "While Hagia Sophia Grand Mosque is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2024-12-22",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Istanbul",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Istanbul. Hagia Sophia Grand Mosque is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-12-21",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Istanbul",
        "rating": 3,
        "review_text": "While Hagia Sophia Grand Mosque is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2024-04-04",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Istanbul",
        "rating": 2,
        "review_text": "Disappointed by our visit to Istanbul during peak season. Mass tourism has made Hagia Sophia Grand Mosque overly crowded and chaotic with noisy tour groups. Several public restrooms lacked basic cleanliness and prices for bottled water and snacks were exorbitant. Local vendors were quite pushy.",
        "review_date": "2026-04-15",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Istanbul",
        "rating": 5,
        "review_text": "Visiting Istanbul was an unforgettable journey! Hagia Sophia Grand Mosque completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-01-09",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Istanbul",
        "rating": 4,
        "review_text": "Wonderful holiday in Istanbul! The sightseeing at Hagia Sophia Grand Mosque was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-07-08",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Istanbul",
        "rating": 3,
        "review_text": "While Hagia Sophia Grand Mosque is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-02-18",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Bangkok",
        "rating": 5,
        "review_text": "Visiting Bangkok was an unforgettable journey! Grand Palace & Emerald Buddha completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-03-08",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Bangkok",
        "rating": 4,
        "review_text": "The cultural depth of Bangkok is truly remarkable. Exploring Wat Arun (Temple of Dawn) in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2024-08-17",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Bangkok",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Grand Palace & Emerald Buddha in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Bangkok is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-08-27",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Bangkok",
        "rating": 4,
        "review_text": "Wonderful holiday in Bangkok! The sightseeing at Grand Palace & Emerald Buddha was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-04-23",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Bangkok",
        "rating": 3,
        "review_text": "While Grand Palace & Emerald Buddha is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-05-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Bangkok",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Bangkok. Grand Palace & Emerald Buddha is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2026-02-15",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Bangkok",
        "rating": 3,
        "review_text": "While Grand Palace & Emerald Buddha is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2024-10-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Bangkok",
        "rating": 2,
        "review_text": "Disappointed by our visit to Bangkok during peak season. Mass tourism has made Grand Palace & Emerald Buddha overly crowded and chaotic with noisy tour groups. Several public restrooms lacked basic cleanliness and prices for bottled water and snacks were exorbitant. Local vendors were quite pushy.",
        "review_date": "2026-01-23",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Bangkok",
        "rating": 5,
        "review_text": "Visiting Bangkok was an unforgettable journey! Grand Palace & Emerald Buddha completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-06-02",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Bangkok",
        "rating": 4,
        "review_text": "Wonderful holiday in Bangkok! The sightseeing at Grand Palace & Emerald Buddha was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-10-05",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Bangkok",
        "rating": 3,
        "review_text": "While Grand Palace & Emerald Buddha is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2024-04-04",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Bangkok",
        "rating": 5,
        "review_text": "Magnificent atmosphere in Bangkok. From the breathtaking panorama at Wat Arun (Temple of Dawn) to the warm, courteous service from every guide, everything was exceptional. Transport was seamless and the vibrant heritage left a lasting impression on our entire family.",
        "review_date": "2024-09-04",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Amalfi Coast",
        "rating": 5,
        "review_text": "Visiting Amalfi Coast was an unforgettable journey! Positano Clifftop Village completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-09-12",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Amalfi Coast",
        "rating": 5,
        "review_text": "Our stay in Amalfi Coast exceeded all expectations. The room was spacious, comfortable, and maintained spotless cleanliness by attentive staff. Public transport and shuttle connectivity to Amalfi Cathedral were remarkably punctual and efficient. Highly recommend this destination for both families and solo travellers!",
        "review_date": "2024-10-02",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Amalfi Coast",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Positano Clifftop Village in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Amalfi Coast is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-10-10",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Amalfi Coast",
        "rating": 4,
        "review_text": "Wonderful holiday in Amalfi Coast! The sightseeing at Positano Clifftop Village was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-04-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Amalfi Coast",
        "rating": 5,
        "review_text": "Visiting Amalfi Coast was an unforgettable journey! Positano Clifftop Village completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-04-23",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Amalfi Coast",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Amalfi Coast. Positano Clifftop Village is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2026-04-12",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Amalfi Coast",
        "rating": 4,
        "review_text": "Wonderful holiday in Amalfi Coast! The sightseeing at Positano Clifftop Village was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-05-11",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Amalfi Coast",
        "rating": 5,
        "review_text": "Magnificent atmosphere in Amalfi Coast. From the breathtaking panorama at Amalfi Cathedral to the warm, courteous service from every guide, everything was exceptional. Transport was seamless and the vibrant heritage left a lasting impression on our entire family.",
        "review_date": "2025-04-11",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Amalfi Coast",
        "rating": 3,
        "review_text": "While Positano Clifftop Village is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2024-02-18",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Amalfi Coast",
        "rating": 5,
        "review_text": "Our stay in Amalfi Coast exceeded all expectations. The room was spacious, comfortable, and maintained spotless cleanliness by attentive staff. Public transport and shuttle connectivity to Amalfi Cathedral were remarkably punctual and efficient. Highly recommend this destination for both families and solo travellers!",
        "review_date": "2024-07-23",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Amalfi Coast",
        "rating": 4,
        "review_text": "The cultural depth of Amalfi Coast is truly remarkable. Exploring Amalfi Cathedral in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2024-09-22",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Grand Canyon",
        "rating": 5,
        "review_text": "Visiting Grand Canyon was an unforgettable journey! South Rim Trail & Mather Point completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-05-31",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Grand Canyon",
        "rating": 4,
        "review_text": "The cultural depth of Grand Canyon is truly remarkable. Exploring Bright Angel Trail in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2024-06-23",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Grand Canyon",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring South Rim Trail & Mather Point in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Grand Canyon is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-12-26",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Grand Canyon",
        "rating": 4,
        "review_text": "Wonderful holiday in Grand Canyon! The sightseeing at South Rim Trail & Mather Point was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-10-28",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Grand Canyon",
        "rating": 3,
        "review_text": "While South Rim Trail & Mather Point is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2024-07-21",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Grand Canyon",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Grand Canyon. South Rim Trail & Mather Point is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-06-02",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Grand Canyon",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring South Rim Trail & Mather Point in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Grand Canyon is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-03-18",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rio de Janeiro",
        "rating": 5,
        "review_text": "Visiting Rio de Janeiro was an unforgettable journey! Christ the Redeemer (Corcovado) completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-03-30",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rio de Janeiro",
        "rating": 4,
        "review_text": "The cultural depth of Rio de Janeiro is truly remarkable. Exploring Sugarloaf Mountain (Pao de Acucar) in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2024-09-20",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rio de Janeiro",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Christ the Redeemer (Corcovado) in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Rio de Janeiro is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-05-17",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rio de Janeiro",
        "rating": 4,
        "review_text": "Wonderful holiday in Rio de Janeiro! The sightseeing at Christ the Redeemer (Corcovado) was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2026-04-08",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rio de Janeiro",
        "rating": 3,
        "review_text": "While Christ the Redeemer (Corcovado) is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2024-08-07",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rio de Janeiro",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Rio de Janeiro. Christ the Redeemer (Corcovado) is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-12-15",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rio de Janeiro",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Christ the Redeemer (Corcovado) in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Rio de Janeiro is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-09-21",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Rio de Janeiro",
        "rating": 3,
        "review_text": "A mixed experience in Rio de Janeiro. Natural beauty and historical sites like Sugarloaf Mountain (Pao de Acucar) are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2024-12-19",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Singapore",
        "rating": 5,
        "review_text": "Visiting Singapore was an unforgettable journey! Gardens by the Bay & Cloud Forest completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-05-30",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Singapore",
        "rating": 4,
        "review_text": "The cultural depth of Singapore is truly remarkable. Exploring Marina Bay Sands SkyPark in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2024-11-12",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Singapore",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Gardens by the Bay & Cloud Forest in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Singapore is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-08-30",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Singapore",
        "rating": 4,
        "review_text": "Wonderful holiday in Singapore! The sightseeing at Gardens by the Bay & Cloud Forest was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-01-06",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Singapore",
        "rating": 3,
        "review_text": "While Gardens by the Bay & Cloud Forest is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2025-06-02",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Singapore",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Singapore. Gardens by the Bay & Cloud Forest is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2026-01-13",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Singapore",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Gardens by the Bay & Cloud Forest in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Singapore is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-01-11",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Singapore",
        "rating": 3,
        "review_text": "A mixed experience in Singapore. Natural beauty and historical sites like Marina Bay Sands SkyPark are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2025-09-21",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Singapore",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Singapore. Gardens by the Bay & Cloud Forest is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-07-10",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Sydney",
        "rating": 5,
        "review_text": "Visiting Sydney was an unforgettable journey! Sydney Opera House completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-01-26",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Sydney",
        "rating": 4,
        "review_text": "The cultural depth of Sydney is truly remarkable. Exploring Sydney Harbour Bridge in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2025-02-13",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Sydney",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Sydney Opera House in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Sydney is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-09-29",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Sydney",
        "rating": 4,
        "review_text": "Wonderful holiday in Sydney! The sightseeing at Sydney Opera House was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-04-21",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Sydney",
        "rating": 3,
        "review_text": "While Sydney Opera House is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2026-01-02",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Sydney",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Sydney. Sydney Opera House is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-07-19",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Sydney",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Sydney Opera House in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Sydney is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-06-20",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Sydney",
        "rating": 3,
        "review_text": "A mixed experience in Sydney. Natural beauty and historical sites like Sydney Harbour Bridge are top-tier, but local transport was congested and confusing to navigate. Our hotel room was clean though somewhat cramped for the nightly rate charged. Good for a quick 2-day visit rather than an extended holiday.",
        "review_date": "2024-09-01",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Sydney",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Sydney. Sydney Opera House is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-06-13",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Sydney",
        "rating": 2,
        "review_text": "Disappointed by our visit to Sydney during peak season. Mass tourism has made Sydney Opera House overly crowded and chaotic with noisy tour groups. Several public restrooms lacked basic cleanliness and prices for bottled water and snacks were exorbitant. Local vendors were quite pushy.",
        "review_date": "2026-02-23",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Edinburgh",
        "rating": 5,
        "review_text": "Visiting Edinburgh was an unforgettable journey! Edinburgh Castle completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2024-02-23",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Edinburgh",
        "rating": 4,
        "review_text": "The cultural depth of Edinburgh is truly remarkable. Exploring The Royal Mile in the morning allowed us to avoid midday heat. Safe atmosphere at night with plenty of security personnel around major landmarks. Food was tasty and authentic, though some tourist menus were slightly marked up in price.",
        "review_date": "2026-01-01",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Edinburgh",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Edinburgh Castle in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Edinburgh is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2025-07-06",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Edinburgh",
        "rating": 4,
        "review_text": "Wonderful holiday in Edinburgh! The sightseeing at Edinburgh Castle was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2024-02-25",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Edinburgh",
        "rating": 3,
        "review_text": "While Edinburgh Castle is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2024-04-03",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Edinburgh",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Edinburgh. Edinburgh Castle is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2025-06-03",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Edinburgh",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Edinburgh Castle in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Edinburgh is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-04-06",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Maui",
        "rating": 5,
        "review_text": "Visiting Maui was an unforgettable journey! Haleakala National Park completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2025-07-02",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Maui",
        "rating": 5,
        "review_text": "Our stay in Maui exceeded all expectations. The room was spacious, comfortable, and maintained spotless cleanliness by attentive staff. Public transport and shuttle connectivity to Road to Hana Highway were remarkably punctual and efficient. Highly recommend this destination for both families and solo travellers!",
        "review_date": "2024-12-03",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Maui",
        "rating": 5,
        "review_text": "An absolute gem of a destination! Exploring Haleakala National Park in the early morning provided glorious, uninterrupted views and peaceful serenity. The culinary culture in Maui is top-notch, with fresh regional delicacies at welcoming bistros. Felt completely safe and well looked after at all hours.",
        "review_date": "2024-11-03",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Maui",
        "rating": 4,
        "review_text": "Wonderful holiday in Maui! The sightseeing at Haleakala National Park was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2026-05-02",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Maui",
        "rating": 5,
        "review_text": "Visiting Maui was an unforgettable journey! Haleakala National Park completely took our breath away with its stunning architecture and majestic views. The local food was delicious and every meal was a delight. The local residents and tour guides showed extraordinary hospitality throughout our stay. Spotless streets and safe neighbourhoods made walking everywhere a joy.",
        "review_date": "2026-05-14",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Maui",
        "rating": 4,
        "review_text": "Really enjoyed our time discovering Maui. Haleakala National Park is an impressive site with well-maintained facilities and informative plaques. Hotel accommodation was clean and cosy. A bit bustling around midday tram stops, but very manageable with walking shoes.",
        "review_date": "2024-09-05",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Maui",
        "rating": 4,
        "review_text": "Wonderful holiday in Maui! The sightseeing at Haleakala National Park was fabulous and we captured spectacular panoramic photos. Street cafes and traditional eateries served flavourful dishes at reasonable rates. The only minor inconvenience was finding metered taxis during evening hours, but overall the trip offered fantastic value for money.",
        "review_date": "2025-07-01",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Maui",
        "rating": 5,
        "review_text": "Magnificent atmosphere in Maui. From the breathtaking panorama at Road to Hana Highway to the warm, courteous service from every guide, everything was exceptional. Transport was seamless and the vibrant heritage left a lasting impression on our entire family.",
        "review_date": "2025-12-20",
        "data_source": "curated_demonstration_corpus"
    },
    {
        "destination_name": "Maui",
        "rating": 3,
        "review_text": "While Haleakala National Park is undeniably iconic and magnificent, the overwhelming crowds and endless queues tested our patience. Entry tickets and nearby restaurants were quite expensive and felt slightly overpriced. Food quality was decent, but you must reserve tables well in advance to avoid long waits.",
        "review_date": "2026-04-25",
        "data_source": "curated_demonstration_corpus"
    }
]

print(f"Loaded {len(REVIEWS)} curated reviews across 54 destinations.")
