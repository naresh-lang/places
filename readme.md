# Places

A utility to get places data from google maps based on lattitude,longitude and radius

## Quick Start Guide

# Install requirements
pip install -r requirements.txt

# Get API Key from Google Places API
My_key is 'AIzaSyAI7xCmfutDPs-C9HBspXcq12i6vGQRvKU'


# Run code (with default configurations)
python run.py


### Repo structure

 - modules/places.py: python module to get data from API
 - run.py: Code entry point
 

### Description

#Check this API with postman, the input of this API will be as follows.

{
	"source":{
		"lat":17.3616,
		"lon":78.4747,
		"radius":3
	}

}

#and it will return the store data as follows( I took charminar's lat and lon).

{
  "result": [
    {
      "Address": "5-2-444, Risala Abdullah, Behind Petrol Pump, New Osman Gunj Road, Risala Abdulla Colony, Hyderabad",
      "store_name": "Andhra Sales Corporation"
    },
    {
      "Address": "India",
      "store_name": "City Furniture"
    },
    {
      "Address": "Bank Street, Koti, Hyderabad",
      "store_name": "Sports World"
    },....


#The service will be as below

http://127.0.0.1:5000/place    ----------> POST Method









