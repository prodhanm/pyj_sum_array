def sumOfList(li):
    total = 0
    for num in li:
        total += num
    return total

def main():
    start = int(input("Enter the starting number of the range of the list: "))
    n = int(input("Enter the limit of the range of the list: "))
    if n <= start:
        print("The limit must be greater than the starting number. Try again.")
        return
    else:
        list_num = list(range(start, n))
    print("list: ", list_num)
    result = sumOfList(list_num)
    print(f"The sum of the list is {result}")

if __name__ == "__main__":
    main()