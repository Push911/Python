x = input("Enter: ")


def roman_to_int(s):
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    toInt = 0
    for i in range(len(s)):
        if i > 0 and rom[s[i]] > rom[s[i - 1]]:
            toInt += rom[s[i]] - 2 * rom[s[i - 1]]
        else:
            toInt += rom[s[i]]
    print(toInt)


roman_to_int(x)
