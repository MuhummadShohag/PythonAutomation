a="python script"
print(a,type(a))
print(a.lower())
print(a.upper())

# it is not modify orginal string that is why string is immutuble
print(a.title())# each every letter string with capital

# dir ,it is showed has available gievn string operation
print(dir(a)) 

# But remember when use this oparation, it is not modify string , but if you want you store this result with variable
my_string_lower=a.lower()
print(my_string_lower)

print(a.capitalize())
print(a.casefold())
print(a.translate())

