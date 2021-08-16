# Weather-Forecast

## Prerequisites

You will need the following things properly installed on your computer.

* [Git](https://git-scm.com/)
* [Python 3](https://www.python.org/) 
* [Google Chrome](https://google.com/chrome/) or any others browsers

## Installation('Windows')

* `$ git clone https://github.com/ericsoft123/Weather-Forecast.git`
* `$ cd Weather-Forecast`
* `create environment $ virtualenv env venv`
* `$ source venv/Scripts/activate`
* `$ pip install -r requirements.txt`
* `$ python manage.py migrate`
* `under open .env.example add your credentials there`
* `change .env.example file to .env`


## Running / Development

* Run `python manage.py runserver` under Project folder.
* Visit your app at [http://localhost:8000).
* Note: Make sure your Environmental is activated.



### Running Tests 

* `python manage.py test`


### Running REST API Client(Extra)

* `open Rest Client\Weather.rest` and test all endpoint inside there or if you do not have it download this VSCODE extension [Rest Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)

* or if you have `postman` check all API inside `Weather.rest`