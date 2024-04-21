import threading

def add(x,y):
    print(x+y)

def sub(x,y):
    print(x-y)

def main():
    a = int(input("enter first num"))
    b = int(input("enter second num"))
    t1 = threading.Thread(target=add, args=(a,b))
    t2 = threading.Thread(target=sub, args=(a,b))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()