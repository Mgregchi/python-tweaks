#!/usr/bin/python3


from strLen import lenght


def conc(iterable, seperator="", *args, **kwargs):
    """# Concatenate iterables.
        If seperator is given, put seperator in-between items.
        e.g: `joined = conc(["Hello", "World"], seperator=", ")`

                `>> Hello, World`
    """
    ind = 0
    result = ""
    iterLength = lenght(iterable)

    """
    for char in iterable:
        result += char + seperator
    """
    while ind != iterLength:
        result += iterable[ind] + \
            seperator if ind != iterLength - 1 else iterable[ind]
        ind += 1
    return result


#print(conc(["Hello", "World"], seperator=", "))
