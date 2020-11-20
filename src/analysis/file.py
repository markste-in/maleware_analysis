import sys
sys.path.append("..")

import os

from util.cleanup import iterdict
from util.pe_header import analyze_pefile
from util.commands import extract_all_strings, filetype
from util.hashing import hash_file

def create_info_dict(file, malware ="unknown", analyzed_sha1 = None):
    if not os.path.exists(file): raise Exception("File does not exist")
    result = {}
    result['filename'] = os.path.basename(file)
    result['md5'] = hash_file(file,"md5")
    result['sha1'] = hash_file(file,"sha1")
    if isinstance(analyzed_sha1, list):
        if result['sha1'] in analyzed_sha1: return -1
    result['filetype'] = filetype(file)
    result["pe_info"] = iterdict(analyze_pefile(file))
    result["strings"] = extract_all_strings(file)
    result["malware"] = malware
    return result