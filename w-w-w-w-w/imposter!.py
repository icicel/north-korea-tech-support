import math
alldigits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_!\"#$%&'()*+/:;<=>?@[\]^`{|}~´¤£€¨§ "
# digits for every base. digitdict is for special digits. idk this code is old
digitdict = {
    12: "0123456789XE",
    26: "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    27: "ABCDEFGHIJKLMNOPQRSTUVWXYZ_",
    29: "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ",
    52: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
    58: "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖabcdefghijklmnopqrstuvwxyzåäö"
}
print("Currently supported bases: 2-" + str(len(alldigits)) + "\nUse periods as decimal points\n")
while True:
    base = int(input("Convert from base: "))
    number = input("Input number to convert: ").replace(",", ".")
    if "." not in number:
        number += "."
    tobase = int(input("Convert to base: "))
    # generate digit lists
    if base in digitdict:
        digits = digitdict[base]
    else:
        digits = alldigits[:base]
    if "a" not in digits:
        number = number.upper()
    if tobase in digitdict:
        todigits = digitdict[tobase]
    else:
        todigits = alldigits[:tobase]
    # convert number to base 10
    maxp = len(number.split(".")[0]) - 1 # maximum/minimum power (digit) of input number
    minp = -len(number.split(".")[1])
    base10 = 0
    for (digit, power) in zip(number.replace(".", ""), reversed(range(minp, maxp + 1))):
        base10 += digits.index(digit) * base ** int(power)
    # convert base 10 to result
    power = math.floor(math.log(base10) / math.log(tobase))
    result = ""
    negative = False
    while base10 != 0:
        result += todigits[int(base10 // (tobase ** power))]
        base10 %= (tobase ** power) # not often you see %=
        if power == 0:
            result += "."
        if power <= -150: # avoid infinite fractions
            result += "...."
            break
        power -= 1
    if result[-1] == ".":
        result = result[:-1]
    # N = D * (N // D) + (N % D)
    # 13 = 3 * 4 + 1
    input(result + "\nPress enter to go again\n")