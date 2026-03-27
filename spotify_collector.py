import requests, base64, time, csv

credentials = base64.b64encode(b"ae9aa195d13542d7a1bd6c68a1ce7553:91e8119c8e764d4f96f10312379d61eb").decode()
token = requests.post("https://accounts.spotify.com/api/token",
    headers={"Authorization": f"Basic {credentials}"},
    data={"grant_type": "client_credentials"}
).json()["access_token"]
headers = {"Authorization": f"Bearer {token}"}

songs = []
current_page = 0

while len(songs) < 100:
    response = requests.get("https://api.spotify.com/v1/search", headers=headers, params={"q": "year:2000-2024", "type": "track", "limit": 10, "offset": current_page}).json()
    songSet = response.get("tracks", {}).get("items", [])
    print(songSet[0].keys())
    if not songSet: break
    filteredSongs = []
    for track in songSet:
        song = {
            "name": track.get("name"),
            "popularity": track.get("popularity"),
            "releaseYear": track.get("album", {}).get("release_date", "")[:4],
            "length": track.get("duration_ms"),
            "artist": track.get("artists", [{}])[0].get("name")
        }
        filteredSongs.append(song)

    songs.extend(filteredSongs)
    current_page += 10
    time.sleep(0.01)
    #print(songSet)

print(songs[0])
print("Hello, World!")
with open("songs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "popularity", "releaseYear", "length", "artist"])
    writer.writeheader()
    writer.writerows(songs)