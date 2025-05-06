#!/usr/bin/env python3
"""
Module for listing all documents in a MongoDB collection
"""
from pymongo.collection import Collection
from typing import List, Dict, Any


def list_all(mongo_collection: Collection) -> List[Dict[str, Any]]:
    """
    Lists all documents in the specified MongoDB collection.

    Args:
        mongo_collection (Collection): The PyMongo collection object.

    Returns:
        List[Dict[str, Any]]: A list of all documents in the collection,
                              or an empty list if the collection is empty.
    """
    return list(mongo_collection.find())
