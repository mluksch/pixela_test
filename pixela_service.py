import string
import uuid

import requests

import config

PIXELA_ENDPOINT = "https://pixe.la/v1"


def create_user(username: str):
    """https://docs.pixe.la/entry/post-user"""
    url = f"{PIXELA_ENDPOINT}/users"
    token = str(uuid.uuid4())
    res = requests.post(url, json={
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    })
    res.raise_for_status()
    with open(f"{config.USER_TOKEN_NAME}.txt", "w") as f:
        f.write(token)
    print(res.json())


def create_new_graph(username: str, graphname: str, unit: str = "commit", type: str = "int", color: str = "shibafu"):
    """https://docs.pixe.la/entry/post-graph"""
    url = f"{PIXELA_ENDPOINT}/users/{username}/graphs"
    graph_id = "".join([letter for letter in graphname.lower() if letter in string.ascii_lowercase])
    with open(f"{config.USER_TOKEN_NAME}.txt") as f:
        usertoken = f.read()
    res = requests.post(url, json={
        "id": graph_id,
        "name": graphname,
        "unit": unit,
        "type": type,
        "color": color
    }, headers={"X-USER-TOKEN": usertoken})
    res.raise_for_status()
    with open(f"{config.GRAPH_TOKEN_NAME}.txt") as f:
        f.write(graph_id)
    print(res.json())
