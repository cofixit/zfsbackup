#!/usr/bin/python3.5

"""

"""

from flask import Flask
from flask import request
app = Flask(__name__)
app.config.from_object('zfsbackup_server')

import pickledb
import json

db = None


@app.route('/clients/register/<address>', defaults={'port': 22})
@app.route('/clients/register/<address>/<port>')
def client_register(address, port):
    if db.get('registered_clients') is None:
        db.dcreate('registered_clients')

    if address in db.dkeys('registered_clients'):
        current_port = db.dget('registered_clients', address)
        return json.dumps({
            'success': False,
            'message': 'Client {} is already registered with port {}.'.format(address, port)
            }), 400

    db.dadd('registered_clients', (address, port))
    db.dump()
    return json.dumps({
        'success': True,
        'message': 'Registered {}:{}'.format(address, port)
        }), 200

@app.route('/clients/remove/<address>')
def client_remove(address):
    if db.get('registered_clients') is None:
        db.dcreate('registered_clients')

    if address not in db.dkeys('registered_clients'):
        return json.dumps({
            'success': False, 
            'message': 'Client {} not registered.'.format(address)
        }), 400

    db.dpop('registered_clients', address)
    return json.dumps({
        'success': True
        }), 200


@app.route('/clients/list')
def client_list():
    if db.get('registered_clients') is None:
        db.dcreate('registered_clients')
    return json.dumps({
        'success': True, 
        'message': db.get('registered_clients')
        }), 200




if __name__ == "__main__":
    if 'DATABASE_FILE' not in app.config:
        raise Exception("No database file provided.")
    db = pickledb.load(app.config['DATABASE_FILE'], True)
    app.run()

