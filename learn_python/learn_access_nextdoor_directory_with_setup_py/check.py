import sys

original_path = list(sys.path)
print(f"{sys.path}")

sys.path.clear()
print(f"{sys.path}")

sys.path = original_path
print(f"{sys.path}")

import os

print(f"{os.getcwd()}")