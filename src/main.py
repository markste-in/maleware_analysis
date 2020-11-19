import json
import os

from util.cleanup import iterdict
from pe_header import analyze_pefile



if __name__ == '__main__':
    print(os.path.curdir)
    file = 'samples/lua54.exe' #some simple benign samples
    if not os.path.exists(file): raise Exception("File does not exist")

    result = iterdict(analyze_pefile(file)) 
    with open("samples/results/sample.json", "w") as outfile: 
        dump = json.dumps(result, sort_keys=False,indent=4, separators=(',', ': '))
        print(dump)
        outfile.write(dump)
    





