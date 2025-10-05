from supplier_app import app  # importe l'application Flask existante
from vercel_wsgi import handle

def handler(event, context):
    # Vercel appelle cette fonction; handle convertit la requête en WSGI
    return handle(app, event, context)
