# Weather-Forecast

## Prerequisites

You will need the following things properly installed on your computer.

* [Git](https://git-scm.com/)
* [Python 3](https://www.python.org/) 
* [Google Chrome](https://google.com/chrome/) or any others browsers

## Installation

* `git clone https://github.com/ericsoft123/Weather-Forecast.git`
* `cd Weather-Forecast`
* `pip3 install -r requirements.txt`
* `change .env.example file to .env`
* `under open .env file and replace with your credential there`


## Running / Development

* Run `python manage.py runserver` under Project folder.
* Visit your app at [http://localhost:8000/api/location/{city}?days={number}](http://localhost:8000/api/location/London?days=1).



### Running Tests 

* `python manage.py test`


### Running REST API Client

* `open Rest Client\Weather.rest` and test all endpoint inside there or if you do not have it download this VSCODE extension [Rest Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)

* or if you have `postman` check all API inside `Weather.rest`