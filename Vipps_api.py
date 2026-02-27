"""
Vipps API integration module

Responsibilities:
- Authenticate with Vipps API
- Create payment requests
- Return payment session data used by the backend
"""

import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Vipps production API base URL
BASE_URL = "https://api.vipps.no"

# Credentials stored securely in environment variables
CLIENT_ID = os.getenv("VIPPS_CLIENT_ID")
CLIENT_SECRET = os.getenv("VIPPS_CLIENT_SECRET")
SUB_KEY = os.getenv("VIPPS_SUBSCRIPTION_KEY")
MERCHANT_SN = os.getenv("MERCHANT_SERIAL_NUMBER")


def get_access_token():
    """
    Request an OAuth access token from Vipps.

    The token is required for all authenticated API requests.
    """
    headers = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "Ocp-Apim-Subscription-Key": SUB_KEY
    }

    response = requests.post(f"{BASE_URL}/accessToken/get", headers=headers)
    response.raise_for_status()

    return response.json()["access_token"]


def create_payment(order_id, phone_number, amount_ore, return_url):
    """
    Create a Vipps payment session.

    Parameters:
    - order_id: Unique identifier for the transaction
    - phone_number: Customer phone number
    - amount_ore: Payment amount in øre (1 NOK = 100 øre)
    - return_url: URL Vipps redirects/calls after payment

    Returns:
    JSON response containing payment URL and session details.
    """
    token = get_access_token()

    headers = {
        "Authorization": f"Bearer {token}",
        "Ocp-Apim-Subscription-Key": SUB_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "customerInfo": {
            "mobileNumber": phone_number
        },
        "merchantInfo": {
            "merchantSerialNumber": MERCHANT_SN,
            "callbackPrefix": return_url,
            "fallBack": return_url,
            "returnUrl": return_url
        },
        "transaction": {
            "orderId": order_id,
            "amount": amount_ore
        }
    }

    response = requests.post(
        f"{BASE_URL}/ecomm/v2/payments",
        headers=headers,
        json=payload
    )
    response.raise_for_status()

    return response.json()
