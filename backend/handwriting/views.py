from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import convert_handwriting

class HandwritingAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            text = request.data.get('text', '')  # Use request.data for DRF
            convert_handwriting(text)
            return Response({'success': True}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'success': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return Response({'success': False, 'error': 'Only POST requests are allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
