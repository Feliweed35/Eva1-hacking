# Lógica de negocio central

from .entities import ScanResult

class ScanService:
    def create_scan_result(self, tool: str, target: str, output: str) -> ScanResult:
        return ScanResult(tool=tool, target=target, output=output, status="success")
