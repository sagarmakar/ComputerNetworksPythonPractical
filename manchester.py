import matplotlib.pyplot as plt
    

def Manchester(inp):
    inp1=list(inp)
    li,init=[],False
    for i in range(len(inp1)):
        if inp1[i]==0:
            li.append(-1)
            if not init:
                li.append(-1)
                init=True
            li.append(1)
        elif inp1[i]==1 :
            li.append(1)
            li.append(-1)
    return li        
    

def Differential_manchester(inp):
    inp1=list(inp)
    li,lock,pre=[],False,''
    for i in range(len(inp1)):
        if inp1[i]==0 and not lock:
            li.append(-1)
            li.append(-1)
            li.append(1)
            lock=True
            pre='S'
        elif inp1[i]==1 and not lock :
            li.append(1)
            li.append(1)
            li.append(-1)
            lock=True
            pre='Z'
        else:
            if inp1[i]==0:
                if pre=='S':
                    li.append(-1);li.append(1)
                else:
                    li.append(1);li.append(-1)
            else:
                if pre=='Z':
                    pre='S'
                    li.append(-1);li.append(1)
                else:
                    pre='Z'
                    li.append(1);li.append(-1)
                         
    return li

    

def plot(li):
    plt.subplot(3,1,1)
    plt.ylabel("Man")
    plt.plot(Manchester(li),color='violet',drawstyle='steps-pre',marker='>')
    plt.subplot(3,1,3)
    plt.ylabel("Dif_Man")
    plt.plot(Differential_manchester(li),color='red',drawstyle='steps-pre',marker='>')
    plt.show()
                

if __name__=='__main__':
    print("Enter the size of Encoded Data : ")
    size=int(input())
    li=[]
    print('Enter the binary bits sequnce of length ',size,' bits : \n')
    for i in range(size):
        li.append(int(input()))
    plot(li) 