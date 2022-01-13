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


def _get_graph_id_from_name(graphname: str):
    graph_id = "".join([letter for letter in graphname.lower() if letter in string.ascii_lowercase])
    return graph_id


def create_new_graph(username: str, graphname: str, unit: str = "count", type: str = "int", color: str = "shibafu"):
    """https://docs.pixe.la/entry/post-graph"""
    url = f"{PIXELA_ENDPOINT}/users/{username}/graphs"
    graph_id = _get_graph_id_from_name(graphname)
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


import datetime


def create_pixel(username: str, graphname: str, quantity: str = "1", date: datetime.datetime = datetime.datetime.now()):
    graph_id = _get_graph_id_from_name(graphname)
    url = f"{PIXELA_ENDPOINT}/users/{username}/graphs/{graph_id}"
    with open(f"{config.USER_TOKEN_NAME}.txt") as f:
        usertoken = f.read()
    res = requests.post(url, json={
        "date": date.strftime("%Y%m%d"),
        "quantity": quantity
    }, headers={
        "X-USER-TOKEN": usertoken
    })
    print(res.json())
    res.raise_for_status()
    print(res.json())


def get_pixel(username: str, graphname: str, date: datetime.datetime):
    with open(f"{config.USER_TOKEN_NAME}.txt") as f:
        usertoken = f.read()
    graphid = _get_graph_id_from_name(graphname)
    url = f"{PIXELA_ENDPOINT}/users/{username}/graphs/{graphid}/{date.strftime('%Y%m%d')}"
    res = requests.get(url, headers={
        "X-USER-TOKEN": usertoken
    })
    res.raise_for_status()
    return res.json()


def get_graph_svg_url(username: str, graphname: str):
    graphid = _get_graph_id_from_name(graphname)
    url = f"{PIXELA_ENDPOINT}/users/{username}/graphs/{graphid}"
    return url


def get_graph_svg(username: str, graphname: str):
    url = get_graph_svg_url(username=username, graphname=graphname)
    res = requests.get(url)
    res.raise_for_status()
    return res.text


def get_graph_html_url(username: str, graphname: str, mode: str = "simple"):
    graphid = _get_graph_id_from_name(graphname)
    url = f"{PIXELA_ENDPOINT}/users/{username}/graphs/{graphid}.html"
    return url


def get_graph_html(username: str, graphname: str, mode: str = "simple"):
    url = get_graph_html_url(username=username, graphname=graphname)
    res = requests.get(url, params={"mode": mode})
    res.raise_for_status()
    return res.text
