import subprocess

def scan_nmap(target: str) -> str:
    try:
        result = subprocess.check_output(['nmap', '-F', target], text=True)
        return result
    except Exception as e:
        return str(e)
