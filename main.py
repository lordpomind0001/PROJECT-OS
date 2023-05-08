import os
import shutil

def run():
    os.system("python Os/Os.py")
run()
print("<Os Terminal>")
def ter():
    t = input("")
    if t == "fix basic":
        print("Fixing os")
        shutil.rmtree("Os/Data")
        print("Fixed")
        ter()
    elif t == "fix hard":
        n = input("are you sure that will reinstall everything.")
        if n == "y":
            pass
        if n == "n":
            print("Cancelled")
            ter()
        os.system("git clone https://github.com/lordpomind0001/PROJECT-OS")
        shutil.copyfile("PROJECT-OS/main.py", "Os/main.py")
        shutil.rmtree("PROJECT-OS")
        print("Done")
        ter()
    if t == "run":
        try:
            run()
            ter()
        except:
            print("failed")
            ter()
    else:
        print("Unknown command")
        ter()
ter()
