Here's the cleaned-up and unified version of your `README.md` for the `facerecog` project:

---

# FaceRecog

## Overview

FaceRecog is a simple tool for scanning images or webcam feeds to detect faces and store the results in MongoDB. It captures face embeddings, bounding boxes, and other metadata for further analysis or use.

## Requirements

* Python 3.8+
* MongoDB instance (local or remote)

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. (Optional) Copy the environment template and set your credentials:

   ```bash
   cp .env.sample .env
   ```

   Update the `.env` file with your MongoDB connection string and any other necessary configurations.

## Usage

### Scan a Directory of Images

```bash
python scan_and_store.py /path/to/images --mongo mongodb://localhost:27017/
```

### Scan via Webcam (if supported in the script)

```bash
python scanner.py --db mongodb://localhost:27017/facerecog --collection results
```

### API Endpoint

Each image is sent to:

```
http://47.129.240.165:3000/scan_faces
```

You can override the default endpoint with `--url`.

### MongoDB Storage

By default, data is stored in the `people` collection inside the `phottam` database. You can override the database and collection using:

```
--db <mongodb-uri> 
--collection <collection-name>
```

## Example Document

A typical MongoDB document looks like:

```json
{
  "image": "path/or/frame",
  "faces": [
    {
      "x": 100,
      "y": 120,
      "w": 50,
      "h": 50,
      "embedding": [0.123, 0.456, ...]
    }
  ],
  "timestamp": "2023-01-01T12:00:00Z"
}
```

## Notes

* Ensure MongoDB is running and accessible.
* You may adjust detection thresholds or parameters in the script for better accuracy.
* API endpoint `http://47.129.240.165:3000/scan_faces` should be active and reachable.

## Contributing

Open issues or submit pull requests for improvements, bug fixes, or new features.

