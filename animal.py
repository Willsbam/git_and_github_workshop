import sys
def default():
    print("Hellow WOrld!")
def cat():
    print("Meow")

def dog():
    print("Woof")

def main():
    if sys.argv[1]=='cat':
        cat()
    else if sys.argv[1]=="dog"
        dog()
    else:
        default()

if __name__=='__main__":
    main():
