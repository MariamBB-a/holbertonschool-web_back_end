#!/usr/bin/env python3
"""
Nginx logs stats from MongoDB
"""


from pymongo import MongoClient


def print_stats(collection):
    """Print statistics of nginx logs"""
    total_logs = collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{total_logs} logs")
    print("Methods:")

    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    print_stats(client.logs.nginx)
