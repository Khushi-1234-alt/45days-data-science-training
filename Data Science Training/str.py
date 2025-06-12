# string is immutable i.e. cannot change 
# denoted by -' ', "same as single quote use for single line strings ", """ multi line code """ 


# print(name)
# print(type(name))

# Accessing methods of string 

# print (name.upper())    # str in upper case
# print (name.lower())    # str in lower case 
# print (content.title())    # str first letter capital of every word 
# print (content.capitalize())    # str first letter capital 
# #print (name.casefold())    # str in lower case 
# print (name.strip())   # remove white space 
# print (name.lstrip())  # remove white space from left
# print (name.rstrip())  # remove white space from right 
# print (name.replace("pvt","ltd"))  # replace the words by new words 
# print (name.split(" "))      # break str where space is present and remove that particular character 
# print (name.partition("a"))  # break into min. 3 different string 
# print (name.startswith("u"))  # return t/f if it start with given character 
# print (name.endswith("g"))    # return t/f if it ends with given character 
# print (name.isalpha())        # return t/f if only he string is an alphabetic string, False otherwise.
# print (name.isalnum())        # Return True if the string is an alpha-numeric string, False otherwise.

# ascii, utf-8

# name = """upflairspvt2632"""
# content = """ my name is khushi....."""
# print(name.encode())
# print(name.encode("utf-8"))
# print(name.encode("ascii"))
# print(name.removeprefix("upf"))
# print(name.removesuffix("2632"))
# print(name.zfill(20))    # add zeroes upto the given condition 
# print(name.center(30,"*"))
# print(name.ljust(30,"*"))
# print(name.rjust(30,"*"))

# indexing or slicing 
# indexing - accessing single character from the string 
# slicing - accessing multiple character from the string 

#INDEXING 
# name = """upflairspvt"""
# print(name[0])    #positive indexing
# print(name[-2])   #negative indexing

#SLICING [start:end:step/skip(optional)]
# name = "upflairspvt"
# print(name[0:8])
# print(name[-9:-1])
# print(name[-9:0])
# print(name[-9:])
# print(name[:-10])
# print(name[-3:])

#formatted string  // f- string 
age = 10
# text = "my age is "+ age 
text = f"my age is {age}" #format of f string 
print (text)

text = "my name is 'Khushi'"
print (text)
text = "my name is \"Khushi\""  # to make same quote throughout the string 
print(text)