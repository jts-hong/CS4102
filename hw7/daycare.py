def greedy(dic_RC):
    inc = []
    dec = []
    final = []
    for i in dic_RC:
        if i[1]-i[0]>=0:
            inc.append(i)
        else:
            dec.append(i)
    inc = sorted(inc,key = lambda item: item[0])
    for i in inc:
        final.append(i)
    dec = sorted(dec,key = lambda item: item[1],reverse=True)
    for i in dec:
        final.append(i)


    C_R =0
    C_T =0
    for room in final:
        if room[0]>=C_R:
            C_T+=(room[0]-C_R)
            C_R=(room[1])
        else:
            C_R =C_R - room[0]+room[1]
        
    print(C_T)

#---Input---#

n = input()
while (True):
    dis_RC=[]
    for i in range (int(n)):
        x = input()
        a=x.split(" ")
        r1 = int(a[0])
        r2 = int(a[1])
        dis_RC.append((r1,r2))
    greedy(dis_RC)
    dis_RC=[]
    try:
        n = input()
        if n=='':
            quit()
    except:
        quit()