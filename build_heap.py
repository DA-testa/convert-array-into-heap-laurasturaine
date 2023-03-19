# python3


def build_heap(data):
    n=len(data)
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range(n//2,-1,-1):
        min_index=i 
        l=2*i+1
        r=2*i+2

        if l<n and data[l]<data[min_index]:
            min_index=l 
        if r<n and data[r]<data[min_index]:
            min_index=r 

        if i!=min_index:
            swaps.append((min_index,i))
            data[i],data[min_index]=data[min_index],data[i]
        else:
             break
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)
    assert len(swaps)<=2*n-1
   

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
