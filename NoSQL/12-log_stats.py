#!/usr/bin/env python3
"""
Nginx logs stats
"""

from pymongo import MongoClient


if __name__ == "__main__":
    collection = MongoClient("mongodb://127.0.0.1:27017").logs.nginx

    print(collection.count_documents({}), "logs")
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for m in methods:
        print("\tmethod", m + ":", collection.count_documents({"method": m}))

    print(
        collection.count_documents({"method": "GET", "path": "/status"}),
        "status check"
    )
