#   import libraries
import random
import numpy as np

#   Python Roulette libary      
class roulette:
    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
    even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]

    def __init__(self, betType=None, rouletteStyle=None, bankAccount=None, rollNumber=None, rollHistory=None, colorHistory=None):
        #   Set the defualts
        if betType is None:
            self.betType = 'Straight'
        else:
            self.betType = betType
        if rouletteStyle is None:
            self.rouletteStyle = 'American'
        else:
            self.rouletteStyle = rouletteStyle
        if bankAccount is None:
            self.bankAccount = 10000.0
        else:
            self.bankAccount = float(bankAccount)
        if rollNumber is None:
            self.rollNumber = 0
        else:
            self.rollNumber = int(rollNumber)
        if rollHistory is None:
            self.rollHistory = []
        else:
            self.rollHistory = rollHistory    
        if colorHistory is None:
            self.colorHistory = []
        else:
            self.colorHistory = colorHistory
            
    def recordColorHistory(self, theRoll):
        #   was the roll red?
        if theRoll in self.red:
            self.colorHistory.append('Red')
        #   was the roll black?
        elif theRoll in self.black:
            self.colorHistory.append('Black')
        #   if the roll wasn't black or red, then it was green
        else:
            self.colorHistory.append('Green')
    
    #   determine if the roll was odd or even
    def determineIfOddOrEven(self, theRoll):
        #   was the roll odd?
        if theRoll in self.odd:
            return('Odd')
        #   was the roll even?
        elif theRoll in self.even:
            return('Even')
        #   if the roll wasn't odd or even it landed on 0, or 00
        else:
            return(False)
    
    #   lets roll the roulette wheel
    def rollTheRouletteWheel(self):
        print('--- Spinning the '+self.rouletteStyle+' roullete wheel ---')
        #   the picked bet must be an interger between -1 and 36
        if self.rouletteStyle is 'American':        
            theRoll = random.randint(-1,36)
        else:
            theRoll = random.randint(0,36)
        #    asign the color history
        self.recordColorHistory(theRoll)  
        #    add the roll to the history     
        self.rollHistory.append(theRoll)
        print('The ball has landed on '+str(theRoll)+' '+str(self.colorHistory[-1]))
        return(theRoll)
   
    #   create a function that checks to see if the bets placed are valid
    def checkBets(self, betPick, betMin):
        betMax = 36
        for i in betPick:
            if int(i) < betMin or int(i) > betMax:
                print('Error: '+str(i)+' is an invalid bet')
                if self.rouletteStyle is 'American':
                    print('Please roll again with a bet between -1 and 36. American roulette has 38 diferent possible numbers, where 00 is represented as -1')
                else:
                    print('Please roll again with a bet between -1 and 36. American roulette has 38 diferent possible numbers, where 00 is represented as -1')
                return(False)
        return(True)        
        
    def roll(self, betAmmount, betPick=None):
        if betPick is None:
            self.betPick = None
        else:
            self.betPick = betPick
        #   Check to see if the bet ammount is valid, if not break
        if float(betAmmount) <= 0.0:
            print('Error: You have bet an incorrect ammount. All bets must be greater than 0.0')
            return()
        
        #   Check to see if there is enough money in the bank account
        if self.bankAccount - betAmmount < 0.0:
            print('Error: You do not have enough money in your bank account to bet this much.')
            return()

        #   beggin the Straight roulette bet and game type
        if self.betType is 'Straight':
            if self.rouletteStyle is 'American':
                #   the picked bet must be an interger between -1 and 36
                if int(betPick) < -1 or int(betPick) > 36:
                    print('Error: You have picked an incorrect bet, please roll again with a bet between -1 and 36. American roulette has 38 diferent possible numbers, where 00 is represented as -1')
                    return()
                else:
                    theRoll = self.rollTheRouletteWheel()
                    print('You bet the ball would land on '+str(betPick))

                    if theRoll == int(betPick):
                        print('**** !!! You have won !!! ***')
                        print('The payout is 35 to 1')
                        payout = 35.0*float(betAmmount)
                        self.bankAccount = self.bankAccount + payout
                        print(str(payout)+' has been added to your account')
                        print('Your new account balance is '+str(self.bankAccount))
                        print('*** End of Roll, Please roll again! ***')
                    else:
                        print('Oh No!, You have lost')
                        self.bankAccount = self.bankAccount - float(betAmmount)
                        print('Your bet of '+str(betAmmount)+' has been removed from your account')
                        print('Your new account balance is '+str(self.bankAccount))
                        print('--- End of Roll, Please roll again! ---')
            elif self.rouletteStyle is 'French':
                #   the picked bet must be an interger between 0 and 36
                if int(betPick) < 0 or int(betPick) > 36:
                    print('Error: You have picked an incorrect bet, please roll again with a bet between 0 and 36. French roulette has 37 diferent possible numbers, bets can be from 0 to 36')
                    return()
                else:
                    theRoll = self.rollTheRouletteWheel()
                    print('You bet the ball would land on '+str(betPick))

                    if theRoll == int(betPick):
                        print('**** !!! You have won !!! ***')
                        print('The payout is 35 to 1')
                        payout = 35.0*float(betAmmount)
                        self.bankAccount = self.bankAccount + payout
                        print(str(payout)+' has been added to your account')
                        print('Your new account balance is '+str(self.bankAccount))
                        print('*** End of Roll, Please roll again! ***')
                    else:
                        print('Oh No!, You have lost')
                        self.bankAccount = self.bankAccount - float(betAmmount)
                        print('Your bet of '+str(betAmmount)+' has been removed from your account')
                        print('Your new account balance is '+str(self.bankAccount))
                        print('--- End of Roll, Please roll again! ---')
            #   you have chosen an incorrect roulette style
            else:
                print('Error: You have chosen an incorrect roulette style!')
                print('The possible roulette styles are American or French')
                print('EX: Set roulette style to American by roulette.(rouletteStyle="American")')
        #   Begin a color choice game
        elif self.betType is 'Color':
            if betPick is 'Red' or betPick is 'Black':

                theRoll = self.rollTheRouletteWheel()
                print('You bet the ball would land on '+betPick)

                if self.colorHistory[-1] is betPick:
                    print('**** !!! You have won !!! ***')
                    print('The payout is 1 to 1')
                    payout = 1.0*float(betAmmount)
                    self.bankAccount = self.bankAccount + payout
                    print(str(payout)+' has been added to your account')
                    print('Your new account balance is '+str(self.bankAccount))
                    print('*** End of Roll, Please roll again! ***')
                else:
                    print('Oh No!, You have lost')
                    self.bankAccount = self.bankAccount - float(betAmmount)
                    print('Your bet of '+str(betAmmount)+' has been removed from your account')
                    print('Your new account balance is '+str(self.bankAccount))
                    print('--- End of Roll, Please roll again! ---')
            else:
                print('Error: You have picked an incorrect color. Acceptable colors are Red and Black.')
                return()
        #   Begin a row betting game
        elif self.betType is 'Row':
            #   A row bet is a bet on 0 or 00
            if self.rouletteStyle is 'American':
                theRoll = self.rollTheRouletteWheel()
                print('You bet "Row", that ball would land on 0, or 00')

                if theRoll == 0 or theRoll == -1:
                    print('**** !!! You have won !!! ***')
                    print('The payout is 17 to 1')
                    payout = 17.0*float(betAmmount)
                    self.bankAccount = self.bankAccount + payout
                    print(str(payout)+' has been added to your account')
                    print('Your new account balance is '+str(self.bankAccount))
                    print('*** End of Roll, Please roll again! ***')
                else:
                    print('Oh No!, You have lost')
                    self.bankAccount = self.bankAccount - float(betAmmount)
                    print('Your bet of '+str(betAmmount)+' has been removed from your account')
                    print('Your new account balance is '+str(self.bankAccount))
                    print('--- End of Roll, Please roll again! ---')
            else:
                print('Sorry row betting is only allowed on the American roulette wheel. Please set the roullete style to American by roulette.(rouletteStyle="American")')
                return()
        #   Begin a split betting game, where you can pick any two numbers
        elif self.betType is 'Split':
            if np.size(betPick) == 1 or np.size(betPick) > 2:
                print('Error: With the split betting game you can pick any two roulette numbers. Please supply a list of two different intergers.')
                return()
            if self.rouletteStyle is 'American':
                #   the picked bet must be an interger between -1 and 36
                if int(betPick[0]) < -1 or int(betPick[0]) > 36:
                    print('Error: You have picked an incorrect bet for your first number, please roll again with a bet between -1 and 36. American roulette has 38 diferent possible numbers, where 00 is represented as -1')
                    return()
                elif int(betPick[1]) < -1 or int(betPick[1]) > 36:
                    print('Error: You have picked an incorrect bet for your second number, please roll again with a bet between -1 and 36. American roulette has 38 diferent possible numbers, where 00 is represented as -1')
                    return()
                else:
                    theRoll = self.rollTheRouletteWheel()
                    print('You bet the ball would land on '+str(betPick))

                    if theRoll == int(betPick[0]) or theRoll == int(betPick[1]):
                        print('**** !!! You have won !!! ***')
                        print('The payout is 17 to 1')
                        payout = 17.0*float(betAmmount)
                        self.bankAccount = self.bankAccount + payout
                        print(str(payout)+' has been added to your account')
                        print('Your new account balance is '+str(self.bankAccount))
                        print('*** End of Roll, Please roll again! ***')
                    else:
                        print('Oh No!, You have lost')
                        self.bankAccount = self.bankAccount - float(betAmmount)
                        print('Your bet of '+str(betAmmount)+' has been removed from your account')
                        print('Your new account balance is '+str(self.bankAccount))
                        print('--- End of Roll, Please roll again! ---')
            elif self.rouletteStyle is 'French':
                #   the picked bet must be an interger between 0 and 36
                if int(betPick[0]) < 0 or int(betPick[0]) > 36:
                    print('Error: You have picked an incorrect bet for your first number, please roll again with a bet between 0 and 36. French roulette has 37 diferent possible numbers, bets can be from 0 to 36')
                    return()
                elif int(betPick[1]) < 0 or int(betPick[1]) > 36:
                    print('Error: You have picked an incorrect bet for your second number, please roll again with a bet between 0 and 36. French roulette has 37 diferent possible numbers, bets can be from 0 to 36')
                    return()
                else:
                    theRoll = self.rollTheRouletteWheel()
                    print('You bet the ball would land on '+str(betPick))

                    if theRoll == int(betPick[0]) or theRoll == int(betPick[1]):
                        print('**** !!! You have won !!! ***')
                        print('The payout is 17 to 1')
                        payout = 17.0*float(betAmmount)
                        self.bankAccount = self.bankAccount + payout
                        print(str(payout)+' has been added to your account')
                        print('Your new account balance is '+str(self.bankAccount))
                        print('*** End of Roll, Please roll again! ***')
                    else:
                        print('Oh No!, You have lost')
                        self.bankAccount = self.bankAccount - float(betAmmount)
                        print('Your bet of '+str(betAmmount)+' has been removed from your account')
                        print('Your new account balance is '+str(self.bankAccount))
                        print('--- End of Roll, Please roll again! ---')
        #   Begin a street betting game, where you can pick any three numbers
        elif self.betType is 'Street':
            if np.size(betPick) <= 2 or np.size(betPick) > 3:
                print('Error: With the street betting game you can pick any three roulette numbers. Please supply a list of three different intergers.')
                return()
            if self.rouletteStyle is 'American':
                #   the picked bet must be an interger between -1 and 36
                if int(betPick[0]) < -1 or int(betPick[0]) > 36:
                    print('Error: You have picked an incorrect bet for your first number, please roll again with a bet between -1 and 36. American roulette has 38 diferent possible numbers, where 00 is represented as -1')
                    return()
                elif int(betPick[1]) < -1 or int(betPick[1]) > 36:
                    print('Error: You have picked an incorrect bet for your second number, please roll again with a bet between -1 and 36. American roulette has 38 diferent possible numbers, where 00 is represented as -1')
                    return()
                elif int(betPick[2]) < -1 or int(betPick[2]) > 36:
                    print('Error: You have picked an incorrect bet for your third number, please roll again with a bet between -1 and 36. American roulette has 38 diferent possible numbers, where 00 is represented as -1')
                    return()
                else:
                    theRoll = self.rollTheRouletteWheel()
                    print('You bet the ball would land on '+str(betPick))

                    if theRoll == int(betPick[0]) or theRoll == int(betPick[1]) or theRoll == int(betPick[2]):
                        print('**** !!! You have won !!! ***')
                        print('The payout is 11 to 1')
                        payout = 11.0*float(betAmmount)
                        self.bankAccount = self.bankAccount + payout
                        print(str(payout)+' has been added to your account')
                        print('Your new account balance is '+str(self.bankAccount))
                        print('*** End of Roll, Please roll again! ***')
                    else:
                        print('Oh No!, You have lost')
                        self.bankAccount = self.bankAccount - float(betAmmount)
                        print('Your bet of '+str(betAmmount)+' has been removed from your account')
                        print('Your new account balance is '+str(self.bankAccount))
                        print('--- End of Roll, Please roll again! ---')
            elif self.rouletteStyle is 'French':
                #   the picked bet must be an interger between 0 and 36
                if int(betPick[0]) < 0 or int(betPick[0]) > 36:
                    print('Error: You have picked an incorrect bet for your first number, please roll again with a bet between 0 and 36. French roulette has 37 diferent possible numbers, bets can be from 0 to 36')
                    return()
                elif int(betPick[1]) < 0 or int(betPick[1]) > 36:
                    print('Error: You have picked an incorrect bet for your second number, please roll again with a bet between 0 and 36. French roulette has 37 diferent possible numbers, bets can be from 0 to 36')
                    return()
                elif int(betPick[2]) < 0 or int(betPick[2]) > 36:
                    print('Error: You have picked an incorrect bet for your third number, please roll again with a bet between 0 and 36. French roulette has 37 diferent possible numbers, bets can be from 0 to 36')
                    return()
                else:
                    theRoll = self.rollTheRouletteWheel()
                    print('You bet the ball would land on '+str(betPick))

                    if theRoll == int(betPick[0]) or theRoll == int(betPick[1]) or theRoll == int(betPick[2]):
                        print('**** !!! You have won !!! ***')
                        print('The payout is 11 to 1')
                        payout = 11.0*float(betAmmount)
                        self.bankAccount = self.bankAccount + payout
                        print(str(payout)+' has been added to your account')
                        print('Your new account balance is '+str(self.bankAccount))
                        print('*** End of Roll, Please roll again! ***')
                    else:
                        print('Oh No!, You have lost')
                        self.bankAccount = self.bankAccount - float(betAmmount)
                        print('Your bet of '+str(betAmmount)+' has been removed from your account')
                        print('Your new account balance is '+str(self.bankAccount))
                        print('--- End of Roll, Please roll again! ---')
            #   you have chosen an incorrect roulette style
            else:
                print('Error: You have chosen an incorrect roulette style!')
                print('The possible roulette styles are American or French')
                print('EX: Set roulette style to American by roulette.(rouletteStyle="American")')
        #   Begin a Corner betting game, where you can pick any four numbers
        elif self.betType is 'Corner':
            if np.size(betPick) <= 3 or np.size(betPick) > 4:
                print('Error: With the corner betting game you can pick any four roulette numbers. Please supply a list of four different intergers.')
                return()
            if self.rouletteStyle is 'American':
                #   the picked bet must be an interger between -1 and 36
                if int(betPick[0]) < -1 or int(betPick[0]) > 36:
                    print('Error: You have picked an incorrect bet for your first number, please roll again with a bet between -1 and 36. American roulette has 38 diferent possible numbers, where 00 is represented as -1')
                    return()
                elif int(betPick[1]) < -1 or int(betPick[1]) > 36:
                    print('Error: You have picked an incorrect bet for your second number, please roll again with a bet between -1 and 36. American roulette has 38 diferent possible numbers, where 00 is represented as -1')
                    return()
                elif int(betPick[2]) < -1 or int(betPick[2]) > 36:
                    print('Error: You have picked an incorrect bet for your third number, please roll again with a bet between -1 and 36. American roulette has 38 diferent possible numbers, where 00 is represented as -1')
                    return()
                elif int(betPick[3]) < -1 or int(betPick[3]) > 36:
                    print('Error: You have picked an incorrect bet for your fourth number, please roll again with a bet between -1 and 36. American roulette has 38 diferent possible numbers, where 00 is represented as -1')
                    return()
                else:
                    theRoll = self.rollTheRouletteWheel()
                    print('You bet the ball would land on '+str(betPick))

                    if theRoll == int(betPick[0]) or theRoll == int(betPick[1]) or theRoll == int(betPick[2]):
                        print('**** !!! You have won !!! ***')
                        print('The payout is 8 to 1')
                        payout = 8.0*float(betAmmount)
                        self.bankAccount = self.bankAccount + payout
                        print(str(payout)+' has been added to your account')
                        print('Your new account balance is '+str(self.bankAccount))
                        print('*** End of Roll, Please roll again! ***')
                    else:
                        print('Oh No!, You have lost')
                        self.bankAccount = self.bankAccount - float(betAmmount)
                        print('Your bet of '+str(betAmmount)+' has been removed from your account')
                        print('Your new account balance is '+str(self.bankAccount))
                        print('--- End of Roll, Please roll again! ---')
            elif self.rouletteStyle is 'French':
                #   the picked bet must be an interger between 0 and 36
                if int(betPick[0]) < 0 or int(betPick[0]) > 36:
                    print('Error: You have picked an incorrect bet for your first number, please roll again with a bet between 0 and 36. French roulette has 37 diferent possible numbers, bets can be from 0 to 36')
                    return()
                elif int(betPick[1]) < 0 or int(betPick[1]) > 36:
                    print('Error: You have picked an incorrect bet for your second number, please roll again with a bet between 0 and 36. French roulette has 37 diferent possible numbers, bets can be from 0 to 36')
                    return()
                elif int(betPick[2]) < 0 or int(betPick[2]) > 36:
                    print('Error: You have picked an incorrect bet for your third number, please roll again with a bet between 0 and 36. French roulette has 37 diferent possible numbers, bets can be from 0 to 36')
                    return()
                elif int(betPick[3]) < -1 or int(betPick[3]) > 36:
                    print('Error: You have picked an incorrect bet for your fourth number, please roll again with a bet between -1 and 36. American roulette has 38 diferent possible numbers, where 00 is represented as -1')
                    return()
                else:
                    theRoll = self.rollTheRouletteWheel()
                    print('You bet the ball would land on '+str(betPick))

                    if theRoll == int(betPick[0]) or theRoll == int(betPick[1]) or theRoll == int(betPick[2]):
                        print('**** !!! You have won !!! ***')
                        print('The payout is 8 to 1')
                        payout = 8.0*float(betAmmount)
                        self.bankAccount = self.bankAccount + payout
                        print(str(payout)+' has been added to your account')
                        print('Your new account balance is '+str(self.bankAccount))
                        print('*** End of Roll, Please roll again! ***')
                    else:
                        print('Oh No!, You have lost')
                        self.bankAccount = self.bankAccount - float(betAmmount)
                        print('Your bet of '+str(betAmmount)+' has been removed from your account')
                        print('Your new account balance is '+str(self.bankAccount))
                        print('--- End of Roll, Please roll again! ---')
            #   you have chosen an incorrect roulette style
            else:
                print('Error: You have chosen an incorrect roulette style!')
                print('The possible roulette styles are American or French')
                print('EX: Set roulette style to American by roulette.(rouletteStyle="American")')        
        #   Begin a line betting game, where you can pick any four numbers
        elif self.betType is 'Line':
            if np.size(betPick) <= 5 or np.size(betPick) > 6:
                print('Error: With the line betting game you can pick any six roulette numbers. Please supply a list of six different intergers.')
                return()
            validBets = False
            if self.rouletteStyle is 'American':
                validBets = self.checkBets(betPick, -1)
            elif self.rouletteStyle is 'French':
                validBets = self.checkBets(betPick, 0)
            #   you have chosen an incorrect roulette style
            else:
                print('Error: You have chosen an incorrect roulette style!')
                print('The possible roulette styles are American or French')
                print('EX: Set roulette style to American by roulette.(rouletteStyle="American")')
                return()  
            #   let the roll begin
            if validBets is True:
                theRoll = self.rollTheRouletteWheel()
                print('You bet the ball would land on '+str(betPick))

                if theRoll == int(betPick[0]) or theRoll == int(betPick[1]) or theRoll == int(betPick[2]) or theRoll == int(betPick[3]) or theRoll == int(betPick[4]) or theRoll == int(betPick[5]):
                    print('**** !!! You have won !!! ***')
                    print('The payout is 5 to 1')
                    payout = 5.0*float(betAmmount)
                    self.bankAccount = self.bankAccount + payout
                    print(str(payout)+' has been added to your account')
                    print('Your new account balance is '+str(self.bankAccount))
                    print('*** End of Roll, Please roll again! ***')
                else:
                    print('Oh No!, You have lost')
                    self.bankAccount = self.bankAccount - float(betAmmount)
                    print('Your bet of '+str(betAmmount)+' has been removed from your account')
                    print('Your new account balance is '+str(self.bankAccount))
                    print('--- End of Roll, Please roll again! ---')
        #   Begin a dozen betting game, where you can pick any 12 numbers
        elif self.betType is 'Dozen':
            if np.size(betPick) <= 11 or np.size(betPick) > 12:
                print('Error: With the Dozen betting game you can pick any 12 roulette numbers. Please supply a list of 12 different intergers.')
                return()
            validBets = False
            if self.rouletteStyle is 'American':
                validBets = self.checkBets(betPick, -1)
            elif self.rouletteStyle is 'French':
                validBets = self.checkBets(betPick, 0)
            #   you have chosen an incorrect roulette style
            else:
                print('Error: You have chosen an incorrect roulette style!')
                print('The possible roulette styles are American or French')
                print('EX: Set roulette style to American by roulette.(rouletteStyle="American")')
                return()  
            #   let the roll begin
            if validBets is True:
                theRoll = self.rollTheRouletteWheel()
                print('You bet the ball would land on '+str(betPick))

                if theRoll == int(betPick[0]) or theRoll == int(betPick[1]) or theRoll == int(betPick[2]) or theRoll == int(betPick[3]) or theRoll == int(betPick[4]) or theRoll == int(betPick[5]) or theRoll == int(betPick[6]) or theRoll == int(betPick[7]) or theRoll == int(betPick[8]) or theRoll == int(betPick[9]) or theRoll == int(betPick[10]) or theRoll == int(betPick[11]):
                    print('**** !!! You have won !!! ***')
                    print('The payout is 2 to 1')
                    payout = 2.0*float(betAmmount)
                    self.bankAccount = self.bankAccount + payout
                    print(str(payout)+' has been added to your account')
                    print('Your new account balance is '+str(self.bankAccount))
                    print('*** End of Roll, Please roll again! ***')
                else:
                    print('Oh No!, You have lost')
                    self.bankAccount = self.bankAccount - float(betAmmount)
                    print('Your bet of '+str(betAmmount)+' has been removed from your account')
                    print('Your new account balance is '+str(self.bankAccount))
                    print('--- End of Roll, Please roll again! ---')
       
        #   Begin a dozen betting game, where you can pick any 12 numbers
        elif self.betType is 'Penta':
            if np.size(betPick) <= 4 or np.size(betPick) > 5:
                print('Error: With the Penta betting game you can pick any 5 roulette numbers. Please supply a list of 5 different intergers.')
                return()
            validBets = False
            if self.rouletteStyle is 'American':
                validBets = self.checkBets(betPick, -1)
            elif self.rouletteStyle is 'French':
                validBets = self.checkBets(betPick, 0)
            #   you have chosen an incorrect roulette style
            else:
                print('Error: You have chosen an incorrect roulette style!')
                print('The possible roulette styles are American or French')
                print('EX: Set roulette style to American by roulette.(rouletteStyle="American")')
                return()  
            #   let the roll begin
            if validBets is True:
                theRoll = self.rollTheRouletteWheel()
                print('You bet the ball would land on '+str(betPick))

                if theRoll == int(betPick[0]) or theRoll == int(betPick[1]) or theRoll == int(betPick[2]) or theRoll == int(betPick[3]) or theRoll == int(betPick[4]):
                    print('**** !!! You have won !!! ***')
                    print('The payout is 6.2 to 1')
                    payout = 6.2*float(betAmmount)
                    self.bankAccount = self.bankAccount + payout
                    print(str(payout)+' has been added to your account')
                    print('Your new account balance is '+str(self.bankAccount))
                    print('*** End of Roll, Please roll again! ***')
                else:
                    print('Oh No!, You have lost')
                    self.bankAccount = self.bankAccount - float(betAmmount)
                    print('Your bet of '+str(betAmmount)+' has been removed from your account')
                    print('Your new account balance is '+str(self.bankAccount))
                    print('--- End of Roll, Please roll again! ---')
        
        #   Begin an even or odd choice game
        elif self.betType is 'EvenOdd':
            if betPick is 'Odd' or betPick is 'Even':
                theRoll = self.rollTheRouletteWheel()
                oddOrEvenTruth = self.determineIfOddOrEven(theRoll)
                print('You bet the ball would land on '+betPick)

                if oddOrEvenTruth is betPick:
                    print('**** !!! You have won !!! ***')
                    print('The payout is 1 to 1')
                    payout = 1.0*float(betAmmount)
                    self.bankAccount = self.bankAccount + payout
                    print(str(payout)+' has been added to your account')
                    print('Your new account balance is '+str(self.bankAccount))
                    print('*** End of Roll, Please roll again! ***')
                else:
                    print('Oh No!, You have lost')
                    self.bankAccount = self.bankAccount - float(betAmmount)
                    print('Your bet of '+str(betAmmount)+' has been removed from your account')
                    print('Your new account balance is '+str(self.bankAccount))
                    print('--- End of Roll, Please roll again! ---')
            else:
                print('Error: You have picked an incorrect bet. Acceptable bets are Odd or Even.')
                return()
                
        #   Begin a multi bet Straight game
        elif self.betType is 'MultiStraight':
            validBets = False
            if self.rouletteStyle is 'American':
                validBets = self.checkBets(betPick, -1)
            elif self.rouletteStyle is 'French':
                validBets = self.checkBets(betPick, 0)
            #   you have chosen an incorrect roulette style
            else:
                print('Error: You have chosen an incorrect roulette style!')
                print('The possible roulette styles are American or French')
                print('EX: Set roulette style to American by roulette.(rouletteStyle="American")')
                return()  
            
            #   let the roll begin
            if validBets is True:
                theRoll = self.rollTheRouletteWheel()
                print('You bet the ball would land on '+str(betPick))

                if theRoll in betPick:
                    print('**** !!! You have won !!! ***')
                    print('The payout is 35 to 1')
                    payout = 35.0*float(betAmmount)
                    #   determine the ammount to be subtracted from your account
                    deductMoney = (len(betPick) - 1.0) * float(betAmmount)
                    self.bankAccount = self.bankAccount + payout - deductMoney
                    print(str(payout)+' has been added to your account')
                    print(str(deductMoney)+' has been removed from your account')

                    print('Your new account balance is '+str(self.bankAccount))
                    print('*** End of Roll, Please roll again! ***')
                else:
                    print('Oh No!, You have lost')
                    self.bankAccount = self.bankAccount - (len(betPick)*float(betAmmount))
                    print('Your bet of '+str(len(betPick)*float(betAmmount))+' has been removed from your account')
                    print('Your new account balance is '+str(self.bankAccount))
                    print('--- End of Roll, Please roll again! ---')
        #    You have chosen an incorrect betting game type            
        else:
            print('Error: We have yet to code this type of betting')
            print('The possible betting game types are: Straight, Color, Row, Split, Street, Corner, Penta, Line, Dozen, EvenOdd, MultiStraight')
            print('EX: Set betting game type to Straight with roulette.(betType="Straight")')

