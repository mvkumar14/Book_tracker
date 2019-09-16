#This is a way that you can loop through the variables in a function definition to then go
#modify the object's values. This was for the book class

def update(self, title=None, author=None, pages=None, month=None, day=None, year=None):
    inputs = {'title': title, 'author': author, 'pages': pages, 'month': month, 'day': day, 'year': year}
    for key, value in inputs.items():
        if value:
            self.key = value
            print(key + "was changed to " + value)