import hashlib

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