#!/usr/bin/env pytho
import CSharp_Utilities


#### Generic Methods for Generating code

def WriteDefaultUsings(ft, file):
    if ft == '.cs':
        CSharp_Utilities.WriteDefault_CS_Usings(file)

def WriteClassName(ft, f, n):
    if ft == '.cs':
        CSharp_Utilities.Write_CS_ClassName(f,n)

def WriteFields(ft, f, fields):
    if ft == '.cs':
        CSharp_Utilities.Write_CS_Fields(f,fields)

def WriteProperties(ft, f, properties):
    if ft == '.cs':
        CSharp_Utilities.Write_CS_Properties(f,properties)

def WriteBindingProperties(ft, f, properties):
    if ft == '.cs':
        CSharp_Utilities.Write_CS_BindingProperties(f, properties)
        print('WritingBindingProperties ViewModel')

def WriteConstructor(ft, f, n):
    if ft == '.cs':
        CSharp_Utilities.Write_CS_Constructor(f,n)

def WriteVMConstructor(ft, f, n):
    if ft == '.cs':
        CSharp_Utilities.Write_CS_VMConstructor(f,n)

def WritePrivateMethods(ft, file, methods):
    if ft == '.cs':
        CSharp_Utilities.Write_CS_Private_Methods(file, methods)

def WriteMethods(ft, file, methods):
    if ft == '.cs':
        CSharp_Utilities.Write_CS_Methods(file, methods)



