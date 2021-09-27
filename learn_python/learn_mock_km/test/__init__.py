# import os
# import sys
#
# os.chdir("..")
#
# if os.path.isdir('myEgg.egg-info')  :
#     print("")
# else :
#     os.system("C:\PythonSDK\python\python.exe -m pip install -e .")
#
# egg_path = str(f"{os.getcwd()}\myEgg.egg-info")
#
# print(f"{egg_path}")
#
# if egg_path in sys.path :
#     print ("Element Exists")
# else :
#     sys.path.append(egg_path)
#
# print(f"{sys.path}")