import requests
import pandas as pd
import json



def makeCall(api, url):
    urls = {"FIRST" : "https://frc-api.firstinspires.org/v3.0/", "TBA" : "https://www.thebluealliance.com/api/v3/", "Statbotics": "https://api.statbotics.io/v2/"}
    paramaters = {}
    f = open("Compiler/Config/apiKeys.json")
    
    credentials = json.load(f)
    f.close()
    if api == "FIRST":
        paramaters = {"Authorization" : credentials["FIRST"]["Auth"], "If-Modified-Since": ""}
    elif api == "TBA":
        paramaters["X-TBA-Auth-Key"] = credentials["TBA"]["Auth"]
    
    return requests.request("GET", urls[api] + url, headers = paramaters)


def writeCSV(df, fp):
    dataframe = pd.DataFrame()
    dataframe = df
    f = open(fp, mode="w")
    toWrite = ""
    for i in range(0, dataframe.__len__):
        toWrite += f"{dataframe[i]},"
    f.write(toWrite)
    f.close()

    
    


    

