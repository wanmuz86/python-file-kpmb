## CREATE YOUR OWN CAESAR CIPHER ENCRYPTOR

# What is the result of c , (+,-,*,/,%,//) 
a = 10
b = 3
# Modulo is the remainder of a division operation (baki)
c = a % b
print(c)

#introduce ASCII table to the students..
#To get an ASCII code of a character... we will use function ord
# What will be shown on the code below?
print(ord('A'))   # 65

#In python you can use the function chr() to transform an ascii code to a character
#What will be shown in the code below?
print(chr(65)) 

#You will now create a function, that will take two parameters
# The function is called shiftChar
# The first parameter is a letter (letter)
# second is the key (how many you want to shift)
# What the function will do is, it will shift the letter given on parameter A depending on the key
# for example shiftChar("A",3) will give you "D"

# def __________ (____,____):

# return ______

# def shiftChar(letter, shift):
# 	return chr(ord(letter) + shift)

# print(shiftChar("A",3))

#Now change the character with Z, what is the result that you should have? (C)
# WHat is the result that you using the current code? (])
# and why? - Because it does not reverse back to A, it continue shows the symbol

# Find the condition when you should reverse back to A (65)
# ord(letter) + shift > 90

#Modify your code, so that it will reverse back to A, based on the condition specify (conditional, repetition) - if else


def shiftChar(letter, shift):
	if ord(letter) + shift <= 90:
		return chr(ord(letter) + shift)
	else:
		return chr(((ord(letter) + shift) % 90)+64)

print(shiftChar("C",3))

# What will happen when condition in (4a) is not filled?
# Remember for ASCII 91 , you want it to be 65
# Which mathematical operation that you can use?

# Now you are going to create a function translateCaesar that will encrypt a sentence given using Caesar Chipher 
# It will take take  first parameter sentence, and the second parameter shift
# You will do a repetion based on the sentence given to call the function shiftChar create previously
# Try with "I AM HAPPY TODAY!" and shift at 5
# Try on paper first, then compare with the result

# def translateCaesar(sentence,shift):
# 	answer = ""
# 	for i in range(0, len(sentence)):
# 		answer += shiftChar(sentence[i],shift)
# 	return answer

# print(translateCaesar("I AM HAPPY TODAY!", 5))

#What is the problem between the code and answer that you write on paper?
# I have % in between my words and the ! is transformed into &

#Fix the code by providing the correct condition for the shiftChar

def translateCaesar(sentence,shift):
	answer = ""
	for i in range(0, len(sentence)):
		if ord(sentence[i]) > 64 and ord(sentence[i]) < 91:
			answer += shiftChar(sentence[i],shift)
		else:
			answer += sentence[i]
	return answer

print(translateCaesar("I AM HAPPY TODAY!", 5))

# Additional exercise: Create another to decrypt the encrypted message to the original message


