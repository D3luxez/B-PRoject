def decimal_to_binary(decimal_num):
  """
  Converts a decimal number to its binary representation.

  Args:
    decimal_num: The decimal number to convert.

  Returns:
    The binary representation of the decimal number as a string.
  """
  if decimal_num == 0:
    return "0"

  binary_num = ""
  while decimal_num > 0:
    remainder = decimal_num % 2
    binary_num = str(remainder) + binary_num
    decimal_num //= 2
  return binary_num

# Get the decimal number from the user
decimal_num = int(input("Enter a number: "))

# Convert the decimal number to binary
binary_num = decimal_to_binary(decimal_num)

# Print the binary representation
print(f"The binary representation of {decimal_num} is {binary_num}")