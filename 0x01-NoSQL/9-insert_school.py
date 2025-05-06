#!/usr/bin/env python3
"""
Module for inserting a new document into a MongoDB collection
"""
from pymongo.collection import Collection
from typing import Any


def insert_school(mongo_collection: Collection, **kwargs) -> Any:
    """
    Inserts a new document into the specified MongoDB collection based on kwargs.

    Args:
        mongo_collection (Collection): The PyMongo collection object.
        **kwargs: Keyword arguments representing the document fields and values.

    Returns:
        Any: The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
