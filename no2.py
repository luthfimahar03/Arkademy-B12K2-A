
import re

username = input("Masukan Username anda: ")
if re.match("^[a-z]{5,9}$", username):
    print ("Sesuai")
else:
    print ("Tidak Sesuai")
    
password = input("Masukan Passwordnya: ")
if re.match("^(?=(?:.*[a-zA-Z]))(?=.*[$=!]{1})(?=.*[A-Z]{1})(?=.*[0-9]{1})(?=.*[$=!])[a-zA-Z0-9$=!]{8,}$", password):
    print ("Sesuai")
else:
    print ("Tidak Sesuai")