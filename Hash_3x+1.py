def hash_function(Wn, A, B, C):
    # Convert Wn into decimal form
    X = int(Wn, 2)
    
    # Counter for zero words
    counter = 0
    
    # Process each word
    if X == 0:
        counter += 1
        if counter % 2 != 0:
            X = A ^ (B * C)
        else:
            X = A & (C * B)
    
    # Apply the 3X+1 conjecture 10 times
    X_prime = X
    for _ in range(10):
        if X % 2 == 0:
            X = X // 2
        else:
            X = 3 * X + 1
    
    # XOR operation
    result = X ^ X_prime
    
    # Return the hexadecimal representation
    return hex(result)

# Example usage:
A = 0b10101010
B = 0b11001100
C = 0b11110000

# Example 32-bit binary word
Wn = '00000000000000000000000000000001'
hash_output = hash_function(Wn, A, B, C)
hash_output
