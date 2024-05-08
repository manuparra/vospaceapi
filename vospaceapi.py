import requests
import os

SKA_TOKEN="<REDACTED>"

CAVERNSERVICE="https://spsrc25.iaa.csic.es/cavern/"
USER="/home/mparra/"
URLPATH=CAVERNSERVICE + "files" + USER
NODE="vos://espsrc.iaa.csic.es~arc/home/mparra/"

print("Token: SKA_TOKEN")
print("CAVERN EndPoint: " + CAVERNSERVICE)
print("User VOSpace: " + USER)
print("Node: " + NODE)
 
def voget(url, destination_path):
    headers = {'Authorization': 'Bearer ' + SKA_TOKEN}
    response = requests.get(URLPATH + url, headers=headers)
    if response.status_code == 200:
        with open(destination_path, 'wb') as f:
            f.write(response.content)
        return "File downloaded successfully to {}".format(destination_path)
    else:
        raise Exception("Failed to download file: {}".format(response.status_code))


def voupload(url, file_path):
    headers = {'Authorization': 'Bearer ' + SKA_TOKEN}
    with open(file_path, 'rb') as f:
        file_content = f.read()
    response = requests.put(URLPATH + url, headers=headers, data=file_content)
    if response.status_code == 200:
        return "File uploaded successfully"
    else:
        raise Exception("Failed to upload file: {}".format(response.status_code))
