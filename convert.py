#!/usr/bin/python3

import fileinput
import sys

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

language = 'sv_SE'
tableFile = 'swedishTable'
language = input('input a language\nswedish, english\n')



if language == 'swedish':
    tableFile = 'swedishTable'
    language = 'swedish'
elif language == 'english':
    print('sorry, english not yet implemented')
else :
    print('language unknown\ndefaulting to swedish')
    language ='swedish'

with open('swedishTable') as f:
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
            if(language == 'swedish'):
                print('LANGUAGES = sv_SE, sv_FI', file=outputFile)
            else:
                print(line.strip('\n'), file=outputFile)
        else:
            print(line.strip('\n'), file=outputFile)
            
    outputFile.close()
    
