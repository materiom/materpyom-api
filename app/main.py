from fastapi import FastAPI

from __init__ import __version__, __description__, __url__
from materpyom.read import materiom_get_one_item, materiom_search

app = FastAPI()


@app.get("/")
async def root():
    return {"Description": __description__,
            "version": __version__,
            "url":__url__}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    """
    Get function to get details of one item
    :param item_id: str
    :return:
    """

    item = materiom_get_one_item(item_string=item_id)

    return item


@app.get("/search/{search_string}")
async def search_items(search_string: str):
    """
    Get function to get all items from a search term
    :param search_string:
    :return:
    """

    items = materiom_search(search_string=search_string)

    return items
