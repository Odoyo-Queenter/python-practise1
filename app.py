import time
from tracemalloc import start
start = input("press enter to start the timer")
print("the timer has started")
#starts the timer
begin = time.time()
#when the user press "enter" the timer will stop
endtimer = input("press enter to stop the timer")
#get the time at the point the user press enter
end = time.time()
#works out the difference between when the timer started
#and when the user presses enter
elapsed = end - begin
#casts it as an integer to get rid of the decimals
elapsed = int (elapsed)
print("the time elapsed is",elapsed,"seconds")
 