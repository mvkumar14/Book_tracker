import sqlite3

conn = sqlite3.connect("test0.db")
print("opened database successfully")
cursor = conn.cursor()

#The following was an experiment to determine if I could minimize the table creation process
# def create_table(name,*columns):
#     with conn:
#         cursor = conn.cursor()
#         #create a table
#         cursor.execute(("CREATE TABLE " + name + "(" + ("?,"*len(columns))[:-1] + ")"),columns)
#
# # with conn:
# #     cursor.execute("CREATE TABLE test ()")
#
# # def print_table(name):
#
#
#
# columns = ["long text","medium text","short text"]
# create_table("goals", "long text","medium text","short text")
# print("operation done")

# "(" + ("?,"*len(columns))[:-1] + ")"

cursor.execute("""CREATE TABLE books (title text, """)