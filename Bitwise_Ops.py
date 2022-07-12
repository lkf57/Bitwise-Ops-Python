# Lauren Farr

# a program that prompts the user for 2 unisigned decimal ints,
# preforms several bitwise operations on them,
# and returns the results in decimal, binary, and hex.

def main():

    # display the instructions
    print("Enter two positive integers, each less than 256.")
    print()

    # prompt for the integers
    integer_a = int(input("Enter integer a: "))
    integer_b = int(input("Enter integer b: "))
    print()

    # checks if the integers are both less than 256
    if (integer_a < 256 and integer_b < 256):

        # calculate and display the bitwise AND of the two integers
        AND = integer_a & integer_b
        print("a & b  =    " + decimal_str(AND), end='')
        print("    " + hexadecimal_str(AND) + 'h', end='')
        print("    " + binary_str(AND) + 'b')

        # calculate and display the bitwise OR of the two integers
        OR = integer_a | integer_b
        print("a | b  =    " + decimal_str(OR), end='')
        print("    " + hexadecimal_str(OR) + 'h', end='')
        print("    " + binary_str(OR) + 'b')
        
        # calculate and display the bitwise XOR of the two integers
        XOR = integer_a ^ integer_b
        print("a ^ b  =    " + decimal_str(XOR), end='')
        print("    " + hexadecimal_str(XOR) + 'h', end='')
        print("    " + binary_str(XOR) + 'b')

        # calculate and display the bitwise compliment of the first integer
        COMP_binary_str = bitwise_comp(binary_str(integer_a))
        
        COMP_decimal = int(COMP_binary_str, 2)
        COMP_decimal_str = decimal_str(COMP_decimal)
        COMP_hex_str = hexadecimal_str(COMP_decimal)
        
        print("  ~ a  =    " + COMP_decimal_str, end='')
        print("    " + COMP_hex_str + 'h', end='')
        print("    " + COMP_binary_str + 'b')

        # calculate and display the bitwise right shift of the two integers
        RIGHT = integer_a >> integer_b
        print("a >> b =    " + decimal_str(RIGHT), end='')
        print("    " + hexadecimal_str(RIGHT) + 'h', end='')
        print("    " + binary_str(RIGHT) + 'b')

        # calculate and display the bitwise left shift of the two integers
        LEFT = integer_a << integer_b
        LEFT_binary_str = binary_str(LEFT)
        
        if len(LEFT_binary_str) > 8:
            LEFT_binary_str = LEFT_binary_str[-8:]
            
        LEFT_decimal = int(LEFT_binary_str, 2)
        LEFT_decimal_str = decimal_str(LEFT_decimal)
        LEFT_hex_str = hexadecimal_str(LEFT_decimal)
        
        print("a << b =    " + LEFT_decimal_str, end='')
        print("    " + LEFT_hex_str + 'h', end='')
        print("    " + LEFT_binary_str + 'b')

    # if the integers are not valid, the program is aborted
    else:

        print("One or both of your numbers is not valid!")
        print("Program aborted.")

# converts an integer into a binary string with padded zeros
def binary_str(integer):
    binary = bin(integer)
    binary_string = str(binary)[2:]
    leading_zeros = 8 - len(binary_string)

    result = ('0' * leading_zeros) + binary_string

    return result

# converts an integer into a hexadecimal string with padded zeros
def hexadecimal_str(integer):
    hexadecimal = hex(integer)
    hex_string = str(hexadecimal)[2:]
    leading_zeros = 2 - len(hex_string)

    result = ('0' * leading_zeros) + hex_string

    return result

# converts an integer into a decimal string with padded zeros
def decimal_str(integer):
    decimal_str = str(integer)
    leading_zeros = 3 - len(decimal_str)

    result = ('0' * leading_zeros) + decimal_str

    return result

# preforms the bitwise compliment operation on a binary string
def bitwise_comp(bin_num):

    result = ""

    for bit in range(0,8):
        value = bin_num[bit]

        if value == '1':
            result = result + '0'

        else: result = result + '1'

    return result
  
main()
