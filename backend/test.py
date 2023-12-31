import requests

URL = "https://www.youtube.com/watch?v=gWpHWOf5zu8&ab_channel=WarnerBros.India"
FILE_TO_SAVE_AS = "myvideddo.mp4" # the name you want to save file as


resp = requests.get(URL) # making requests to server

with open(FILE_TO_SAVE_AS, "wb") as f: # opening a file handler to create new file
    f.write(resp.content) # writing content to file



