# -*- coding: utf-8 -*-
import requests
from odoo import models, fields, api, _


def _call_api(url, token):
    _headers = {"Authorization": "Bearer " + token}
    return requests.get(url=url,
                        headers=_headers)


def _parse_response(response):
    if response.status_code != 200:
        return {"success": False, "message": _("An error occurred, contact your administrator.")}
    return response.json()


def get_data_ruc(url, token):
    response = _call_api(url, token)
    return _parse_response(response)
