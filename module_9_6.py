import itertools
def all_variants1(text):
  length = len(text)
  for x in range(length):
    for y in range(x,length):
      yield text[x:y + 1]
def all_variants2(text):
    for i in range(len(text)):
      combinations = []
      combinations = itertools.combinations(text, i + 1)
      subsequences = [''.join(c) for c in combinations]
      declimer = f'\n'
      res = declimer.join(subsequences)
      yield res
a = all_variants1('abc')
print(a)
for i in a:
    print(i)

a = all_variants1("abcd")
print(a)
for i in a:
  print(i)

b = all_variants2(text = 'abcd')
print(b)
for i in b:
    print(i)

b2 = all_variants2(text = 'abc') #
print(b2)
for i in b2:
    print(i)