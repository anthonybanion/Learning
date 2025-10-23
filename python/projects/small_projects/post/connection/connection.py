#Brief: Connection to the database
#Date: 05/11/2024
#Version: 1.0

import sqlite3

def openConnection():
    conexion=sqlite3.connect('post/post.db')
    return conexion