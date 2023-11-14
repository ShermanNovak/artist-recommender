# artist-recommender

A simple content-based recommendation system using cosine similarity based on music artists scraped from MusicBrainz.
Reference: https://www.kaggle.com/datasets/pieca111/music-artists-popularity/data.


This Flask API was used in TICK to recommend events performed by the top 10 similar artists on the event details page. 
- A content-based recommendation system was chosen as it is easier to obtain a dataset on artists instead of generating a large number of user interactions.
- Since the data scraped from MusicBrainz had 1-2 million artists, and it would take a significantly long time to compute the top 10 similar artists for each of them, a starting number of 100,000 artists were included. Future improvements would involve increasing the number of artists, and trying out other types of recommendation systems, including Collaborative Filtering.

### setting up
1. python createModel.py
2. flask run
