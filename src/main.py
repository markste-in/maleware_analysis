from pathlib import Path
from tqdm import tqdm

from util.json_helper import write_to_json, get_all_strings, clean_strings, prep_list_strings
from analysis.file import create_info_dict
from analysis.string_analysis import *
from util.hashing import get_hash_from_filenames

import numpy as np

inp_folder = './../samples/malware/malware'
inp_folder_type = "malware"
out_folder = './../samples/results/'

if __name__ == '__main__':

    files = [f for f in Path(inp_folder).rglob('*') if f.is_file()]
    print(files)
    #exit()
    print("Found", len(files), "files to process")

    #Get hashes from file names to check what was previously analyzed (will be skipped)
    analyzed = get_hash_from_filenames(out_folder)

    for file in tqdm(files):
        results = create_info_dict(file, malware = inp_folder_type, analyzed_sha1= analyzed)
        if isinstance(results,dict): write_to_json(results,out_folder)

    strings = get_all_strings(out_folder)
    cleaned_strings = []
    for i in strings:
        cleaned_strings.append(clean_strings(i))
    X = prep_list_strings(cleaned_strings)

    (f,x) = bag_of_words(X, 1)
    print(x.shape)

    with open('count_of_vectors.npy', 'wb') as f:
        np.save(f,x)


    # from pandas import json_normalize
    #print(json_normalize([flatten_json(result['pe_info'])]))




