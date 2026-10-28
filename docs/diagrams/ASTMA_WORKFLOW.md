# ASTMA_WORKFLOW.md — Aspect-Sentiment Tourism Mining & Analytics Pipeline

**Specialization:** Aspect-Sentiment Tourism Mining & Analytics (ASTMA)  
**Standard:** Text Mining & Machine Learning Pipeline Architecture  
**Inputs:** Unstructured Natural Language Tourist Reviews  
**Outputs:** 3-Class Sentiment Polarity, Confidence Scores, 9-Aspect Sentiment Ratings, Keyphrases, and Visual Aggregations  

---

## 1. Complete ASTMA Workflow Diagram

```mermaid
graph TD
    RawInput["1. Raw Tourist Review Text<br><i>'The bamboo forest was magical and serene, but the shrines were crowded and overpriced.'</i>"]
    
    subgraph Preprocessing["2. Text Preprocessing Pipeline"]
        P1["Unicode & Case Normalization (lower)"]
        P2["Contraction Expansion ('can't' $\rightarrow$ 'cannot')"]
        P3["Punctuation & HTML Stripping"]
        P4["Clause & Sentence Segmentation (delimiters: '.', ';', 'but', 'however')"]
        P5["Stopword Filtering with Negation Preservation ('not', 'never', 'hardly')"]
    end

    subgraph FeatureExtraction["3. Numerical Vectorization"]
        TFIDF["Sublinear TF-IDF Vectorizer<br>• N-Gram Range: (1, 2) unigrams & bigrams<br>• Min DF: 3 | Max Features: 8,000"]
    end

    subgraph SentimentModel["4. Supervised Sentiment Classification"]
        LogReg["Multinomial Logistic Regression Classifier<br>• Regularization: L2 (C=1.0)<br>• Solver: L-BFGS<br>• Class Weight: Balanced"]
        Softmax["Calibrated Probability Estimation (predict_proba)"]
    end

    subgraph PolarityOutput["5. Sentiment Polarity"]
        Pos["Positive"]
        Neu["Neutral"]
        Neg["Negative"]
    end

    subgraph AspectEngine["6. 9-Aspect Semantic Clause Extraction"]
        AspectLex["Domain Tourism Lexicons & Context Search"]
        subgraph NineAspects["The 9 Tourism Dimensions"]
            A1["1. Attractions (temple, scenery, views)"]
            A2["2. Food (restaurant, dining, meal, taste)"]
            A3["3. Cleanliness (spotless, tidy, hygiene)"]
            A4["4. Price (expensive, value, budget, cost)"]
            A5["5. Crowd (packed, quiet, tourists, serene)"]
            A6["6. Safety (secure, night, walking, danger)"]
            A7["7. Transport (bus, metro, taxi, train, access)"]
            A8["8. Accommodation (hotel, bed, room, resort)"]
            A9["9. Hospitality (staff, friendly, host, welcome)"]
        end
        NegationLogic["Negation Inversion Engine<br><i>('not clean' $\rightarrow$ Negative)</i>"]
    end

    subgraph KeywordEngine["7. Keyphrase & Salience Extraction"]
        KW["Destination TF-IDF Term Weighting<br><i>Isolates high-frequency descriptive nouns & adjectives</i>"]
    end

    subgraph Aggregation["8. Destination-Level Aggregation"]
        AggMath["Mathematical Aggregation:<br>• Review Count & Average Star Rating<br>• Sentiment Proportions (Pos %, Neu %, Neg %)<br>• Aspect Sentiment Scores (0 to 100 per dimension)<br>• No-data handling (null if 0 mentions)"]
    end

    subgraph Visualization["9. Interactive Information Visualization"]
        V1["Aspect Radar Chart (Multi-axis profile)"]
        V2["Sentiment Ring Chart (Proportion breakdown)"]
        V3["Monthly Time-Series Trends (Volume & rating)"]
        V4["Highlight Badges & Review Explorer"]
    end

    %% Pipeline Data Connections
    RawInput --> Preprocessing
    Preprocessing --> TFIDF
    TFIDF --> LogReg
    LogReg --> Softmax
    Softmax --> PolarityOutput
    PolarityOutput --> Aggregation

    Preprocessing --> AspectEngine
    AspectEngine --> NineAspects
    NineAspects --> NegationLogic
    NegationLogic --> Aggregation

    Preprocessing --> KeywordEngine
    KeywordEngine --> Aggregation

    Aggregation --> Visualization
```

---

## 2. Mathematical Pipeline Formulation

### 2.1 Term Frequency-Inverse Document Frequency (TF-IDF)
For term $t$ in review $d$ across corpus $D$:
$$\text{TF}(t, d) = 1 + \ln(f_{t, d}) \quad \text{for } f_{t, d} > 0$$
$$\text{IDF}(t, D) = \ln\left(\frac{1 + |D|}{1 + |\{d \in D : t \in d\}|}\right) + 1$$
$$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \text{IDF}(t, D)$$

### 2.2 Multinomial Logistic Regression Polarity Classifier
For input feature vector $\mathbf{x} \in \mathbb{R}^{8000}$ and class $k \in \{\text{negative}, \text{neutral}, \text{positive}\}$:
$$P(y = k \mid \mathbf{x}) = \frac{\exp(\mathbf{w}_k^T \mathbf{x} + b_k)}{\sum_{j=1}^{3} \exp(\mathbf{w}_j^T \mathbf{x} + b_j)}$$
$$\hat{y} = \arg\max_{k \in \{1, 2, 3\}} P(y = k \mid \mathbf{x})$$

### 2.3 Aspect Polarity Index
For aspect $a \in \{1, \dots, 9\}$ of destination $d$, aggregating $N_{a}$ mentioned clauses:
$$\text{Score}(d, a) = \begin{cases}
\text{null} & \text{if } N_a = 0 \\
\left(\frac{N_{a, \text{pos}} + 0.5 \cdot N_{a, \text{neu}}}{N_a}\right) \times 100 & \text{if } N_a > 0
\end{cases}$$
This ensures destinations with zero review data for a specific aspect are transparently shown as `"No data yet"` rather than falsely penalized with a score of 0/100.
