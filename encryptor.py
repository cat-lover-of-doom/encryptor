# encryptor project by sebastian wist 19/02/22

# importing necesary modules
import os
import time
import json
import sys
import random

version = 1.0
typing_speed = 50
seleccion1 = 0
message = ''
key = ''
os.system('cls')

ball = ['frame.txt', 'frame2.txt', 'frame3.txt', 'frame4.txt',
        'frame5.txt', 'frame6.txt', 'frame7.txt', 'frame8.txt', 'frame9.txt']
menu1 = ('     [1]. Encryption' + '\n' + '     [2]. Decryption' + '\n')
menu2 = ('     [1]. Binarization' + '\n' + '     [2]. Rotation' +
         '\n' + '     [3]. Dictionary' + '\n' + '     [4]. XOR' + '\n')
# dictionaries used for dictionary encryption
sub_nochange = {
    'a': 'a', 'b': 'b', 'c': 'c',
    'd': 'd', 'e': 'e', 'f': 'f',
    'g': 'g', 'h': 'h', 'i': 'i',
    'j': 'j', 'k': 'k', 'l': 'l',
    'm': 'm', 'n': 'n', 'o': 'o',
    'p': 'p', 'q': 'q', 'r': 'r',
    's': 's', 't': 't', 'u': 'u',
    'v': 'v', 'w': 'w', 'x': 'x',
    'y': 'y', 'z': 'z',
    ' ': ' ', ',': ',', '.': '.',
    '"': '"',  "'": "'", '-': '-',
    '?': '?', '!': '!', ';': ';',
    ':': ':', '(': '(', ')': ')',
    '’': '’', '—': '—', '“': '“',
    '”': '”', '%': '%',
    '0': '0', '1': '1', '2': '2',
    '3': '3', '4': '4', '5': '5',
    '6': '6', '7': '7', '8': '8',
    '9': '9',


}
sub_emoji = {
    'a': '😂', 'b': '😅', 'c': '😉',
    'd': '😍', 'e': '😏', 'f': '😋',
    'g': '😒', 'h': '😖', 'i': '😔',
    'j': '😜', 'k': '😡', 'l': '😤',
    'm': '😨', 'n': '😩', 'o': '😪',
    'p': '😭', 'q': '😱', 'r': '😵',
    's': '☝', 't': '⚡', 'u': '⚠',
    'v': '♠', 'w': '♥', 'x': '♦',
    'y': '♣', 'z': '🚽',
    ' ': ' ', ',': ',', '.': '.',
    '"': '"',  "'": "'", '-': '-',
    '?': '?', '!': '!', ';': ';',
    ':': ':', '(': '(', ')': ')',
    '’': '’', '—': '—', '“': '“',
    '”': '”', '%': '%',
    '0': '0', '1': '1', '2': '2',
    '3': '3', '4': '4', '5': '5',
    '6': '6', '7': '7', '8': '8',
    '9': '9',
}


# encryption proceses
def binarization(message):
    # defines the string as blanck to build on top of it
    encrypted = ''
    # for loop to apply the procces to every leter
    for letter in message:
        # checks if the letter is a space
        if letter == ' ':
            letter = ord(letter)
            letter = bin(letter)
            x = letter.replace('0b', '|')
            encrypted = encrypted + x + ' '
        else:
          # conversion to binary an printing the text
            letter = ord(letter)
            letter = bin(letter)
            x = letter.replace('0b', '|')
        encrypted = encrypted + x
    print('(' + message + ')' ' encrypted in binary: ')
    print(encrypted)


def debinarization(message):
    encrypted = ''
    message = message.replace('|', ' 0b')
    word = message.split()
    # it creates a character from the number, in base 2
    for i in range(len(word)):
        text = chr(int(word[i], 2))
        encrypted = encrypted + text
    print(message + ' decrypted from binary: ')
    print(encrypted)


def rotation_cypher(message, key):
    encrypted = ''
    try:
        key = int(key)
    except ValueError:
        key = key
    # checks vor validity of the key
    if isinstance(key, int) == True:
        if key > 26 or key < 0:
            print('invalid key, substituting with 3 \n')
            time.sleep(1)
            key = 3
        for letter in message:
            if letter == ' ':
                new = ' '
            else:
                # rotates and checks validity
                new = ord(letter) + key
                if new > ord('z'):
                    new = new - 26
                elif new < ord('a'):
                    new = new + 26
                new = chr(new)
            encrypted = encrypted + new
            # same procces as above but with a string as a key
    else:
        if len(message) == len(key):
            key = key
        else:
            for i in range(len(message) - len(key)):
                key = key + (key[i % len(key)])
                key = ("" . join(key))

        for i in range(len(message)):
            if message[i] == ' ':
                new = ' '
            else:
                new = ord(message[i]) + ord(key[i])
                new = chr(new)

            encrypted = encrypted + new
    print(message + ' encrypted with a rotation of ' + str(key) + ': ')
    print(encrypted)


