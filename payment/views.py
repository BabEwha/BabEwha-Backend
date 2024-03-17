from django.http import JsonResponse
from rest_framework import views
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Receipt
from .serializers import ReceiptSerializer
from .utils import send_receipt_to_ai_model, update_receipt_with_api_response

class ReceiptUploadView(views.APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = ReceiptSerializer(data=request.data)
        if serializer.is_valid():
            receipt = serializer.save()
            # 영수증 이미지를 외부 API로 전송하고 응답을 받음
            api_response = send_receipt_to_ai_model(receipt.receipt_image.path)
            # API 응답을 바탕으로 Receipt 인스턴스 업데이트
            update_receipt_with_api_response(receipt.id, api_response)
            return JsonResponse({'message': 'Receipt processed successfully.'})
        return JsonResponse(serializer.errors, status=400)
