# OTP - One Time Password generator
import random

numbers = "0123456789"

def OTP_generator():
    print("Generated OTP: ",end ="")
    for x in range(0,4): #(0,4) => length of OTP
        otp = random.choice(numbers)
        print(otp, end = " ")

request = input("\nHit (G) to generate: ").lower()

while request == "g":
    OTP_generator()
    re_request = input("\n\nRegenerate OTP? \n\n (yes/no): ").lower()
    if re_request == "yes":
        pass
    elif re_request == "no":
        print("Never share your OTP 😂🤣😂")
        break
    else:
        print("Wrong Input,rerun the program")
        break



