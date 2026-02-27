"""
FastAPI backend for Coffee Tasting Booking System

Responsibilities:
- Serve the website
- Create Vipps payments
- Receive Vipps webhook callbacks
- Trigger ESP32 robot arm after successful payment
"""

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import uuid
import os

from vipps_api import create_payment
from esp32 import activate_robot_arm

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Serve static files (CSS, images, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure HTML templates (Jinja2)
templates = Jinja2Templates(directory="templates")

# Environment configuration
ROBOT_COST = int(os.getenv("ROBOT_COST"))  # Price sent to Vipps
ESP32_IP = os.getenv("ESP32_IP")          # ESP32 device address


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """
    Render the main webpage.
    """
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/pay")
def pay(request: Request, phone: str = Form(...)):
    """
    Creates a Vipps payment request.

    Steps:
    1. Generate a unique order ID
    2. Call Vipps API to create payment
    3. Redirect user to Vipps payment page
    """
    order_id = str(uuid.uuid4())

    # Public callback endpoint (exposed via ngrok during development)
    callback_url = "https://fragmented-georgeanna-iatric.ngrok-free.dev/vipps-callback"

    result = create_payment(order_id, phone, ROBOT_COST, callback_url)
    payment_url = result["url"]

    return RedirectResponse(payment_url)


@app.post("/vipps-callback")
def vipps_callback(data: dict):
    """
    Webhook endpoint called by Vipps after payment.

    When payment confirmation is received:
    - Activate the ESP32 robot arm
    """
    print("Vipps callback:", data)

    activate_robot_arm()

    return {"status": "robot activated"}
