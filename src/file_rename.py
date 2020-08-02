import os
import argparse
import sys

params = None
parser = argparse.ArgumentParser()

# sample command line
# python.exe .\file_Rename.py -p c:\sample_data -v --starts-with "file" --name "hello" --limitcount 5 --startcount 100
def parse():
    global params
    global parser
    parser.add_argument("--dirpath", "-p", help="Provide a path to directory to rename the files",
                        action="store", required=True, dest="dpath")
    parser.add_argument("--starts-with", "-s", help="Find files that start with the provided string",
                        action="store", default="", dest="swith")
    parser.add_argument("--ends-with", "-e", help="Find files that end with the provided string",
                        action="store", default="", dest="ewith")
    parser.add_argument("--quiet", "-q", action="store_false", default=True, dest="verbose")
    parser.add_argument("--verbose", "-v", action="store_true", default=True, dest="verbose")
    parser.add_argument("--name", "-n", action="store",help="Provide base name for files to rename with",
                        required=True, dest="fname")
    parser.add_argument("--startcount", type=int, action="store",help="Provide base name for files to rename with",
                        default=0, dest="startcount")
    parser.add_argument("--limitcount", type=int, action="store",help="Provide base name for files to rename with",
                        default=0, dest="limitcount")
    parser.add_argument("--dryrun", action="store_true",default=False,
                        help="Perform only a dry run and print name change summary",
                        dest="dryrun")                    
    params = parser.parse_args()

def print_params():
    if params.verbose:
        print("Params:")
        for k,v in params.__dict__.items():
            print(f"{k:15}:{v}")
    
def validate_params():
    if params.dpath is None:
        parser("Directory is needed to fetch the files from")
        SystemExit()

def get_files(file_path):
    return os.listdir(file_path)

def filter_files(fileset):
    flist = [x for x in fileset if x.startswith(params.swith) and x.endswith(params.ewith)]
    if not len(flist):
        raise SystemExit("No files selected to rename")
    return flist
    

def create_new_filenames(fileset):
    filenameset = []
    cwidth = len(str(params.startcount + params.limitcount))
    if params.limitcount == 0:
        tgt_count = len(fileset)
    else:
        tgt_count = min(len(fileset), params.limitcount)
    for i in range(params.startcount, params.startcount + tgt_count):
        name = f"{params.fname}{str(i).zfill(cwidth)}"
        filenameset.append(name)
    return filenameset

def main():
    parse()
    print_params()
    validate_params()
    
    try:
        fileset = get_files(params.dpath)
    except FileNotFoundError:
        raise SystemExit(f"directory {params.dpath} not found")

    # Filtering fileset for swith
    fileset = filter_files(fileset)

    os.chdir(params.dpath)
    
    for k, v in dict(zip(fileset,create_new_filenames(fileset))).items():
        if params.dryrun is True:
            print(f"{k} will be renamed as {v}")
        else:
            if params.verbose:
                print(f"File rename: {k} --> {v}")
            os.rename(k,v)
    print(f"Num files changed: {len(fileset)} at path {get_files(params.dpath)}")

if __name__ == "__main__":
    main()