import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# read csv
df = pd.read_csv('./data/artists.csv')

# process and clean data
df2 = df[df['ambiguous_artist'] == False]
df2 = df2[['tags_mb', 'artist_mb']]
df2['tags_mb'] = df2['tags_mb'].str.lower()
df2 = df2[df2['tags_mb'].apply(lambda x: isinstance(x, str))]
df2['tags_mb'] = df2['tags_mb'].str.replace(' ', '')
df2['tags_mb'] = df2['tags_mb'].str.replace(';', ' ')
df2 = df2.dropna(subset=['tags_mb'])

# limit number of rows (to avoid kernel crashing)
df2 = df2[:1000]

# vectorise tags
vectorizer = TfidfVectorizer()
vectorized = vectorizer.fit_transform(df2['tags_mb'])
similarities = cosine_similarity(vectorized)

# matrix of similarities
df3 = pd.DataFrame(similarities, columns=df2['artist_mb'], index=df2['artist_mb']).reset_index()

with open('./pickle/cosine_similarity_matrix.pkl', 'wb') as file:
    pickle.dump(df3, file)