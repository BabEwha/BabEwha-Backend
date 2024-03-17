import requests
from .models import Receipt

def send_receipt_to_ai_model(image_path):
    
    url = "http://18.116.163.161/ai/reciept"
    files = {'image': open(image_path, 'rb')}
    response = requests.post(url, files=files)
    return response.json()  # 외부 API로부터 받은 JSON 응답

def update_receipt_with_api_response(receipt_id, api_response):
    receipt = Receipt.objects.get(receipt_id=receipt_id)
    receipt.delivery_fee = api_response.get('delivery_fee')
    receipt.discount_percent = api_response.get('discount_percent')
    receipt.discount_static = api_response.get('discount_static')
    receipt.save()

def calculate_payment_amount(order, delivery_fee, discount_static, discount_percent, current_number_of_people):
    amount = (order.menu_price + (delivery_fee - discount_static) / current_number_of_people) * (1 + discount_percent / 100.0)
    return amount
