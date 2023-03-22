height = int(input())

print(r"\./")
# the r means raw string: \ should be treated literally and not as an escape character 
# it would work in this case without the r however
# more generally e.g. "\n\n" would mean two new lines but r"\n\n" would mean the literal characters \n\n

for stem in range(height):
  print(".|.")
