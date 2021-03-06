# Weather-Forecast

# WeatherApp Preview 
![Preview](https://user-images.githubusercontent.com/15068184/129510250-4ccb4a70-2eef-4ce3-a307-f1184b28c6f0.gif)


## Prerequisites

You will need the following things properly installed on your computer.

* [Git](https://git-scm.com/)
* [Python 3](https://www.python.org/) 
* [Google Chrome](https://google.com/chrome/) or any others browsers

## Installation('Windows')

* `$ git clone https://github.com/ericsoft123/Weather-Forecast.git`
* `$ cd Weather-Forecast`
* `create environment $ virtualenv myvenv --python=python3.7`
* `$ source myvenv/Scripts/activate`
* `$ pip install -r requirements.txt`
* `under open .env.example add your credentials there`
* `change .env.example file to .env`


## Running / Development

* Run `python manage.py runserver` under Project folder.
* [Visit your app at](http://localhost:8000).
* Note: Make sure your Environmental is activated.



### Running Tests 

* `python manage.py test`
* `Preview Test`
![Preview Test](https://user-images.githubusercontent.com/15068184/129511257-683c9ddb-7ed6-492a-b9bc-f4327cb9aed2.gif)


### Running REST API Client(Extra)

* `open Rest Client\Weather.rest` and test all endpoint inside there or if you do not have it download this VSCODE extension [Rest Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)

* or if you have `postman` check all API inside `Weather.rest`