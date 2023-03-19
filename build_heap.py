def build_heap(data):
    swaps = []
    n=len(data)

    for i in range(n//2,-1,-1):
        down(data,i,n,swaps)
    return swaps

def down(data,i,n,swaps):
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
        down(data,min_index,n,swaps)
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

    i_type=input()

    if "I" in i_type:
        n = int(input())
        data=list(map(int, input().split()))

    if "F" in i_type:
        fn=input("Enter the filename")
        with open(f"tests/{fn}") as file:
            n=int(file.readline())
            data=list(map(int, file.readline().split()))
    assert len(data)==n 

    swaps=build_heap(data)
        # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

