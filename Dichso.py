def so(a):
    match a:
        case "1": return "one "
        case "2": return "two "
        case "3": return "three "
        case "4": return "four "
        case "5": return "five "
        case "6": return "six "
        case "7": return "seven "
        case "8": return "eight "
        case "9": return "nine "
        case "0": return " "

def tram(a):
    return so(a).capitalize() + "hundred "

def chuc(a):
    match a:
        case "1":
            match n[2]:
                case "1": return "eleven "
                case "2": return "twelve "
                case "3": return "thirteen"
                case "4": return "fourteen"
                case "5": return "fifteen"
                case "6": return "sixteen"
                case "7": return "seventeen"
                case "8": return "eighteen"
                case "9": return "nineteen"
                case "0": return "and ten"
        case "2": return "twenty "
        case "3": return "thirty "
        case "4": return "forty "
        case "5": return "fifty "
        case "6": return "sixty "
        case "7": return "seventy "
        case "8": return "eighty "
        case "9": return "ninety "

n = list(input("n= "))
if n[2] == "1":
    print(tram(n[0]) + chuc(n[1]))
else:
    print(tram(n[0]) + chuc(n[1]) + so(n[2]))

