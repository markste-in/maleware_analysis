
import json
import os
import glob
import re

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

def write_to_json(dic, targetdir):
    outdir = os.path.dirname(targetdir)
    os.makedirs(outdir,exist_ok=True)
    with open(os.path.join(outdir, dic['sha1'] + ".json"), "w") as outfile:
        dump = json.dumps(dic, sort_keys=False, indent=4, separators=(',', ': '))
        outfile.write(dump)

def get_all_strings(target_dir):
    files = glob.glob(os.path.join(target_dir,"*.json"))
    strings = []
    for file in files:
        if not os.path.exists(file): raise Exception("Requested file does not exist: " + file)
        with open(file) as json_file:
            data = json.load(json_file)
            strings.append(data["strings"])
    return strings

def clean_strings(l):
    """
    Cleans (removes a lot of unnecessary chars) a non-nested list of strings
    :param l: list of strings
    :return: cleaned list of strings
    """
    out = []
    for i in l:
        splitted = re.split('; |, |\n|\s|_|/|\(|\)|\0|\\\\|\{|\}\[|\]|@', i)
        out.extend([s for s in splitted if len(s) >= 2])
    return out

def prep_list_strings(l):
    out = []
    for i in l:
        out.append(" ".join(i))
    return out
