def to_camal_case(text):
    """Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
    The first word within the output should be capitalized only if the original word was capitalized 
    (known as Upper Camel Case, also often referred to as Pascal case)."""
    list = [x for x in text]
    print(list)
    if len(list) != 0: 
        for i in range(len(list)):
            print(i)
            if list[i] in ('-', '_'):
                list[i+1] = list[i+1].upper()
    list = ''.join([i for i in list if i not in ('-', '_')])
    return list
print(to_camal_case("the_stealth_warrior"))