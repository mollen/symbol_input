import fileinput

def writeIBUSTable(lines, outputFile):
    nrSymbols = len(lines)
    for lineID in range(nrSymbols):
        line = lines[lineID]
        words = line.split(' ')
        frequency = 1
        print(words[0], words[1].strip('\n'), frequency, file=outputFile, sep='\t')

tableType = 'IBUS'
language = 'sv_SE'

tableFile = 'swedishTable'
if language == 'sv_SE':
    tableFile = 'swedishTable'

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
            if(language == 'sv_SE'):
                print('LANGUAGES = sv_SE', file=outputFile)
            else:
                print(line.strip('\n'), file=outputFile)
        else:
            print(line.strip('\n'), file=outputFile)
            
    outputFile.close()
    
