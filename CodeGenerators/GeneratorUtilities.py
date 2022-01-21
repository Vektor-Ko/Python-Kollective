#!/usr/bin/env pytho

def GetType(value):
    if value == 'v':
        return 'void'
    elif value == 'b':
        return 'bool'
    elif value == 's':
        return 'string'
    elif value == 'd':
        return 'double'
    elif value == 'L':
        return 'List<T>'
    elif value == 'D':
        return 'Dictionary<T,T>'

def TNL(value):
    return value.replace('\n','')

#### Generic Methods for Generating code

def WriteDefaultUsings(ft, file):
    if ft == '.cs':
        WriteDefault_CS_Usings(file)

def WriteClassName(ft, f, n):
    if ft == '.cs':
        Write_CS_ClassName(f,n)
    elif ft == '.cpp':
        print('todo')

def WriteFields(ft, f, fields):
    if ft == '.cs':
        Write_CS_Fields(f,fields)

def WriteProperties(ft, f, properties):
    if ft == '.cs':
        Write_CS_Properties(f,properties)

def WriteConstructor(ft, f, n):
    if ft == '.cs':
        Write_CS_Constructor(f,n)

def WritePrivateMethods(ft, file, methods):
    if ft == '.cs':
        Write_CS_Private_Methods(file, methods)

def WriteMethods(ft, file, methods):
    if ft == '.cs':
        Write_CS_Methods(file, methods)
    elif ft == '.cpp':
        print("ToDo")





### Methods for generating CS code
def WriteDefault_CS_Usings(file):
    file.write('using System;\n\n')

def Write_CS_ClassName(file, name):
    file.write('public class {}{{\n'.format(name))

def Write_CS_Fields(file, fields):
    file.write('\t#region Fields\n')
    for field in fields:
        fType = field[0]
        fName = field[1]
        file.write('\tprivate {} {};\n'.format(fType, fName))
    file.write('\t#engregion\n')

def Write_CS_Constructor(file, name):
    file.write('\n\t#region Ctor\n')
    print(name)
    file.write('\tpublic {}()'.format(name.replace('\n', '')))
    file.write('{\n')
    file.write('\t}')
    file.write('\n\t#endregion\n')
    file.write('\n')

def Write_CS_Properties(file, properties):
    file.write('\n\t#region Properties\n')
    for prop in properties:
        pType = prop[0]
        pName = prop[1]
        if len(prop) == 3:
            print(len(prop))
            pSet = prop[2]
            file.write('\tpublic {} {} {{get; private set;}}\n'.format(pType, pName))
        elif len(prop) == 2:
            print(len(prop))
            file.write('\tpublic {} {} {{get; set;}}\n'.format(pType, pName))
    file.write('\n\t#endregion\n')

def Write_CS_Private_Methods(file, methods):
    file.write('\n\t#region Private Methods\n')
    for method in methods:
        returnType = method[0]
        methodName = method[1]
        file.write('\tprivate {} {}()\n'.format(returnType, methodName))
        file.write('\t{\n')
        file.write('\t}\n')
    file.write('\n\t#endregion\n')

def Write_CS_Methods(file, methods):
    file.write('\n\t#region Public Methods\n')
    for method in methods:
        file.write('\n')
        returnType = method[0]
        methodName = method[1]
        file.write('\tpublic {} {}()\n'.format(returnType, methodName))
        file.write('\t{\n')
        file.write('\t}\n')
    file.write('\t#endregion\n')
