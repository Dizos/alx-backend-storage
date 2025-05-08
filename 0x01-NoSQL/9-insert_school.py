#!/usr/bin/env python3
"""Module to insert a new document into a MongoDB collection"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection based on kwargs.

    Args:
        mongo_collection: PyMongo collection object
        **kwargs: Keyword arguments representing document fields

    Returns:
        The _id of the newly inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
