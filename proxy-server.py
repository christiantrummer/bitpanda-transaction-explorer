# proxy_server.py
from flask import Flask, request, Response
import requests
from flask_cors import CORS
import json
from datetime import datetime
import logging

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BITPANDA_BASE_URL = "https://api.bitpanda.com/v1"

@app.before_request
def log_request_info():
    logger.info('='*50)
    logger.info(f'[{datetime.now()}] Incoming {request.method} request to {request.url}')
    logger.info('Headers:')
    for header, value in request.headers:
        if header == 'X-Api-Key':
            logger.info(f'{header}: [HIDDEN]')
        else:
            logger.info(f'{header}: {value}')
    logger.info(f'Query Parameters: {dict(request.args)}')

@app.route('/<path:path>', methods=['GET'])
def proxy(path):
    try:
        url = f"{BITPANDA_BASE_URL}/{path.lstrip('/')}"
        logger.info(f'Forwarding request to: {url}')

        headers = {
            key: value for (key, value) in request.headers
            if key.lower() not in ['host', 'accept-encoding']  # Remove encoding to prevent compression
        }

        # Add specific headers
        headers.update({
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        })

        logger.info('Making request to Bitpanda...')
        response = requests.get(
            url,
            headers=headers,
            params=request.args,
            timeout=10
        )
        
        logger.info(f'Bitpanda responded with status code: {response.status_code}')
        
        try:
            # Try parsing JSON to ensure it's valid
            json_content = response.json()
            logger.info('Successfully parsed JSON response')
            # Return parsed and re-serialized JSON
            return Response(
                json.dumps(json_content),
                status=response.status_code,
                content_type='application/json'
            )
        except json.JSONDecodeError as e:
            logger.error(f'Invalid JSON response: {str(e)}')
            return {'error': 'Invalid JSON response from Bitpanda'}, 500

    except requests.RequestException as e:
        logger.error(f'Error making request to Bitpanda: {str(e)}')
        return {'error': str(e)}, 500
    except Exception as e:
        logger.error(f'Unexpected error: {str(e)}')
        return {'error': str(e)}, 500

@app.route('/health', methods=['GET'])
def health_check():
    return {'status': 'healthy', 'timestamp': str(datetime.now())}

if __name__ == '__main__':
    logger.info('='*50)
    logger.info('Starting Bitpanda Proxy Server')
    logger.info(f'Proxy server will forward requests to: {BITPANDA_BASE_URL}')
    logger.info('Available endpoints:')
    logger.info('  - /health : Health check endpoint')
    logger.info('  - /* : All other paths will be forwarded to Bitpanda')
    logger.info('Example usage:')
    logger.info('  http://127.0.0.1:5000/wallets')
    logger.info('  http://127.0.0.1:5000/wallets/transactions')
    logger.info('='*50)
    
    app.run(port=5000, debug=True)
