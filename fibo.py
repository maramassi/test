def fibonacci(n):
    """
    Generate Fibonacci sequence up to n terms
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    return fib_sequence

def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using recursion
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

if __name__ == "__main__":
    # Example usage
    n = 10
    print(f"First {n} Fibonacci numbers:")
    print(fibonacci(n))
    
    print(f"\n10th Fibonacci number (recursive):")
    print(fibonacci_recursive(9))  # 0-indexed, so 9th is the 10th number