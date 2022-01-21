#!/usr/bin/env pytho
import GeneratorUtilities

ClassDict = {}
# Initialize Name of the class
ClassDict['Name'] = ""

# Initialize Fields array for class
ClassDict['Fields'] = []

# Initialize Properties array for class
ClassDict['Properties'] = []

# Initialize Private Method array for class
ClassDict['Private Methods'] = []

# Initialize Methods array for class
ClassDict['Methods'] = []

gu = GeneratorUtilities
 
 ## Opens file passed in as argument then parses file to 
 ## retrieve class definition, and creating values to 
 ## insert into ClassDict
def GetClassDefFromFile(filepath):
    with open(filepath) as fp:
        for line in fp:
            values = line.split()
            if len(values) == 0:
                continue
            key = values[0]
            # End of file reached
            if key == 'E':
                k = key

            # Name of the class reached
            elif key == 'N':
                l = len(line)
                n = l - 2
                ClassDict['Name'] = line[-n:]

            # Property with Original value backing
            elif key == 'OP':
                t = gu.TNL(gu.GetType(values[1]))
                n = gu.TNL(values[2])
                origN = '_Original_{}'.format(n)
                ClassDict['Fields'].append([t,origN])
                ClassDict['Properties'].append([t,n,'true'])

            # Private set Property with Original value backing
            # This will auto generate Public set method for this property
            elif key == 'OPP':
                t = gu.TNL(gu.GetType(values[1]))
                n = gu.TNL(values[2])
                origN = '_Original_{}'.format(n)
                setN = 'Set{}'.format(n)
                ClassDict['Fields'].append([t,origN])
                ClassDict['Properties'].append([t,n, 'true'])
                ClassDict['Methods'].append([t, setN])

            # Field reached
            elif key == 'F':
                t = gu.TNL(gu.GetType(values[1]))
                n = gu.TNL(values[2])
                ClassDict['Fields'].append([t,n])

            # Property reached
            elif key == 'P':
                pT = gu.TNL(gu.GetType(values[1]))
                pN = gu.TNL(values[2])
                ClassDict['Properties'].append([pT,pN])

            # Private Method reached
            elif key == 'PM':
                rt = gu.TNL(gu.GetType(values[1]))
                n = gu.TNL(values[2])
                ClassDict['Private Methods'].append([rt, n])

            # Public Method reached
            elif key == 'M':
                rt = gu.TNL(gu.GetType(values[1]))
                n = gu.TNL(values[2])
                ClassDict['Methods'].append([rt, n])
    return ClassDict
            
