# IceTunes - Mood-Based Song Detector 🎵

IceTunes is a **Streamlit**-powered web app that detects your mood based on text input and suggests personalized Spotify playlists.

## 🚀 Features
- 🎭 **Mood Detection**
- 🎨 **Dynamic UI** with mood-based colors
- 🎶 **Spotify API Integration**
- 🤖 **Sentiment Analysis** with TextBlob

## 🛠️ Installation
```sh
pip install streamlit textblob spotipy python-dotenv
git clone https://github.com/yourusername/IceTunes.git
cd IceTunes
```

Create a `.env` file:
```ini
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
```

Run the app:
```sh
streamlit run app.py
```

## 🎯 How It Works
1. Enter a mood description.
2. Click **"Recommend Music 🎧"**.
3. Get **5 song recommendations** & a **playlist link**.

## 🔥 Tech Stack
- **Python, Streamlit, TextBlob, Spotify API**

## 📜 License
MIT License

## 🤝 Contributing
Fork & submit PRs! 💡
