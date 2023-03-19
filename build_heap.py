def build_heap(data):
    n=len(data)
    swaps = []

    for i in range(n//2,-1,-1):
        swaps=s_down(i,data,swaps)
    return swaps

        #min_index=i 
        #l=2*i+1
        #r=2*i+2

def s_down(i,data,swaps):
    n=len(data)
    min_index=i 
    l=2*i+1
    r=2*i+2
    if l<n and data[l]<data[min_index]:
        min_index=l 
    if r<n and data[r]<data[min_index]:
        min_index=r 

    if i!=min_index:
        swaps.append((i,min_index))
        data[i],data[min_index]=data[min_index],data[i]
        swaps=s_down(min_index,data,swaps)
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
    return swaps


def main():

    # input from keyboard
    #n = int(input().strip())
    #data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    sort_type=input()


    if "I" in sort_type:
        n = int(input())
        u_data=input()
        data=list(map(int, u_data.split(" ")))
        assert len(data)==n 

    elif "F" in sort_type:
        fl=input()
        if "a" in fl:
            return
        with open(f"./test/{fl}",mode="r") as fl:
            n=int(fl.readline())
            data=list(map(int, fl.readline().split(" ")))
        assert len(data)==n 

    else:
        return

    saraksts=[[]for i in range(n)]
    for i in range(n):
        if data[i]<n:
            saraksts[data[i]].append(i)
    swaps=build_heap(data)
        # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)



if __name__ == "__main__":
    main()

