#This files aim is to find out personal info about you and add it to a file

import random
from read_file import Dating
class User:

    def __init__(self, name='', age='', gender='', gender_interest='', job_title='', height='', drugs='', drug_intake='', fav_drug=''):
        self.name = name
        self.age = age
        self.gender = gender
        self.gender_interest = gender_interest
        self.job_title = job_title
        self.height = height
        self.drugs = drugs
        self.drug_intake = drug_intake
        self.fav_drug = fav_drug

    @property
    def props(self):
        if self.drugs == 'yes' and int(self.age) >= 18:
            f = open('/Users/ruthamey/Documents/Basic_projects/user_info.txt', 'a')
            id = str(random.randint(10000000, 99999999))
            f.write(f'\n{id}  {self.name :<20}  {self.age :<20}  {self.gender :<20}  {self.gender_interest :<20}  {self.height :<20}  {self.job_title :<20}  {self.drugs :<20}  {self.drug_intake :<20}  {self.fav_drug :<20}')
            f.close()
            print(f'cmonn your user id is {id}')
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
        input('Are you a fellow drug taker: '), 
        input('How often do you take drugs: (1 - occasionally, 2 - often, 3 - \'Cause I\'m a fuckin\' sasquatch\' we fucking eat this shit for our mornin\' breakfast) '), 
        input('What\'s your favourite drug: '))


idu = User.user_input()
print(idu.props)
