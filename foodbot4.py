import sqlite3

conn = sqlite3.connect("foodbot.db")
cur = conn.cursor()

user_id = """CREATE TABLE IF NOT EXISTS user_id(
        NUM INTEGER PRIMARY KEY,
        NAME TEXT,
        ORDER_LIST TEXT,
        TOTAL_AMOUNT INTEGER
    )"""

food_info = """CREATE TABLE IF NOT EXISTS info_food(
          FOOD_ITEMS TEXT PRIMARY KEY,
          FOOD_PRICE INTEGER
    )"""


def my_table(conn, info):
    cur = conn.cursor()
    cur.execute(info)

def table_value(info):
    try:
        cur.execute("INSERT INTO user_id(NUM,NAME) VALUES(?, ?)", info)
    except:
        print("Number Already Exists")


def table_value2(f_info):
    try:
        cur.execute("INSERT INTO info_food(FOOD_ITEMS,FOOD_PRICE) VALUES(?, ?)", f_info)
    except:
        print("Item Already Exists")

def print_menu():
    cur.execute("SELECT * FROM info_food")
    print(cur.fetchall())




if __name__ == "__main__":
    my_table(conn, user_id)
    my_table(conn, food_info)
    msg = input("ENTER HERE COMMAND")
    if msg == "/help":
        print("HELLO !!\n WHAT HELP U WANT FROM BELOW OPTIONS? \n 1. WANT TO REGISTER ---> (write)/register/ COMMAND \n 2.WANT INFO ABOUT MENU--->(write)/menu/ COMMAND. \n 3. ADD ITEM TO ORDER--->(write)/+item/ 4.CANCEL OF ORDER--->(write)/cancel/ COMMAND \n 5.PAYMENT ISSUES---> (write)/payement/ COMMAND .\n")

    elif msg == "/register/":
        u_info = input(print("Input number and name")).split(',')
        print(u_info)

    elif msg == "/menu/":
        print("FOOD ITEM ---> FOOD PRICE \n DABELI ---> 10 \n WADAPAV ---> 10 \n PATTIS ---> 15 \n PIZZA ---> 60")

    elif msg=="/+item/":
        f_info = input(print("Input Food Item and Price")).split(',')
        print(f_info)

    numb = input("enter number")
    print(numb)

    m = input("enter order and quantity")
    n = m.split(',')
    print(n)

    price = cur.execute("SELECT FOOD_PRICE FROM info_food WHERE FOOD_ITEMS = ?", (n[0],)).fetchone()
    print(price)

    t_price = int(n[1]) * int(price[0])
    print(t_price)

    lis = [n[0], t_price, numb]
    print(lis)

    cur.execute("UPDATE user_id SET ORDER_LIST=?,TOTAL_AMOUNT=? WHERE NUM=?", lis)

    #table_value2(f_info)
    #table_value(u_info)

    #u_info = input(print("Input number and name")).split(',')
    #table_value(u_info)
    #f_info = input(print("Input Food Item and Price")).split(',')
    #table_value2(f_info)



conn.commit()

conn.close()