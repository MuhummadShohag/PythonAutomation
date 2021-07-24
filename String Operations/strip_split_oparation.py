a="Python"
print(a)

# strip oparation working when if there has string toward left or right space which is removed space
a="   Python  "
print(a.strip())

# if you want to any letter or anything
print(a.strip("P"))

b="Python is easy"
print(b.strip("easy"))

# it is removing only right side
print(b.rstrip())

# it is removing inly left side
print(b.lstrip())

# you can apply multiple time like lstrip,rstrip
print(a.strip("P").strip("y"))


# it is split with space by default, it showed list way
b="Python is easy"
print(b.split())
print(b.split("is"))

