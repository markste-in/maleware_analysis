#from pandas import json_normalize
from util.json_helper import create_dict, write_to_json, get_all_strings, clean_strings, prep_list_strings
from analysis.string_analysis import *
import glob
from tqdm import tqdm
inp_folder = './../samples/benign/benignware/*'
inp_folder_type = "benign"
out_folder = './../samples/results/'

if __name__ == '__main__':

    files = glob.glob(inp_folder)
    print("Found", len(files), "files to process")
    for file in tqdm(files):
        results = create_dict(file,malware = inp_folder_type)
        write_to_json(results,out_folder)

    strings = get_all_strings(out_folder)
    cleaned_strings = []
    for i in strings:
        cleaned_strings.append(clean_strings(i))
    X = prep_list_strings(cleaned_strings)
    print(len(X))

    (f,x) = bag_of_words(X, 1)
    print(x.shape)





        #print(json_normalize([flatten_json(result['pe_info'])]))




