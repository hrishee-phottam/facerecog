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

