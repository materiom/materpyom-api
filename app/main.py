from fastapi import FastAPI
from typing import List

from __init__ import __version__, __description__, __url__
from materpyom.read import materiom_get_one_item, materiom_search, materiom_search_by_type

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


@app.get("/sandbox/search")
async def search_items() -> List:
    """
    Get function to get the material systems
    :return:
    """

    items = materiom_search_by_type(object_type="Material")

    if 'results' in items:
        return items['results']
    else:
        return []


@app.get("/sandbox/{id}")
async def sandbox_id(id: str):
    """
    Get function to get details of a material system.
    :param id: str of item id that we want to return
    :return:
    """

    item = materiom_get_one_item(item_string=id)

    return item


# TODO
## RECEIPE
# fieilds:
# url: /receipe/{id}

# return {"field_1":"example","field_2":"example_2"}

## DATA SANDBOX
## MATERIAL SYSTEMS <- MATERIAL VARIATIONS
# materials with 3 ingredients, which one are they? get all materials with key word search.
# get_material_variations/{id}

# return {[{"field_1":"example","field_2":"example_2"}]}

## Export Data:
# generate csv with data in it

##