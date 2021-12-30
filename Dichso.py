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
                case "1": return "and eleven"
                case "2": return "and twelve"
                case "3": return "and thirteen"
                case "4": return "and fourteen"
                case "5": return "and fifteen"
                case "6": return "and sixteen"
                case "7": return "and seventeen"
                case "8": return "and eighteen"
                case "9": return "and nineteen"
                case "0": return "and ten"
        case "2": return "twenty "
        case "3": return "thirty "
        case "4": return "forty "
        case "5": return "fifty "
        case "6": return "sixty "
        case "7": return "seventy "
        case "8": return "eighty "
        case "9": return "ninety "

n = list(input("n = "))
if n[1] == "1":
    print(tram(n[0]) + chuc(n[1]))
else:
    print(tram(n[0]) + chuc(n[1]) + so(n[2]))

