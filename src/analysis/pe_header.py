import pefile
import peutils
import os

def analyze_pefile(filename):

    out ={}
    try:
        pe = pefile.PE(filename)
        out["pe_info"] = pe.dump_dict()
    except pefile.PEFormatError as E:
        print("Error:", str(E))
        out["pe_info"] = {"PEFormatError" : True}

    with open('../db/signatures/UserDB.TXT', 'rt') as f:
        sig_data = f.read()
    signatures = peutils.SignatureDatabase(data=sig_data)

    matches = signatures.match_all(pe,ep_only=True)
    if matches: print("Found signature match:", matches)
    out["signature_matches"] = matches
    try:
        sig_gen = signatures.generate_ep_signature(pe, os.path.basename(filename))
        out["generated_ep_signature"] = sig_gen
    except pefile.PEFormatError as E:
        out["generated_ep_signature"] = str(E)
    return out