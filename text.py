import streamlit as st
from textblob import TextBlob
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
import os
from dotenv import load_dotenv

st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #ff9a9e, #fad0c4);
        font-family: 'Poppins', sans-serif;
    }
    .stTextInput>div>div>input {
        background-color: white;
        color: black;
        border-radius: 10px;
        padding: 10px;
    }
    .stButton>button {
        background: linear-gradient(to right, #ff758c, #ff7eb3);
        border: none;
        color: white;
        font-size: 18px;
        border-radius: 12px;
        padding: 12px 20px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(to right, #ff7eb3, #ff758c);
        transform: scale(1.05);
    }
    .stAlert {
        background-color: rgba(255, 255, 255, 0.5);
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Header with Color
st.markdown("<h1 style='text-align: center; color: teal;'>🎵 IceTunes - Mood-Based Song Detector 🎶</h1>", unsafe_allow_html=True)

# Load API keys from .env file
load_dotenv()
CLIENT_ID = os.getenv("273b530d5aff406ea1838671151eb2c0")
CLIENT_SECRET = os.getenv("326052e9d3f345ada36010743896d735")

# Initialize Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

# Mood-based playlists (Add your own!)
mood_playlists = {
    "happy": "0jrlHA5UmxRxJjoykf7qRY",  # Spotify Happy Hits playlist
    "sad": "25ZzkJkOuYir9kHr2CqwPQ",  # Sad Vibes
    "energetic": "3y96TXf7zKJTv48OlP4xEB",  # Workout Mix
    "relaxed": "4kOdiP5gbzocwxQ8s2UTOF",  # Chill Hits
    "romantic": "5QOrHPIzTFh80WhHmbOcCp",  # Love Songs
}

# Streamlit UI
st.subheader("Describe your mood, and we'll suggest a playlist!")

# User Input
user_input = st.text_area("How are you feeling today? (type using keyword happy/sad/energetic/relaxed/romantic)", "")


if st.button("Recommend Music 🎧"):
    if user_input.strip() == "":
        st.warning("Please enter your mood description!")
    else:
        # Perform sentiment analysis
        sentiment = TextBlob(user_input).sentiment.polarity
        if "happy" in user_input.lower():
            mood = "happy"
        elif "sad" in user_input.lower():
            mood = "sad"
        elif "energetic" in user_input.lower():
            mood = "energetic"
        elif "relaxed" in user_input.lower():
            mood = "relaxed"
        elif "romantic" in user_input.lower():
            mood = "romantic"
        else:
        # Determine mood
           if sentiment > 0.5:
               mood = "happy"
           elif sentiment > 0.1:
               mood = "energetic"
           elif sentiment < -0.3:
               mood = "sad"
           elif sentiment <= 0.1:  # Ensure relaxed is properly assigned
               mood = "relaxed"
           else:
               mood = "romantic"
        
        st.success(f"🎶 Your mood is detected as: **{mood.capitalize()}**")

        mood_colors = {
            "happy": "#FFD700",      # Gold
            "sad": "#4682B4",        # Steel Blue
            "energetic": "#FF4500",  # Orange Red
            "relaxed": "#32CD32",    # Lime Green
            "romantic": "#FF69B4"    # Hot Pink
        }
        bg_color = mood_colors.get(mood, "#FFFFFF")  # Default to white

# Inject CSS to change background color dynamically
        st.markdown(
           f"""
    <style>
        .stApp {{
            background-color: {bg_color};
        }}
    </style>
    """,
    unsafe_allow_html=True
)
           
        
        # Get a playlist
        playlist_id = mood_playlists.get(mood, mood_playlists["happy"])
        results = sp.playlist_tracks(playlist_id)
        tracks = results["items"]

        # Pick a few random songs
        random.shuffle(tracks)
        st.subheader(f"🔥 Recommended {mood.capitalize()} Songs:")
        for track in tracks[:5]:  # Show 5 songs
            song_name = track["track"]["name"]
            artist_name = track["track"]["artists"][0]["name"]
            st.write(f"🎵 **{song_name}** - {artist_name}")

        st.markdown(f"[🎧 Open Full Playlist](https://open.spotify.com/playlist/{playlist_id})")
        
