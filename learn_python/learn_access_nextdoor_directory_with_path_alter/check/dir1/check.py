import sys

original_path = list(sys.path)

# sys.path.clear()
# print(f"{sys.path}")

#sys.path.append(original_path)
print(f"{sys.path}")

sys.path.append("C:\\PycharmProjects\\coding_dojo_1\\learn_access_nextdoor_directory_with_path_alter")

print(f"{sys.path}")

import parent.child1.child2.helloMe

print(f"{parent.child1.child2.helloMe.hello()}")

from nextdoor.child1.child2.helloMe import hello

print(f"{hello()}")