#!/usr/bin/python3

import fileinput
import sys
from os import listdir
from os.path import isfile

from sys import exit

def writeIBUSTable(lines, outputFile):
    nrSymbols = len(lines)
    for lineID in range(nrSymbols):
        line = lines[lineID]
        words = line.split(' ')
        frequency = 1
        if(len(words) >= 2):
            print(words[0], words[1].strip('\n'), frequency, file=outputFile, sep='\t')
        else:
            print("line", lineID, "not properly formatted: ", line)
            
tableType = 'IBUS'

tables = listdir("./tables")

table = input('input a table\n' + str(tables) + '\n')

language = 'swedish'
tableFile = 'swedish'

if table == 'swedish':
    tableFile = 'swedish'
    language = 'swedish'
elif table == 'english':
    tableFile = 'english'
    language = 'english'
elif set([table]) & set(tables):
    tableFile = table
    language = 'other'
else :
    print('unknown table\ndefaulting to swedish')


with open('./tables/' + tableFile) as f:
    lines = f.readlines()
    lines = list(line for line in lines if line.strip(' ').strip('\n') and (not line.startswith('#')))

if(tableType == 'IBUS'):
    outputFile = 'ibusTable'
    outputFile = open(outputFile, 'w')
    templateFile = 'ibusTableTemplate'
    
    for line in fileinput.input(templateFile):
        if line == '###INSERT_HERE###\n':
            writeIBUSTable(lines, outputFile)
        elif line == 'LANGUAGES = sv_SE\n':
            if language == 'swedish':
                print('LANGUAGES = sv_SE, sv_FI', file=outputFile)
            elif language == 'english':
                print('LANGUAGES = en_US, en_GB', file=outputFile)
            elif language == 'other':
                print('LANGUAGES = other', file=outputFile)
            else:
                print(line.strip('\n'), file=outputFile)
        else:
            print(line.strip('\n'), file=outputFile)
            
    outputFile.close()
    
