#!/usr/bin/env pytho

class SpecObject:
    name = ""
    lines = []
    def __init__(self, name, lines):
        self.name = name
        self.lines = lines

class Spec:
    objects = []
    arrays = []
    def __init__(self, name):
        self.name = name

ClassDict = {}
ClassDict['Objects'] = []


def GetSpecDefinition(filePath):
    with open(filePath) as fp:
        objectLines = []
        buildingObject = False
        currentObject = ''
        buildingArray = False
        currentArray = ''
        currentLineCounter = 0
        for line in fp:
            currentLineCounter += 1
            values = line.split()
            if len(values) == 0:
                continue
            newSpec = Spec("newSpec")
            key = values[0]

            if key == 'E':
                k = key
                print('At the end of the spec')
                print('Objects = '+str(len(newSpec.objects)))


            elif key == 'O':
                if buildingObject == False:
                    print('current object = '+values[1])
                    currentObject = values[1]
                    buildingObject = True
                elif buildingObject == True:
                    objectLines.append(line)

            elif key == 'OE':
                # you have reached the end of the object decleration
                if buildingObject == True:
                    if currentObject == values[1]:
                        print("reached the end of object: "+ currentObject)
                        buildingObject = False
                        currentObject = ''
                        newObject = SpecObject(currentObject, objectLines)
                        newSpec.objects.append(newObject)
                        # create object object with the lines you gathered
                    else:
                        objectLines.append(line)
                else:
                    if currentObject == values[1]:
                        print("reached the end of object: "+ currentObject)
                        buildingObject = False
                        currentObject = ''
                        
                    # pass in all previous lines into object constructor

            elif key == 'A':
                if buildingObject == True:
                    objectLines.append(line)
                elif buildingObject == False:
                    if buildingArray == False:
                        buildingArray = True
                        currentArray = values[2]
                    elif buildingArray == True:
                        print('Error found Array decleration inside Array decleration')
                        return
                    

            elif key == 'AE':
                print('found end of array')
                if buildingObject == True:
                    objectLines.append(line)
                elif buildingArray == True:
                    print("Error found array decleration within array")
                    return

            elif key == 'M':
                if buildingObject == True:
                    objectLines.append(line)
                else:
                    print('found member decleration')
            else:
                if buildingObject == True:
                    objectLines.append(line)
                elif buildingObject == False:
                    print("Error encountered incorrect value at line" + str(currentLineCounter))
                    return
