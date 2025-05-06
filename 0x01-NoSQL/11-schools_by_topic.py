#!/usr/bin/env python3
"""
Module for retrieving schools with a specific topic from a MongoDB collection
"""
from pymongo.collection import Collection
from typing import List, Dict, Any


def schools_by_topic(mongo_collection: Collection, topic: str) -> List[Dict[str, Any]]:
    """
    Returns a list of schools that have a specific topic in their topics array.

    Args:
        mongo_collection (Collection): The PyMongo collection object.
        topic (str): The topic to search for in the topics array.

    Returns:
        List[Dict[str, Any]]: A list of documents for schools with the specified topic.
    """
    return list(mongo_collection.find({"topics": topic}))
