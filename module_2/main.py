# This is a script that reads the txt files and sends them to the server.
import os 
import requests

current_path = os.path.dirname(__file__)
# Path to the feedback folder
feedback_path = os.path.join(current_path, "feedback\\")



folder = os.listdir(feedback_path)

list = []

for file in folder:
    with open(feedback_path + file, 'r') as f:
        list.append({"title":f.readline().rstrip("\n"),
            		"name":f.readline().rstrip("\n"),
            		"date":f.readline().rstrip("\n"),
            		"feedback":f.read().rstrip("\n")})
        print(list[-1])

for item in list:
    resp = requests.post('http://127.0.0.1:80/feedback/', json=item)
    if resp.status_code != 201:
        raise Exception('POST error status={}'.format(resp.status_code))
    print('Created feedback ID: {}'.format(resp.json()["id"]))