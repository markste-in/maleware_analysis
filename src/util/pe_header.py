import pefile

def analyze_pefile(filename):

    out ={}
    try:
        pe = pefile.PE(filename)
        out["pe_info"] = pe.dump_dict()
    except pefile.PEFormatError as E:
        print("Error:", str(E))
        out["pe_info"] = {"PEFormatError" : True}
    return out