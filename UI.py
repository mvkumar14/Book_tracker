import PySimpleGUI as sg
import book_class as bk
import pickle as pk

#This shouldn't really change ever, not sure if scoping is currently correctly done
source = "G:\Data\Programs\Book_tracker\storage.txt"

#this is the sample book that I'm going to use to test all my data:
HP = bk.Book("Harry Potter","JK Rowling",453,'library',weeks=1)
current_books = {HP.title:HP}


#definition of pickle functions
def save_data():
    storage = open(source,"wb")
    test_book = bk.Book("Harry Potter","JK Rowling",123,"personal")
    books = {test_book.title:test_book}
    data = pk.dump(books,storage)
    storage.close()

def load_data(*args): # this is expandable with multiple args accepted I have to work out how to store multiple types of objects in the same file. Perhaps a nested dictionary.
    storage = open(source,"rb")
    global current_books
    current_books = pk.load(storage)
    storage.close()


main_layout = [[sg.Button("Add a Book")],
               [sg.Button("View Books")],
               [sg.Exit()]]
main_window = sg.Window('Main Window',main_layout)

# I personally like the layout better when I can change all the windows in one area of my code
# this is why I have organized the layout/ window generation as a function.
def add_book_win():
    add_book_layout = [[sg.Text("Add a Book")],
                       [sg.Text("Title",size=[5,1]),sg.InputText()],
                       [sg.Text("Author",size=[5,1]),sg.InputText()],
                       [sg.Text("Pages",size=[5,1]),sg.InputText()],
                       [sg.Text("Type",size=[5,1]),sg.Radio('Library',"GROUP1",default=True,key="Library"),sg.Radio('Personal',"GROUP1",key="Personal")],
                       [sg.Text("Month",size=[5,1]),sg.InputText(size= [20,1]),sg.Text("Day",size=[5,1]),sg.InputText(size= [20,1]),sg.Text("Year",size=[5,1]),sg.InputText(size= [20,1])],
                       [sg.CButton("Submit"),sg.CButton("Cancel")]]

    return sg.Window("Add a Book",add_book_layout)

def view_book_win():
    #the listbox should list the books, and when one is selected the details should be arranged on the right side of the window

    place_txt = "<-- Select a book from the list"
    col = [[sg.Text(place_txt,key="_PLACE_",size=[10,5])],
           [sg.Button("Edit Details"),sg.Button("Renew")]]


    view_book_layout = [[sg.Listbox(current_books.keys(),size=(20,10),enable_events=True,key='_LIST_'),sg.Column(col)],
                        [sg.Button("Send")],[sg.Exit()]]

    return sg.Window("View Books",view_book_layout)

def edit_book_win():
    return add_book_win()



#The following functions open the windows. this is to make the main loop more readable.

def open_add_book_win():
    # add_book_isactive = True
    main_window.Hide()
    # You have to create the layout and window at this point for the
    # windows to be created properly.
    add_book_window = add_book_win()
    while True:
        ev2, val2 = add_book_window.Read()
        if ev2 is None or ev2 == "Exit":
            add_book_window.Close()
            # add_book_isactive = False
            main_window.UnHide()
            break
        elif ev2 == "Submit"and "" not in val2.values():
            print("This should only print when there are values submitted")
            if val2["Library"]:
                btype = "library"
            else:
                btype = "personal"
            test_book = bk.Book(val2[0],None,val2[1],btype,val2[2],val2[3],val2[4])
            print("This is after object"+test_book.title)
            test_book.print()

def open_view_book_win():
    # view_books_isactive = True
    main_window.Hide()
    view_books_window = view_book_win()
    while True:
        ev2, val2 = view_books_window.Read()
        current_list_book = None
        #The "Send" code was a test to see if I could output data based on current window state
        # if ev2 == "Send":
        #     print("This is a test")
        if ev2 == '_LIST_':
            # print(type(val2),val2)
            view_books_window.element("_PLACE_").Update(val2['_LIST_'])
            current_list_book = val2['_LIST_']
            view_books_window.refresh()
        elif ev2 == "Renew":
            pass
        elif ev2 == "Edit Details":
            open_edit_book_win(view_books_window,current_list_book)
        elif ev2 is None or ev2 == "Exit":
            view_books_window.Close()
            # view_books_isactive = False
            main_window.UnHide()
            break
# hide window is a window object that .hide will be called upon
# book is a string which will serve as the key for current_books to lookup
def open_edit_book_win(hide_window,book):
    hide_window.Hide()
    edit_book_window = edit_book_win()
    while True:
        ev2, val2, = edit_book_window.Read()
        if ev2 is None or ev2 == "Exit":
            edit_book_window.Close()
            # add_book_isactive = False
            hide_window.UnHide()
            break
        if ev2 is "Submit":
            # # update(title=val2[0],
            #        pages=val2[1],
            #        month=val2[2],
            #        day=val2[3],
            #        year=val2[4])
            edit_book_window.Close()
            # add_book_isactive = False
            hide_window.UnHide()

""" HERE IS THE START OF THE MAIN CODE. IT REFERENCES THE ABOVE FUNCTIONS"""
# not sure if I need these? < - they may be useful for tracking what is open and what isn't
add_book_isactive = False
view_books_isactive = False
while True:
    event,values = main_window.Read()
    if event is None or event == "Exit":
        break
    elif event == 'Add a Book':
        open_add_book_win()
    elif event == "View Books":
        open_view_book_win()





#The values match the order in which they were entered:

# 0 = title

# 1 = # of pages

# 2 = Due Date Month

# 3 = Due date Day

# 4 = Due date Year



