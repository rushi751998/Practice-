# Keyword argument is not passed

number1 = dict([('x',5),('y',-5)])
print ('Numbers ',number1)

# Keyword agrgument is also passed
number2 = dict([('x',5),('y',-5)],z =8)
print ('Numbers ',number2)


# zip() creates an iterable in python 3

number3 = dict(dict(zip(['X','Y','z'],[5,-5,8])))
print ('Numbers ',number3)