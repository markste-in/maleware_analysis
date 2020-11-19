from util.hashing import hash_file
import pefile
from strings import extract_all_strings
import os

def analyze_pefile(filename):
    out ={}
    out['filename'] = os.path.basename(filename)
    out['md5'] = hash_file(filename,"md5")
    out['sha1'] = hash_file(filename,"sha1")
    try:
        pe = pefile.PE(filename)
        out["pe_info"] = pe.dump_dict()
    except Exception as E:
        print("Error" + E)
        return out   
    out["strings"] = extract_all_strings(filename)
    return out