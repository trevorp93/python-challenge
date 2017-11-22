import os

regularAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']


data = os.path.join("raw_data", "paragraph_2.txt")

textfile = open(data,"r")
text = textfile.read()
letters = 0
words = 1
sentences = 0
average1 = 0.00
average2 = 0.00

for x in text:
	if (x in regularAlphabet):
		letters = letters + 1
	elif x == " ":
		words = words + 1
	elif x ==("." or "!" or "?"):
		sentences = sentences + 1
average1 = letters/words
average2 = words/sentences

print(" ")
print("Paragraph Analysis")
print("-----------------")
print('Approximate Word Count:',words)
print("Approximate Sentence Count",sentences)
print('Average Letter Count:',average1)
print("Average Sentence Length:",average2)
print(" ")


