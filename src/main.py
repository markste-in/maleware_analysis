import os
#from pandas import json_normalize

from util.json_helper import create_dict, write_to_json

import glob

if __name__ == '__main__':
    files = glob.glob('./../samples/*.exe')
    print(os.path.dirname(files[0]))
    for file in files:
        results = create_dict(file)
        write_to_json(results,file)
        print(results)
        #print(json_normalize([flatten_json(result['pe_info'])]))




