#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response #import Flask to allow us to interact with APIs using python code

# initiale our Flask app server with the __name__ function being our "main method"
app = Flask(__name__,               
            static_url_path='', 
            static_folder='../')

# Make some additional imports to allow me to make the API requests and manipulated the JSON retuened
# before feeding the data into the HTML pages  
import requests
import json
import numpy as np #NOTE: I took a different approach to manipulating the data using numpy and pandas
import pandas as pd

##### SECTION 1 - BUS STOP INFORMATION #####

# Get the list of Dublin bus stops as per the gov.ie webpage https://data.gov.ie/dataset/real-time-passenger-information-rtpi-for-dublin-bus-bus-eireann-luas-and-irish-rail
url = "https://data.smartdublin.ie/cgi-bin/rtpi/busstopinformation?stopid&format=json"
response = requests.get(url) #request data from URL 
data = response.json()  #store response as local variable in json form
#print(data)

##create .json codedump from Dublin Bus API
# filename = 'bus.json'
# f=open(filename,'w')
# json.dump(data, f, indent=4)

#create a formatted pandas df and .csv file data from Dublin Bus API
busList = [] 
for stop in data["results"]:
    busList.append(stop["stopid"])
    busList.append(stop["fullname"])
    busList.append(stop["operators"][0]["routes"]) 
#print(busList)

if busList == 0:  #create a feedback loop in case no data was found
    print('No Bus Routes Found')
else:
    a = np.asarray([ busList ]) 
    a = pd.DataFrame(a).T
    b = pd.DataFrame(np.asarray(a.iloc[::3, :]))
    c = np.asarray(a.iloc[1::3, :])
    d = np.asarray(a.iloc[2::3, :])
    b['2'] = c
    b['3'] = d
    b.columns=['StopID','Name','Routes'] # data is now fully formatted in a Pandas df
    
bus = [b.to_dict('index')]  #converting it to a dictionary allows it to interact with the html pages in a similar way to json.




##### SECTION 2 - LIVE ARRIVALS DATA FOR 3 BUS STOPS  ##########

######## Unfortunately I couldnt get a full dump to get any user input (Bus Stop Number) so I chose 3 to display ###############
# the challenge was getting the user input back into the server .py file to rerun the download.
# I tried to run a download directly from the htmp file but hit the CORB restrictions.

urla = "https://data.smartdublin.ie/cgi-bin/rtpi/realtimebusinformation?stopid="
urlb = str(235)  #intention was that these numbers could be changed by a user input
urlb1 = str(15)
urlb2 = str(810)
urlc = "&format=json"

url2 = urla+urlb+urlc
response2 = requests.get(url2) #request data from URL
data2 = response2.json()  #store response as local variable in json form

#create a formatted pandas df and .csv file data from Dublin Bus API
busArrivals = [] 
for nextBus in data2["results"]:
    busArrivals.append(nextBus["route"])
    busArrivals.append(nextBus["destination"])
    busArrivals.append(nextBus["duetime"]) 
print('RealTime Arrival Info for Bus Stop:', data2["stopid"])

if busArrivals == 0:
    print('No Bus Routes Found... you will have to walk')
else:
    aa = np.asarray([ busArrivals ]) 
    aa = pd.DataFrame(aa).T
    bb = pd.DataFrame(np.asarray(aa.iloc[::3, :]))
    cc = np.asarray(aa.iloc[1::3, :])
    dd = np.asarray(aa.iloc[2::3, :])
    bb['2'] = cc
    bb['3'] = dd
    bb.columns=['Route','Destination','Duetime']

live = bb.to_dict('index')

############### REPEATED #####################

url3 = urla+urlb1+urlc
response3 = requests.get(url3)
data3 = response3.json()

#create a formatted pandas df and .csv file data from Dublin Bus API
busArrivals1 = [] 
for nextBus in data3["results"]:
    busArrivals1.append(nextBus["route"])
    busArrivals1.append(nextBus["destination"])
    busArrivals1.append(nextBus["duetime"]) 
print('RealTime Arrival Info for Bus Stop:', data3["stopid"])

if busArrivals1 == 0:
    print('No Bus Routes Found... you will have to walk')
else:
    aaa = np.asarray([ busArrivals1 ]) 
    aaa = pd.DataFrame(aaa).T
    bbb = pd.DataFrame(np.asarray(aaa.iloc[::3, :]))
    ccc = np.asarray(aaa.iloc[1::3, :])
    ddd = np.asarray(aaa.iloc[2::3, :])
    bbb['2'] = ccc
    bbb['3'] = ddd
    bbb.columns=['Route','Destination','Duetime']

live2 = bbb.to_dict('index')

############### REPEATED #####################

url4 = urla+urlb2+urlc
response4 = requests.get(url4)
data4 = response4.json()

