import time
t_start = time.perf_counter()
f = open('input.txt')
n = int(f.readline())
f.close()
fib1 = 0
fib2 = 1
for _ in range(2, n+1):
    fib1, fib2 = fib2, fib1 + fib2
if n == 0:
    result = 0
else:
    result = fib2
f = open('output.txt', 'w')
f.write(str(result))
f.close()
print("Время работы: %s секунд " % (time.perf_counter() - t_start))