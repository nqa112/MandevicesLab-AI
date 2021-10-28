print('\t\t\t\tTHE MINION GAME\n\b\t\tKevin makes words starting with vowels.\n\t\tStuart makes words starting with consonants.')

while True:
    s = input('\nEnter a word in UPPERCASE: ')

    if s.isupper() and s.isalpha() and len(s) < 10**6 :
        break
    else:
        print('\nInvalid: Your word must be in uppercase letters [A-Z], no space and smaller than 10^6 characters \n')

s1 = ' '.join(s)        # add space between characters
x = list(s1.lower())    # turn string into array
count_list = []         # create array of vowels counted

for chr in x :
    while chr in 'ueoai' :                              # do while character is vowel
        space = (len(x) + 1 - x.index(chr)) // 2 - 1    # number of spaces from that character to the last character of the string
        count_vowels = int(len(x)-x.index(chr) - space )
        x.remove(chr)                                   # remove that vowel after counting
        count_list.append(count_vowels)                 # add count result into the list

        break
    
Kevin = sum(count_list)

possible_substrings = 0

for i in range(len(s)) :
    possible_substrings = possible_substrings + len(s)-i

Stuart = possible_substrings - Kevin                    # number of consonants

if Kevin > Stuart :
    print ('\n\t\t\t\tKevin', Kevin)
elif Kevin < Stuart :
    print ('\n\t\t\t\tStuart', Stuart)
else :
    print ('\n\t\t\t\tDraw')











