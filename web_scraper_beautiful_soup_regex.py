import requests
from bs4 import BeautifulSoup
import re 
import time 


html  = requests.get("http://www.menuism.com/restaurant-locations/dominos-pizza-7144") 
data = html.text   #Store the text from the url into object 'data'
soup = BeautifulSoup(data, "html.parser") #Create instance of beautiful Soup
"""
# OPTIONAL TEST CODE --- THIS GETS ALL THE LINKS ON THE HOME DOMINOS LOCATIONS SITE!!!!!
dominosList = soup.findAll("li", {"class", ""}) #NOTE: soup.findAll(tagName, tagAttributes)
count = 0
for name in dominosList:
    print name
    count +=1
print count 
print """
# this just city, state lat/lon used for testing 
def getLatLon(cityState):
    time.sleep(1) 
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'sensor': 'false', 'address': '%s' % (cityState)}
    r = requests.get(url, params=params)
    results = r.json()['results']
    location = results[0]['geometry']['location']
    location['lat'], location['lng']
	#(37.3860517, -122.0838511)
    return location

# this is street address lat/lon for 17 stores with no googlemap !
def getLatLonGoogle(address):
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=%s' % (address))
    resp_json_payload = response.json()
    return (resp_json_payload['results'][0]['geometry']['location'])

	
#THIS GETS ALL THE LINKS ONLY IN THE UNITED STATES !!!!!!!
statesList=soup.findAll("a", {"href":re.compile("dominos-pizza-7144/us")}) #NOTE: soup.findAll(tagName, tagAttributes using REGEX-necessary here)
states = 0
"""for state in statesList:
    print state
    states +=1
print states """
#########################       THIRD STEP     ##########################################
count = 0 # for testing purposes to see how many rows of data -- we want 7,600-ish
for a in statesList:
    #Iterate over all rows in statesList 
    state = a.text # get the data of each row 
    stateData = str(a.text) # turn each row into a string for parsing 
    stateName = stateData.split(" Domino's")[0] #use the python split method with [0] which means "everything up to"     
    #print stateName######### 
    r  = requests.get(a['href']) # make get call to the url to list all the the dominos locations in a state
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    allDominosList = soup.find_all(title = re.compile("Domino's Pizza in ")); # find all a tags that have title "Domino's pizza in" in them
    
    for eachDominos in allDominosList:

        #### GET CITY AND STATE !!! ######
        dataCityState = eachDominos['title']
        stringCityState = str(dataCityState)
        #print stringCityState
        cityAndState = re.search('in (.+?) -', stringCityState).group(1) #takes the city,state 
        cityState = str(cityAndState) #both city and state as a string 
        cityName = cityAndState.split(", ")[0]  #city 
        #print cityName
        stateName = cityAndState.split(", ")[1] #state 
        #print stateName 		
        ##### End of City and State Code #####

        #### GET STORE URL !!! #####
        storeURL = eachDominos['href']
        #print storeURL 
        #### End of Store URL Code #####

        #### GET STORE NUMBER !!! #####
        storeNumberData = str(storeURL).split("-")
        storeNumber = storeNumberData[-1]
        #print storeNumber
        #### End of Store Number Code #####
		
		
        ##### GET LAT and LON ####
        r = requests.get(eachDominos['href'])
        data = r.text
        soup = BeautifulSoup(data, "html.parser")
        try:
            latitude = soup.findAll(itemprop="latitude")[0]["content"]
            longitude = soup.findAll(itemprop="longitude")[0]["content"]
            #latLon.append((latitude, longitude))
        except Exception: 
            #this just gets lat/lon for city/state not specific address 
            """lat_lon = getLatLon(cityState)
            lat_lonStr = str(lat_lon).split(",")
            #print lat_lonStr
            latitude = latitude
            longitude = longitude"""
            #gets street address 
            street = soup.findAll(itemprop="streetAddress")[0].contents[0]
            street = street.replace("\n","")
            street = street.replace("\t","")
            #alternate way to scrape city, state from each website but we already have it above 
            """
            city = soup.findAll(itemprop="addressLocality")[0].contents[0]
            city = city.replace("\t","")
            city = city.replace("\n","")
            state = soup.findAll(itemprop="addressRegion")[0].contents[0]
            state = state.replace("\t","")
            state = state.replace("\n","")
            streetCityState = street+", "+city+" "+state
            #print streetCityState
            latLong = getLatLonGoogle(streetCityState)
            latitude = latLong["lat"]
            longitude = latLong["lng"]"""
            #print latitude, longitude 
            #print 
            streetCityState = street+", "+cityState 
            latitude_longitude = getLatLonGoogle(streetCityState)			
            latitude = latitude_longitude["lat"]
            longitude = latitude_longitude["lng"]
            #print streetCityState
            #print latitude, longitude 
            #print 
            count+=1	#counts number of stores that don't have googlemaps and need to be geocoded 
		
        print cityName, stateName, storeNumber, storeURL,latitude,longitude


	

