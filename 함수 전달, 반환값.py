#__________________________________________________________________________________________________전달값, 반환값
def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {} 원 입니다.".format (balance+money))
    return balance + money # 값 반환
def withdraw(balance, money):
    if balance >= money : 
        print("출금이 완료되었습니다. 잔액은 {} 원입니다".format(balance - money))
        return balance - money
    else :
        print("잔액이 모자랍니다. 잔액은 {}입니다".format(balance))
        return balance
def withdraw_nihgt(balance, money):
    commission = 100 
    return commission, balance - money - commission
balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_nihgt(balance, 500)
print("수수료는 {}원입며, 잔액은 {}원입니다.".format(commission, balance))