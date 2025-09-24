import emoji
from textblob import TextBlob
import difflib

# Build a mapping of emoji -> description string (lowercased)
_EMOJI_DB = {}
for em_char, em_alias in emoji.EMOJI_DATA.items():
    # EMOJI_DATA keys are emoji chars; value may contain 'en' description
    desc = emoji.EMOJI_DATA.get(em_char, {}).get('en', '')
    if not desc:
        # fallback: try alias conversions
        try:
            # get the alias text (like ':smile:')
            alias = emoji.demojize(em_char)
            desc = alias.replace(":", " ").strip()
        except:
            desc = ''
    if desc:
        _EMOJI_DB[em_char] = desc.lower()

def _find_best_emojis_for_word(word, top_n=2):
    word = word.lower()
    # score by substring or close match in descriptions
    results = []
    for em, desc in _EMOJI_DB.items():
        if word in desc:
            results.append((em, 1.0))  # exact-ish match boost
        else:
            # fuzzy similarity using difflib
            # compute similarity between word and description tokens
            tokens = desc.split()
            best = 0.0
            for tok in tokens:
                sim = difflib.SequenceMatcher(None, word, tok).ratio()
                if sim > best:
                    best = sim
            if best > 0.6:  # threshold
                results.append((em, best))
    # sort by score
    results.sort(key=lambda x: x[1], reverse=True)
    return [r[0] for r in results[:top_n]]

def add_emoji(text: str, max_emojis=6):
    if not text or not text.strip():
        return text
    blob = TextBlob(text)
    # pick important words: nouns, verbs, adjectives, proper nouns
    keywords = [w.lower() for w, tag in blob.tags if tag.startswith(('NN', 'VB', 'JJ', 'RB', 'NNP'))]
    # also include nouns from noun phrases
    for np in blob.noun_phrases:
        keywords.extend([t.lower() for t in np.split()])

    added = []
    # iterate keywords and find matching emojis dynamically
    for kw in keywords:
        matches = _find_best_emojis_for_word(kw, top_n=2)
        for m in matches:
            if m not in added:
                added.append(m)
            if len(added) >= max_emojis:
                break
        if len(added) >= max_emojis:
            break

    # If nothing found, try sentiment-driven *choose emoji by emotion* but still pick from DB dynamically
    if not added:
        polarity = blob.sentiment.polarity
        emotion_keywords = []
        if polarity > 0.3:
            emotion_keywords = ["smile", "happy", "joy", "good"]
        elif polarity < -0.3:
            emotion_keywords = ["sad", "cry", "angry", "upset"]
        else:
            emotion_keywords = ["neutral", "meh"]
        for ek in emotion_keywords:
            matches = _find_best_emojis_for_word(ek, top_n=2)
            for m in matches:
                if m not in added:
                    added.append(m)
                if len(added) >= max_emojis:
                    break
            if len(added) >= max_emojis:
                break

    # Append emojis to the end of text spaced nicely
    if added:
        return text + "  " + " ".join(added)
    return text
