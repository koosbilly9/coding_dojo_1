from markdown import markdown

with open("README.md", "r") as f:
    readMe = f.read()

print(markdown(f"{readMe}"))