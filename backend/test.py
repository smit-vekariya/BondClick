# import requests

# URL = "https://www.youtube.com/watch?v=gWpHWOf5zu8&ab_channel=WarnerBros.India"
# FILE_TO_SAVE_AS = "myvideddo.mp4" # the name you want to save file as


# resp = requests.get(URL) # making requests to server

# with open(FILE_TO_SAVE_AS, "wb") as f: # opening a file handler to create new file
#     f.write(resp.content) # writing content to file



import requests

url = "https://www.fast2sms.com/dev/bulkV2"

payload = "variables_values=121212&route=otp&numbers=9510584817"
headers = {
    'authorization': "PBbi7C2nmYZOgvWXATLIFqQrpH1oys3GhjeDMcVSE0xU89lzk5hHKXMGB9NnU0dOqL1iQPw3DuSokZfx",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)