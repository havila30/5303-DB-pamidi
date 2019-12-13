import markovify
import pymongo

with open("grimms_fairy_tales.txt", errors ="ignore") as f:
text = f.read()

text_model=markovify.Text(text)


print ("\n")

for i in range(1000000):
print(make_short_sentence(250))


