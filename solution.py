
def newTrial(input, output = ""):
    for index in range(len(input)):
        if (input[index].isalpha()):
            output += input[index]

        elif(input[index].isalnum()):
            cursor = 1
            index2 = 2
            while cursor != 0:
                if (input[index + index2] == '['):
                    cursor += 1
                    
                elif (input[index + index2] == ']'):
                    cursor -= 1

                index2 += 1
            for times in range(int(input[index]) - 1):

                output = newTrial (input[index + 2 : index + index2 - 1], output)
    return output



test = "3[2[c]ab]e"
test2 = "3[ab2[3[ER]g]2[Q]f]"

print(newTrial(test2))