#!/usr/bin/env python3
"""
Nginx logs stats
"""

from pymongo import MongoClient


if __name__ == "__main__":
    collection = MongoClient("mongodb://127.0.0.1:27017").logs.nginx

    print("{} logs".format(collection.count()))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        print("\tmethod {}: {}".format(
            method,
            collection.count({"method": method})
        ))

    print(
        "{} status check".format(
            collection.count(
                {"method": "GET", "path": "/status"}
            )
        )
    )
