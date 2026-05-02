#!/usr/bin/env python3
"""
Nginx logs stats
"""

from pymongo import MongoClient


if __name__ == "__main__":
    col = MongoClient("mongodb://127.0.0.1:27017").logs.nginx

    print(str(col.count()) + " logs")
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for m in methods:
        print("\tmethod " + m + ": " + str(col.count({"method": m})))

    print(
        str(col.count({"method": "GET", "path": "/status"})) + " status check"
    )
