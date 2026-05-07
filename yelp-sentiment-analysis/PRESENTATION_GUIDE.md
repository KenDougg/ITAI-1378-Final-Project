# Presentation Guide: 12-Slide Deck
## Yelp Sentiment Analysis - Group 5 | 10-Minute Presentation

**File:** `docs/Yelp_Sentiment_Analysis_Presentation.pptx`  
**Duration:** 10 minutes (7-8 min content, 2-3 min for Q&A)  
**Created:** Automatically generated with `python-pptx`

---

## Slide Breakdown & Speaking Notes

### **Slide 1: Title Slide** (30 seconds)
**Title:** Sentiment Analysis  
**Subtitle:** Analyzing Customer Reviews from Yelp

**Speaking Points:**
- "Good morning everyone, I'm [name] from Group 5"
- "Today we're presenting our work on sentiment analysis of Yelp reviews"
- "This project took the feedback from 1,000 real customer reviews and built a machine learning system to automatically classify sentiment"
- Acknowledge team members and professor

**Tone:** Professional, enthusiastic

---

### **Slide 2: The Problem** (1-1.5 minutes)
**Title:** The Problem

**Key Points on Slide:**
- Challenge: Thousands of reviews monthly
- Question: How to understand customer sentiment automatically?
- Issue: Manual analysis takes ~1 hour per 100 reviews
- Opportunity: Build an ML system
- Impact: Save 20+ hours/month + identify satisfaction drivers

**Speaking Points:**
- "Businesses like restaurants receive thousands of customer reviews every month across platforms like Yelp"
- "The challenge is: how can we efficiently understand what customers are saying?"
- "Right now, many businesses manually read reviews, which is expensive and slow"
- "We wanted to build a system that could automatically classify reviews as positive, negative, or neutral"
- "If we can classify reviews automatically, we can save time and immediately identify the most important feedback"

**Interactive Element:** Ask audience - "How many of you read restaurant reviews before visiting?"

---

### **Slide 3: Business Impact** (1 minute)
**Title:** Why Does This Matter?

**Key Points:**
- ✅ Triage Negative Reviews: Auto-flag urgent feedback
- 📊 Track Trends: Monitor sentiment over time
- 🎯 Target Marketing: Extract positive keywords
- 🔍 Root Cause Analysis: Identify common complaints
- ⚡ Real-time Response: Respond to feedback faster

**Speaking Points:**
- "Imagine you're a restaurant manager. You get 500 reviews this month."
- "With our system, you get instant notifications: 'We found 12 negative reviews that need urgent attention'"
- "You can respond to angry customers within hours instead of weeks"
- "You can also see: what words appear most in positive reviews? 'Great service', 'delicious food', 'friendly staff'"
- "You use those insights to train your team and in your marketing"

**Connection:** "This is why sentiment analysis matters in the real world"

---

### **Slide 4: Our Dataset** (1 minute)
**Title:** Our Dataset: Yelp Reviews

**Key Points:**
- Source: Hugging Face yelp_review_full (650,000+ reviews)
- Sample Used: 1,000 reviews
- Classes: Negative (40%), Positive (39%), Neutral (20%)
- Split: 80% train / 20% test

**Speaking Points:**
- "We used the Yelp dataset from Hugging Face, which has over 650,000 reviews"
- "We sampled 1,000 reviews for our project—manageable size for fast development"
- "Each review is labeled with a star rating from 1-5"
- "We mapped these to three sentiment categories"
- "Our training set had 800 reviews, and we tested on 200 completely unseen reviews"
- "This 80/20 split gives us a realistic estimate of how the model will perform in the real world"

**Key Insight:** "The real challenge we discovered: only 20% of reviews are neutral (3 stars). This imbalance matters!"

---

### **Slide 5: Technical Approach** (1.5 minutes)
**Title:** Our Approach: TF-IDF + Machine Learning

**Key Steps:**
1. Preprocessing (lowercase, remove URLs, lemmatize)
2. Feature Extraction (5,000 TF-IDF features)
3. Model Training (two models to compare)
4. Evaluation (multiple metrics)
5. Prediction (classify new reviews)

**Speaking Points:**
- "First, we preprocess the text. Reviews are messy—they have typos, URLs, punctuation"
- "We make everything lowercase, remove noise, and convert words to their base forms"
- "Example: 'I love the restaurant!' becomes 'love restaurant'"
- ""Then we convert text to numbers using TF-IDF. Think of it as importance scores for each word"
- "We extract 5,000 features—basically the 5,000 most important words in the dataset"
- "Then we train ML models on these features to learn patterns"
- "Finally, we test on data the models have never seen before"

**Visual:** Point to the pipeline diagram on the slide

---

### **Slide 6: Models Compared** (1 minute)
**Title:** Two Models Trained & Compared

**Left Column - Logistic Regression:**
- Interpretable
- Fast training
- Accuracy: 67.5%

**Right Column - Naive Bayes (Best):**
- Very fast (0.02 sec) ⭐
- Competitive accuracy
- Accuracy: 68.0% 🏆

