# -*- coding: UTF-8 -*-
import hashlib
import os
import re
import argparse
import json
import shutil
import datetime

from click import command
from setuptools.config.expand import cmdclass


# 兼容下chardet
def install_module(module_name):
    try:
        __import__(module_name)
    except ImportError:
        print(f'{module_name} not found. Installing...')
        cmd = rf"python -m pip install {module_name}"
        print(cmd)
        os.system(cmd)

install_module("chardet")
import chardet

def execute_command(command):
    print("exc command",command)
    exit_code = os.system(command)
    print("exc command ExitCode",exit_code)
    return exit_code

# 
# def GetEnCodingType(FilePath):
#     with open(FilePath, 'rb') as f:
#         result = chardet.detect(f.read())
#     return result['encoding']
# 
# 
# def ProcessStr(Describe,a,b):
#     regex = rf"{a}(.+?){b}"
#     Files = re.findall(regex, Describe)
#     return Files
# 
# def RemoveSubStr(s, sub):
#     return s.replace(sub, '')
# 
# def PrintDividingline(Msg=""):
#     print("-------------------------------------------- ", Msg)
# 
# def ReadFromJson(Path):
#     print(f"ReadFromJson {Path}")
#     if not os.path.exists(Path):
#         print(f"ReadFromJson not exists {Path}")
#         return {}
#     Encoding = GetEnCodingType(Path)
#     with open(Path, 'r',encoding=Encoding) as f:
#         # 读取文件内容
#         data = f.read()
#     # 解析json数据
#     JsonData = json.loads(data)
#     return JsonData
# 
# def SaveToJson(save_obj, path):
#     print(f"save path {path}")
#     json_dumps = json.dumps(save_obj)
#     write = open(path, 'w')
#     write.write(json_dumps)
#     write.close()

# def CopyFileByProperty(Source,Target,Property):
#     print("CopyPakFile",Source,Target,Property)
#     # Input   Root Dir and get all img in per Dir.
#     # Out     Every img with its filename and its dir and its path
#     Cahce = set()
#     for root, dirs, files in os.walk(Source):
#         for file in files:
#             if os.path.splitext(file)[1] in Property:
#                 FilePath = os.path.join(root, file)
#                 FileNewPath = os.path.abspath(Target+"/" + file)
#                 if FileNewPath in Cahce:
#                     print("FileNewPath in Cahce" , FileNewPath,file)
#                 Cahce.add(FileNewPath)
#                 if os.path.exists(FileNewPath) == False:
#                     shutil.copyfile(FilePath,FileNewPath)
# 
# 
def delete_path(root_path):
    print("Delete All File",root_path)
    for root, dirs, files in os.walk(root_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
# 
# 
# def ExecCmd(Cmd):
#     print("ExecCmd:",Cmd)
#     return os.system(Cmd)
# 
# def ReadTXTNRowData(Path,Row):
#     print("TXT    Path ", Path)
#     line = ""
#     with open(Path, 'r') as f:
#         lines = f.readlines()
#         if len(lines) >= (Row + 1):
#             line = lines[Row]
#         f.close()
#     print("Get line",line)
#     line = line.replace("\n", "")
#     print("Get line replace \\n", line)
#     return line
# 
# def EnsurePath(FilePath):
#     print("Ensure Path Name",FilePath)
#     directory = os.path.dirname(FilePath)
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#     else:
#         print(FilePath)
# 
# def GetFileTime(FilePath):
#     timestamp = os.path.getctime(FilePath)
#     dt_object = datetime.datetime.fromtimestamp(timestamp)
#     return dt_object.strftime("%Y%m%d%H%M%S")
# 
# 
# def CheckTask(task_name):
#     result = os.system('schtasks /query | findstr /i {}'.format(task_name))
#     return result == 0  # 如果找到任务，findstr命令返回0，否则返回非0值
# 
# # 删除任务
# def DeleteTask(task_name):
#     result = os.system('schtasks /delete /f /tn {}'.format(task_name))
#     return result == 0  # 如果任务删除成功，schtasks命令返回0，否则返回非0值
# 
# def GetNumberInStr(Str):
#     match = re.findall(r"[-+]?\\d*\\.\\d+|\\d+", Str)
#     return match
# 
# def GetFileHashValue(file_path):
#     sha256_hash = hashlib.sha256()
#     with open(file_path,"rb") as f:
#         # Read and update hash in chunks of 4K
#         for byte_block in iter(lambda: f.read(4096),b""):
#             sha256_hash.update(byte_block)
#     return sha256_hash.hexdigest()