def rotation_decypher(message, key):
    encrypted = ''
    try:
        key = int(key)
    except ValueError:
        key = key
    # checks vor validity of the key
    if isinstance(key, int) == True:
        if key > 26 or key < 0:
            print('invalid key, substituting with 3 \n')
            time.sleep(1)
            key = 3
        for letter in message:
            if letter == ' ':
                new = ' '
            else:
                if ord(letter) > ord('z'):
                    letter = letter + 26
                elif ord(letter) < ord('a'):
                    letter = letter - 26

                new = ord(letter) - key

                new = chr(new)

            encrypted = encrypted + new
    else:
        if len(message) == len(key):
            key = key
        else:
            for i in range(len(message) - len(key)):
                key = key + (key[i % len(key)])
                key = ("" . join(key))

        for i in range(len(message)):
            if message[i] == ' ':
                new = ' '
            else:
                new = ord(message[i]) - ord(key[i])
                new = chr(new)

            encrypted = encrypted + new
    print(message + ' decrypted with a rotation of ' + str(key) + ': ')
    print(encrypted)


def alphabet_cypher(message, dic):

    encrypted = ''
    # checks if it needs to open a file
    if dic == 'custom':
        name_of_dic = input('enter dictionary path:')

    for letter in message:

        if dic == 'custom':
            with open(name_of_dic) as g:
                custom_dic = g.read()
                custom_dic = json.loads(custom_dic)
                encrypted = encrypted + custom_dic[letter]
        # replaces the current letter with the one in the dicionary
        else:
            encrypted = encrypted + str(dic[letter])
    print(message + 'encrypted with ' + 'dictionary: ')
    print(encrypted)


def print_all_ord():
    for i in range(65, 110000):

        print(chr(i) + str(i), end='  ')


def XOR_cypher(message, key, baseline):
    encrypted = ''
    try:
        baseline
    except NameError:
        baseline = 65
    else:
        # checks for the baselines to aply the modifier by starting at a certain minimum
        if baseline == '65' or baseline == 'A' or baseline == '0':
            baseline = 65
        if baseline == '200' or baseline == 'default' or baseline == '1' or baseline == '' or baseline == ' ':
            baseline = 200
        elif baseline == '24328' or baseline == 'chinese' or baseline == '2':
            baseline = 24328
        elif baseline == '128512' or baseline == 'emoji' or baseline == '4':
            baseline = 128512
        elif baseline == '1041' or baseline == 'russian' or baseline == '3':
            baseline = 1041
        elif baseline == '127462' or baseline == 'flag' or baseline == '5':
            baseline = 127462

    # it checks if the key is as long as the message
    if len(message) == len(key):
        key = key
    else:
        # if it isnt it cycles it back trough itself
        for i in range(len(message) - len(key)):
            key = key + (key[i % len(key)])
            key = ("" . join(key))
            # replaces for every letter
    key = key.replace(' ', '꥕')
    for i in range(len(message)):
        message = message.replace(' ', '꥕')
        crypt = ord(message[i]) ^ ord(key[i])
        # adds 65 to the value to garantee its not ilegal
        crypt += baseline
        # checks if the value is legal
        if chr(crypt).isprintable() == False:
            encrypted = encrypted + '@' + str(crypt) + '@' + ''
        encrypted = encrypted + chr(crypt) + ''
    # checks fo ilegal characters

    # prints the message and the key and the result
    if len(message) < 50 or len(key) < 50:
        print(message + ' encrypted with ' + key + ' in XOR:', end=' ')
        print(encrypted)
    else:
        print(encrypted)


