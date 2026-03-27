import requests, base64, time, csv

credentials = base64.b64encode(b"").decode()
token = requests.post("https://accounts.spotify.com/api/token",
    headers={"Authorization": f"Basic {credentials}"},
    data={"grant_type": "client_credentials"}
).json()["access_token"]
headers = {"Authorization": f"Bearer {token}"}

songs = []
current_page = 0

while len(songs) < 1000:
    response = requests.get("https://api.spotify.com/v1/search", headers=headers, params={"q": "year:2000-2024", "type": "track", "limit": 10, "offset": current_page}).status_code
    print(response)
#     songSet = response.get("tracks", {}).get("items", [])

#     if not songSet: break
#     filteredSongs = []
#     for track in songSet:
#         song = {
#             "name": track.get("name"),
#             "releaseYear": track.get("album", {}).get("release_date", "")[:4],
#             "length": track.get("duration_ms"),
#             "artist": track.get("artists", [{}])[0].get("name")
#         }
#         filteredSongs.append(song)

#     songs.extend(filteredSongs)
#     current_page += 10
#     time.sleep(0.01)
#     #print(songSet)
# print(songs[0])
# print("Hello, World!")
# with open("songs.csv", "w", newline="", encoding="utf-8") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "releaseYear", "length", "artist"])
#     writer.writeheader()
#     writer.writerows(songs)
