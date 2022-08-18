from start import Dating
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
        return straight_female

    def preference_gay(self):
        gay = []
        for line in Dating.open_file(self):
            if line[54:73].strip() == 'male' and line[76:93].strip() == 'male':#and (self.age + 2) >= line[32:35] and (self.age - 2) <= line[32:35]:
                gay.append(line[0:9].strip())
            elif line[54:73].strip() == 'male' and line[76:93].strip() == 'everyone':
                gay.append(line[0:9].strip())
        return gay

    def preference_lesbian(self):
        lesbian = []
        for line in Dating.open_file(self):
            if line[54:73].strip() == 'female' and line[76:93].strip() == 'female': #if (self.age + 2) >= line[32:35] and (self.age - 2) <= line[32:35]:
                lesbian.append(line[0:9].strip())  
            elif line[54:73].strip() == 'female' and line[76:93].strip() == 'everyone':
                lesbian.append(line[0:9].strip())              
        return lesbian

    def preference_bisexual_male(self):
        bisexual_male = []
        for line in Dating.open_file(self):   
            if line[54:73].strip() == 'male' and line[76:93].strip() == 'everyone': #and (self.age + 2) >= line[32:35] and (self.age - 2) <= line[32:35]:
                bisexual_male.append(line[0:9].strip())
            elif line[54:73].strip() == 'male' and line[76:93].strip() == 'male':
                bisexual_male.append(line[0:9].strip())              
        return bisexual_male

    def preference_bisexual_female(self):
        bisexual_female = []
        for line in Dating.open_file(self):   
            if line[54:73].strip() == 'female' and line[76:93].strip() == 'everyone': #and (self.age + 2) >= line[32:35] and (self.age - 2) <= line[32:35]:
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
                            if line[164:165].strip() == '1':
                                print(f'They occassionally take drugs, with their favourite being {line[185:210].strip()}')
                            elif line[164:165].strip() == '2':
                                print(f'They often take drugs, with their favourite being {line[185:210].strip()}')
                            elif line[164:165].strip() == '3':
                                print(f'They fuckin\' love taking drugs, with their favourite being {line[185:210].strip()}')
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
                            if line[164:165].strip() == '1':
                                print(f'They occassionally take drugs, with their favourite being {line[185:210].strip()}')
                            elif line[164:165].strip() == '2':
                                print(f'They often take drugs, with their favourite being {line[185:210].strip()}')
                            elif line[164:165].strip() == '3':
                                print(f'They fuckin\' love taking drugs, with their favourite being {line[185:210].strip()}')
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
                            if line[164:165].strip() == '1':
                                print(f'They occassionally take drugs, with their favourite being {line[185:210].strip()}')
                            elif line[164:165].strip() == '2':
                                print(f'They often take drugs, with their favourite being {line[185:210].strip()}')
                            elif line[164:165].strip() == '3':
                                print(f'They fuckin\' love taking drugs, with their favourite being {line[185:210].strip()}')
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
                            if line[164:165].strip() == '1':
                                print(f'They occassionally take drugs, with their favourite being {line[185:210].strip()}')
                            elif line[164:165].strip() == '2':
                                print(f'They often take drugs, with their favourite being {line[185:210].strip()}')
                            elif line[164:165].strip() == '3':
                                print(f'They fuckin\' love taking drugs, with their favourite being {line[185:210].strip()}')
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
                            if line[164:165].strip() == '1':
                                print(f'They occassionally take drugs, with their favourite being {line[185:210].strip()}')
                            elif line[164:165].strip() == '2':
                                print(f'They often take drugs, with their favourite being {line[185:210].strip()}')
                            elif line[164:165].strip() == '3':
                                print(f'They fuckin\' love taking drugs, with their favourite being {line[185:210].strip()}')
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
                            if line[164:165].strip() == '1':
                                print(f'They occassionally take drugs, with their favourite being {line[185:210].strip()}')
                            elif line[164:165].strip() == '2':
                                print(f'They often take drugs, with their favourite being {line[185:210].strip()}')
                            elif line[164:165].strip() == '3':
                                print(f'They fuckin\' love taking drugs, with their favourite being {line[185:210].strip()}')
                            next = input('Would you like to talk to this person or move on to the next? \n(yes/next) \n')
                            if next == 'yes':
                                print('omg yay!')
                                break


m = Match()
m.pairing()


#id = line[0:9]
#name = line[9:28]
#age = line[32:35]
#gender = line[54:73]
#g_i = line[76:93]
#height = line[98:115]
#job = line[120:135]
#drug_intake =
#fav_drug =