def find_cube_pairs(target):
    # List to store valid pairs
    solutions = []  
    # Find the approximate cube root of the target to set an upper limit
    max_num = round(target ** (1 / 3))  

    # Iterate over possible values of a and b
    for a in range(1, max_num + 1):  
        for b in range(a, max_num + 1):  # Ensure b ≥ a to avoid duplicates
            if a**3 + b**3 == target:  # Check if the sum of cubes matches the target
                solutions.append((a, b))  # Store the valid pair
    
    return solutions  # Return the list of valid pairs

# Call the function with 1729
pairs = find_cube_pairs(1729)

# Print the results
print("Valid cube pairs for 1729:")
for a, b in pairs:
    # Display valid pairs in formatted output
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")
