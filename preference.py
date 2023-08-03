#This file works out the people in txt file who are of your prference and then one by one shows you them

from read_file import Dating
from your_info import User

#need to work out how to stop after talking to someone
#what happens next when you want to talk to them


class Preference(User):

    def __init__(self):
        super(Preference, self).__init__()
        

    def preference_straight_men(self):
        straight_men = []
        all_lines = Dating.open_file(self)
        for line in all_lines:
            if line[54:73].strip() == 'male' and line[76:93].strip() == 'female':
                straight_men.append(line[0:9].strip())
        return straight_men

    def preference_straight_female(self):
        straight_female = []
        all_lines = Dating.open_file(self)
        for line in all_lines:
            if line[54:73].strip() == 'female' and line[76:93].strip() == 'male':
                straight_female.append(line[0:9].strip())
        return straight_female

    def preference_gay(self):
        gay = []
        for line in Dating.open_file(self):
            if line[54:73].strip() == 'male' and line[76:93].strip() == 'male':
                gay.append(line[0:9].strip())
            elif line[54:73].strip() == 'male' and line[76:93].strip() == 'everyone':
                gay.append(line[0:9].strip())
        return gay

    def preference_lesbian(self):
        lesbian = []
        for line in Dating.open_file(self):
            if line[54:73].strip() == 'female' and line[76:93].strip() == 'female': 
                lesbian.append(line[0:9].strip())  
            elif line[54:73].strip() == 'female' and line[76:93].strip() == 'everyone':
                lesbian.append(line[0:9].strip())              
        return lesbian

    def preference_bisexual_male(self):
        bisexual_male = []
        for line in Dating.open_file(self):   
            if line[54:73].strip() == 'male' and line[76:93].strip() == 'everyone': 
                bisexual_male.append(line[0:9].strip())
            elif line[54:73].strip() == 'male' and line[76:93].strip() == 'male':
                bisexual_male.append(line[0:9].strip())              
        return bisexual_male

    def preference_bisexual_female(self):
        bisexual_female = []
        for line in Dating.open_file(self):   
            if line[54:73].strip() == 'female' and line[76:93].strip() == 'everyone': 
                bisexual_female.append(line[0:9].strip())  
            elif line[54:73].strip() == 'female' and line[76:93].strip() == 'female':
                bisexual_female.append(line[0:9].strip())
        return bisexual_female

p = Preference()



class Match():

    def __init__(self):
        pass

    def info(self):
        l1 = []
        for line in Dating.open_file(self):
            l1.append(line[0:8])
        return l1

    def pairing(self):
        for line in Dating.open_file(self):
            pass 
        if line[54:73].strip() == 'male' and line[76:93].strip() == 'female':
            while True:
                l2 = [] 
                for i in p.preference_straight_female():
                    l2.append(i)
                matches = [x for x in m.info() if x in l2]
                for line in Dating.open_file(self):     
                    for i in range(len(matches)):
                        if matches[i] == line[0:8]:
                            print(f'Okay so we have {line[9:28].strip()} they are {line[32:35].strip()} years old.')
                            print(f'They are {line[98:115].strip()}cm tall and there job is {line[120:135].strip()}')
                            next = input('Would you like to talk to this person or move on to the next? \n(yes/next) \n')
                            if next == 'yes':
                                print('omg yay!')
                                break
        elif line[54:73].strip() == 'female' and line[76:93].strip() == 'male':
            while True:
                l2 = [] 
                for i in p.preference_straight_men():
                    l2.append(i)
                matches = [x for x in m.info() if x in l2]
                for line in Dating.open_file(self):     
                    for i in range(len(matches)):
                        if matches[i] == line[0:8]:
                            print(f'Okay so we have {line[9:28].strip()} they are {line[32:35].strip()} years old.')
                            print(f'They are {line[98:115].strip()}cm tall and there job is {line[120:135].strip()}')
                            next = input('Would you like to talk to this person or move on to the next? \n(yes/next) \n')
                            if next == 'yes':
                                print('omg yay!')
                                break
        elif line[54:73].strip() == 'male' and line[76:93].strip() == 'male':
            while True:
                l2 = [] 
                for i in p.preference_gay():
                    l2.append(i)
                matches = [x for x in m.info() if x in l2]
                for line in Dating.open_file(self):     
                    for i in range(len(matches)):
                        if matches[i] == line[0:8]:
                            print(f'Okay so we have {line[9:28].strip()} they are {line[32:35].strip()} years old.')
                            print(f'They are {line[98:115].strip()}cm tall and there job is {line[120:135].strip()}')
                            next = input('Would you like to talk to this person or move on to the next? \n(yes/next) \n')
                            if next == 'yes':
                                print('omg yay!')
                                break
        elif line[54:73].strip() == 'female' and line[76:93].strip() == 'female':
            while True:
                l2 = [] 
                for i in p.preference_lesbian():
                    l2.append(i)
                matches = [x for x in m.info() if x in l2]
                for line in Dating.open_file(self):     
                    for i in range(len(matches)):
                        if matches[i] == line[0:8]:
                            print(f'Okay so we have {line[9:28].strip()} they are {line[32:35].strip()} years old.')
                            print(f'They are {line[98:115].strip()}cm tall and there job is {line[120:135].strip()}')
                            next = input('Would you like to talk to this person or move on to the next? \n(yes/next) \n')
                            if next == 'yes':
                                print('omg yay!')
                                break
        elif line[54:73].strip() == 'male' and line[76:93].strip() == 'everyone':
            while True:
                l2 = [] 
                for i in p.preference_bisexual_male():
                    l2.append(i)
                for i in p.preference_bisexual_female():
                    l2.append(i)
                matches = [x for x in m.info() if x in l2]
                for line in Dating.open_file(self):     
                    for i in range(len(matches)):
                        if matches[i] == line[0:8]:
                            print(f'Okay so we have {line[9:28].strip()} they are {line[32:35].strip()} years old.')
                            print(f'They are {line[98:115].strip()}cm tall and there job is {line[120:135].strip()}')
                            next = input('Would you like to talk to this person or move on to the next? \n(yes/next) \n')
                            if next == 'yes':
                                print('omg yay!')
                                break


        elif line[54:73].strip() == 'female' and line[76:93].strip() == 'everyone':
            while True:
                l2 = [] 
                for i in p.preference_bisexual_male():
                    l2.append(i)
                for i in p.preference_bisexual_female():
                    l2.append(i)
                matches = [x for x in m.info() if x in l2]
                for line in Dating.open_file(self):     
                    for i in range(len(matches)):
                        if matches[i] == line[0:8]:
                            print(f'Okay so we have {line[9:28].strip()} they are {line[32:35].strip()} years old.')
                            print(f'They are {line[98:115].strip()}cm tall and there job is {line[120:135].strip()}')
                            next = input('Would you like to talk to this person or move on to the next? \n(yes/next) \n')
                            if next == 'yes':
                                print('omg yay!')
                                break


m = Match()
m.pairing()
