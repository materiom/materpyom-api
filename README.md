# materpyom-api
Fast api to interact with cordra database and website

## install

Following `https://fastapi.tiangolo.com/tutorial/` to set this up.

`pip install fastapi[all]`

You all so need to install materpyom - `https://github.com/materiom/materpyom`

## local

`uvicorn main:app --reload` and then go to `http://127.0.0.1:8000`

You can look at ` http://127.0.0.1:8000/docs` to see automatic documentation on the api

To get api schema use `http://127.0.0.1:8000/openapi.json`


export MATERIOM_USER=admin
export MATERIOM_PASSWORD=Mit200912!
export PYTHONPATH=./app

## Tests

use pytest to run all tests