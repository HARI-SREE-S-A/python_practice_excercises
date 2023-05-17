import string
def name():

    lisst = string.ascii_lowercase[::1]
    for n in lisst:
        with open(str(n),'w') as file:
            file.write(n)
            file.close()



name()
