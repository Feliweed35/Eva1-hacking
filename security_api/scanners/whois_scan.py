import subprocess

def scan_whois(domain: str) -> str:
    try:
        result = subprocess.check_output(['whois', domain], text=True)
        return result
    except Exception as e:
        return str(e)
