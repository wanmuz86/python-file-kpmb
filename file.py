#myfile = open("goodbye-world.txt","r")

#Part 1 - read all items in the file
# str = myfile.read()
# #read all
# print(str)

#Part 2 - read all the items line by line
# line1= myfile.readline()
# line2= myfile.readline()
# line3= myfile.readline()
# #read by line
# print(line1)
# print(line2)
# print(line3)

# Part 3 - read all the items line by line but using for loop
#for str in myfile:
#	print(str, end="") 

#myfile.close()

# Part 4 - write an item in the file, mode w+ (overwrite), bandingkan dengan a+

# myfile = open("hello-world.txt","a+")
# name = input("What is your name?")
# myfile.write(name)
# myfile.write("\n")
# myfile.close()
# print("Data succesfully saved")

# Part 5 - Write an item in a file, comma separate it, (CSV)
# myfile = open("books.txt","a+")
# ans = "y"
# while ans == "y":
# 	isbn = input("Enter ISBN number")
# 	name = input("Enter book name")
# 	author = input("Enter author name")
# 	price = input("Enter book price")
# 	rec = isbn+","+name+","+author+","+price
# 	myfile.write(rec)
# 	myfile.write("\n")
# 	ans = input("Do you want to add? (y/n)")
# myfile.close()

# Part 6 - Read from a file, use loop to go through each line split the comma and write a sentence from it
# myfile = open("books.txt","r")
# for str in myfile:
# 	currentline = str.split(",")
# 	message = "ISBN is: "+currentline[0]+" , book name is : "+currentline[1]+" , author name is: "+currentline[2]+", book price is"+currentline[3]
# 	print(message, end="") 
# myfile.close()



