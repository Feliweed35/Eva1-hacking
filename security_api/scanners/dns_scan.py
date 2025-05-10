import subprocess

def scan_dns(domain: str) -> str:
    try:
        result = subprocess.check_output(['nslookup', domain], text=True)
        return result
    except Exception as e:
        return str(e)
