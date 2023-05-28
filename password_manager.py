import art
print(art.text2art(text="welcome to password genrator", font="rnd-small"))


storage={} #created empty dictionary which is going to store id as key and password as value
#add function will add new id and password to dictionary
def add(id,password):
    load_from_file()
    storage[id]=password
    save_to_file()
#access function will be used to access password using id as argument
def access(id):
    load_from_file()
    password_found=False
    for key in storage:
        if id==key:
            print(f"your password id {storage[key]}")
            password_found=True
            break
    if not password_found:  #this part of code only run after all id are checked
            print(f"No password found for ID {id}")

#this function will save the added id and password which is in storage dict to a text file 
def save_to_file():
    with open("passwords.txt", "w") as file:
        for id, password in storage.items():
            file.write(f"{id}:{password}\n")
#this function will load the text file which is password.txt
def load_from_file():
    try:
        with open("passwords.txt", "r") as file:
            for line in file:
                id, password = line.strip().split(":")
                storage[id] = password
    except FileNotFoundError:
        pass
def genrate_password():
    from day5 import passwordgenerator
    id=input("Enter the id for which you want to genrate password:")
    password_1=passwordgenerator.stored_password()
    add(id,password_1)
    print(f"Succesfully stored '{password_1}' for '{id}'")

def store_password():
    id=input("Enter the id:") 
    password_1  = input("Enter the password to store:")
    add(id,password_1)
    print(f"Succesfully stored '{password_1}' for '{id}'")

terminate=True
while(terminate==True):
    choose=int(input("Enter 1 to genrater password or 0 to access password:"))
    if choose==1:
        genrate_password()

    elif choose==0:
        id=input("Enter your id:")
        access(id)
    else:
        store_password()    
    terminate=bool(int(input("Enter 0 to terminate Or Enter 1 to access password")))

    