**Speaking Points:**
- "We experimented with two different machine learning models"
- "Logistic Regression is a classic model used for classification—very interpretable"
- "Naive Bayes is simpler and even faster—trains in 20 milliseconds!"
- "Interestingly, both had similar accuracy around 68%"
- "Naive Bayes was slightly faster and just as accurate, so we used that as our final model"
- "68% might sound modest, but this is quite good for a 3-class problem with class imbalance"

**Key Point:** "We chose Naive Bayes because of its balance of speed and accuracy"

---

### **Slide 7: What Worked Well ✓** (1 minute)
**Title:** What Worked Well ✓

**Key Results:**
- 🟢 Positive Reviews: 86% correctly identified
- 🔴 Negative Reviews: 86% correctly identified
- ⚡ Fast Training: Naive Bayes trained in 0.02 seconds
- 📊 Clear Separation: Strong vs. weak sentiments are separable
- ✅ Overall Accuracy: 68% on unseen test data

**Speaking Points:**
- "The good news: our model is really good at identifying strongly positive and negative reviews"
- "When someone writes 'Great service!' or 'Terrible experience, never going back!', the model gets it right 86% of the time"
- "The model learns that words like 'love', 'great', 'amazing' predict positive reviews"
- "And words like 'bad', 'terrible', 'disappointing' predict negative reviews"
- "Plus, it's incredibly fast—processes hundreds of reviews per second"

**Confidence Builder:** "This is solid performance for a first model"

---

### **Slide 8: The Challenge ✗** (1.5 minutes)
**Title:** The Challenge: Neutral Class ✗

**Key Problem:**
- 🟡 Neutral (3-star) Reviews: 0% accuracy (ALL misclassified)
- ❌ Why:
  - Class Imbalance: 204 neutral vs 400+ positive/negative
  - Ambiguous Language: 3-star reviews mix good and bad
  - TF-IDF Limitation: Can't understand context
- 💡 Silver Lining: Real problem, documented insight

**Speaking Points:**
- "Now, the challenge: our model completely failed on neutral reviews"
- "All 41 neutral reviews in our test set were misclassified"
- "This might sound like a failure, but it's actually a really important discovery"
- "There are three reasons:"
  - "First, **class imbalance**. We only had 204 neutral reviews compared to 400+ positive and negative. The model learned that positive and negative are more common, so it defaults to those"
  - "Second, **3-star reviews are inherently ambiguous**. They often have mixed sentiment: 'Great food, but slow service' or 'Nice place, but expensive'"
  - "Third, **TF-IDF limitation**. Our feature extraction can't understand context or nuance. It sees 'good' and 'bad' independently, not 'good... but bad'"
- "This is actually really valuable—we now understand the problem!"

**Key Insight:** "Understanding failures is just as important as celebrating successes"

---

### **Slide 9: Real Examples** (1.5 minutes)
**Title:** Real Examples: Successes vs. Failures

**Success Case 1:**
- Text: "Love this place! Best restaurant in town."
- Predicted: POSITIVE ✓ (92% confidence)

**Success Case 2:**
- Text: "Terrible experience. Cold food, rude staff."
- Predicted: NEGATIVE ✓ (87% confidence)

**Failure Case:**
- Text: "Nice place, but food quality is mediocre."
- Actual: NEUTRAL
- Predicted: POSITIVE ✗ (72% confidence)

**Speaking Points:**
- "Let me show you specific examples"
- "Here's a success: 'Love this place! Best restaurant in town.' The model correctly predicted positive, with 92% confidence"
- "Here's another success: 'Terrible experience. Cold food, rude staff.' Correctly predicted negative with 87% confidence"
- "Now a failure: 'Nice place, but food quality is mediocre.' This is actually a neutral (3-star) review—the person likes some aspects but has complaints"
- "But our model saw 'Nice place' and predicted positive. Why? Because positive sentiment words appeared in training data more frequently in positive reviews"
- "The model didn't understand the balancing 'but'—that there's also a complaint"

**Analysis:** "This perfectly illustrates why the neutral class is hard"

---

### **Slide 10: Key Learnings** (1 minute)
**Title:** Key Learnings

**Takeaways:**
- 🧠 Text Preprocessing Matters: Big accuracy boost
- 🎯 Simple Models Work: Competitive with complex methods
- ⚖️ Class Imbalance is Real: Minority classes get ignored
- 📚 TF-IDF Limitations: Ignores word order, context, sarcasm
- ✍️ Honest Analysis: Understanding failures is valuable

**Speaking Points:**
- "What did we learn from building this model?"
- "First: **preprocessing matters**. When we added lemmatization and stopword removal, accuracy improved by ~5%"
- "Second: **simple models work well**. Naive Bayes is much simpler than deep learning, trained instantly, and performed just as well"
- "Third: **class imbalance is a real problem**. In real-world data, minority classes often get ignored by default"
- "Fourth: **TF-IDF has limitations**. It doesn't understand 'not good' as negative—it treats 'not', 'good' separately"
- "Finally: **honest analysis beats perfect metrics**. Acknowledging that our model fails on neutral reviews is more valuable than claiming 68% means we solved the problem"

