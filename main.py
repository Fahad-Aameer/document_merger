with open("../MailMerge/Input/Names/invited_names.txt") as names:
    list_of_names = names.readlines()
with open("../MailMerge/Input/Letters/starting_letter.txt") as letter:
    read_letter = letter.read()

for i in list_of_names:
    name = i.strip('\n')
    new_letter = read_letter.replace('[name]', name)
    with open(f"../MailMerge/Output/ReadyToSend/Letter for {name}.txt", mode="w") as letter:
        letter.write(new_letter)
