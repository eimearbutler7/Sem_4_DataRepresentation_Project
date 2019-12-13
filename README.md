# Semester 4 DataRepresentation Project
<img align="right" src="https://prateekvjoshi.files.wordpress.com/2014/10/1-main.png" width="500">

This repository contains DataRepresentation Project Q4 2019 (5 credits)

The 2 primary files are:
- server/b_restserver.py, from which the Flask App Server is run
- the HTML file "busviewer" from which the user can interact with the Flask app server. 

To run this document you must have installed the followng programs:

- software to run python code (https://www.python.org/), for example the Anaconda package (https://www.anaconda.com/. Flask should already be installed as part of Anaconda. 
- access to a internet browser, for example Google Chrome. 

The purpose of the page is to 1) show the bus stops in Dublin where entries to the list can be added to, updated or deleted, 2) retrieve live data for a select list of "favourite" 3 bus stops. Both datasets contribute to the "live data"(yellow) results <div>. 

By running the Flask server using "python b_restserver.py" you can then access the html interface through the local port "http://127.0.0.1:5000/busviewer.html", the raw data imported from the Dublin Bus data regarding each bus stop in the network is stored here http://127.0.0.1:5000/bus while the Real Time data for the selected 3 sample bus stops is here http://127.0.0.1:5000/live, http://127.0.0.1:5000/live1, http://127.0.0.1:5000/live2. Unfortunately I couldnt get a full dump to get any user input (Bus Stop Number) so I chose 3 to display. 

## In total, I have sought to complete at least the following tasks as outlined in the assignment.

1. To build upon the sample labs: implement a basic Flask server that has a REST API and perform CRUD operations
2. One database	table imported  from Dublin Bus that interact wit the web interface, using AJAX calls to perform CRUD operations
4. A second complementary database table contributing to live update functionality
5. App calls on data from third	party API (Dublin Bus)
6. To add some CSS formatting so the web page looks nice.

