n = int(input("Enter the number of terms: "))

first = 0
second = 1

print("Fibonacci Series:", end=" ")

for _ in range(n):
    print(first, end=" ")
    next_term = first + second
    first = second
    second = next_term
