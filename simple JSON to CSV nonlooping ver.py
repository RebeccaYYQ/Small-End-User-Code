"""example data
                "type": "Filler",
                "unitNumber": "111",
                "streetNumber": 111,
                "streetName": "Test"

output
type,unitNumber,streetNumber,streetName
Filler,111,111,Test
"""

headerRow = []
dataRow = []

def cleanKey(key):
    headerRow.append(key[1:-1])

def cleanValue(value):
    noComma = value.strip()

    #if the last character is , remove it
    if value[-1] == ",":
        noComma = noComma[:-1]

    #if there is " around it remove
    if noComma[0] == '"':
        dataRow.append(noComma[1:-1])
    else:
        dataRow.append(noComma)

#below multi-line input is from stackoverflow https://stackoverflow.com/questions/30239092
print("Enter/Paste your content. Hit enter, then Ctrl-D to continue")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

for i in contents:
    #print("item: " + i)
    #trim whitespace and split each item
    sublist = i.strip().split(":")
    #print(sublist)
    #print("=----")
    cleanKey(sublist[0])
    cleanValue(sublist[1])
            
print(','.join(headerRow))
print(','.join(dataRow))
