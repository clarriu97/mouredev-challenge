
fib_numbers = []

for i in range(50):
    if i == 0 or i == 1:
        fib_numbers.append(i)
        continue
    current_fib = fib_numbers[i-1] + fib_numbers[i-2]
    fib_numbers.append(current_fib)

print("The 50 first numbers of the Fibonacci sequence are: ", end="")
for num in fib_numbers:
    print(num, end=" ")
