import sys
import random

while True :

    player = int(input('참여자수 입력 [Quit: 0] ? '))
    deploy =  player * 2
    if player == 0 : 
        sys.exit()
    #bet = int(input('베팅금액 입력 [Quit: 0] ? '))
    
    hwatoo_image = random.sample(range(20), deploy)  # 패 돌리기 
    hwatoo_gguk = {} 
    guest_hwatoo = {}  
    guest_pae = {}

    for i in range(deploy) :   
        hwatoo_image[i] = hwatoo_image[i] + 1    # 0~19 를 1~20으로 변환 (끗으로 표시)\
    #print(hwatoo_image)
    
    i = 0
    for i in range(deploy) : 
        hwatoo_gguk[i] = hwatoo_image[i] 
        if hwatoo_gguk[i] >= 10 :
            hwatoo_gguk[i] = hwatoo_gguk[i] - 10   # 10 ~ 20을 한자리 끗으로 변환 (첫번째 패)
    #print(hwatoo_image, hwatoo_gguk)

    i = 0
    while i < deploy :
        guest_hwatoo[i] = hwatoo_gguk[i] + hwatoo_gguk[i+1]
    
        if guest_hwatoo[i] >= 10 :
                guest_hwatoo[i] = guest_hwatoo[i] - 10
        guest_pae[i] = str(guest_hwatoo[i]) + '끗' 
     
        if hwatoo_gguk[i] == hwatoo_gguk[i+1] :
            guest_hwatoo[i] = hwatoo_gguk[i]
            guest_pae[i] = str(guest_hwatoo[i]) + '땡'
    
        i = i + 2
  
    print('hwatoo_image\thwatoo_gguk\tguest_hwatoo\tguest_pae')
    print(hwatoo_image, '\t', hwatoo_gguk, '\t', guest_hwatoo, '\t', guest_pae)
  
    # 패 판독하기 
    win = max(zip(guest_pae.values(), guest_pae.keys()))
    print('WIN ==> Guest %d is %s' %(win[1]/2, win[0]))

    

