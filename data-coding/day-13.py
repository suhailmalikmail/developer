# strings are immutable
a = "!!! Suhail !!!!!!!! Suhail"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Suhail","john"))
print(a.split(" "))

bloghading = "introduction tO Js"
print(bloghading.capitalize())

str1 = "welcome to the console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Suhail"))

str1 = "welcom to the console!!!"
print(str1.endswith ("!!!"))

str1 = "welcome to the console!!!"
print(str1.endswith ("to", 4, 10))  

str1 = "He's name is junaid. He is an honest main."
print(str1.find("ishh"))
# print(str1.index("ishh"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())

str1 = "welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Marry Christmas\n"
print(str1.isprintable())

str1 = "     "
print(str1.isspace())
str2 = " "
print(str2.isspace())

str1 = "World Health Organization"
print(str1.istitle())

str2 = "To kill a Mocking bird "
print(str2.istitle())

str1 = "python is a Interpreted lanuage"
print(str1.startswith("python"))

str1 = "Python is a Interpreted Lanuage"
print(str1.swapcase())

str1 = "His name is Malik.Malik is an honest man"
print(str1.title())