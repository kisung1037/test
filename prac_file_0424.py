from os import linesep


with open('bar.txt', 'rt') as file:
  data = file.read()
  print(data)

with open("bar.txt",'wt') as file:
  print("file out", file=file)