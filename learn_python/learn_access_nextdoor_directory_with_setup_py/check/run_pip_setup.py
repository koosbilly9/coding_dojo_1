import os

print(f"{os.getcwd()}")

os.chdir("..")

print(f"{os.getcwd()}")

os.system('C:\PythonSDK\python\python.exe -m pip install -e .')