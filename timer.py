import time
#To change countdown durration lower the i value to desired number of seconds. 
def stopwatch():
    i = 5
    while i >= 1:
        print(i)
        i-=1
        time.sleep(1)
    return 
