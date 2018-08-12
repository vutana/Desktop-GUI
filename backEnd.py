# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 13:22:21 2018

@author: vutan
"""

import sqlite3

def connect():
    conn=sqlite3.connect("books.db") #Connect to database
    cur=conn.cursor()                #Define the cursor object & execute SQL statement
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()                    #Create the table if table does not exist
    conn.close()    

def insert(title,author,year,isbn):   #Function that inserts data into database
    conn=sqlite3.connect("books.db")  #Connect to Database
    cur=conn.cursor()                 
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title,author,year,isbn))  #Insert tuple
    conn.commit()
    conn.close()

def view():                           #Fetch all the rows of table
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book") #Grab selection and insert in listbox
    rows=cur.fetchall()               #return a tuple
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn)) #return a tuple
    rows=cur.fetchall() #Select from database where title is equal to something=? or author is = to something and so on...
    conn.close()
    return rows
    
def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,)) #Delete from book where id is = to something
    conn.commit()
    conn.close()
    
def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()           #Update book where values or equal to something where id is also equal to something else
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()
    
    
connect()






