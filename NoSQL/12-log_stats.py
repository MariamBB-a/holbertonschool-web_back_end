#!/usr/bin/env python3
"""
Nginx logs stats
"""

from pymongo import MongoClient


if __name__ == "__main__":
    col = MongoClient("mongodb://127.0.0.1:27017").logs.nginx

    print(col.count(), "logs")
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for m in methods:
        print("\tmethod {}: {}".format(m, col.count({"method": m})))

    print(
        "{} status check".format(
            col.count({"method": "GET", "path": "/status"})
        )
    )
