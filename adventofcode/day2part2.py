
def one_set(altered: list):
    index = 0
    end = len(altered)-1
    while index < end:
        opcode = altered[index]
        if opcode == 99:
            return altered
        current = altered[index:index+4]
        code, apos, bpos, cpos = current
        if code == 99:
            return altered
        elif code == 1:
            altered[cpos] = altered[apos] + altered[bpos]
            index += 4
        elif code == 2:
            altered[cpos] = altered[apos] * altered[bpos]
            index += 4


    return altered

def main(l: list, wanted: int):
    unaltered = l
    noun = 1
    verb = 1
    found = False
    while noun < 99 and not found:
        while verb < 99 and not found:
            tester = unaltered.copy()
            tester[1] = noun
            tester[2] = verb
            put = one_set(tester)
            if put[0] == wanted:
                print(f"found {put[1], put[2]} as {100 * put[1] + put[2]}")
                return put[1], put[2]
            else:
                print(f"nothing found in {put[1], put[2]}")
                verb += 1
        noun += 1
        verb = 1

data = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,9,19,23,2,23,13,27,1,27,9,31,2,31,6,35,1,5,35,39,1,10,39,43,2,43,6,47,1,10,47,51,2,6,51,55,1,5,55,59,1,59,9,63,1,13,63,67,2,6,67,71,1,5,71,75,2,6,75,79,2,79,6,83,1,13,83,87,1,9,87,91,1,9,91,95,1,5,95,99,1,5,99,103,2,13,103,107,1,6,107,111,1,9,111,115,2,6,115,119,1,13,119,123,1,123,6,127,1,127,5,131,2,10,131,135,2,135,10,139,1,13,139,143,1,10,143,147,1,2,147,151,1,6,151,0,99,2,14,0,0]
main(data, 19690720)