from config import vuln_app
import os
from flask import jsonify

app = vuln_app.app

@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Cross-Origin-Resource-Policy'] = 'same-origin' 
    return response

if __name__ == '__main__':
    vuln_app.run(host='0.0.0.0', port=5000, debug=False)
