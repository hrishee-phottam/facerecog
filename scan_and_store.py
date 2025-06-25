import argparse
import os
import logging
import requests
from pymongo import MongoClient


def scan_image(file_path: str, url: str) -> dict:
    """Send an image file to the scan API and return parsed JSON."""
    with open(file_path, 'rb') as f:
        response = requests.post(url, files={'image': f})
    response.raise_for_status()
    return response.json()


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan images and store results in MongoDB")
    parser.add_argument('path', help='Directory containing image files')
    parser.add_argument('--url', default='http://47.129.240.165:3000/scan_faces',
                        help='Face scanning API endpoint')
    parser.add_argument('--mongo', default='mongodb://localhost:27017/',
                        help='MongoDB connection URI')
    parser.add_argument('--db', default='phottam', help='MongoDB database name')
    parser.add_argument('--collection', default='people', help='MongoDB collection name')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

    client = MongoClient(args.mongo)
    collection = client[args.db][args.collection]

    for root, _, files in os.walk(args.path):
        for name in files:
            if name.lower().endswith((
                '.jpg', '.jpeg', '.png', '.bmp', '.gif')):
                file_path = os.path.join(root, name)
                try:
                    logging.info('Scanning %s', file_path)
                    data = scan_image(file_path, args.url)
                    data['filename'] = name
                    collection.insert_one(data)
                except Exception as exc:
                    logging.error('Failed to process %s: %s', file_path, exc)


if __name__ == '__main__':
    main()
