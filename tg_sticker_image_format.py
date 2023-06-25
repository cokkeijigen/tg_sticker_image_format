# encoding:utf-8
import os
import sys

def check_import(redo: bool = False) -> bool:
    try:
        from PIL import Image
        return True
    except ImportError as err:
        os.system('pip install pillow')
        print(str(err))
        if not redo:
            return check_import(True)
        print('install pillow failed.')
        return False

def folder(path: str) -> str:
    if not (os.path.exists(path) and os.path.isdir(path)):
        os.makedirs(path)
    return path
    
def run_handle(file_path: str) -> None:
    isfile: bool = os.path.isfile(file_path)
    if isfile:
        fileN: str = os.path.basename(file_path)
        file_path = os.path.dirname(file_path)
        file_list: list[str] = [fileN]
    else:
        file_list: list[str] = os.listdir(file_path)
    if not (file_list or len(file_list) < 1): 
        return print('failed.')
    save_path: str = file_path if isfile else os.path.dirname(file_path)  + ('' if isfile else '\\image_new')
    from PIL import Image
    for file in file_list:
        try:
            img: Image = Image.open(str(f'{file_path}/{file}')).convert('RGBA')
            save_file: str = f"{folder(save_path)}\\{file[:file.find('.')]}{'_new' if  isfile else ''}.png"
            print(save_path)
            if img.size[0] == img.size[1]:
                img.resize((512, 512)).save(save_file)
            else:
                basemap: Image = Image.new(mode='RGBA', size=(512, 512))
                if img.size[0] > img.size[1]:
                    adjustHigh: float = 512 * img.size[1] / img.size[0]
                    basemap.paste(img.resize((512, int(adjustHigh))),
                                (0, int((512 - adjustHigh) / 2)),
                                img.resize((512, int(adjustHigh))))
                else:
                    adjustWidth: float = 512 * img.size[0] / img.size[1]
                    basemap.paste(img.resize((int(adjustWidth), 512)),
                                (int((512 - adjustWidth) / 2), 0),
                                img.resize((int(adjustWidth), 512)))
                basemap.save(save_file)
            print(f'{file} done.')
        except Exception as err:
            print(f'{file} failed. err: {str(err)}')
    pass

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(os.path.dirname("c:\\Users\\iTsukezigen\Desktop\\625141945.jpg"))
    else:
        check_import()
        run_handle(sys.argv[1])
    pass
