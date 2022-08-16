
from datetime import datetime
from random import randint
from prettytable import *
import mysql.connector
from time import sleep
# import requests
import json



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pyconnect"
)


mycursor = mydb.cursor()
# greatings
def greet():
    Time = datetime.now().hour
    if Time > 0 and Time < 12:
        print("Good morning")
    elif Time > 12 and Time < 16:
        print("Good afternoon")
    elif Time > 16 and Time < 19:
        print("Good afternoon")
    elif Time > 19 and Time < 24:
        print("Good evening")

def end():
    print("Visit again, Have a nice day")
    exit()

def db():
    d = datetime.now().strftime("%d - %m - %y")
    t = datetime.now().strftime("%H : %M : %S")
    cur.execute("insert into details values (null, '{}', {}, {}, '{}', '{}', '{}','{}')".format(cust_name, cust_age, username, purchased_products[0],
    cust_address, d, t))
    con.commit()
    end()

    purchased_products = []
    def cart():
        receipt = PrettyTable([" ", "Details"])
        receipt.add_row(["Name", cust_name])
        receipt.add_row(["Age", cust_age])
        receipt.add_row(["Contact number", username])
        receipt.add_row(["Products", purchased_products[0]])
        receipt.add_row(["Shipping address", cust_address])
        print(receipt)
        choice = input("Confirmation to place the order (y/n) : ")
    if choice == 'y' or choice == 'Y':
        print("Payment method will be 'Cash On Delivery'")
        print("Online payment method is not available at this moment ....SORRY for the inconvenience")
        print("Thank you {cust_name}, Your order will reach you within 2-3days")
        db()

def create():
     mycursor.execute("CREATE TABLE dogs (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), state VARCHAR(255),used VARCHAR(255))")
def profile():
    print(f"Name : {cust_name}")
    print(f"Age : {cust_age}")
    print(f"Contact number : {username}")
    print(f"Address : {cust_address}")
    menu()

def admin():
    ad_details = ["pythoncoder", "pycharm"]
    print("=================")
    print("Welcome to ADMIN PAGE")
    print("=================")
    while True:
            ad_username = input("Enter Admin's username : ")
            ad_password = input("Enter Admin's password : ")
            if ad_username != ad_details[0]:
                print("You have entered the wrong username")
                print("Please type the correct one")
                continue
            elif ad_password != ad_details[1]:
                print("You have entered the wrong password")
                print("Please type the correct one")
                continue
            else:
                print("Verified successfully")
                break
    choice = input("Do you want to see the customer detail records (y/n) : ")
    if choice == 'y' or choice == 'Y':
        cur.execute("select count(*) from details")
        total = cur.fetchall()
        if total[0][0] == 0:
            print("No records found")
        else:
            print("\t\t CUSTOMERS DETAILS")
            cur.execute("select * from details")
            a = cur.fetchall()
            for i in a:
                print(i)
    else:
        print("Thank you")
        menu()


def display():
    mycursor.execute("SELECT * FROM dogs")

    myresult = mycursor.fetchall()

    for x in myresult:
      print(x)
def insert():
    a=input("enter dog name:")
    b=input("enter dog state")
    c=input("enter uses")

    sql = "INSERT INTO dogs (name, state,used) VALUES (%s, %s,%s)"
    val = [
      (a, b,c),
    ]

    mycursor.executemany(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "was inserted.")
def menu():
    print("Available options :")
    print("1. create")
    print("2. display")
    print("3. insert")
    print("4. exit")
    choice = int(input("Enter your choice (Type number) : "))
    if choice not in [1, 2, 3, 4]:
        print("Please select the correct option")
        menu()
    elif choice == 1:
        create()
    elif choice == 2:
        display()
    elif choice == 3:
        insert()
    else:
       end()

greet()

menu()