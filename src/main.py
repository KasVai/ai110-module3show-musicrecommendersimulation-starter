"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs

PROFILES = {
    "High-Energy Pop":   {"genre": "pop",      "mood": "intense",   "energy": 0.90},
    "Chill Lofi":        {"genre": "lofi",     "mood": "chill",     "energy": 0.35},
    "Deep Intense Rock": {"genre": "rock",     "mood": "intense",   "energy": 0.92},
}

# Edge case profiles designed to expose scoring weaknesses
EDGE_CASES = {
    # Mood and energy directly contradict each other — sad songs are all low energy,
    # so the system is forced to choose: reward the mood or the energy, never both.
    "Sad but High-Energy":   {"genre": "classical", "mood": "sad",      "energy": 0.95},

    # Genre does not exist in the catalog — the +2.0 genre bonus never fires,
    # reducing the system to mood + energy only.
    "Genre Ghost (k-pop)":   {"genre": "k-pop",     "mood": "happy",    "energy": 0.75},

    # Genre + mood combo that no song in the catalog satisfies simultaneously,
    # so the max achievable score is capped at 2.0 + energy bonus.
    "Impossible Combo":      {"genre": "classical", "mood": "energetic","energy": 0.80},

    # Only one song has this mood (Velvet Underground, r&b/romantic),
    # testing whether a rare mood signal still surfaces the right song.
    "Rare Mood (romantic)":  {"genre": "pop",       "mood": "romantic", "energy": 0.55},
}

def main() -> None:
    songs = load_songs("data/songs.csv")

    for profile_name, user_prefs in {**PROFILES, **EDGE_CASES}.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\n" + "=" * 40)
        print(f"  Profile: {profile_name}")
        print("=" * 40)
        for i, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"\n#{i}: {song['title']} by {song['artist']}")
            print(f"    Genre: {song['genre']}  |  Mood: {song['mood']}  |  Energy: {song['energy']}")
            print(f"    Score: {score:.2f}")
            print(f"    Why:   {explanation}")
        print("\n" + "=" * 40)


if __name__ == "__main__":
    main()
