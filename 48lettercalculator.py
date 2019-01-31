sentence = "thingy pingy"
count = {}
check = "t"
for x in sentence:
 if not x in count.keys():
  count[x] = 1
 else:
  count[x] = count[x]+1
print(count[check])