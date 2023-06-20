"""example data
                        "type": "Residential",
                        "unitNumber": "2B",
                        "streetNumber": "59",
                        "streetName": "McCaroll",

output
                        "type": "{{type}}",
                        "unitNumber": "{{unitNumber}}",
                        "streetNumber": "{{streetNumber}}",
                        "streetName": "{{streetName}}",
"""
output = []


#below multi-line input is from stackoverflow https://stackoverflow.com/questions/
print("Enter/Paste your content. Hit enter, then Ctrl-D to get output")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

for i in contents:
    #trim whitespace and split each item
    sublist = i.strip().split(":")

    #get the key, and the length of the entire value (including whitespace and comma)
    key = sublist[0][1:-1]
    valueLen = len(sublist[1])

    #subtract the value from that string
    removedValue = i[:-valueLen]

    #add in the key as a variable
    output.append(removedValue + ' "{{' + key + '}}",')
        
print('\n'.join(output))
