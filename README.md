# 🎵 Billboard 100 → Spotify Playlist Bot

This Python script scrapes the Billboard Hot 100 chart for a user-specified date and automatically creates a private Spotify playlist with the top 20 songs using the Spotify Web API.

---

## 🚀 What It Does

- Asks the user for a date (format: `YYYY-MM-DD`).
- Scrapes the Billboard Hot 100 chart for that day.
- Extracts the top 20 song titles.
- Searches for each song on Spotify.
- Creates a **private playlist** in your Spotify account.
- Adds the found tracks to that playlist.

---

## 📁 Project Structure

```
.
├── main.py                   # The main automation script
├── .env                      # Environment variables for Spotify credentials
└── README.md                 # You're here!
```

---

## 🔐 .env File Setup

Create a `.env` file in the project root and add your Spotify credentials:

```
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here
SPOTIFY_USERNAME=your_spotify_username
```

---

## ▶️ How to Run

1. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the script:
   ```bash
   python billboard_to_spotify.py
   ```

3. When prompted, enter a date in the format `YYYY-MM-DD` (e.g., `2005-07-16`).

---

## 📝 Output

- The script prints the top 20 song titles from that date.
- It also shows the found Spotify track URIs.
- The new playlist will appear in your Spotify account (as private).

---

## 📌 Notes

- You’ll be asked to log in via Spotify once (a browser window will open).
- The script uses `spotipy`, a lightweight Python client for the Spotify Web API.
- If a song is not found, it may be skipped silently (you can enhance this by adding error handling).
- Some song titles may not match Spotify exactly (you can add fuzzy searching or artist support).

