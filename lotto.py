List = [
    [939,4,11,28,39,42,45,6],[938,4,8,10,16,31,36,9],[937,2,10,13,22,29,40,26],[936,7,11,13,17,18,29,43],[935,4,10,20,32,38,44,18]
    ]
hoicha = 5
for i in range(hoicha) :
    print(List[i][0], '회차 => ', List[i][1],List[i][2],List[i][3],List[i][4],List[i][5],List[i][6], '+보너스 : ', List[i][7])
print("======================================================================================================================")

Lotto = [0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0]

num_of_lotto = 45
for i in range(hoicha) :
    for k in range(num_of_lotto + 1) :
        Lotto[k] = Lotto[k] + List[i].count(k)
#for i in range(1, num_of_lotto + 1) :
#    if Lotto[i] != 0 :
#        print(i, "=> ", Lotto[i])
#print("======================================================================================================================")

#i = Lotto.index(max(Lotto))
#print("Max : ", i, Lotto[i])

m = max(Lotto)
result = [i for i, j in enumerate(Lotto) if j == m]
print("Max => ", m, ":", result)







