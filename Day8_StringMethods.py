#Today - task 

#count()
#endswith() 
#startswith()
#encode()
#isalnum() = abc123
#isalpha() = abc
#isdigit() = 123
#join()
#lstrip()
#zfill()
#swapcase()

# #isalfa - alfa
# txt = "roht"
# print(txt.isalpha())


#isalnum - alfa or number  ex- abc123, 123abc, abc, 123
# txt = ""   
# new = txt.isalnum()
# print(new)


# "Hello123".isalnum()  # Returns True
# "123".isalnum()  # Returns True
# "@#$%".isalnum()  # Returns False
# print("Hello World".isalnum())  # Returns False (space is not alphanumeric)
# "".isalnum()  # Returns False (empty string)







txt = "Hii, Good After Noon Students Noon"

newTxt = txt.count("Noon")
print(newTxt)

#  = "Hii, Good After Noon Students Noon"

# print(.startswith("After"))

#  = "Hii, Good After Noon Students Noon"

# print(.encode())

#  = "rohit"
# print(txt.isalnum())

# txt = "rohit"
# print(txt.isalpha())

# txt = "123"

# print(txt.isdigit())

# txt = "HII, GOOD AFTER NOON!"
# print(txt)

# newTxt = txt.split()
# print(txt.split())

# newTxt2 = " ".join(newTxt)
# print(newTxt2)

# txt = "       Mohit lilhare       "
# print(f"my name is {txt}, im form balaghat.")
# print(f"my name is {txt.lstrip().rstrip()}, im form balaghat.")

# txt = "123"
# print(txt.zfill(5))   00123

txt = "Hi, GooD AFTER Noon!"
print(txt)
print(txt.swapcase())





