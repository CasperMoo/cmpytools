import os, fnmatch, json
# import pandas as pd

def findAllFiles(root, pattern = '*'):
    patterns = pattern if isinstance(pattern, list) else [pattern]

    for path, subdirs, files in os.walk(root):
        for name in files:
            for pat in patterns:
                if fnmatch.fnmatch(name, pat):
                    yield os.path.join(path, name), name

def read(path):
    if not os.path.exists(path):
        raise Exception('"{}"文件不存在'.format(path))
    with open(path) as f:
        return f.read()
    return None

def write(filePath: str, text: str, append: bool = False):
    method = 'a' if append else 'w'
    with open(filePath, method) as f:
        f.write(text)

def writeDictFile(filePath: str, data: dict, indent=4):
    with open(filePath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent)

def readDictFile(filePath: str):
    if not os.path.exists(filePath):
        raise Exception('"{}"文件不存在'.format(filePath))
    with open(filePath, 'r') as f:
        return json.load(f)

# def writeCsvFile(filePath: str, data: pd.DataFrame):
#     try:
#         os.remove(filePath)
#     except OSError:
#         pass
#     data.to_csv(filePath, index=False)


# def readCsvFile(filePath: str):
#     if not os.path.exists(filePath):
#         raise Exception('"{}"文件不存在'.format(filePath))
#     return pd.read_csv(filePath, index_col=None)


def prettyfyDict(dict):
    return json.dumps(dict, indent=1)

def inputFilePath(prompt: str):
    file_path = input(prompt).strip()
    while not os.path.isfile(file_path):
        print('"{}"文件不存在'.format(file_path))
        file_path = input(prompt)
    return file_path

def inputDirectoryPath(prompt: str):
    dir_path = input(prompt).strip()
    # dir_path = os.path.join(dir_path, '')
    while not os.path.isdir(dir_path):
        print('"{}"目录不存在'.format(dir_path))
        dir_path = input(prompt)
    return dir_path


