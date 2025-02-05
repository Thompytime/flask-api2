from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# External API URL (CoinGecko's Bitcoin price)
EXTERNAL_API_URL = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'

@app.route('/api/price')
def get_bitcoin_price():
    try:
        # Fetch data from the external API
        response = requests.get(EXTERNAL_API_URL)
        
        # Ensure the response is a valid JSON
        data = response.json()
        
        # Extract the Bitcoin price in USD
        price = data.get('bitcoin', {}).get('usd', 'No data available')
        
        if price == 'No data available':
            return jsonify({"error": "Bitcoin price not found"}), 404
        
        return jsonify({"bitcoin_price_usd": price})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
