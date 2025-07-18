# balance : 초기 잔액을 설정하는 변수를 초기화 해주세요.
# 금액은 여러분 마음대로 설정해 주세요.

# 사용자로부터 atm 기계에 사용 목적에 맞는 기능을 선택할 수 있도록
# 기능 입력을 받는 기능을 구현해주세요.
# 입금, 출금, 종료, 입출금 내영 영수증

# 매뉴창은 항시 표시되어 있어야 함
# 사용자 목적을 입력받는 기능이 있어야함
balance = 50000


while True:
    num = input("어서오십시오. 사용하실 기능의 번호를 선택해주십시오.\n"
                "(1.입금, 2.출금, 3.영수증 보기, 4.종료): ")

    if num == '4': #4번은 종료기능
        break

    if num == '1': #입금 기능 구현 -> feat/deposit 브랜치에서 작업
        deposit_amout = int(input('입금하실 금액을 입력해주세요: ')) # str -> int
        balance += deposit_amout # balance = balance + deposit_amout 와 동일
        print(f'입금하신 금액은 {deposit_amout}원 입니다, 현재 잔액은 {balance}원 입니다.')

    if num == '2':
        withdraw_amout = int(input('출금하실 금액을 입력해 주세요: '))
        withdraw_amout = min(balance, withdraw_amout) # 원금초과하면 자동으로 전액 출금
        balance -= withdraw_amout
        print(f'출금하신 금액은 {withdraw_amout}원 입니다, 현재 잔액은 {balance}원 입니다.')

    if num == '3':
        pass

print(f"서비스를 종료합니다. 고객님의 현재 잔액은 {balance}원 입니다.")