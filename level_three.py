'''
This was my first attempt at writing this function

def findMaxinlist(sequence):
    a = 0
    b = 1
    for a in range(len(myList)-2):
        #a += 1
        #b += 1
        if myList[a]>=myList[b]:
            return myList[a]
            b = b+1
        else:
            return myList[b]
            a = a+2
        print(a, b)
'''

# And here's my revised attempt

def findMaxinlist(sequence):
    max = myList[0]
    for number in myList[1:]:
        #chat gpt helped me out with line 21
        if number > max:
            max = number
    return max


myList = [1, 2, 3, 8, 9, 2, 4]

result = findMaxinlist(myList)
print(result)