import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_model():
    df = pd.read_csv('data/destinasi-wisata-preprocessed.csv')

    # Kolom yang diambil
    required_cols = ['Place_Name', 'Category', 'City', 'clean_text']
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Kolom '{col}' tidak ditemukan di dataset.")

    df[required_cols] = df[required_cols].fillna('')

    # TF-IDF langsung dari teks bersih
    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(df['clean_text'])
    similarity = cosine_similarity(vectors)

    return df, similarity


def get_places_by_category(model, category_keyword):
    df, _ = model
    
    # 1. Bersihkan keyword dan pecah menjadi kata-kata (tokens)
    #    Misal: "jakarta pantai indah" -> ["jakarta", "pantai", "indah"]
    tokens = category_keyword.lower().split()
    
    if not tokens:
        return []

    # 2. Buat kolom temporary untuk pencarian gabungan (Name + City + Category)
    #    Kita gunakan lowercase untuk pencarian case-insensitive
    #    Kita lakukan ini pada copy dataframe atau langsung pada series boolean
    
    # Logic: Row terpilih jika SEMUA token ada di dalam gabungan string data row tersebut.
    # Contoh: Row "Pantai Indah Kapuk", City="Jakarta", Category="Bahari"
    # Combined: "pantai indah kapuk bahari jakarta"
    # Token "jakarta" -> Ada
    # Token "pantai" -> Ada
    # Token "indah" -> Ada
    # Match!
    
    # Vectorized check:
    # Kita buat series gabungan string lower
    searchable_text = (
        df['Place_Name'].fillna('') + ' ' + 
        df['Category'].fillna('') + ' ' + 
        df['City'].fillna('')
    ).str.lower()
    
    # Mulai dengan semua True
    mask = pd.Series([True] * len(df))
    
    # Filter iteratif per token
    for token in tokens:
        mask = mask & searchable_text.str.contains(token)
        
    filtered = df[mask]

    return sorted(filtered['Place_Name'].unique().tolist())


def recommend(place_name, model, n=5):
    df, similarity = model

    place_name = place_name.strip()
    names = df['Place_Name'].tolist()

    idx = df.index[df['Place_Name'] == place_name][0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:n+1]

    return [
        {
            "name": df.iloc[i]['Place_Name'],
            "category": df.iloc[i]['Category'],
            "city": df.iloc[i]['City'],
            "score": round(float(score), 3)
        }
        for i, score in scores
    ]
