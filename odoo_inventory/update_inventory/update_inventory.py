from typing import TypedDict
from requests import Session, HTTPError
import json


class OdooConfig(TypedDict):
    username: str
    password: str
    base_url: str
    db: str


def create_session(config: OdooConfig) -> Session:
    headers = {"Content-Type": "application/json"}

    data_connect = {
        "params": {
            "db": config['db'],
            "login": config['username'],
            "password": config['password'],
        }
    }

    session = Session()

    r = session.post(url=f"{config['base_url']}/web/session/authenticate", data=json.dumps(data_connect),
                     headers=headers)

    try:
        result = r.json()["result"]
        if result.get("session_id"):
            session.cookies["session_id"] = result.get("session_id")
    except KeyError as e:
        raise HTTPError(
            "Authentication failed. \n "
            "Check your login credentials \n"
            f"{r.json()['error']['data']['debug']}") from e

    return session
