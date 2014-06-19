import requests, sys, string, os, time

api_key = "d89c8496-3a4a-4400-ac48-b20ae365223e"
url = "https://na.api.pvp.net/api/lol/static-data/na/v1.2/versions?api_key="
debug = False

while True:
    data = open("version.txt", "r")
    my_v = data.read()
    
    response = requests.get(url + api_key)
    
    index1 = 0
    while response.text[index1] != "\"":
        index1 += 1
    
    index2 = index1 + 1
    while response.text[index2] != "\"":
        index2 += 1
    
    latest_v = response.text[(index1 + 1) : index2]
    
    
    if latest_v != my_v:
        
        if debug:
            print "Oh no! You are not up to date!"
            print latest_v
            print my_v
 
        path = open("path.txt", "r").read()
        os.system(path)
        
        write_data = open("version.txt", "w")
        write_data.write(latest_v)
        write_data.close()
        data.close()

        if debug:
            time.sleep(1)
        else:
            time.sleep(3600) #sleep for one hour
    else:
        if debug:
            print "Up to date!"
    
    data.close()
    if debug:
        time.sleep(1)
    else:
        time.sleep(60)
