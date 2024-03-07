#! /usr/bin/env python3

from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server
import urllib
import json

species = {
    "Cyberman": 'John Lumic',
    'Dalek': 'Davros',
    'Judoon': 'Shadow Proclamation Convention 15 Enforcer',
    'Human': 'Leonardo da Vinci',
    'Ood': 'Klineman Halpen',
    'Silence': 'Tasha Lem',
    'Slitheen': 'Coca-Cola salesman',
    'Sontaran': 'General Staal',
    'Time Lord': 'Rassilon',
    'Weeping Angel': 'The Division Representative',
    'Zygon': 'Broton',
}


def simple_app(environ, start_response):
    global species
    status = '404 Unknown'
    response_body = json.dumps({"credentials": "unknown"}).encode('utf-8')
    if environ['QUERY_STRING'] != '':
        parsed_query_string = urllib.parse.parse_qsl(environ['QUERY_STRING'], keep_blank_values=True)
        key, value = parsed_query_string[-1]
        if key == 'species' and value in species:
            status = '200 OK'
            response_body = json.dumps({"credentials": species[value]}).encode('utf-8')

    headers = [('Content-type', 'application/json; charset=utf-8')]

    start_response(status, headers)

    return [response_body]


with make_server('localhost', 8888, simple_app) as httpd:
    httpd.serve_forever()
