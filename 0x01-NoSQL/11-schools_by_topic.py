#!/usr/bin/env python3
"""Module to list schools with a specific topic in a MongoDB collection"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic in their topics field.

    Args:
        mongo_collection: PyMongo collection object
        topic (str): The topic to search for

    Returns:
        list: List of documents where the topics field contains the specified topic
    """
    return list(mongo_collection.find({"topics": topic}))
