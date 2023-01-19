import time
from random import randint
from korail2 import Korail
from korail2 import *

korail = Korail("1460624313", "eoaoWkd1!") # with membership number
korail = Korail("010-4764-3016", "eoaoWkd1!") # with phone number

dep = '서울'
arr = '부산'
date = '20230121'
tr_time = '100000'
psgrs = [AdultPassenger(2)]
# psgrs = [AdultPassenger(2)]
# trains = korail.search_train(dep, arr, date, tr_time, train_type=TrainType.KTX, include_no_seats=True)
trains = korail.search_train(dep, arr, date, tr_time, passengers=psgrs, include_no_seats=True)

print(*trains, sep="\n")

train_num = input("몇 번째 기차를 예매하시겠어요?(0번부터 시작)")
train_num = int(train_num)

flag = False
i = 0

# 루프 시작
while flag == False:
    try:
        i += 1
        # time.sleep(randint(2, 4))
        time.sleep(0.1)
        print(f"{i}번째 시도")
        reservation = korail.reserve(trains[train_num], passengers=psgrs)
        print(reservation)
        flag = True
        
    except:
        pass