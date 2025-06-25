# facerecog

This repository provides a simple script to scan image files for faces and store the returned data in MongoDB.

## Requirements

- Python 3.8+
- Packages listed in `requirements.txt`

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

Run the scanner on a directory of images:

```bash
python scan_and_store.py /path/to/images --mongo mongodb://localhost:27017/
```

Each image is sent to `http://47.129.240.165:3000/scan_faces`. The JSON response (for example, face embeddings and bounding boxes) is stored in the `people` collection of the `phottam` database. Use `--url`, `--db`, and `--collection` to override defaults.
=======
# FaceRecog

## Overview

FaceRecog demonstrates a simple workflow for scanning images or webcam frames, detecting faces with OpenCV, and storing the results in MongoDB. The repository contains a basic script that shows how to capture frames and insert face detection output into a collection.

## Setup

1. Install **Python 3.8+**.
2. (Optional) Create and activate a virtual environment.
3. Install required packages:
   ```bash
   pip install opencv-python pymongo
   ```
4. Start a MongoDB instance or provide a connection string to an existing server.

## Running the Scanner

Use the face-scanning script to read images or frames and insert detection results into your database. An example invocation might look like:

```bash
python scanner.py --db mongodb://localhost:27017/facerecog --collection results
```

The script connects to MongoDB using the URI supplied with `--db` and writes each detection to the specified collection. You can also pass `--input <path>` to scan a directory of images instead of using the webcam.

## Example Result

A typical document inserted into MongoDB resembles the following structure:

```json
{
  "image": "path/or/frame",
  "faces": [
    {"x": 100, "y": 120, "w": 50, "h": 50}
  ],
  "timestamp": "2023-01-01T12:00:00Z"
}
```

This example shows the detected face coordinates and a timestamp. Modify the script as needed to fit your data format.

## Usage Tips

- Ensure the camera is accessible when scanning in real time.
- Verify that the MongoDB connection string is correct and the database is reachable.
- Adjust detection parameters in the script if you need different accuracy or performance.

## Contributing

Feel free to open issues or pull requests if you have ideas to improve this project.

