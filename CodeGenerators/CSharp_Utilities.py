#!/usr/bin/env pytho
import TextUtilities

tu = TextUtilities

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
    file.write('\tpublic {}()'.format(name.replace('\n', '')))
    file.write('{\n')
    file.write('\t}')
    file.write('\n\t#endregion\n')
    file.write('\n')

def Write_CS_VMConstructor(file, name):
    file.write('\n\t#region Ctor\n')
    file.write('\tpublic {}ViewModel({} model)'.format(tu.TNL(name), tu.TNL(name)))
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
            pSet = prop[2]
            file.write('\tpublic {} {} {{get; private set;}}\n'.format(pType, pName))
        elif len(prop) == 2:
            file.write('\tpublic {} {} {{get; set;}}\n'.format(pType, pName))
    file.write('\n\t#endregion\n')

def Write_CS_BindingProperties(file, properties):
    file.write('\n\t#region Properties\n')
    for prop in properties:
        pType = prop[0]
        pName = prop[1]
        print(file.write('\tprivate {} _{};\n'.format(pType, pName)))
        file.write('\tpublic {} {} {{get=>_{}; set=>_{} = value;}}\n'.format(pType, pName, pName, pName))
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
