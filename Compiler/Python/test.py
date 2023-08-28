# import requests

# paramaters = {}
# payload = {}

# responseFile = open("statboticsRead-In.json", mode="w")


# response = requests.request("GET", "https://api.statbotics.io/v2/team_event/1391/2023mrcmp", headers = paramaters, data=payload)

# responseFile.write(response.text)
# print(response.text)

# import requests

# key = "oPPHkGl0iiYsAvlMObdoj0PcYcI7gSE8qlrZ8NCmzYodo2fNmWfAh90c6RFKqboe"


# paramaters = {"X-TBA-Auth-Key" : key}
# payload = {}

# responseFile = open("tbaRead-In.json", mode="w")


# response = requests.request("GET", "https://www.thebluealliance.com/api/v3/team/frc1391/event/2023mrcmp/matches", headers = paramaters, data=payload)

# responseFile.write(response.text)
# print(response.text)

# import base64
# import requests
# import json

# username = "razzlecat"
# password = "8b87b15f-3fe3-4c80-b711-e927a7100945"
# url = "https://frc-api.firstinspires.org/v3.0/2023"

# part1 = (username+":"+password)

# credentials = "Basic cmF6emxlY2F0OjhiODdiMTVmLTNmZTMtNGM4MC1iNzExLWU5MjdhNzEwMDk0NQ=="# + str(base64.b64encode(part1.encode("ascii")))

# paramaters = {"Authorization" : credentials,
#               "If-Modified-Since": ""}
# payload = {}

# responseFile = open("responseData.json", mode="w")


# response = requests.request("GET", "https://frc-api.firstinspires.org/v3.0/2023/avatars?teamNumber=1391", headers = paramaters, data=payload)

# responseFile.write(response.text)
# print(response.text)

