import subprocess
def extract_all_strings(file):
    lst=subprocess.check_output(['strings', file]).decode().split('\n')
    return lst