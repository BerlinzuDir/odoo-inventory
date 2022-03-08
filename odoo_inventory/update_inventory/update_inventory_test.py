import json
import pytest
from requests import HTTPError
from .update_inventory import create_session

TEST_CONFIG = dict(username='admin', password='admin', base_url='http://localhost:8069', db='odoo')


def test_odoo_session_authentication_returns_authenticated_session():
    session = create_session(TEST_CONFIG)

    res = session.post(url=f"{TEST_CONFIG['base_url']}/web/session/get_session_info", data=json.dumps({}),
                       headers={"Content-Type": "application/json"})

    assert res.json()['result']['is_admin']


def test_odoo_session_authentication_throws_AuthError_on_faulty_credentials():

    with pytest.raises(HTTPError) as e:
        create_session(
            dict(username='admin', password='wrong password', base_url='http://localhost:8069', db='odoo'))
    assert 'Authentication failed' in str(e)