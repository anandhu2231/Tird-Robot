import mysql.connector
import sys
from PIL import Image
from mysql.connector import Error
import PIL.Image

def digital_to_binary(image_name):
        # Convert digital data to binary format
        with open(image_name, 'rb') as file:
            binaryData = file.read()
        return binaryData
    
name_input = input("Enter your name")
phone_input = input("Enter your phone")

#image = Image.open('images.jpg')
#blob_value = open('images.jpg', 'rb').read()
#image_input = blob_value

connection = mysql.connector.connect(host='192.168.1.8',
                                         database='user_info',
                                         user='raspberrypi.domain.name',
                                         password='',
                                        )
db = connection
   # if connection.is_connected():
    #    db_Info = connection.get_server_info()
    #    print("Connected to MySQL Server version ", db_Info)
    #    cursor = connection.cursor()
       # cursor.execute("select database();")
      #  record = cursor.fetchone()
       # print("You're connected to database: ", record)

#except Error as e:
  #  print("Error while connecting to MySQL", e)
#finally:
    #if connection.is_connected():
       # cursor.close()
        #connection.close()
        #print("MySQL connection is closed")
image = "images.jpg"

tmp = 1
pls = 2

Picture = digital_to_binary(image)
cur = db.cursor()
 
cur.execute("INSERT INTO info (name, phone, temp, pulse, photo) VALUES (%s, %s, %s, %s, %s)", (name_input, phone_input, tmp, pls, Picture))

db.commit()

# sql_insert_blob_query = """ INSERT INTO ab (image) VALUES (%s)""" 
    

#print(Picture)
#cursor = connection.cursor()
    
            # Convert data into tuple format
#insert_blob_tuple = (Picture)
#cursor.execute(sql_insert_blob_query, insert_blob_tuple)
#connection.commit()
