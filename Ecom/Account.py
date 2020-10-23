import random

#accountList = [item for item in range(11111,222222)]
accountList = [11111,222222]

class Account:
    cnt =0
    def __init__(self,accBalance=5000.0,accTy='Saving'):
        if Account.cnt==2:
            print('Account cannot be created...strictly 2 accounts for now')
            return

        self.accountNo=accountList[Account.cnt]
        Account.cnt+=1
        self.accountType=accTy
        self.accountBalance=accBalance

    def __str__(self):
        #return f'\n{self.__dict__}'
        return '''
                Account No : {}
                Account Type : {}
                Account Balance : {}
        '''.format(self.accountNo,self.accountType,self.accountBalance)

    def __repr__(self):
        return str(self)
