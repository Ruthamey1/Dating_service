"""Moofs dating service
Bad trip
Using the questions provided we will find you matches where are between 2 years younger and 2 years older than you
if you are staright then men who are taller for females and vise versa
we provide a service for gay, lesbian, bisexual and straight people
Everyoene using the app is recommended to be a drug taker
and everyone is over 18


"""

class Dating:

    def __init__(self):
        pass
       

    def open_file(self):
        try:
            f = open('/Users/ruthamey/Documents/Basic_projects/user_info.txt')
            all_lines = f.readlines()
        except FileNotFoundError:
            print('File not found')
        return all_lines



    

