# api/index.py
from supplier_app import app  # importe l’application Flask
import awsgi                 # bibliothèque qui adapte WSGI à AWS Lambda

def handler(event, context):
    return awsgi.response(app, event, context)
