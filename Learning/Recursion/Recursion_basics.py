# Head Recursion
count = 0
def func():
    global count
    if count == 4:
        return 
    print("Rachit")
    count += 1
    func()

func()

# Tail Recursion

count = 0 
def func():
    global count
    if count == 4 :
        return
    count+= 1
    func()
    print("Rachit")

func()

