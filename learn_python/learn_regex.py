import re

text = "Hi daar slaai blaar 12 12 12 koos 12 12"


x = re.search("aai",text)

print(x.string)
print(x.span())
print(x.group())

x = re.search("12",text)
print(x.group())

