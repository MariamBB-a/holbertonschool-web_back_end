#!/usr/bin/env python3
"""
Find schools by topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have a specific topic.

    Args:
        mongo_collection: pymongo collection object
        topic (str): topic to search for

    Returns:
        list of matching documents
    """
    return list(mongo_collection.find({"topics": topic}))
