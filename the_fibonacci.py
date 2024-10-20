#Simple way calculating fibonacci number:
import time
n=77 
start_time=time.time()
fibPrev=1
fib=1
for _ in range(2,n):
    s,d=fibPrev,fib=fib,fib+fibPrev
    print(d)
end_time=time.time()
print("[Time elapsed for n={}] {}".format(n,end_time-start_time))






print("Fibonacci number for n ={} :{}".format(n,(d)))