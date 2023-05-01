def find_acronym():
    look_up = input('What software acronym would you like to took up?\n')

    found = False
    try:
        with open('acronyms.txt') as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print('File not found')
        return

    if not found:
        print('This acronym does not exists')

def add_acronym():
    acronym = input('What acronym do you want to add?\n')
    definition = input('What is the definition?\n')
    try:
        with open('acronyms.txt') as file:
            found = False
            for line in file:
                    if acronym in line:
                        print(f'Acronym {acronym} already exists')
                        found = True
                        break
            if not found:
                with open('acronyms.txt', 'a') as filewrite:
                    filewrite.write(acronym + ' - ' + definition + '\n')
    except FileNotFoundError as e:
        print('File not found')
        return

def main():
    choice = input('Do you want to find(F) or add(A) an acronym?\n')
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()

main()