def XOR_decypher(message, key, baseline):
    encrypted = ''

    try:
        baseline
    except NameError:
        baseline = 200
    else:
        # checks for the baselines to aply the modifier by starting at a certain minimum
        if baseline == '65' or baseline == 'A' or baseline == '0':
            baseline = 65
        if baseline == '200' or baseline == 'default' or baseline == '1' or baseline == '' or baseline == ' ':
            baseline = 200
        elif baseline == '24328' or baseline == 'chinese' or baseline == '2':
            baseline = 24328
        elif baseline == '128512' or baseline == 'emoji' or baseline == '4':
            baseline = 128512
        elif baseline == '1041' or baseline == 'russian' or baseline == '3':
            baseline = 1041
        elif baseline == '127462' or baseline == 'flag' or baseline == '5':
            baseline = 127462

    # it checks if the key is as long as the message
    if len(message) == len(key):
        key = key
    else:
        # if it isnt it cycles it back trough itself
        for i in range(len(message) - len(key)):
            key = key + (key[i % len(key)])
            key = ("" . join(key))
    key = key.replace(' ', '꥕')

    # replaces for every letter
    for i in range(len(message)):
        crypt = (ord(message[i]) - baseline) ^ ord(key[i])
        encrypted = encrypted + chr(crypt) + ''

    # prints the result
    if len(message) < 50 or len(key) < 50:
        print(message + ' encrypted with ' + key + ' in XOR:', end=' ')
        encrypted = encrypted.replace('꥕', ' ')
        print(encrypted)
    else:
        encrypted = encrypted.replace('꥕', ' ')
        print(encrypted)


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


def slow_type(t, endparameter):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('', end=str(endparameter))


def clear(number):
    for i in range(number):
        print('\n')

# main processes


def animation(filename, delay, repeat):
    frames = []
    for name in filename:
        with open(name, "r", encoding='utf8') as f:
            frames.append(f.readlines())
    for i in range(repeat):
        for frame in frames:
            print("".join(frame), end='\r')
            time.sleep(delay)
            os.system('cls')


def intro_text():
    animation(ball, 0.1, 5)
    slow_type('encryptor program version' + ' ' +
              '(' + str(version) + ')', '\r')
    time.sleep(1)
    clear(69)
    main()


def main():
    print(menu1)
    inptu = input('plesase select a procces:')
    if inptu == '1':
        seleccion1 = 1
    elif inptu == '2':
        seleccion1 = 2
    else:
        print('incorrect seleccion')
        clear(30)
        main()
    clear(69)
    print(menu2)
    inptu = input('plesase select a procces:')
    if seleccion1 == 1:
        if inptu == '1':
            clear(69)
            binarization(input('please insert a message:'))
        elif inptu == '2':
            clear(69)
            message = input('please insert a message:')
            key = input(
                'please insert key(rotation amount , can also be a string):')
            rotation_cypher(message, key)
        elif inptu == '3':
            clear(69)
            message = input('please insert a message:')
            dic = input(
                "please insert a dictionary name (you can choose 'sub_emoji' by default or 'custom' for yout own):")
            if dic == 'sub_emoji':
                dic = sub_emoji
            alphabet_cypher(message, dic)
        elif inptu == '4':
            clear(69)
            message = input('please insert a message:')
            key = input("please insert a key (can be a string or a number):")
            bass = input(
                'would you like to change the baseline (1-5) (is not recomended if you dont know what you are doing, its recomended to say NO) \n Y/N:')
            if bass == 'no' or bass == 'NO' or bass == 'n' or bass == 'N' or bass == '':
                basel = 'default'
            else:
                basel = input('please select your custom baseline:')
            XOR_cypher(message, key, basel)
    elif seleccion1 == 2:

        if inptu == '1':
            clear(69)
            debinarization(input('please insert a message:'))
        elif inptu == '2':
            clear(69)
            message = input('please insert a message:')
            key = input(
                'please insert key(rotation amount , can also be a string):')
            rotation_decypher(message, key)
        elif inptu == '3':
            clear(69)
            message = input('please insert a message:')
            dic = input(
                "please insert a dictionary name (you can choose 'sub_emoji' by default or 'custom' for yout own):")
            alphabet_cypher(message, dic)
        elif inptu == '4':
            clear(69)
            message = input('please insert a message:')
            key = input("please insert a key (can be a string or a number):")
            bass = input(
                'would you like to change the baseline (0-5)(is not recomended if you dont know what you are doing, its recomended to say NO) \n Y/N:')
            if bass == 'no' or bass == 'NO' or bass == 'n' or bass == 'N' or bass == '':
                basel = 'default'
            else:
                basel = input('please select your custom baseline:')
            XOR_decypher(message, key, basel)
    time.sleep(3)
    clear(3)
    repeto = input('would you like to do another process? Y/N: ')
    if repeto == 'yes' or repeto == 'YES' or repeto == 'y' or repeto == 'Y':
        main()
    else:
        pass


# dectects IDE pythonw is for IDLE
if 'pythonw.exe' in sys.executable:
    main()
else:
    main()
