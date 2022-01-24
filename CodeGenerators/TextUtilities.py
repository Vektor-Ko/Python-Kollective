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
