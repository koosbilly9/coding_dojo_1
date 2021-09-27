import os
import sys

os.chdir("..")
os.system("C:\PythonSDK\python\python.exe -m pip install -e .")
os.environ["HOME"] = os.getcwd()
os.environ["TWO_TASK"] = "tdipsp92_tdipsp92.w9.bmw.za"

print(f"os path = {sys.path}")
