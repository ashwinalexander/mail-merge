#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
# Get all the names
# Get the starting letter

def read_names():
    with open("Input/Names/invited_names.txt","r") as f:
        all_names = f.read()
        all_names_array = all_names.split("\n")
        return  all_names_array

def get_letter_contents():
    with open("Input/Letters/starting_letter.txt", "r") as f:
        letter = f.read()

        return letter


all_recipients = read_names()
starting_letter = get_letter_contents()

for rec in all_recipients:
    new_letter = starting_letter.replace("[name]",rec)
    with open(f"Output/ReadyToSend/letter_for_{rec}.txt","w") as g:
        g.write(new_letter)

