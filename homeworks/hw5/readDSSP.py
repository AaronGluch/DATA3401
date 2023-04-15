import sys
import os

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r') as f:
    lines = f.readlines()

start = 0
for i in range(len(lines)):
    if '#' in lines[i]:
        start = i+1

AAloc = 0
ACCloc = 0
for i in range(len(lines[start])):
    if lines[start][i] == 'L':
        AAloc = i
for i in range(len(lines[start]) - 8):
    if lines[start][i + 8] == '1':
        ACCloc = i + 8
ACCloc = 35

maxDict = {
'A': 129.0,
'R': 274.0,
'N': 195.0,
'D': 193.0,
'C': 167.0,
'Q': 225.0,
'E': 223.0,
'G': 104.0,
'H': 224.0,
'I': 197.0,
'L': 201.0,
'K': 236.0,
'M': 224.0,
'F': 240.0,
'P': 159.0,
'S': 155.0,
'T': 172.0,
'W': 285.0,
'Y': 263.0,
'V': 174.0,
'!': 100.0,
}

def p(input):
    name = ''
    slashchecker = 0
    for c in range(len(input)):
        if (input[::-1][c] != '/') & (slashchecker == 0):
            name += input[::-1][c]
        else: slashchecker = 1
    name = name[::-1]
    if '.dssp' in name:
        name = name[0:len(name) - 5]
    return name

protein = p(input_file)

AA = []
ACC = []
acc = ''
for i in range(start, len(lines)):
    AA.append(lines[i][AAloc])
for i in range(start, len(lines)):
    for j in range(ACCloc, ACCloc + 3):
        acc += lines[i][j]
    ACC.append(acc)
    acc = ''

ACCuseable = []
for i in range(len(ACC)):
    ACCuseable.append(int(ACC[i].replace(" ", "")))

RSA = []
for i in range(len(ACC)):
    RSA.append(ACCuseable[i] / maxDict[AA[i]])

row1 = ''
for i in range(len(protein) + 1):
    row1 += " "
row1 += 'AA ACC RSA(ACC/AA)\n'
rows = []
row = ""
for i in range(len(AA)):
    row += protein
    row += " "
    row += AA[i]
    row += "  "
    row += ACC[i]
    row += " "
    row += str(RSA[i])
    row += '\n'
    rows.append(row)
    row = ""

if os.path.isfile(output_file):
    o = open(output_file, 'a')
    o.write("\n")
    o.write(row1)
    o.write("".join(rows))
    o.close()
else:
    o = open(output_file, 'w')
    o.write(row1)
    o.write("".join(rows))
    o.close()