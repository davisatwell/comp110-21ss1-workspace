"""Revealing Binary Value of Decs"""

__name__ == '__main__'

# Function to convert decimal number
# to binary using recursion
def DecimalToBinary(num):
     
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')
 
# Driver Code
if __name__ == '__main__':
     
    # decimal value
    dec_val = (input("Enter Value: "))
    dec_val2 = int(dec_val)
     
    # Calling function
    DecimalToBinary(dec_val2)