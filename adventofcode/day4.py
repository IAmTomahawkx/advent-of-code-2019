
top = 789857
bot = 240920

def has_adjacent(num):
    s = str(num)
    for index, char in enumerate(s):
        if index == 5:
            continue
        if s[index+1] == char:
            return True
    return False

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
