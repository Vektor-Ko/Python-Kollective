## Source Code Generator for C#
import sys
import getopt
import ClassDefParser
import GeneratorUtilities

all_args = sys.argv[1:]
gutils = GeneratorUtilities


try:
    opts, args = getopt.getopt(all_args, "f:t:", ["viewmodel ="])

    if len(opts) < 2:
        print('usage: ClassGenerator.py -f <required:filepath> -t <required:filetype> -vm <boolean>')

    for opt, arg in opts:
        if opt in ['-f']:
            filePath = arg
        elif opt in ['-t']:
            fileType = arg
        elif opt in ['--viewmodel']:
            vm = arg

    ClassDef = ClassDefParser.GetClassDefFromFile(filePath)
    file = open("{}{}".format(ClassDef['Name'].replace('\n',''), fileType), 'w')

    gutils.WriteDefaultUsings(fileType,file)
    gutils.WriteClassName(fileType,file, ClassDef['Name'])

    if len(ClassDef['Fields']) > 0:
        gutils.WriteFields(fileType,file, ClassDef['Fields'])

    gutils.WriteConstructor(fileType,file, ClassDef['Name'])

    if len(ClassDef['Properties']) > 0:
        gutils.WriteProperties(fileType, file, ClassDef['Properties'])
        
    if len(ClassDef['Private Methods']) > 0:
        gutils.WritePrivateMethods(fileType,file, ClassDef['Private Methods'])

    if len(ClassDef['Methods']) > 0:
        gutils.WriteMethods(fileType,file, ClassDef['Methods'])
    file.write('}')

except getopt.GetoptError:
    print("Error")

