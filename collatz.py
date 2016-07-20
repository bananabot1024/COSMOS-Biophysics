#   Enter starting integer and execute Collatz logic
start = int(raw_input("Enter starting integer: "))
cur_int = start
count = 0
#   Collatz conjecture loop
while cur_int != 1 :
    if cur_int%2 == 0:
        cur_int /=2
    else:
        cur_int = cur_int * 3 + 1
    count = count + 1
print 'Start integer', start, 'satisfies Collatz conjecture in', count,'steps' 

