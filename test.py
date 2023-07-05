import time

def wait(time_to_wait):
    time_to_wait = str(time_to_wait)
    time.sleep((float(time_to_wait)/1000))

x = 1
yo_mama = ("yo mama haha")
current_loop_iteration = 1

if x == 1:
    wait(1000)
    print("hello world")
    wait(100)

y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

for element in y:
    wait(200)
    print(f"whoa i found something {current_loop_iteration}")
    current_loop_iteration = current_loop_iteration + 1
    if type(element) is int or float:
        wait(800)
        print("it was a number \n")
    if type(element) is str:
        wait(800)
        print("it was text \n")
    else:
        wait(800)
        print(f"it was {yo_mama}!! nah im just kidding i have no clue what that was \n")




