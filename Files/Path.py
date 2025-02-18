import pathlib

# Create a path object from string
path = pathlib.Path("./foo.txt")
print(path)

# Pass an absolute path
path = pathlib.Path("home/yuna/mnt/d/Learning/1.Python/PythonBasics/Files/foo.txt")
print(path)

# Home
print("Home Directory: ".format(pathlib.Path.home()))

# Current Working Dir
print("CWD: {}".format(pathlib.Path.cwd()))
