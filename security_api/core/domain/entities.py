# Representaciones del dominio

from dataclasses import dataclass

@dataclass
class ScanResult:
    tool: str
    target: str
    output: str
    status: str
