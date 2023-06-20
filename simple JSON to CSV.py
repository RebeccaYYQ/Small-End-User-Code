"""example data
                 },
                    "status": null,
                    "main": [{
                        "type": "Filler",
                        "itemOne": "111",
                        "itemTwo": fa234,
                        "itemThree": "Test"

output
status,type,itemOne,itemTwo,itemThree
null,Filler,111,fa234,Test
"""

brackets = ['{','[','}',']']

def program(contents):
    headerRow = []
    dataRow = []
    
    for i in contents:
        #trim whitespace and split each item
        stripKeyValue = i.strip().split(":")

        #if that key or value has an open or close bracket, ignore it
        #if it is not a bracket, continue with program
        if any([x in stripKeyValue[0] for x in brackets]):
            continue
        elif any([x in stripKeyValue[1] for x in brackets]):
            continue
        else:
            #remove the " from the key
            headerRow.append(stripKeyValue[0][1:-1])

            #remove whitespace from the value
            cleanValue = stripKeyValue[1].strip()

            #if the last character in value is , remove it
            if cleanValue[-1] == ",":
                cleanValue = cleanValue[:-1]

            #if there is " around the value, remove it
            if cleanValue[0] == '"':
                dataRow.append(cleanValue[1:-1])
            else:
                dataRow.append(cleanValue)
                
    print(','.join(headerRow))
    print(','.join(dataRow))

#below multi-line input is from stackoverflow https://stackoverflow.com/questions/30239092
def getUserInput():
    print('------------------------------------------------------------------------')
    print("Input data, then hit enter, then Ctrl-D to get output")
    
    jsonData = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        jsonData.append(line)
    return jsonData

#-------------------------------------------------------------

jsonData = getUserInput()

while True:
    program(jsonData)
    jsonData = getUserInput()
