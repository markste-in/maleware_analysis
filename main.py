import pefile
import json
import hashlib

def hash_file(fname, hash_fnc): #https://stackoverflow.com/a/3431838
    if hash_fnc == 'md5': hash_fun = hashlib.md5()
    elif hash_fnc == "sha1" : hash_fun = hashlib.sha1()
    else: return -1

    try:
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_fun.update(chunk)
        return hash_fun.hexdigest()
    except:
        return -1
    
def hex_NoneCheck(value):
    if type(value) != type(None):
        return hex(value)
    return ""

def analyze_pefile(filename):
    out ={}
    out['filename'] = filename
    out['md5'] = hash_file(filename,"md5")
    out['sha1'] = hash_file(filename,"sha1")
    try:
        pe = pefile.PE(filename)
    except:
        return json.dumps(out)
    

    sections = []
    for section in pe.sections:
        sections.append(
            {
                "Section" : section.Name.decode().rstrip('\x00'), #https://stackoverflow.com/a/38883513
                "SectionName" : section.name,
                "VirtualAddress" : hex_NoneCheck(section.VirtualAddress),
                "Misc_PhysicalAddress" : hex_NoneCheck(section.Misc_PhysicalAddress),
                "MiscVSize" : hex_NoneCheck(section.Misc_VirtualSize),
                "SizeOfRawData" : section.SizeOfRawData,
                "PointerToRawData" : section.PointerToRawData,
                "next_section_virtual_address" : hex_NoneCheck(section.next_section_virtual_address),
                "IMAGE_SCN_MEM_EXECUTE" : section.IMAGE_SCN_MEM_EXECUTE,
                "IMAGE_SCN_MEM_READ" : section.IMAGE_SCN_MEM_READ

            }
        )
    out['sections'] = sections

    imports = []
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        function_names = []
        for function in entry.imports:
            function_names.append(function.name.decode())
        imports.append({
            "dllName" : entry.dll.decode(),
            "functionNames" : function_names
            })
    out['imports'] = imports

    return out

if __name__ == '__main__':
    result = analyze_pefile('lua54.exe')
    #print(result)

    # Writing to sample.json 
    with open("sample.json", "w") as outfile: 
        dump = json.dumps(result, sort_keys=False,indent=4, separators=(',', ': '))
        #print(dump)
        outfile.write(dump)
    





