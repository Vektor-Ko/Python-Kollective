import sys
import getopt
import MappingDefParser

all_args = sys.argv[1:]

try:
    opts, args = getopt.getopt(all_args, "f:t:")
    print(opts)

    #if len(opts) < 1:
        #print('usage: SpecGenerator.py -f <required:filepath> -t <required:filetype')

    filePath = ''
    classFileType = ''

    for opt, arg in opts:
        print(arg)
        if opt in ['-f']:
            filePath = arg
        elif opt in ['-t']:
            classFileType = arg

    MappingDef = MappingDefParser.GetSpecDefinition('./JSONDef.txt')
    
except getopt.GetoptError:
    print("Error")
