#!/bin/bash
echo '
General
What NoSQL means
What is difference between SQL and NoSQL
What is ACID
What is a document storage
What are NoSQL types
What are benefits of a NoSQL database
How to query information from a NoSQL database
How to insert/update/delete information from a NoSQL database
How to use MongoDB


**README Requirements Checklist:**
- Present at project root
- Explains project purpose, installation, and usage
- Lists files and their purposes

**4. Setup Notes**
- Ensure MongoDB is running: `sudo service mongod start`
- Verify MongoDB version: `mongo --version` (should show 4.2.8)
- Verify PyMongo version: `python3 -c 'import pymongo; print(pymongo.__version__)'` (should show 3.10.1)
- If `/data/db` is missing, create it: `sudo mkdir -p /data/db`
- Ensure proper permissions for `/data/db`: `sudo chown -R mongodb:mongodb /data/db`

**5. Testing**
- MongoDB command: `cat 0-list_databases.js | mongo` should output database names
- Python script: `python3 0-list_databases.py` should print database names
- Check file lengths: `wc -l 0-list_databases.js 0-list_databases.py README.md`
- Validate code style: `pycodestyle 0-list_databases.py`'
