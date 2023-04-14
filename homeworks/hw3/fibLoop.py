from time import process_time

def fibLoop():
    total_time = 0
    num_calls = 0
    def getFib(n):
        nonlocal total_time
        nonlocal num_calls
        start = process_time()
        if n == 0:
            result = 0
        elif n == 1:
            result = 1
        else: 
            a = 0 
            b = 1 
            for i in range(2, n + 1):
                result = a + b 
                a = b 
                b = result 
        end = process_time()
        total_time += end - start
        num_calls += 1
        return(result)
    while True:
        val = input("Please enter a non-negative integer or type stop: ")
        if val == "stop":
            break
        try:
            n = int(val)
        except:
            print("Invalid input")
            continue
        if n < 0:
            print("Invalid input")
            continue
        print("fib({}) = {}".format(n, getFib(n)))
        if num_calls > 0:
            print("average runtime: {} seconds".format(total_time / num_calls))