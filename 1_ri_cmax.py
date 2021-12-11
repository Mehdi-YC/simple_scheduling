
def graph(jobs,title):
    t=0
    shape=0
    l2 = "||"+"__"*sum([j[0] for j in jobs])
    l1="||"
    for j in jobs:
        if t < j[1]:
            l1+=" "*(j[1]-t)
            t+=j[1]-t
        if shape % 2:
            l1 += u"\u25A0"*j[0]
            #l1 += u"\u25A1"*j[0]
        else:
            l1 += u"\u25A1"*j[0]
        shape += 1
        t+=j[0]


    print(f"\n{title} graph : \n")
    print(l1)
    print(l2)
    print("cmax : ",len(l1)-2)



jobs = [[int(x.split("/")[0]),int(x.split("/")[1])] for x in input("entrez vos jobs séparé par , et / eg : 1/2 , 4/5 : ").split(",")]
sorted_jobs = sorted(jobs, key=lambda x: x[1])

print("jobs : ",jobs)
print("sorted jobs : ",sorted_jobs)


graph(jobs,"not sorted")
graph(sorted_jobs,"sorted")
