def sumOfList(li):
    total = 0
    for num in li:
        total += num
    return total

def main():
    # Example usage
    list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = sumOfList(list_num)
    print(f"The sum of the list is {result}")

if __name__ == "__main__":
    main()