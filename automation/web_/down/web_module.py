import webbrowser
import sys


def dothis():
    # open browser 
    # if (webbrowser.open("https://www.msn.com")):
    #     print("web open")
    
    # run file with arguments
    # for i in sys.argv:
    #     print(i, end=" ")
    #     print(type(i))

    # python web_module.py l1 l2 l3 
    print(f"file name : {sys.argv[0]}")
    print(f"all args : {sys.argv[1:]}")
    


if __name__ == "__main__":
    dothis()
