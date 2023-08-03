#This files aim is to find out personal info about you and add it to a file

import random
from read_file import Dating
class User:

    def __init__(self, name='', age='', gender='', gender_interest='', job_title='', height=''):
        self.name = name
        self.age = age
        self.gender = gender
        self.gender_interest = gender_interest
        self.job_title = job_title
        self.height = height
    
    @property
    def props(self):
        if  int(self.age) >= 18:
            f = open('/Users/ruthamey/Documents/Basic_projects/user_info.txt', 'a')
            id = str(random.randint(10000000, 99999999))
            f.write(f'\n{id}  {self.name :<20}  {self.age :<20}  {self.gender :<20}  {self.gender_interest :<20}  {self.height :<20}  {self.job_title :<20}')
            f.close()
            print(f'Your user id is {id}')
        else:
            print('I\'m sorry i don\'t think this is the app for you')
        

    @staticmethod   
    def user_input():
        return User(input('Lets start with your name: '), 
        int(input('What\'s your age: ')),    
        input('What\'s your gender: '),    
        input('Looking for: (male /female /everyone) '),
        input('What do you do for work: '),
        input('How tall are you: (in cm) '),
    


idu = User.user_input()
print(idu.props)
