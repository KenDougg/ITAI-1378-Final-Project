# Presentation Outline: Yelp Sentiment Analysis
## ITAI 1378 - Group 5

### Slide 1: Title Slide
**Content:**
- **Title:** Sentiment Analysis of Yelp Reviews
- **Subtitle:** Bridging customer feedback to business insights
- **Group Members:** Esbeide Ibarra, Joel Garza, Nhat Nam Khanh Nguyen
- **Course:** ITAI 1378 - Final Project
- **Professor:** Viswanatha Rao
- **Date:** May 2026

**Visual:** Simple, professional design with Yelp logo reference or sentiment emoji

---

### Slide 2: Problem Definition & Business Impact
**Title:** Why Does Sentiment Analysis Matter?

**Content:**
> "Businesses receive thousands of customer reviews, but manually analyzing them is time-consuming and inefficient."

**The Problem:**
- ✗ Manual review reading is slow (one person = ~5-10 reviews/hour)
- ✗ Missing patterns in customer feedback
- ✗ Slow response to negative reviews
- ✗ Difficulty identifying satisfaction drivers

**The Question:**
"Can we automatically classify customer sentiment from review text?"

**Business Impact:**
- 💰 Save 20+ hours/month on review analysis
- 📊 Identify trends quickly (monthly sentiment score)
- ⚡ Prioritize urgent negative feedback for fast response
- 📈 Track improvement over time

**Visual:** Diagram showing manual vs. automated workflow
```
Manual:          AI System:
Read review  →   [Model]
Think...     →   Instant
Classify...  →   Sentiment Label
```

---

### Slide 3: Dataset & Approach
**Title:** Data: 1,000 Yelp Reviews | Method: TF-IDF + Machine Learning

**Dataset:**
- **Source:** Hugging Face yelp_review_full (650K+ reviews)
- **Sample:** 1,000 reviews (manageable size for iteration)
- **Classes:** 
  - Negative (1-2 stars): 404 reviews (40.4%)
  - Positive (4-5 stars): 392 reviews (39.2%)
  - Neutral (3 stars): 204 reviews (20.4%)

**Technical Approach:**
```
Original Text
    ↓
[Preprocessing] - Remove stopwords, lemmatize
    ↓
[TF-IDF] - Convert to 5,000 numerical features
    ↓
[Train Models] - Logistic Regression & Naive Bayes
    ↓
[Evaluate] - Accuracy, Precision, Recall, F1-Score
    ↓
[Sentiment] - Negative / Neutral / Positive
```

**Preprocessing Steps:**
1. Lowercase
2. Remove URLs & special characters
3. Tokenize
4. Remove stopwords
5. Lemmatization

**Visual:** Show example before/after preprocessing
- Before: "Thanks Yelp! I was looking for... bad reception!!!"
- After: "thanks yelp looking bad reception"

---

### Slide 4: Model Training & Validation
**Title:** Two Models Trained & Compared

**Models:**
1. **Logistic Regression**
   - Fast, interpretable
   - 67.5% accuracy
   
2. **Naive Bayes** ✓ WINNER
   - Fast (0.02 sec training)
   - 68% accuracy (slightly better)

**Validation Strategy:**
- **Train/Test Split:** 80% / 20% (stratified to maintain class distribution)
- **Training Set:** 800 reviews
- **Test Set:** 200 reviews (unseen data)

**Per-Class Performance:**
| Class | Precision | Recall | F1-Score |
|-------|-----------|--------|----------|
| Negative | 66% | 86% | 0.75 |
| **Neutral** | **0%** | **0%** | **0.00** ⚠️ |
| Positive | 70% | 86% | 0.77 |

**Key Finding:** Neutral class FAILS due to class imbalance & ambiguous language

**Visual:** Confusion matrix heatmap showing:
- Strong diagonal for Positive/Negative
- All Neutral samples misclassified

---

### Slide 5: Results & Performance Analysis
**Title:** What Worked & What Didn't

**Success Cases ✓**
- Positive reviews: 86% correctly identified
- Negative reviews: 86% correctly identified
- Model easily distinguishes "Great!" from "Terrible!"

**Example Success:**
```
"Love this place! Best restaurant in town 
 with amazing food and friendly staff."
→ Predicted: POSITIVE ✓ (Confidence: 92%)
```

**Failure Cases ✗**
- Neutral reviews: 0% correctly identified (all 41 samples misclassified!)
- Sarcasm not detected
- Mixed sentiments ("good food, bad service") confused

