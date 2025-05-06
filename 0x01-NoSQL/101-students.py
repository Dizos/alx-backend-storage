#!/usr/bin/env python3
"""
Module for retrieving students sorted by average score from a MongoDB collection
"""
from pymongo.collection import Collection
from typing import List, Dict, Any


def top_students(mongo_collection: Collection) -> List[Dict[str, Any]]:
    """
    Returns all students sorted by their average score in descending order.

    Args:
        mongo_collection (Collection): The PyMongo collection object.

    Returns:
        List[Dict[str, Any]]: A list of student documents with an added
                              'averageScore' key, sorted by averageScore
                              in descending order.
    """
    pipeline = [
        {
            "$addFields": {
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
