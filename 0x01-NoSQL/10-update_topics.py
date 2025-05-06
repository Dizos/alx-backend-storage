#!/usr/bin/env python3
"""
Module for updating topics of a school document in a MongoDB collection
"""
from pymongo.collection import Collection
from typing import List


def update_topics(mongo_collection: Collection, name: str, topics: List[str]) -> None:
    """
    Updates the topics of all school documents with the specified name.

    Args:
        mongo_collection (Collection): The PyMongo collection object.
        name (str): The name of the school to update.
        topics (List[str]): The list of topics to set for the school.

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
