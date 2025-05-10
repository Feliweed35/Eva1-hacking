# Adaptador de entrada/salida para los escáneres

from scanners.google_dorks import scan_google_dorks
from scanners.dns_scan import scan_dns
from scanners.whois_scan import scan_whois
from scanners.nmap_scan import scan_nmap

def run_scan(tool: str, target: str) -> str:
    if tool == 'google_dorks':
        return scan_google_dorks(target)
    elif tool == 'dns':
        return scan_dns(target)
    elif tool == 'whois':
        return scan_whois(target)
    elif tool == 'nmap':
        return scan_nmap(target)
    else:
        return "Herramienta no soportada."
