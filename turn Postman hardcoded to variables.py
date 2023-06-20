"""
example data
                 },
                    "status": null,
                    "main": [{
                        "type": "Filler",
                        "itemOne": "111",
                        "itemTwo": fa234,
                        "itemThree": "Test"

output
                 },
                    "status": "{{status}}",
                    "main": [{
                        "type": "{{type}}",
                        "itemOne": "{{itemOne}}",
                        "itemTwo": "{{itemTwo}}",
                        "itemThree": "{{itemThree}}",
"""

brackets = ['{','[','}',']']

def program(contents):
    output = []
    for keyValue in contents:
        #trim whitespace and split each item
        stripKeyValue = keyValue.strip().split(":")

        #if that key or value has an open or close bracket, ignore it and add to output
        #if it is not a bracket, continue with program
        if any([x in stripKeyValue[0] for x in brackets]):
            output.append(keyValue)
        elif any([x in stripKeyValue[1] for x in brackets]):
            output.append(keyValue)
        else:
            #get the key, and the length of the entire value (including whitespace and comma)
            key = stripKeyValue[0][1:-1]
            valueLen = len(stripKeyValue[1])

            #subtract the entire value from the original KeyValue string
            removedValue = keyValue[:-valueLen]

            #add in the key as a variable
            output.append(removedValue + ' "{{' + key + '}}",')
            
    print('\n'.join(output))

#below multi-line input is from stackoverflow https://stackoverflow.com/questions/30239092
def getUserInput():
    print('------------------------------------------------------------------------')
    print("Input data, then hit enter, then Ctrl-D to get output")
    
    postmanData = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        postmanData.append(line)
    return postmanData

#-------------------------------------------------------------

postmanData = getUserInput()

while True:
    program(postmanData)
    postmanData = getUserInput()
    
