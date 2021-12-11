def graph(machines,jobs,cmax):
    spaces = " "*(len(machines))
    i=0
    for m in machines.values():
        print(spaces+' ||')
        shape = 0
        j = ''
        for job in m:
            if shape % 2:
                j += u"\u25A0"*job
            else:
                j += u"\u25A1"*job
            shape += 1
        i+=1
        print(i,'||'+j)

    print(spaces+' ||'+'_'*(cmax+3))



def withspt():
    m = 1
    jobs = [int(x) for x in input("entrez vos jobs séparé par , : ").split(",")]
    #["5","4","8"]
    #[5,4,8]
    machines = {x:[] for x in range(m)}
    #{0:[]}
    jobs.sort()
    #[4,5,8]
    i = 0
    for job in jobs:
        machines[i%m].append(job)
        i+=1
    #{0:[4,5,8]}
    print(machines)
    cmax = max([sum(x) for x in machines.values()])
    #[sum(x) for x in machines.values()]
    x=1
    cbar=0
    while x < len(machines[0])+1:
        cbar += sum(machines[0][:x])
        x+=1

    cbar=cbar#/ len(machines[0])
    graph(machines,jobs,cmax)
    print("cmax : ",cmax)
    print("cbar : ",cbar)

def withoutspt():
    m = 1
    jobs = [int(x) for x in input("entrez vos jobs séparé par , : ").split(",")]

    machines = {x:[] for x in range(m)}
    i = 0
    for job in jobs:
        machines[i%m].append(job)
        i+=1


    print(machines)
    cmax = max([sum(x) for x in machines.values()])
    graph(machines,jobs,cmax)

    x=1
    cbar=0
    while x < len(machines[0])+1:
        cbar += sum(machines[0][:x])
        x+=1
    cbar=cbar#/ len(machines[0])
    
    print("cmax : ",cmax)
    print("cbar : ",cbar)





print("1 :  without spt")
withoutspt()
print('2 - with spt')
withspt()


#2,5,4,2,3,5,7,5,4,8,2


