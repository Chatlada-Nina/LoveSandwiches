import gspread
from google.oauth2.service_account import Credentials


""" 
The SCOPE lists the APIs that the program should access in order to run
SCOPE is a constant variable because in Python, we write it in capitals
"""
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwiches")

#Use worksheet method to call the "sales" value that corresponds to the name of the worksheet we have
sales = SHEET.worksheet("sales")

#Use gspread method get_all_values() to pull all the values from our sales worksheet
data = sales.get_all_values()

print(data)

