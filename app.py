from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)

# Allow all origins (you can also specify a list of allowed origins instead of '*')
CORS(app, origins=["https://thompytime.github.io"])

EXTERNAL_API_URL = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'

@app.route('/api/price')
def get_bitcoin_price():
    try:
        response = requests.get(EXTERNAL_API_URL)
        data = response.json()
        price = data.get('bitcoin', {}).get('usd', None)
        
        if price is None:
            return jsonify({"error": "Bitcoin price not found"}), 404
        
        return jsonify({"bitcoin_price_usd": price})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
