import urllib.request , urllib.parse , urllib.error
import  json

api_key = 'ae0cc7b89fc74ef995847af02a14f304'  # My OpenCage API key on 2476 ID
serviceurl = "https://api.opencagedata.com/geocode/v1/json?"


while True :
    address = input("Enter Location: ")
    if len(address) < 1: break
    url = serviceurl + urllib.parse.urlencode({'q': address, 'key' : api_key})
    print("Retrieving url :", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("Retrived", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

        if not js or 'status' not in js or js['status'] != 'ok':
            print("    == Faliure to Retrieve ==     ")
            continue
    lat = js["results"][0]["geometry"]["lat"]
    lng = js["results"][0]["geometry"]["lng"]
    city = js["results"][0]["components"]["city"]
    country = js["results"][0]["components"]["country"]
    state = js["results"][0]["components"]["state"]
    print("Latitude =", lat,"  ", "Longitude =",lng)
    print(city, "city", state, ",", country, "\n")
    #print(data)
    
