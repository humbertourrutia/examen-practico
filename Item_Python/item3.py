#Item 3
import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "QfoGH3S4NYqFgOw88VkeSAGWBx1JoQiK"
while True: 
    orig = input("Ciudad de Origen: ") 
    if orig == "quit" or orig == "q": 
        break
    dest = input("Ciudad de Destino Final: ")
    if dest == "quit" or dest == "q": 
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    #json_data = requests.get(url).json()
    #print(json_data)
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================") 
        print("Direccion desde " + (orig) + " a " + (dest)) 
        print("Duracion del viaje: " + (json_data["route"]["formattedTime"])) 
        #print("Millas: " + str(json_data["route"]["distance"])) 
        print("Kilometros: " + str("{:.1f}".format((json_data["route"]["distance"])*1.61)))
        #print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"])) 
        print("=============================================")
    for each in json_data["route"]["legs"][0]["maneuvers"]: 
        print((each["narrative"]) + " (" + str("{:.1f}".format((each["distance"])*1.61) + " km)")) 
        print("=============================================\n")