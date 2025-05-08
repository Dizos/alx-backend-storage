#!/usr/bin/env python3
"""Module to update topics of school documents in a MongoDB collection"""

def update_topics(mongo_collection, name, topics):
    """
    Updates the topics field of all documents in a MongoDB collection where name matches.

    Args:
        mongo_collection: PyMongo collection object
        name (str): The school name to match
        topics (list): List of strings representing the topics to set

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
