import sys
import os
import platform

print("current sys.path : " + str(sys.path))
if os.name == "posix" :
    package_home=os.environ["PACKAGE_HOME"]
    library_path=os.path.join(package_home, "lib", "python", "w9_scanning_mask")

    if library_path in sys.path:
        pass
    else:
        sys.path.insert(0, library_path)
        print("added path : " + str(sys.path))

print("current sys.path : " + str(sys.path))
print("package_home - needed for dbconnect.dat location ~/config")
if os.name == "nt":
    os.environ["HOME"] = "C:\\PycharmProjects\\w9_scanning_mask\\w9_scanning_mask"
    os.environ["PACKAGE_HOME"] = "C:\\PycharmProjects\\w9_scanning_mask\\w9_scanning_mask"
    os.environ["TWO_TASK"] = "tdipsp92_tdipsp92.w9.bmw.za"

print("final sys.path : " + str(sys.path))

print (
platform.architecture(executable=sys.executable, bits='', linkage=''),
platform.machine(),
platform.node(),
platform.platform(aliased=0, terse=0),
platform.processor(),
platform.python_build(),
platform.python_compiler(),
platform.python_branch(),
platform.python_implementation(),
platform.python_revision(),
platform.python_version(),
platform.python_version_tuple(),
platform.release(),
platform.system(),
platform.system_alias(platform.system(), platform.release(), platform.version()),
platform.version(),
platform.uname()
)

if os.name == "java":
    platform.java_ver(release='', vendor='', vminfo=('', '', ''), osinfo=('', '', ''))

if os.name == 'nt':
   platform.win32_ver()


if os.name == 'posix':
    platform.linux_distribution()
    platform.libc_ver()