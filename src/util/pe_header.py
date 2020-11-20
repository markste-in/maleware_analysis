import os
import pefile
from .commands import extract_all_strings, filetype
from .hashing import hash_file


def analyze_pefile(filename):
    out ={}
    out['filename'] = os.path.basename(filename)
    out['md5'] = hash_file(filename,"md5")
    out['sha1'] = hash_file(filename,"sha1")
    out['filetype'] = filetype(filename)
    try:
        pe = pefile.PE(filename)
        out["pe_info"] = pe.dump_dict()
    except pefile.PEFormatError as E:
        print("Error:", str(E))
        out["pe_info"] = {"PEFormatError" : True}
    out["strings"] = extract_all_strings(filename)
    return out