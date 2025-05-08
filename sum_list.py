def sumOfList(li):
    total = 0
    for num in li:
        total += num
    return total

def main():
    list_num = []
    while True:
        num = int(input("Enter an element (-1 to stop): "))
        if num == -1:
            break
        else:
            list_num.append(num)
    
    result = sumOfList(list_num)
    print(f"The sum of the list is {result}")

if __name__ == "__main__":
    main()