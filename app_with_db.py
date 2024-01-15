from flask import Flask, request
import os
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# Connect to MongoDB
con_str = os.environ.get('CONN_STR')
client = MongoClient(con_str)
db = client["flask_db"]
records_collection = db["records"]

@app.route('/')
def hello_world():
    # Record client IP address and current date in MongoDB
    client_ip = request.remote_addr
    current_date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    records_collection.insert_one({"ip": client_ip, "date": current_date})

    # Display the last 10 records
    last_records = records_collection.find().sort("_id", -1).limit(10)
    records_html = "<h2>Last 10 Records:</h2>"
    for record in last_records:
        records_html += f"<p>IP: {record['ip']} | Date: {record['date']}</p>"

    # Additional information
    my_name = "Mayssa Ayachi"
    project_name = "myFlaskapp"
    version = "V2"
    current_date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    # HTML response with the added information and last 10 records
    return f"""
    <p>Name: {my_name}</p>
    <p>Project Name: {project_name}</p>
    <p>Version: {version}</p>
    <p>Current Date: {current_date}</p>
    {records_html}
    """

if __name__ == '__main__':
    app.run(debug=True)
