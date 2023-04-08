def leetspeak(msg):
    ledger = {
        "a": "4",
        "e": "3",
        "i": "1",
        "k": "|<",
        "l": "7",
        "o": "0",
        "p": "?",
        "s": "$",
        "t": "7"
    }
    output = ""
    for c in msg:
        output += ledger.get(c, c)
    return output

print("---------LEETSPEAK Translator---------")
target = input("Type in a lowercase sentence: ")

print(leetspeak(target))