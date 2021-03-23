
def mycompare(a, b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i]**2 != b[i]:
            return False
    return True


a = [1,2,3,4]
b = [1,4,9,16]
print(mycompare(a,b))

a = [1,2,3,4]
b = [1,2,3,16]
print(mycompare(a,b))

a = [1,4,5]
b = [1,2]
print(mycompare(a,b))