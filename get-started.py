import pathlib, shutil, os, sys
from dotenv import load_dotenv

load_dotenv()
 
path_root_bot = os.getenv('DIRECTORY')

def extensions_exists_in_path(extension, path):
    file_dir = path
    file_ext = f"*.{extension}"
    try:
        dir_file = list(pathlib.Path(file_dir).glob(file_ext))[0]
        if os.path.exists(dir_file):
            return dir_file
    except:
        return None
    
def move_file(dir_src, dir_dst):
    try:
        shutil.move(dir_src, dir_dst)
    except Exception as err:
        sys.exit(err)


for num in range(2):
    file = extensions_exists_in_path(path=path_root_bot + "started\\", extension="py")
    print(file)
    move_file(dir_dst=path_root_bot, dir_src=file)

shutil.rmtree(path_root_bot + "started\\")