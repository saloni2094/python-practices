###Numeric
#1. int
#int x
x = 10
print(type(x))

#2. float
x = 3.14
print(type(x))

#3. complex
x = 10 + 5j #real, imaginary
print(type(x))

### Text
#1. str
x = 'first"bit" solution'
x = "firstbit's solution"
x = '''this is first line
     this is second line'''
x = """This is first line
     this is second line"""
print(type(x))

### sequential
#1.list
x =[10,20,30,40]
#2.tuple
x = (10,20,30,40)
#3. range
x = range(50,90)

###set type
#1. set
x = {10,20,30,40}
#2.frozenset
x = frozenset({20,60,80})

###maping
#1.dict
x = {'id':101}

###other
#1.Boolean
x = True
#2.Nonetype
x = None
print(type(x))
