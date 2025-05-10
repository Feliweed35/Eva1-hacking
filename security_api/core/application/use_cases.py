# Casos de uso (reglas de aplicación)

from core.domain.services import ScanService

class PerformScanUseCase:
    def __init__(self, scan_service: ScanService):
        self.scan_service = scan_service

    def execute(self, tool: str, target: str, output: str):
        return self.scan_service.create_scan_result(tool, target, output)
