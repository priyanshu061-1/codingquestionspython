def emptypackets(arr):
    result=[x for x in arr if x!=0]
    zeroes = [0]*(len(arr)-len(result))
    return result+zeroes

arr=[4,5,6,0,7,0,6]
output=emptypackets(arr)
print(output)