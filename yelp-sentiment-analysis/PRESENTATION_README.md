# Presentation Materials - Quick Access Guide

**Last Updated:** May 7, 2026  
**Status:** ✅ Ready for 10-Minute Presentation

---

## 📺 PowerPoint Presentation

**File:** `docs/Yelp_Sentiment_Analysis_Presentation.pptx`

### Quick Facts:
- 📊 **12 professional slides**
- ⏱️ **~10 minutes** (7-8 min content + 2-3 min Q&A)
- 💾 **44 KB** (small, shareable, portable)
- 🎨 **Professional color scheme** (dark blue + sentiment colors)
- ✅ **Ready to present** (no editing required, but customizable)

### How to Open:
- **PowerPoint:** Double-click file → Opens in Microsoft PowerPoint
- **Google Slides:** Upload to Google Drive → Edit online → Share
- **LibreOffice:** Open with LibreOffice Impress (free alternative)
- **Online:** Use Office365, Google Slides, or similar web tools

### Slide Overview:
1. Title slide (team members)
2. The Problem (30 sec)
3. Business Impact (1 min)
4. Our Dataset: 1,000 Yelp Reviews (1 min)
5. Technical Approach: TF-IDF + ML (1.5 min)
6. Models Compared: LogReg vs Naive Bayes (1 min)
7. What Worked Well ✓ (1 min)
8. The Challenge: Neutral Class ✗ (1.5 min)
9. Real Examples: Success & Failures (1.5 min)
10. Key Learnings (1 min)
11. Future Improvements (1 min)
12. Q&A / Closing (1 min intro + 2-3 min questions)

---

## 📖 Speaker Guide

**File:** `PRESENTATION_GUIDE.md` (in project root)

### What It Contains:
- ✅ **Full scripts** - What to say on each slide
- ✅ **Timing breakdown** - Exactly when to move to next slide
- ✅ **Delivery tips** - Do's & don'ts for presenting
- ✅ **Engagement ideas** - How to interact with audience
- ✅ **Q&A prep** - Common questions with ready answers
- ✅ **Examples** - Real stories with numbers
- ✅ **Last-minute checklist** - Before you present

### How to Use:
1. **Read** the guide for each slide (30 min total)
2. **Practice** with the scripts while viewing slides (1-2 rehearsals)
3. **Time yourself** (should be 7-8 minutes)
4. **Mark notes** in the guide for your personal cues
5. **Have handy** during Q&A for reference if needed

### Key Sections:
- **Slide 2-3 Scripts:** How to open about the business problem
- **Slide 9 Scripts:** Real examples to tell as stories
- **Slide 10-11 Scripts:** Learnings and future work
- **Q&A Prep:** Answers to likely questions
- **Timing:** Exactly how long each section should take

---

## 🎯 Quick Presentation Prep Plan

### Day Before Presentation (30 min)
- [ ] Read PRESENTATION_GUIDE.md once carefully
- [ ] Skim the PowerPoint slides
- [ ] Test opening the file on your computer

### 1 Hour Before Presentation (45 min)
- [ ] Go through the full script once (7-8 min)
- [ ] Review PRESENTATION_GUIDE.md
- [ ] Practice with the slides once (5-10 min)
- [ ] Check on the actual projector/screen if possible

### 15 Minutes Before Presentation (10 min)
- [ ] Arrive early and set up
- [ ] Test the file on the projector
- [ ] Have water nearby
- [ ] Take a few deep breaths
- [ ] Smile (confidence matters!)

