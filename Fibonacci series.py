def fibonacci(n):
    # Initialize the first two terms of the Fibonacci sequence
    a, b = 0, 1
    sequence = []

    # Generate the Fibonacci sequence up to n terms
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence

# Number of terms to be printed
n_terms = int(input("Enter the number of Fibonacci terms to print: "))

# Print the Fibonacci sequence
print(f"Fibonacci sequence up to {n_terms} terms:")
print(fibonacci(n_terms))

