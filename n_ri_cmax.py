def graph(machines,jobs,cmax):
    spaces = " "*(len(machines))

    i=0
    for m in machines.values():
        print(spaces+'||')
        shape = 0
        j = ''
        for job in m:
            if shape % 2:
                j += u"\u25A0"*job
            else:
                j += u"\u25A1"*job
            shape += 1
        i+=1
        print(i,'  ||'+j)

    print(spaces+'||'+'_'*(cmax+3))
    underline = spaces+'-'*(cmax+5)
    print(underline)



def withspt():
    m = int(input("le nombre de machines : "))
    jobs = [int(x) for x in input("entrez vos jobs séparé par , : ").split(",")]

    machines = {x:[] for x in range(m)}
    jobs.sort()

    i = 0
    for job in jobs:
        machines[i%m].append(job)
        i+=1


    print(machines)
    cmax = max([sum(x) for x in machines.values()])
    graph(machines,jobs,cmax)
    print("cmax : ",cmax)

def withoutspt():
    m = int(input("le nombre de machines : "))
    jobs = [int(x) for x in input("entrez vos jobs séparé par , : ").split(",")]

    machines = {x:[] for x in range(m)}
    i = 0
    for job in jobs:
        machines[i%m].append(job)
        i+=1


    print(machines)
    cmax = max([sum(x) for x in machines.values()])
    graph(machines,jobs,cmax)
    print("cmax : ",cmax)

print("1 :  without spt")
withoutspt()
print('2 - with spt')
withspt()