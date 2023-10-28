from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    input_artist = request.form.get('artist')
    if not input_artist:
        return jsonify({'error': 'Please provide an artist name in the POST request body'})
    
    input_artist = input_artist.lower()

    with open('./pickle/cosine_similarity_matrix.pkl', 'rb') as file:
        cosine_sim = pickle.load(file)

        try: 
            recommendations = pd.DataFrame(cosine_sim.nlargest(11, input_artist)['artist_mb'])
            recommendations = recommendations[recommendations['artist_mb'] != input_artist]
        except: 
            return jsonify({'error': 'Artist not present in current database'})
    
    return jsonify({'input_artist': input_artist, 'recommended_artists': recommendations.values.flatten().tolist()})