#   import libraries
import random

#   Python Roulette libary      
class roulette:
    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

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
        
        
    def roll(self, betAmmount, betPick=None):
        if betPick is None:
            self.betPick = None
        else:
            self.betPick = betPick
        #   Check to see if the bet ammount is valid, if not break
        if float(betAmmount) <= 0.0:
            print('Error: You have bet an incorrect ammount. All bets must be greater than 0.0')
            return
        
        #   Check to see if there is enough money in the bank account
        if self.bankAccount - betAmmount < 0.0:
            print('Error: You do not have enough money in your bank account to bet this much.')
            return
        
        #   beggin the Straight roulette bet and game type
        if self.betType is 'Straight':
            if self.rouletteStyle is 'American':
                #   the picked bet must be an interger between -1 and 36
                if int(betPick) < -1 or int(betPick) > 36:
                    print('Error: You have picked an incorrect bit, please roll again with a bet between -1 and 36. American roulette has 38 diferent possible numbers, where 00 is represented as -1')
                    return
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
                    print('Error: You have picked an incorrect bit, please roll again with a bet between 0 and 36. French roulette has 37 diferent possible numbers, bets can be from 0 to 36')
                    return
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
                return
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
                return
        #    You have chosen an incorrect betting game type            
        else:
            print('Error: We have yet to code this type of betting')
            print('The possible betting game types are: Straight, Color')
            print('EX: Set betting game type to Straight with roulette.(betType="Straight")')

