
import random
import string
size = int (input("Enter the size of password: "))
allchar =  string.ascii_letter+string.digits+string.punctuation
password = ''.join(rancom.choice(allchar) for i in range(size))
print (password)
