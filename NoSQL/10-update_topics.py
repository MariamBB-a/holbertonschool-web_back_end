#!/usr/bin/env python3
"""
Update all topics of a school document by name
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics field of all documents matching the school name.

    Args:
        mongo_collection: pymongo collection object
        name (str): school name to match
        topics (list): list of topics to set

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