---

### **Slide 11: Future Improvements** (1 minute)
**Title:** Next Steps: Future Improvements

**Quick Wins:**
- Use SMOTE to balance classes (→ 70-72% accuracy)
- Implement class weights

**Advanced:**
- BERT Transformers: Understand context (→ 75%+ accuracy)
- Aspect-Based Sentiment: Food/service scores separately
- Collect more neutral examples

**Production:**
- Deploy with confidence thresholds
- Build API for business integration

**Speaking Points:**
- "Now, how would we improve this for the real world?"
- "**Quick wins**: We could use SMOTE to artificially balance our training data, which could boost accuracy to 70-72%"
- "**Advanced approaches**: We could switch to BERT, a transformer model that understands context. That would handle 'good... but bad' correctly"
- "**Strategic**: We could build an aspect-based system that gives separate scores for food, service, ambiance—more useful for restaurants"
- "**Production**: We could add confidence thresholds—'only flag this review if I'm more than 85% sure it's negative'"

**Call to Action:** "This is a solid foundation for future work"

---

### **Slide 12: Q&A** (2-3 minutes)
**Title:** Questions?

**Subtitle:** 68% Accuracy • Strong Foundation • Clear Path Forward

**Talking Points Ready:**
Have these ready for likely questions:

**Q: Why is 68% accuracy good?**
- "68% is solid for a 3-class problem with class imbalance. Random guessing would be 33%. We're 2x better."

**Q: Can you use this in production?**
- "Yes, but with caution. Use it to auto-flag strong 1-2 star reviews for urgent response. Don't rely on it for neutral classification yet."

**Q: Why not use deep learning (BERT)?**
- "BERT would help, but Naive Bayes is 1000x faster to train, easier to debug, and nearly as accurate. We chose the right tool for the job."

**Q: How did you handle class imbalance?**
- "We acknowledged it and plan to use SMOTE next. For now, we're using stratified splitting to maintain proportions in train/test sets."

**Q: What would you do differently?**
- "Collect more neutral examples before training. Use BERT for better context understanding. Build aspect-based system instead of single score."

**Closing Statement:**
"Thank you for your attention. Our code, documentation, and models are all on GitHub for anyone who wants to build on this work. We're happy to answer questions!"

---

## Presentation Tips

### **Timing Breakdown** (10 minutes total)
- Slide 1 (Title): 30 sec
- Slides 2-5 (Problem/Data/Approach): 4 min
- Slides 6-9 (Models/Results): 3 min
- Slides 10-11 (Learnings/Future): 1.5 min
- Slide 12 (Q&A): 1 min intro, then 2-3 min for questions

### **Delivery Tips**

✅ **DO:**
- Make eye contact with your audience
- Speak clearly and confidently
- Use hand gestures to point to slides
- Tell stories with the examples (Slides 9)
- Own the failures—they show maturity
- Have fun! You did cool work

❌ **DON'T:**
- Read text directly from slides
- Talk too fast through results
- Hide the neutral class issue (embrace it!)
- Use jargon without explaining (TF-IDF, lemmatization, etc.)
- Apologize for 0% on neutral—it's a real problem with a real cause

### **Engagement Ideas**

1. **Icebreaker** (Slide 2): "How many of you read reviews before visiting restaurants?" (Show of hands)
2. **Thought Experiment** (Slide 3): "You run a restaurant. You get 500 reviews. How long to read them all?"
3. **Live Q&A** (Slide 9): "Why do you think we failed on this review?"
4. **Challenge Question**: "What would you do to improve the neutral class detection?"

### **Handling Questions**

**If someone asks something you don't know:**
- "That's a great question. I don't have the answer right now, but I'd love to research it."
- "Let me make a note of that—it's definitely something to explore."

**If criticism comes up:**
- "You're absolutely right. Class imbalance is a known issue, and that's exactly why SMOTE is a great next step."
- "I appreciate the feedback. That demonstrates exactly why honest analysis is important."

---

## File Info

**Generated:** May 7, 2026  
**Generator:** `create_presentation.py` (python-pptx)  
**Slides:** 12  
**File Size:** 44 KB  
**Format:** Microsoft PowerPoint 2007+ .pptx

**To Edit:**
- Open in PowerPoint, Google Slides, or LibreOffice Impress
- Customize colors, fonts, logos as needed
- Add company/university branding
- Replace placeholder names with your own

**To Regenerate:**
```bash
python create_presentation.py
```

---

## Last-Minute Checklist

Before presenting:
- [ ] Test the presentation on the actual projector/screen
- [ ] Have a backup on USB or cloud (Google Drive, OneDrive)
- [ ] Practice the entire presentation once (7-8 minutes)
- [ ] Memorize your opening and closing lines
- [ ] Have water nearby (helps with dry mouth)
- [ ] Arrive 5 minutes early to set up
- [ ] Have a pen handy for notes on questions

---

**Good luck! You've got this! 🎉**
