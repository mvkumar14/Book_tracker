#this is the part of the code that calculates how many pages a day of a book you need to read

#inputs are:
#reading frequency (ex: I will read this book every other day vs every day)
#due date ( library or personal goal)
#number of pages

import random

def rate_calc(pages,frequency,due):
    pgpday = pages/due
    pg_p_session = pgpday*frequency
    return round(pg_p_session)

for _ in range(100):
    print(rate_calc(random.randint(50,350),random.randint(1,3),random.randint(1,14)))

# I need to call the rate_calc on all the "currently reading" books whenever the program is launched