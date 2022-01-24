## Source Code Generator for C#
import sys
import getopt
import ClassDefParser
import GeneratorUtilities

all_args = sys.argv[1:]
gutils = GeneratorUtilities


try:
    opts, args = getopt.getopt(all_args, "f:t:", ["viewmodel ="])
    print(opts)

    if len(opts) < 2:
      print('usage: ClassGenerator.py -f <required:filepath> -t <required:filetype> -vm <boolean>')

    for opt, arg in opts:
        if opt in ['-f']:
            filePath = arg
        elif opt in ['-t']:
            classFileType = arg
        elif opt in ['--viewmodel ']:
            vm = arg

    ClassDef = ClassDefParser.GetClassDefFromFile(filePath)
    classFile = open("{}{}".format(ClassDef['Name'].replace('\n',''), classFileType), 'w')

    gutils.WriteDefaultUsings(classFileType,classFile)
    gutils.WriteClassName(classFileType,classFile, ClassDef['Name'])
    if len(ClassDef['Fields']) > 0:
        gutils.WriteFields(classFileType,classFile, ClassDef['Fields'])

    gutils.WriteConstructor(classFileType,classFile, ClassDef['Name'])

    if len(ClassDef['Properties']) > 0:
        gutils.WriteProperties(classFileType, classFile, ClassDef['Properties'])
        
    if len(ClassDef['Private Methods']) > 0:
        gutils.WritePrivateMethods(classFileType,classFile, ClassDef['Private Methods'])

    if len(ClassDef['Methods']) > 0:
        gutils.WriteMethods(classFileType,classFile, ClassDef['Methods'])
    classFile.write('}')
    classFile.close()


    if vm == 'true':

        ViewModelFile = open("{}ViewModel{}".format(ClassDef['Name'].replace('\n',''), classFileType), 'w')

        gutils.WriteDefaultUsings(classFileType,ViewModelFile)
        gutils.WriteClassName(classFileType,ViewModelFile, ClassDef['Name'])
        if len(ClassDef['Fields']) > 0:
            gutils.WriteFields(classFileType,ViewModelFile, ClassDef['Fields'])

        gutils.WriteVMConstructor(classFileType,ViewModelFile, ClassDef['Name'])

        if len(ClassDef['Properties']) > 0:
            gutils.WriteBindingProperties(classFileType, ViewModelFile, ClassDef['Properties'])
            
        if len(ClassDef['Private Methods']) > 0:
            gutils.WritePrivateMethods(classFileType,ViewModelFile, ClassDef['Private Methods'])

        if len(ClassDef['Methods']) > 0:
            gutils.WriteMethods(classFileType,ViewModelFile, ClassDef['Methods'])
        ViewModelFile.write('}')
        ViewModelFile.close()


except getopt.GetoptError:
    print("Error")

