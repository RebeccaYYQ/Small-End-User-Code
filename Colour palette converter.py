#Last change was 28 Jan 2021

#code to convert color palettes, from something like #FFFFFF, #FFFFFF, #FFFFFF
#into [color=#FFFFFF]██[/color][color=#FFFFFF]██[/color][color=#FFFFFF]██[/color]
#this is for BBCode. Makes the colours more visible/easy to read than just numbers.

result = []

print("Type done when done")

palette = input("Palette: ")

while palette != "done":
    broken = list(palette)
    
    #find the hex codes
    for i in range(len(palette)):
        if broken[i] == "#":
            #print(broken[i+1] + broken[i+2] + broken[i+3] + broken[i+4] + broken[i+5] + broken[i+6])
            result.append("[color=#" + broken[i+1] + broken[i+2] + broken[i+3] + broken[i+4] + broken[i+5] + broken[i+6] + "]██[/color]")

    #print all list results on the same line, not seperated by a space 
    print(*result, sep = "")
    result.clear()
    
    #get inputs again
    print("")
    palette = input("Palette: ")
