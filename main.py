from os import listdir
from os.path import isfile, join
mypath = 'C:/Users/danie/Documents/school/ict/DA203SPB/Evidence/All External Images/'.replace('/', '\\')
# print(listdir(mypath + '/banner'))
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# print(onlyfiles)

def faf(directory):
  items = listdir(directory)
  files = [[join(directory, f)[53:], f] for f in items if isfile(join(directory, f))]
  directories = [f for f in items if not isfile(join(directory, f))]
  for d in directories:
    d_files = faf(join(directory, d))
    files.extend(d_files)
  return files

with open('all_dirs.csv', 'w') as f:
  all_files = faf(mypath)
  for i in all_files:
    one = i[0]
    two = i[1]
    f.write(one + ',' + two + '\n')
