import json
import os

from util.cleanup import iterdict
from pe_header import analyze_pefile
from util.json import flatten_json
from pandas import json_normalize
import pandas as pd

from glob import glob

if __name__ == '__main__':
    files = glob('samples/*.exe')

    for file in files:
        if not os.path.exists(file): raise Exception("File does not exist")
        result = iterdict(analyze_pefile(file)) 
        with open("samples/results/" + result['sha1'] + ".json", "w") as outfile: 
            dump = json.dumps(result, sort_keys=False,indent=4, separators=(',', ': '))
            outfile.write(dump)
        print("... done with", file)
    # print(dump)
    # print(pd.DataFrame([flatten_json(result)]))
    # print(json_normalize([flatten_json(result)]))
    # print(files)
    # print(json_normalize([flatten_json(result['pe_info'])]))




