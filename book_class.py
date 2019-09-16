import datetime
class Book:
    def __init__(self,title,author,pages,type,month=None,day=None,year=None,weeks=None):
        #input variable initialization
        self.title = title
        self.author = author
        self.pages = pages
        self.type = type # this is "library" or "personal"
        if month and day and year:
            self.due_date = datetime.date(year,month,day)
        elif weeks:
            self.due_date = datetime.date.today() + datetime.timedelta(days=round(weeks*7))
        elif day:
            self.due_date = datetime.date.today() + datetime.timedelta(days= day)
        else:
            self.due_date = datetime.date.today() + datetime.timedelta(days=21)

        #"synthetic" variable initialization
        self.current_pg_num = 0
        self.days_left = (self.due_date - datetime.date.today()).days

        # print(self.days_left)
    def update(self,title=None,author=None,pages=None,month=None,day=None,year=None):
        inputs = {'title':title,'author':author,'pages':pages,'month':month,'day':day,'year':year}
        for key,value in inputs.items():
            if value:
                self.key = value
                print(key + "was changed to "+ value)
    def renew(self): #this should make the due date 3 weeks from today.
        pass
    def rate_calc(self,frequency):
        pgpday = self.pages / self.days_left
        pg_p_session = pgpday * frequency
        return round(pg_p_session)
    def print(self):
        print(self.title,self.author)
    def set_due_date(self,month=None,day=None,year=None,renew = None):
        if renew:
            self.due_date += datetime.timedelta(days=21)
        print("date updated, new due date is:"+str(self.due_date))
    #With UI elements this shouldn't be a huge problem, but there should be an "edit
    #details page somewhere where I can modify this.
    def set_type(self,change):
        if change == self.type:
            print("The type is already "+change)
        elif change == "library":
            self.type = change
            print("Type changed, the book is now a " +self.type+ " book")
        elif change == "personal":
            self.type = change
            print("Type changed, the book is now a " + self.type + " book")
        else:
            print("No valid input was given type remains: "+ self.type)


# HP = Book("Harry Potter","JK Rowling",453,'library',weeks=1)
# HP.set_due_date(renew=True)
# HP.set_type("personal")
# HP.update(title = "Harry Potter and The Sorcerer's Stone")
