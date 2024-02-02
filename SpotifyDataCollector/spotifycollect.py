import spotipy
import pandas as pd
import csv
import time
import datetime
from collections.abc import Iterable
from spotipy.oauth2 import SpotifyClientCredentials
from ytmusicapi import YTMusic


# referenced this article: https://medium.com/@maxtingle/getting-started-with-spotifys-api-spotipy-197c3dc6353b

input_file = 'C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/SpotifyDataCollector/CSVs/ufo_cleaned.csv'
output_file = 'C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/SpotifyDataCollector/spotified_csvs/ufo_spotified.csv'


# Setting up Spotify connection and Spotipy obj


client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Setting up Youtube Music API Obj
ytmusic = YTMusic()

# opening files to read names & artists and opening files to write to 
with open(input_file, 'r', newline='', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

# running 10k requests from spotify API and parsing results
    artist_name = []
    track_name = []
    popularity = []
    track_id = []
    playcount = []
    duration = []
    markets = []
    explicit = []
    genre = []
    instrument = []
    year = []
    
    print("Task Opened: making request and writing data")
    start = datetime.datetime.now()
    print(f'Starting Task at: {datetime.datetime.now()}')

    for row in reader:

        song = row[0]
        artist = row[1]


        query = f'remaster%20track:{song}%20artist:{artist}'

        # waiting to prevent rate-limiting
        time.sleep(0.5)

        # Spotify API Results
        spot_tracks = sp.search(q=query, type='track', limit=30,offset=0)

        # Youtube Music API Results

        # you_tracks = ytmusic.search(f"{song} {artist}")

        # for row, resp in enumerate(you_tracks):
        #     if(resp['category']== 'Songs'):
        #         if resp['title'] not in track_name:
        #             track_name.append(resp['title'])
        #             artist_name.append(resp['artists'][0]['name'])
        #             playcount.append(resp['views'])
        #             duration.append(resp['duration_seconds'])
        #             explicit.append(resp['isExplicit'])
        #             genre.append(row[2])
        #             instrument.append(row[3])
        #             year.append(row[4])

        # Spotify Track Loop
        if isinstance(spot_tracks['tracks']['items'], Iterable):
            for j, t in enumerate(spot_tracks['tracks']['items']):
                    if isinstance(t['artists'], Iterable):
                        for i, tist in enumerate(t['artists']):
                            if  artist.lower() in t['artists'][i]['name'].lower() and t['name'].lower() in song.lower() and t['name'].lower() not in track_name:
                                artist_name.append(t['artists'][0]['name'].lower())
                                track_name.append(t['name'].lower())
                                track_id.append(t['id'])
                                popularity.append(t['popularity'])
                                duration.append(t['duration_ms'])
                                markets.append(t['available_markets'])
                                explicit.append(t['explicit'])
                                genre.append(row[2])
                                instrument.append(row[3])
                                year.append(row[4])



track_dataframe = pd.DataFrame({'artist_name' : artist_name, 'track_name' : track_name, 'track_id' : track_id, 'genre': genre, 'instrument': instrument, 'year': year, 'popularity' : popularity, 'duration_ms': duration,'explicit': explicit, 'available_markets': markets})
track_dataframe.to_csv(output_file)
print(track_dataframe.shape)
print(track_dataframe.head(15))

print(f'Task Closed at: {datetime.datetime.now()}')

