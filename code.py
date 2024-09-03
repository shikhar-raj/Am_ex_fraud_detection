def find_15th_digit(account_number):
    # Convert the 14-digit account number to a list of integers
    digits = [int(d) for d in str(account_number)]
    
    if len(digits) != 14:
        raise ValueError("Account number must be 14 digits long")
    
    # Insert a placeholder for the 15th digit (to be guessed)
    digits.append(0)
    
    # Double every second digit from the right (starting from the rightmost digit)
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        # If doubling results in a number greater than 9, subtract 9 from it
        if digits[i] > 9:
            digits[i] -= 9
    
    # Calculate the total sum of the digits
    total_sum = sum(digits)
    
    # The 15th digit is the one that makes the total sum divisible by 10
    check_digit = (10 - (total_sum % 10)) % 10
    
    return check_digit

# Example usage:
account_number = 99390049372722  # Replace with your 14-digit account number
digit_15 = find_15th_digit(account_number)
print(f"The 15th digit of the account number is: {digit_15}")
