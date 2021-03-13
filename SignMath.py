import numpy as np
import random


class mathMode:
    def slideMath(self, smean, ssd, slide, cycle, days):
        self.smean = 60
        self.ssd = 5
        self.slide = 20
        self.cycle = 20
        self.days = 4
        
        dist = np.random.normal(smean, ssd)

        seenSign = dist/cycle
        signForDays = seenSign*days

        signPerc = signForDays/slide

        if signPerc >= 1:
            signPerc = 1
        signsSighted = signPerc*slide
        signPerF = "{:.2f}".format(signPerc*100)

        return signsSighted, signPerF


    def userExperience(self):
        mean = input('Enter the mean time in seconds that a student can see the sign: ')
        standev = input('Enter the standard deviation of the curve: ')
        slude = input('Enter the amount of slides the sign will display: ')
        cycle = input('Enter the time in seconds between slide cycles: ')
        da = input('Enter the number of days per week a student sees the sign: ')

        if int(da) > 7:
            print('c\'mon mayne, theres only 7 days in a week')
            exit()
        try:
            hmm = danumbz.slideMath(int(mean), int(standev),int(slude), int(cycle), int(da))
        except ValueError:
            print('ERROR: Not all inputs are positive integers!')
        except:
            print('ERROR: Something went wrong :(')
        return hmm


danumbz = mathMode()
# danumbz.userExperience()
