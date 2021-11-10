def count(s):
    con, vow = 0, 0

    for idx, char in enumerate(s):
        if char in "AEIOU":
            vow += len(s) - idx
        else:
            con += len(s) - idx
    
    if con > vow:
        print(f"\nStuart {con}")
    elif con < vow:
        print(f"\nKevin {vow}")
    else:
        print("\nDraw")

    return

if __name__ == '__main__':
    s = input('\nEnter a word in UPPERCASE: ')

    if s.isupper() and s.isalpha() and len(s) < pow(10, 6):
        count(s)
    else:
        print('\nWrong format, type again.\n')