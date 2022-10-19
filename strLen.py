#!/usrbin/python3

def lenght(str):
    """Function that counts length of char / iterables
    """
    count = 0
    #inp = input("Enter a string: ")
    for char in str:
        count += 1
    return count
    #print(f"{inp} is {count} chars")
