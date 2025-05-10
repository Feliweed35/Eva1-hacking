from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import ScanRequestSerializer, ScanResponseSerializer
from adapters.scanner_adapter import run_scan
from core.domain.services import ScanService
from core.application.use_cases import PerformScanUseCase

class ScanAPIView(APIView):
    def post(self, request):
        serializer = ScanRequestSerializer(data=request.data)
        if serializer.is_valid():
            tool = serializer.validated_data['tool']
            target = serializer.validated_data['target']
            output = run_scan(tool, target)

            use_case = PerformScanUseCase(ScanService())
            scan_result = use_case.execute(tool, target, output)

            response_serializer = ScanResponseSerializer(scan_result)
            return Response(response_serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
