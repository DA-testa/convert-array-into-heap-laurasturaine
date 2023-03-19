# python3

import os

def build_heap(data):
    swaps = []
    izm=len(data)
  

    for i in range(izm//2,-1,-1):
        s_down(data,i,swaps)
    return swaps
        #min_index=i 
        #l=2*i+1
        #r=2*i+2

def s_down(data,i,swaps):
    izm=len(data)
    min_index=i 
    left=2*i+1
    right=2*i+2
    if left<izm and data[left]<data[min_index]:
        min_index=left 
    if right<izm and data[right]<data[min_index]:
        min_index=right 

    if i!=min_index:
        swaps.append((i,min_index))
        data[i],data[min_index]=data[min_index],data[i]
        s_down(data,min_index,swaps)
           # while min_index<n//2:
                #l=2*min_index+1
              #  r=2*min_index+2
               # if r<n and data[r]<data[min_index]:
               #     min_index=r 
               # if l<n and data[l]<data[min_index]:
               #     min_index=l 
               # if i!=min_index:
                   # swaps.append((min_index,i))
                  #  data[i], data[min_index]=data[min_index], data[i]
               # else:
                #    break



def main():
    
    # input from keyboard
    #n = int(input().strip())
    #data = list(map(int, input().split()))

    teksts=input()
    if "I" in teksts:
        n = int(input())
        data=list(map(int, input().split()))
        assert len(data)==n 
        swaps=build_heap(data)

        print(len(swaps))
        for i, j in swaps:
            print(i, j)

    elif "F" in teksts:
        fl=input()
        cels='./tests/'
        ma=os.path.join(cels,fl)
        if "a" in fl:
            print("Faila nosaukumā ir kļūda")
            return
        else:
            try:
                with open(ma, mode="r") as fl:
                n=int(fl.readline())
                da=list(map(int, fl.readline().split()))
            except Exception as error:
                print("Error", str(error))

    else:
        print("Ievadiet burtu 'I' vai 'F':")
        return


if __name__ == "__main__":
    main()
