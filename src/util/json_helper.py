from .cleanup import iterdict
from .pe_header import analyze_pefile
import json
import os

def flatten_json(y): #changed version of https://stackoverflow.com/a/51379007
    out = {}

    def flatten(x, name=''):
        if isinstance(x, dict):
            for a in x:
                flatten(x[a], name + a + '_')
        elif isinstance(x,list) or isinstance(x, tuple):
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

def create_dict(file):
    if not os.path.exists(file): raise Exception("File does not exist")
    result = iterdict(analyze_pefile(file))
    return result

def write_to_json(dic, targetdir):
    outdir = os.path.join(os.path.dirname(targetdir), "results")
    os.makedirs(outdir,exist_ok=True)
    with open(os.path.join(outdir, dic['sha1'] + ".json"), "w") as outfile:
        dump = json.dumps(dic, sort_keys=False, indent=4, separators=(',', ': '))
        outfile.write(dump)

