from pathlib import Path
from tqdm import tqdm

from util.json_helper import write_to_json, get_all_strings, clean_strings, prep_list_strings
from analysis.file import create_info_dict
from analysis.string_analysis import *
from util.hashing import get_hash_from_filenames


inp_folder = './../samples/benign/benignware/'
inp_folder_type = "benign"
out_folder = './../samples/results/'

if __name__ == '__main__':

    files = [f for f in Path(inp_folder).rglob('*')]

    print("Found", len(files), "files to process")
    analyzed = get_hash_from_filenames(out_folder)

    for file in tqdm(files):
        results = create_info_dict(file, malware = inp_folder_type, analyzed_sha1= analyzed)
        if isinstance(results,dict): write_to_json(results,out_folder)

    strings = get_all_strings(out_folder)
    cleaned_strings = []
    for i in strings:
        cleaned_strings.append(clean_strings(i))
    X = prep_list_strings(cleaned_strings)
    #print(X)

    (f,x) = bag_of_words(X, 1)
    print(x.shape)

    # from pandas import json_normalize
    #print(json_normalize([flatten_json(result['pe_info'])]))




