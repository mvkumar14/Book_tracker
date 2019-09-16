import datetime

a = datetime.date(2019,10,9)
b = datetime.date.today()
print("datetime data:")
print(b)
c = a-b
print(c)
print(type(a),type(b),type(c),"\n")
# this is how to convert a "timedelta" datatype to an int datatype
c = (a-b).days
print("here it is converted to int data:")
print(c)
print(type(c))