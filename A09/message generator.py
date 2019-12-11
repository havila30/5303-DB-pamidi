import markovify

with open("beowulf.txt", errors ="ignore") as f:
    sample_1 = f.read()

with open("grimms_fairy_tales.txt", errors="ignore") as g:
    sample_2 = g.read()

model_a = markovify.Text(sample_1)
model_b = markovify.Text(sample_2)


model_combo = markovify.combine([ model_a, model_b ], [ .5, .5 ])


for i in range(10000):
    print(model_combo.make_sentence())

print ("\n")



