def graph(machines,jobs,cmax):
    spaces = " "*(len(machines))

    i=0
    for m in machines.values():
        print(spaces+' ||')
        shape = 0
        j = ''
        for job in m:
            if shape % 2:
                j += u"\u25A0"*job[0]
            else:
                j += u"\u25A1"*job[0]
            shape += 1
        i+=1
        print(i,'||'+j)

    print(spaces+' ||'+'_'*(cmax+3))
    underline = spaces+' '+'-'*(cmax+5)
    print(underline)


def withspt():
    m = int(input("machines: "))
    jobs = [(int(x.split("/")[0]),int(x.split("/")[1])) for x in input("entrez vos jobs séparé par , et / eg : 1/2,4/5 : ").split(",")]

    print(jobs)
    machines = {x:[] for x in range(m)}
    jobs = sorted(jobs,key=lambda x: x[0]/x[1])
    print(jobs)
    i = 0
    for job in jobs:
        machines[i%m].append(job)
        i+=1


    print(machines)
    cmax = sum(x[0] for x in machines[0])
    graph(machines,jobs,cmax)
    print("cmax : ",cmax)

    x=1
    cwbar=0
    jp = [p[0] for p in machines[0]]
    jw = [w[1] for w in machines[0]]
    while x < len(jw)+1:
        print(sum(jp[:x]),"x",jw[x-1],"=",sum(jp[:x])*jw[x-1])
        cwbar += sum(jp[:x])*jw[x-1]
        x+=1
    #cwbar=cwbar/ len(jw)
    print("cwbar : ",cwbar)

def withoutspt():
    m = int(input("machines: "))
    jobs = [(int(x.split("/")[0]),int(x.split("/")[1])) for x in input("entrez vos jobs séparé par , et / eg : 1/2,4/5 : ").split(",")]

    machines = {x:[] for x in range(m)}

    i = 0
    for job in jobs:
        machines[i%m].append(job)
        i+=1


    print(machines)
    cmax = sum(x[0] for x in machines[0])
    graph(machines,jobs,cmax)
    print("cmax : ",cmax)

    x=1
    cwbar=0
    jp = [p[0] for p in machines[0]]
    jw = [w[1] for w in machines[0]]
    while x < len(jw)+1:
        print(sum(jp[:x]),"x",jw[x-1],"=",sum(jp[:x])*jw[x-1])
        cwbar += sum(jp[:x])*jw[x-1]
        x+=1
    #cwbar=cwbar/ len(jw)
    print("cwbar : ",cwbar)



print("1 :  without spt")
withoutspt()
print('2 - with spt')
withspt()
#1/2,4/5,8/7,5/4,2/4,2/3,1/2
