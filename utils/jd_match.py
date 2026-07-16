from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match(resume_text, jd_text):

    tfidf = TfidfVectorizer(stop_words="english")

    vectors = tfidf.fit_transform([resume_text, jd_text])

    score = cosine_similarity(vectors)[0][1]

    return round(score * 100, 2)