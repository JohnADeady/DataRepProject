# Import necessary libraries
import requests
import json
from xlwt import *

# Url from rapidapi for Deezer including parameter & header
url = "https://deezerdevs-deezer.p.rapidapi.com/search"

querystring = {"q":"eminem"}

headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "8d8466e673msh79c6f787e83a8afp14d89fjsn3ca0b2b06bb0"
    }

# Get API using request and convert to JSON
response = requests.request("GET", url, headers=headers, params=querystring)
songs = response.json()

#for song in songs['data']:
	#print(song)

# save this to a file
filename = "deezer.json"
if filename:
	# Writing JSON data
	with open(filename, 'w') as f:
		json.dump(songs, f, indent=4)

# write to excel file
w = Workbook()
ws = w.add_sheet('eminem')
row = 0;

# Add title columns
ws.write(row,0,"id")
#ws.write(row,1,"readable")
ws.write(row,1,"title")
#ws.write(row,3,"title_short")
#ws.write(row,4,"title_version")
#ws.write(row,4,"link")
ws.write(row,4,"duration")
ws.write(row,5,"rank")
#ws.write(row,7,"explicit_lyrics")
#ws.write(row,8,"explicit_content_lyrics")
#ws.write(row,9,"explicit_content_cover")
#ws.write(row,10,"preview")
ws.write(row,2,"artist")
ws.write(row,3,"album")
#ws.write(row,14,"type")

row += 1

# Add each row to the excel
for song in songs["data"]:
	ws.write(row,0, song["id"])
	#ws.write(row,1,song["readable"])
	ws.write(row,1,song["title"])
	#ws.write(row,3,song["title_short"])
	#ws.write(row,4,song["title_version"])
	#ws.write(row,5,song["link"])
	ws.write(row,4,song["duration"])
	ws.write(row,5,song["rank"])
	#ws.write(row,7,song["explicit_lyrics"])
	#ws.write(row,8,song["explicit_content_lyrics"])
	#ws.write(row,9,song["explicit_content_cover"])
	#ws.write(row,10,song["preview"])	
	ws.write(row,2,song["artist"]["name"])
	ws.write(row,3,song["album"]["title"])
	#ws.write(row,14,song["type"])
	row += 1
	
# save to excel titled eminem
w.save('eminem.xls')