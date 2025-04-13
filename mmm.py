def count_bits_to_swap(a, b):
    xor = a ^ b
    count = 0
    while xor:
        count += xor & 1
        xor >>= 1
    return count

a = 29  
b = 15  
print(f"Bits to be swapped: {count_bits_to_swap(a, b)}")
