top = 789857
bot = 240920

def has_adjacent(num):
    s = str(num)
    found_double = False
    index = 0
    while index < len(s)-1:
        char = s[index]
        if index == 5:
            break
        if s[index+1] == char:
            count = 0
            for ind, c2 in enumerate(s[index+1:]):
                if c2 == char:
                    count += 1
                else:
                    break
            index += count
            if count == 1:
                found_double = True
        index += 1
    return found_double

def check_increase(num):
    s = str(num)
    for index, char in enumerate(s):
        if index == 0:
            continue
        if int(s[index-1]) <= int(char):
            continue
        else:
            return False
    return True

def main():
    cur = bot
    amo = 0
    while cur < top:
        if not has_adjacent(cur):
            cur += 1
            continue
        print(cur)
        if not check_increase(cur):
            cur += 1
            continue
        amo += 1
        cur += 1
    print(amo)

if __name__ == "__main__":
    main()
    #print(has_adjacent(123444))
