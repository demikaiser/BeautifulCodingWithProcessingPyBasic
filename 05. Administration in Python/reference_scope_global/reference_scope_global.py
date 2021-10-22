x = 100
def function1():
    x = 200
    print(x)
function1()
print(x)

y = 300
def function2():
    global y
    y = 400
    print(y)
function2()
print(y)




