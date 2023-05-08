# initiating
import os
key_word = '```Python Grapher\n'
flag = 0
conter = 0

# get the .md file path (name)
file_path = input('Please scan in the file path:\n') 

# read .md file, and extract file into a list
with open(file_path, 'r', encoding='utf-8') as f:
    file = f.readlines()

# def. a swap_file(.py) list for generating photographs
swap_file = [
    'import matplotlib.pyplot as plt\n',
    'import numpy as np\n',
]

# def. a list of finall_file(.md)
finall_file = []

# core code for for generating swap_file list and finall_file list
for line in file:
    
    if flag == 1 and line[0] != '`':
        swap_file.append(line)
    else:
        finall_file.append(line)

    if line == key_word:
        if flag == 0:
            conter = conter + 1
        flag = 1

    if line == 'plt.close()\n':
        flag = 0

# generating swap_file.py file
with open('swap_file.py', 'w+', encoding='utf-8') as sf:
    for sfline in swap_file:
        sf.write(sfline)

# generating finall_file.md file
with open('finall_file.md', 'w+', encoding='utf-8') as ff:
    for ffline in finall_file:
        ff.write(ffline)

os.system('python swap_file.py')
os.remove('swap_file.py')

print('In total', conter, 'Fig(s), ','Finished!')