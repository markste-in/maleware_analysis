import numbers

def iterdict(d): # removes byte characters and empty dicts/lists etc...
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