### During Presentation
- [ ] Follow the guide loosely (don't read word-for-word)
- [ ] Make eye contact with audience
- [ ] Use the real examples (Slide 9) to engage
- [ ] Acknowledge the neutral class failure as a strength
- [ ] Answer Q&A using the prep guide if needed

---

## 📝 Key Talking Points (Quick Reference)

### Opening (Slide 1-3)
> "Today we built a machine learning system to automatically understand what customers think from their reviews on Yelp. Why? Because analyzing thousands of reviews manually takes forever. We wanted to show you how AI can solve a real business problem."

### Data (Slide 4)
> "We used 1,000 real Yelp reviews. We split them 80% for training, 20% for testing on completely new data."

### Results (Slide 6-9)
> "We got 68% accuracy. That means it correctly classified 2 out of 3 reviews. It's especially good at identifying strong positive and negative reviews (86% correct). But here's the interesting part—it completely failed on neutral reviews. Why? Because..."
> [See Slide 8 script in PRESENTATION_GUIDE.md]

### Learnings (Slide 10-11)
> "Most importantly, we learned that class imbalance is a real problem in machine learning. Companies need to be aware of this when building systems."

### Close (Slide 12)
> "We've got a solid foundation. The next step would be to collect more neutral examples and try BERT, a more advanced model. But for a first pass, this shows what's possible."

---

## 🎬 Presentation Checklist

### Before Presentation
- [ ] PowerPoint file downloaded/accessible
- [ ] Backup copy on USB (just in case)
- [ ] Backup copy on cloud (Google Drive, OneDrive)
- [ ] PRESENTATION_GUIDE.md read at least once
- [ ] All 12 slides reviewed
- [ ] Practiced full presentation once (7-8 min)

### During Presentation
- [ ] Open PowerPoint smoothly
- [ ] Make eye contact with audience
- [ ] Speak clearly (slower than normal)
- [ ] Use hand gestures (point to slides)
- [ ] Tell stories with examples (Slide 9)
- [ ] Own the failures (Slide 8)
- [ ] Smile and have energy

### Q&A
- [ ] Listen carefully to questions
- [ ] Have the guide nearby for answers
- [ ] Say "great question" to any tough ones
- [ ] If you don't know, say so honestly
- [ ] Refer to your documentation for details

### After Presentation
- [ ] Thank audience and Professor
- [ ] Offer to share code/documentation
- [ ] Ask if anyone wants to look at the analysis
- [ ] Collect feedback for future improvements

---

## 🔧 Customization Tips

### Easy Changes (1-2 minutes):
- Add school/team logo
- Change colors to match school branding
- Update team names/roles
- Add semester or date

### More Changes (5-10 minutes):
- Add your own screenshot/demo
- Reorganize bullets
- Add/remove slides
- Change fonts

### To Regenerate Completely:
```bash
python create_presentation.py
```
This creates a fresh presentation from the Python script.

**Note:** Edits in PowerPoint will be lost if you regenerate.

---

## 📊 Presentation Stats

| Metric | Value |
|--------|-------|
| **Slides** | 12 |
| **Duration** | 10 minutes |
| **Content Time** | 7-8 minutes |
| **Q&A Time** | 2-3 minutes |
| **File Size** | 44 KB |
| **Color Scheme** | Professional (dark blue + sentiment colors) |
| **Font Sizes** | 60pt (titles) - 16pt (text) |
| **Aspect Ratio** | 16:9 (widescreen) |
| **Format** | .pptx (PowerPoint 2007+) |
| **Compatible With** | PowerPoint 2007+, Google Slides, LibreOffice |

---

## 💡 Pro Tips for Great Presentation

1. **Own Your Failures:** "Our model failed on neutral reviews, and here's why..." (Shows maturity)
2. **Tell Stories:** Use Slide 9 examples like you're explaining to a friend
3. **Engage Audience:** Ask "How many of you read reviews?" on Slide 2
4. **Be Confident:** You know this material better than anyone in the room
5. **Speak Slowly:** Pace yourself. Pause between major points
6. **Use Silence:** After a big statement, pause. Let it sink in
7. **Eye Contact:** Look at different people around the room
8. **Energy:** Smile, use hand gestures, show you're excited
9. **Practice:** One full run-through at normal speed
10. **Have Fun:** This is cool work. Enjoy sharing it!

---

## 🆘 Troubleshooting

### Problem: PowerPoint won't open
**Solution:** 
- Try Google Slides (upload the file)
- Use LibreOffice Impress (free download)
- Use Office 365 online (if your school provides it)

### Problem: Slides look different on projector
**Solution:**
- Test on the actual projector beforehand
- 16:9 ratio should work on most modern devices
- If needed, adjust display settings

### Problem: Forgot what to say on a slide
**Solution:**
- Have PRESENTATION_GUIDE.md open on your phone/laptop nearby
- Take a glance at the guide if needed
- Pause briefly (it feels normal to audience)

### Problem: Someone asks a question you can't answer
**Solution:**
- "That's a great question. Let me look into that and get back to you"
- "I don't have that data handy, but it's definitely something to explore"
- Refer to the inference report or documentation if relevant

### Problem: Running out of time
**Solution:**
- Skip Slide 11 if needed (future improvements)
- Condense Q&A
- You can always say "We have more details in our GitHub repo"

---

## 📂 File Structure

```
yelp-sentiment-analysis/
├── docs/
│   ├── Yelp_Sentiment_Analysis_Presentation.pptx  ← THE PRESENTATION
│   ├── AI_usage_log.md
│   ├── inference_report.md
│   └── presentation_outline.md
│
├── PRESENTATION_GUIDE.md                           ← SPEAKER NOTES
├── PRESENTATION_README.md                          ← THIS FILE
├── QUICK_REFERENCE.md
├── create_presentation.py
└── [other project files]
```

---

## ✅ Final Checklist

Before you present, make sure:
- [ ] You have the PowerPoint file
- [ ] You've read PRESENTATION_GUIDE.md
- [ ] You've practiced once (7-8 minutes)
- [ ] You know the main talking points
- [ ] Backup files are ready
- [ ] You're excited about your work!

---

## 🎉 You're Ready!

Everything you need is in this repository:
1. ✅ Professional PowerPoint (12 slides)
2. ✅ Complete speaker guide
3. ✅ Timing breakdowns
4. ✅ Q&A preparation
5. ✅ Engagement tips
6. ✅ Last-minute checklist

**Now go present with confidence!** 🚀

---

**Questions?**
- Check PRESENTATION_GUIDE.md for detailed help
- Review the inference report for technical background
- Refer to README.md for project overview
- Have fun! You've got this! 💪

---

**Good luck, Group 5!** 🎓
