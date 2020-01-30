import googlemaps
API_KEY = 'AIzaSyAI7xCmfutDPs-C9HBspXcq12i6vGQRvKU'

def search(lat,lon,radius):
	gmaps = googlemaps.Client(key=API_KEY)
	places_result = gmaps.places_nearby(location=[lat,lon],radius=1000*radius,open_now=False,type='store')
	result = places_result['results']
	stores_list = []
	for data in result:
		stores_list.append({'store_name':data['name'],'Address':data['vicinity']})
	return stores_list

	
	