#create a formatted pandas df and .csv file data from Dublin Bus API
busArrivals2 = [] 
for nextBus in data4["results"]:
    busArrivals2.append(nextBus["route"])
    busArrivals2.append(nextBus["destination"])
    busArrivals2.append(nextBus["duetime"]) 
print('RealTime Arrival Info for Bus Stop:', data4["stopid"])

if busArrivals2 == 0:
    print('No Bus Routes Found... you will have to walk')
else:
    aaaa = np.asarray([ busArrivals2 ]) 
    aaaa = pd.DataFrame(aaaa).T
    bbbb = pd.DataFrame(np.asarray(aaaa.iloc[::3, :]))
    cccc = np.asarray(aaaa.iloc[1::3, :])
    dddd = np.asarray(aaaa.iloc[2::3, :])
    bbbb['2'] = cccc
    bbbb['3'] = dddd
    bbbb.columns=['Route','Destination','Duetime']

live3 = bbbb.to_dict('index')

######## SECTION 3 - SET UP OF APP ROUTE FOR LIVE DATA ########################################

@app.route('/live', methods=['GET'])  # GET live data from ../live page
def get_live():
    return jsonify( {'live':live})

@app.route('/live/<string:route>', methods =['GET'])
def get_route(route):
    foundBus = list(filter(lambda t : t['route'] == route , live))
    if len(foundBus) == 0:
        return jsonify( { 'route' : '' }),204
    return jsonify( { 'route' : foundBus[:] })
#curl -i http://localhost:5000/cars/test

@app.route('/live2', methods=['GET'])   # Repeated
def get_live2():
    return jsonify( {'live':live2})

@app.route('/live2/<string:route>', methods =['GET']) 
def get_route2(route):
    foundBus = list(filter(lambda t : t['route'] == route , live))
    if len(foundBus) == 0:
        return jsonify( { 'route' : '' }),204
    return jsonify( { 'route' : foundBus[:] })
#curl -i http://localhost:5000/cars/test

@app.route('/live3', methods=['GET'])   # Repeated
def get_live3():
    return jsonify( {'live':live3})

@app.route('/live3/<string:route>', methods =['GET'])
def get_route3(route):
    foundBus = list(filter(lambda t : t['route'] == route , live))
    if len(foundBus) == 0:
        return jsonify( { 'route' : '' }),204
    return jsonify( { 'route' : foundBus[:] })
#curl -i http://localhost:5000/cars/test




###########################

@app.route('/bus', methods=['GET']) #Function to reteieve information from the ../bus page
def get_bus():
    return jsonify( {'bus':bus})
#curl -i http://localhost:5000/bus


@app.route('/bus/<string:StopID>', methods =['GET']) 
def get_StopID(StopID):
    foundBus = list(filter(lambda t : t['StopID'] == StopID , bus))
    if len(foundBus) == 0:
        return jsonify( { 'bus' : '' }),204
    return jsonify( { 'bus' : foundBus[:] })
#curl -i http://localhost:5000/cars/test



@app.route('/bus', methods=['POST'])    # function to receive in the requested information to create a new bus stop
def create_bus(): 
    if not request.json:
        abort(400)
    if not 'StopID' in request.json:
        abort(400)
    bus1={                                      # data formatted and...
        "StopID":  request.json['StopID'],
        "Name": request.json['Name'],
        "Routes":request.json['Routes'],

    }
    bus.append(bus1)                        # appended to the ../bus page raw data
    return jsonify( {'bus':bus1 }),201


@app.route('/bus/<string:StopID>', methods =['PUT'])   # create a function [PUT] to update the bus data in ../bus page 
def update_bus(StopID):
    foundBus=list(filter(lambda t : t['StopID'] ==StopID, bus))
    if len(foundBus) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'Name' in request.json and type(request.json['Name']) != str:
        abort(400)
    if 'Routes' in request.json and type(request.json['Routes']) is not str:
        abort(400)

    foundBus[0]['Name']  = request.json.get('Name', foundBus[0]['Name'])
    foundBus[0]['Routes'] =request.json.get('Routes', foundBus[0]['Routes'])
    return jsonify( {'bus':foundBus[0]})


@app.route('/bus/<string:StopID>', methods =['DELETE'])   # create a function [DELETE] to delete the bus data in ../bus page 
def delete_bus(StopID):
    foundBus = list(filter (lambda t : t['StopID'] == StopID, bus))
    if len(foundBus) == 0:
        abort(404)
    bus.remove(foundBus[0])
    return  jsonify( { 'result':True })

@app.errorhandler(404)  #function to catch 404 errors
def not_found404(error):
    return make_response( jsonify( {'error':'Not found' }), 404)

@app.errorhandler(400)  #function to catch 400 errors
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)


if __name__ == '__main__' :   # main method initialising the Flask app server
    app.run(debug= True)