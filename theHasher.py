import hashlib
import os

# MD5,SHA1,SHA256,SHA3_256 Hashes!
# Brute Force Attack!
# SR18 --> Intro
print(r"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~         
*             _____   ____     ____     ____                  #
*            /       |    \     /|     /    \                 #
*           |        |     |   / |     \    /                 #
*             \      |    /      |      \__/                  #
*               |    |  /        |     /    \                 #   
*                /   |  \        |     \    /                 #
*          _____/    |    \    __|__    \__/                  #
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
print('\n*********************************************************************')
print('* ShadowRoot18                                                      *')
print('* theHasher                                                         *')
print('* Operation : Create hashes with MD5 || Sha1 || Sha256 || sha3_256. *')
print('* Operation_2 : Save those Hashes in specific files.                *')
print('* Operation_3 : Brute force attack / with the files you created.    *')
print('* Operation_4 : Have fun !                                          *')
print('*********************************************************************\n')


# md5 hash function
def md5(text):
    # the hash in hexadecimal
    md = hashlib.md5(text.encode('utf-8')).hexdigest()
    # return the hash!
    return md


# sha1 hash function
def sha1(text):
    # the hash in hexadecimal
    sha1 = hashlib.sha1(text.encode('utf-8')).hexdigest()
    # return the hash!
    return sha1


# sha256 hash function
def sha256(text):
    # the hash in hexadecimal
    sha256 = hashlib.sha256(text.encode('utf-8')).hexdigest()
    # return the hash!
    return sha256


# sha3_256 hash function
def sha3_256(text):
    # the hash in hexadecimal
    sha3_256 = hashlib.sha3_256(text.encode('utf-8')).hexdigest()
    # return the hash!
    return sha3_256


# theHasher
# Run foreverrr!! Except Exit.
while True:
    print('\n********** theHasher **********\n')
    print('\t  [+] theHasher> 1.md5')
    print('\t  [+] theHasher> 2.sha1')
    print('\t  [+] theHasher> 3.sha256')
    print('\t  [+] theHasher> 4.sha3_256')
    print('\t  [+] theHasher> 5.bfa (Brute force attack)')
    print('\t  [+] theHasher> 6.exit')
    print('\n*******************************\n')
    # input
    option = input('>')
    # md5 area
    if option == 'md5':
        # Text area
        md5_text = input('[+] Insert the Text : ')
        # check md5 if its blank
        if md5_text:
            md5_res = md5(md5_text)
            # Print the Hash
            print(f'[+] Hash : {md5_res}')
            # sizes
            print('[+] Size : 32 hexadecimal digits')
            print('[+] Size : 128 bits in binary')
            # Save area
            md5_save = input('[?] Save the Hash ? [y] = yes  or [any key] = no : ')
            # save the hash
            if md5_save == 'y':
                print('Successfully saved!')
                print('Execution completed!.Back to theHasher')
                # append the hash & the text to the txt file
                with open('md5.txt', 'a') as md5_file:
                    md5_file.write(md5_res)
                    md5_file.write(f' > {md5_text}\n')

            # No saving!
            else:
                print('No saving.Interesting')
                print('Execution completed!.Back to theHasher\n')


        else:
            print('\nText can not be blank\n')

    # sha1 area
    elif option == 'sha1':
        # Text area
        sha1_text = input('[+] Insert the Text : ')
        # check sha1 if its blank
        if sha1_text:
            sha1_res = sha1(sha1_text)
            # Print the Hash
            print(f'[+] Hash : {sha1_res}')
            # sizes
            print('[+] Size : 40 hexadecimal digits')
            print('[+] Size : 160 bits in binary')
            # Save area
            sha1_save = input('[?] Save the Hash ? [y] = yes  or [any key] = no : ')
            # save the hash
            if sha1_save == 'y':
                print('Successfully saved!')
                print('Execution completed!.Back to theHasher')
                # append the hash & the text to the txt file
                with open('sha1.txt', 'a') as sha1_file:
                    sha1_file.write(sha1_res)
                    sha1_file.write(f' > {sha1_text}\n')

            # No saving!
            else:
                print('No saving.Interesting')
                print('Execution completed!.Back to theHasher\n')


        else:
            print('\nText can not be blank\n')

    # sha256 area (Recommended very powerful hash value!)
    elif option == 'sha256':
        # Text area
        sha256_text = input('[+] Insert the Text : ')
        # check sha1 if its blank
        if sha256_text:
            sha256_res = sha256(sha256_text)
            # Print the Hash
            print(f'[+] Hash : {sha256_res}')
            # sizes
            print('[+] Size : 64 hexadecimal digits')
            print('[+] Size : 256 bits in binary')
            # Save area
            sha256_save = input('[?] Save the Hash ? [y] = yes  or [any key] = no : ')
            # save the hash
            if sha256_save == 'y':
                print('Successfully saved!')
                print('Execution completed!.Back to theHasher')
                # append the hash & the text to the txt file
                with open('sha256.txt', 'a') as sha256_file:
                    sha256_file.write(sha256_res)
                    sha256_file.write(f' > {sha256_text}\n')

            # No saving!
            else:
                print('No saving.Interesting')
                print('Execution completed!.Back to theHasher\n')


        else:
            print('\nText can not be blank\n')
    # sha3_256 area
    elif option == 'sha3_256':
        # Text area
        sha3_256_text = input('[+] Insert the Text : ')
        # check sha1 if its blank
        if sha3_256_text:
            sha3_256_res = sha3_256(sha3_256_text)
            # Print the Hash
            print(f'[+] Hash : {sha3_256_res}')
            # sizes
            print('[+] Size : 64 hexadecimal digits')
            print('[+] Size : 256 bits in binary')
            # Save area
            sha3_256_save = input('[?] Save the Hash ? [y] = yes  or [any key] = no : ')
            # save the hash
            if sha3_256_save == 'y':
                print('Successfully saved!')
                print('Execution completed!.Back to theHasher')
                # append the hash & the text to the txt file
                with open('sha3_256.txt', 'a') as sha3_256_file:
                    sha3_256_file.write(sha3_256_res)
                    sha3_256_file.write(f' > {sha3_256_text}\n')

            # No saving!
            else:
                print('No saving.Interesting')
                print('Execution completed!.Back to theHasher\n')


        else:
            print('\nText can not be blank\n')
    # Brute force attack area
    # same comments for all the choices , because we use the same technique!
    elif option == 'bfa':
        while True:
            # choose function
            hash_res = input('[+] Insert the Cryptographic hash function : ')
            # md5 area for bfa
            if hash_res == 'md5':
                # insert the hash value
                md5_output = input('[+] Insert the Hash : ')
                with open('md5.txt', 'r') as md5_file2:
                    m = md5_file2.readlines()
                # Directory used
                md5_dict = {}
                empty = os.stat('md5.txt').st_size == 0
                # check if the file is empty. And if it is inform the user
                if not empty:
                    for line in m:
                        value = line.split(' ', 1)[0]
                        key = (line.split(' ', 2)[2])
                        md5_dict[key] = value
                    # brute force attack
                    for k, v in md5_dict.items():
                        if md5_output == v:
                            print("\nA match successfully Found..")
                            print(f'Hash value: [{md5_output}]')
                            print(f'Text: {k}\n')

                else:
                    print('\nThe file is empty make sure you have at least one saved hash!\n')
                # escape the loop
                break
            # sha1 area for bfa
            elif hash_res == 'sha1':
                sha1_output = input('[+] Insert the Hash : ')
                with open('sha1.txt', 'r') as sha1_file2:
                    m = sha1_file2.readlines()
                sha1_dict = {}
                empty = os.stat('sha1.txt').st_size == 0
                if not empty:
                    for line in m:
                        value = line.split(' ', 1)[0]
                        key = (line.split(' ', 2)[2])
                        sha1_dict[key] = value
                    for k, v in sha1_dict.items():
                        if sha1_output == v:
                            print("\nA match successfully Found..")
                            print(f'Hash value: [{sha1_output}]')
                            print(f'Text: {k}\n')

                else:
                    print('\nThe file is empty make sure you have at least one saved hash!\n')
                break
            # sha256 area for bfa
            elif hash_res == 'sha256':
                sha256_output = input('[+] Insert the Hash : ')
                with open('sha256.txt', 'r') as sha256_file2:
                    m = sha256_file2.readlines()
                sha256_dict = {}
                empty = os.stat('sha256.txt').st_size == 0
                if not empty:
                    for line in m:
                        value = line.split(' ', 1)[0]
                        key = (line.split(' ', 2)[2])
                        sha256_dict[key] = value
                    for k, v in sha256_dict.items():
                        if sha256_output == v:
                            print("\nA match successfully Found..")
                            print(f'Hash value: [{sha256_output}]')
                            print(f'Text: {k}\n')

                else:
                    print('\nThe file is empty make sure you have at least one saved hash!\n')
                break
            # sha3_256 area for bfa
            elif hash_res == 'sha3_256':
                sha3_256_output = input('[+] Insert the Hash : ')
                with open('sha3_256.txt', 'r') as sha3_256_file2:
                    m = sha3_256_file2.readlines()
                sha3_256_dict = {}
                empty = os.stat('sha3_256_file2').st_size == 0
                if empty:
                    print('empty')
                if not empty:
                    for line in m:
                        value = line.split(' ', 1)[0]
                        key = line.split(' ', 2)[2]
                        sha3_256_dict[key] = value
                    for k, v in sha3_256_dict.items():
                        if sha3_256_output == v:
                            print("\nA match successfully Found..")
                            print(f'Hash value: [{sha3_256_output}]')
                            print(f'Text: {k}\n')

                else:
                    print('\nThe file is empty make sure you have at least one saved hash!\n')
                break
            else:
                print('\nException Error')
                print('Valid values : md5,sha1,sha256,sha3_256\n')


    # Just exit
    elif option == 'exit':
        print('Exiting..')
        break
    # Valid values
    else:
        print('\nException Error')
        print('Valid values : md5,sha1,sha256,sha3_256,bfa,exit\n')
