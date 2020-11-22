# OTP - One Time Password
import string
import random

numbers = string.digits # will return 0123456789

def OTP_generator():

    print("Generated OTP: " , end = "")
    for x in range(0,4): #(0,4) => 4 chars
        otp = ""
        otp_gen = random.choice(numbers) # makes random choices 
        otp = otp + otp_gen
        print(otp,end = " ")


OTP_generator()