**Example Failure:**
```
"Service was slow and food was just okay. 
 Nothing special but not bad."
→ Actual: NEUTRAL (3 stars)
→ Predicted: NEGATIVE ✗ (Confidence: 67%)
```

**Why Neutral Failed:**
- Too few training examples (204 vs 400+ for others)
- Ambiguous language naturally present in 3-star reviews
- TF-IDF ignores context ("good...but bad" reads as positive + negative)

**Visual:** Side-by-side confusion matrices showing where model struggles

---

### Slide 6: Key Learnings & Future Work
**Title:** What We Learned & Next Steps

**Key Findings:**
1. ✓ Text preprocessing is crucial (stopwords + lemmatization boost accuracy)
2. ✓ Simple ML models (Naive Bayes) work well for text classification
3. ✓ Strong sentiments (1-2 / 4-5 stars) are easily separable
4. ✗ Class imbalance is a real and challenging problem
5. ✗ TF-IDF can't capture context or sarcasm

**Limitations Encountered:**
- Class imbalance (neutral underrepresented)
- No context awareness (can't understand "good X but bad Y")
- Sarcasm not detected
- English-only support

**Future Improvements (Priority Order):**
1. **Quick Win:** Apply SMOTE to balance classes
2. **Medium:** Implement class weights in model
3. **Advanced:** Use BERT/Transformers for context understanding
4. **Long-term:** Build aspect-based sentiment (food/service/ambiance separately)

**Takeaway Message:**
"68% accuracy is a solid baseline for real-world deployment. Focus should now shift to handling edge cases (neutral reviews) and deploying with confidence thresholds."

**Visual:** Roadmap showing simple → advanced approaches
```
Current: TF-IDF + NB (68%)
    ↓
Next: SMOTE + Class Weights (70-72%)
    ↓
Future: BERT Transformers (75-80%)
    ↓
Advanced: Aspect-Based AI (per-dimension sentiment)
```

---

## Presentation Notes for Speakers

### Timing
- **Slide 1 (Title):** 30 seconds - Quick intro
- **Slide 2 (Problem):** 1-1.5 min - Set context, build urgency
- **Slide 3 (Dataset/Method):** 1.5-2 min - Technical details, show example
- **Slide 4 (Models/Validation):** 1-1.5 min - Explain approach quickly
- **Slide 5 (Results):** 1.5-2 min - Show successes & failures honestly
- **Slide 6 (Learnings):** 1-1.5 min - Conclude with takeaways & future

**Total: 7-8 minutes** (leaves 2 min for questions in 10-min slot)

### Delivery Tips
- Lead with the business problem (why customers care)
- Show real examples of correct predictions (build confidence)
- Be HONEST about failures (show neutral class completely missed)
- End on positive note (this is a solid baseline, clear path forward)
- Avoid jargon; explain TF-IDF, precision, recall in simple terms
- Use visuals to break up text-heavy slides

### Common Questions & Answers

**Q: Why did the model fail on neutral reviews?**
A: Two reasons: (1) We only had 204 neutral examples vs 400+ for other classes, and (2) 3-star reviews are genuinely ambiguous—"good food, slow service"—so hard to classify even for humans.

**Q: Can you deploy this in production?**
A: YES, but with caution. Use it to auto-flag strong 1-2 star reviews for urgent attention. Don't rely on it for neutral classification yet. With class balancing, we could hit 70%+.

**Q: Why not use deep learning (BERT)?**
A: Great question for future work! BERT would help with context but takes much longer to train. For this scope, Naive Bayes is 1000x faster and still effective.

**Q: How did you validate results?**
A: We split data 80/20 into train & test sets. The 68% accuracy is on completely unseen test data, so it's a realistic estimate.

**Q: What would you do differently?**
A: (1) Collect more neutral examples first, (2) Use class weights or SMOTE to handle imbalance, (3) Try BERT for better context, (4) Build aspect-based system (food/service separately).

---

**Presentation Design Notes:**
- Keep slides clean and visual (avoid bullet-point overload)
- Use consistent color scheme (sentiment colors: 🔴 red/negative, 🟡 yellow/neutral, 🟢 green/positive)
- Include at least one chart/visualization per slide
- Use large fonts (min 24pt)
- Show real examples of successful predictions to build credibility
- End with forward-looking roadmap (inspires confidence in team)
