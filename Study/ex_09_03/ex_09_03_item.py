jjj = { "기모" : 1 , "리나" : 2,  "파덕" : 0}

#전체 딕셔너리 출력
print("전체딕셔너리",jjj)


#딕셔너리의 key값만 출력
print("key값만받기", list(jjj))


#딕셔너리 key값만 출력2
print (jjj.keys())


#딕셔너리 value값만 출력
print (jjj.values())


item_list = jjj.items()
print(item_list)


for aaa,bbb in jjj.items() :
    print(aaa,bbb)




#newlist = jjj.items()
#print(newlist[1])
