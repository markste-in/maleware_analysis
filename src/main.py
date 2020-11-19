import pefile
import json
import hashlib
import os
from strings import extract_all_strings
from util.cleanup import iterdict

def hash_file(fname, hash_fnc): #https://stackoverflow.com/a/3431838
    if hash_fnc == 'md5': hash_fun = hashlib.md5()
    elif hash_fnc == "sha1" : hash_fun = hashlib.sha1()
    else: return -1

    try:
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_fun.update(chunk)
        return hash_fun.hexdigest()
    except:
        return -1

def analyze_pefile(filename):
    out ={}
    out['filename'] = filename
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
    


if __name__ == '__main__':
    print(os.path.curdir)
    file = 'samples/lua54.exe'
    if not os.path.exists(file): raise Exception("File does not exist")

    result = iterdict(analyze_pefile(file)) 
    with open("samples/results/sample.json", "w") as outfile: 
        dump = json.dumps(result, sort_keys=False,indent=4, separators=(',', ': '))
        print(dump)
        outfile.write(dump)
    





