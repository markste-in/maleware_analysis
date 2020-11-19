import pefile
import json
import hashlib
import numbers
from strings import extract_all_strings

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
    
def hex_NoneCheck(value):
    if type(value) != type(None):
        return hex(value)
    return ""

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
    return out

def iterdict(d):
    if not d: 
        return ""
    for k, v in d.items():
        if k == "Imported symbols": 
            print("")
        if isinstance(v, dict) :
            iterdict(v)
        elif isinstance(v,list):
            iterlist(v)
        elif isinstance(v,tuple):
            ittertuple(v)
        else:
            v = convert_rest(v)
            d.update({k: v})
    return d

def iterlist(l):
    if not l: 
        return ""
    for i in l:
        if isinstance(i,list):
            iterlist(i)
        elif isinstance(i,dict) :
            iterdict(i)
        elif isinstance(i,tuple):
            ittertuple(i)
        else:
            i = convert_rest(i)
    return l

def ittertuple(t):
    if not t: return ""
    for e in t:
        if isinstance(e,list):
            iterlist(e)
        elif isinstance(e, dict) :
            iterdict(e)
        elif isinstance(e,tuple):
            ittertuple(e)
        else:
            e = convert_rest(e)
    return t

def convert_rest(r):
    if (not isinstance(r, str)) and (not isinstance(r, numbers.Number)):
        r = r.decode().rstrip('\x00')
    return r

if __name__ == '__main__':
    result = analyze_pefile('lua54.exe')
    result = iterdict(result)
    with open("sample.json", "w") as outfile: 
        dump = json.dumps(result, sort_keys=False,indent=4, separators=(',', ': '))
        print(dump)
        outfile.write(dump)
    





