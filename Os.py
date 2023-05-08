try:
        def install():
                import os
                try:
                        os.system("pip install colorama")
                except:
                        pass
                try:
                        os.system("pip install time")
                except:
                        pass
                try:
                        os.system("pip install subprocess")
                except:
                        pass
                try:
                        os.system("pip install json")
                except:
                        pass
        def check():
                try:
                        try:
                                import os
                                pass
                        except:
                                setup()
                        for filename in os.listdir("Os/Data"):                      
                                if filename == ("Notes" and "data.json") or ("Notes" and "data.json" and "Pygames"):
                                        security()
                                elif filename != ("Notes" and "data.json"):
                                        setup()
                except:
                        setup()
        def setup():
                try:
                        import subprocess
                except:
                        pass
                subprocess.run("clear")
                y = input(Fore.WHITE + "Hello user. Do you want to start instalation? [y/n] ")
                if y == "y":
                        pass
                elif y == "n":
                        print("Ok.")
                        exit()
                else:
                        exit()
                print("This will take less than 1 minute. Then we let you use our wonderful Os.")
                print("Setup is currently downloading needed packages.")
                import os
                try:
                        from colorama import Fore
                        import subprocess
                        import time
                        import json
                        pass
                except:
                        install()
                        pass
                time.sleep(2)
                print("Setup is currencly creating files that are needed to run os")
                try:
                        os.mkdir("Os/Data")
                except:
                        pass
                time.sleep(2)
                print("Now we will collect some data that are needed.")
                time.sleep(2)
                subprocess.run("clear")
                ho = input("How you wanna use that system Gaming or Normal? ")
                if ho == "Gaming":
                        func = "gaming"
                        print(Fore.YELLOW + "Function set to gaming.")
                        print(Fore.YELLOW + "Installing Pygame...")
                        def ins():
                                os.system("pip install pygame")
                                pass
                        try:
                                import pygame
                                pass
                        except:
                                ins()
                        time.sleep(5)
                        try:
                                os.mkdir("Os/Data/Pygames")
                        except:
                                pass
                        print(Fore.GREEN + "Pygame installed")
                elif ho == "Normal":
                        func = "normal"
                        print(Fore.YELLOW + "Function set to normal.")
                else:
                        print(Fore.RED + "Unknown mode!")
                        exit()
                time.sleep(2)
                subprocess.run("clear")
                print(Fore.WHITE + "Input your user that you want to have.")
                nm = input("")
                nmm = nm
                if nm == "Skip":
                        nmm = "Admin"
                        onoffs = "False"
                        pas = ""
                        pass
                else:             
                        print(Fore.WHITE + "Do you wish to have a password? [y/n]")
                        onoff = input("")
                        if onoff == "y":
                                onoffs = "True"
                                print("Ok then. What password do you wish to have?")
                                pasw = input("")
                                pas = pasw
                                pass
                        elif onoff == "n":
                                onoffs = "False"
                                pas = ""
                                pass
                time.sleep(2)
                subprocess.run("clear")
                print("Just some small finishes.")
                time.sleep(5)
                setup = {"Version": None, "Function": None, "Users": {"Admin": {"Passwordonoff": None, "Password": None}}}
                setup["Users"][f"{nmm}"] = {"Passwordonoff": onoffs, "Password": pas}
                setup["Version"] = "1,0,5"
                setup["Function"] = func        
                with open("Os/Data/data.json", "w") as f:
                        json.dump(setup, f, indent=4)
                subprocess.run("clear")
                print("Almost done!")
                try:
                        os.mkdir("Os/Data/Notes")
                except:
                        pass
                time.sleep(2)
                print("Done!")
                time.sleep(2)
                security()              
        def pch():
                try:
                        from colorama import Fore
                        import json
                except:
                        install()
                        pass
                try:
                        with open("Os/Data/data.json", "r") as f:
                                op = json.load(f)
                        user = input("User?")
                        ops = op["Users"][f"{user}"]["Password"]
                except:
                        print(f"User <{user}> not found")
                        pch()
                ps = input("Put your new password here: ")
                if ps == ops:
                        print(Fore.RED + "This password is already used by you.")
                elif ps is not ops:
                        print(Fore.GREEN + f"New Pass {ps}")
                        pss = op["Users"][f"{user}"]["Password"] = ps
                        with open("Os/Data/data.json", "w") as f:
                                json.dump(pss, f, indent=4)
                        menu1()
        def security():
                try:
                        import json
                        from colorama import Fore
                        import time
                        import subprocess
                except:
                        install()
                        pass
                try:
                        with open("Os/Data/data.json", "r") as f:
                                pasw = json.load(f)
                        try:
                                #us = pasw["Users"]
                                #us1 = pasw["Users": {"Administrator": {"Password": "", "Passwordonoff": "False"}}]
                                #if us == us1:
                                        #startup()
                                #else:
                                        #pass
                                user = input(Fore.WHITE + "User: ")
                                password = pasw["Users"][f"{user}"]["Password"]
                                pasonoff = pasw["Users"][f"{user}"]["Passwordonoff"]
                        except:
                                print(Fore.RED + "Unknown User.")
                                time.sleep(1)
                                subprocess.run("clear")
                                security()
                        if pasonoff == "False":
                                startup()
                        elif pasonoff == "True":
                                for i in range(4):                       
                                        pas = input(Fore.WHITE + "Enter Password. ")
                                        t = 4
                                        if pas == password:
                                                print(Fore.GREEN + "Correct Password!")
                                                print(Fore.GREEN + f"Logged in as {user}")
                                                time.sleep(1)
                                                subprocess.run("clear")
                                                startup()
                                                break
                                        else:
                                                print(Fore.RED + f"Incorrect Password Tries = {t - i - 1}" )
                except:
                        setup()
        def startup():
                try:
                        from colorama import Fore
                        import time
                        import subprocess
                        pass
                except:
                        install()
                        pass
                print(Fore.WHITE + "Starting...")
                time.sleep(2)
                print(Fore.GREEN + "StartUp Completed.")
                time.sleep(2)
                subprocess.run("clear")
                menu1()
        def menu1():
                try:
                        from colorama import Fore
                        import subprocess
                        import os, shutil
                        import time
                        import json
                        pass
                except:
                        install()
                        pass
                menu = input(Fore.WHITE + "")
                if menu == "terminal":
                        exit()
                elif menu == "factoryreset":
                        print("Deleting Data")
                        time.sleep(3)
                        shutil.rmtree("Os/Data")
                        print("Data Deleted")
                        print("Deleting os packages")
                        os.system("pip uninstall colorama")
                        os.system("Y")
                        os.system("pip uninstall pygame")
                        os.system("Y")
                        os.system("pip uninstall json")
                        os.system("Y")
                        os.system("pip uninstall time")
                        os.system("Y")
                        os.system("pip uninstall subprocess")
                        os.system("Y")
                        exit()
                if menu == "play":
                        try:
                                import pygame
                                pass
                        except:
                                os.system("pip install pygame")
                                pass
                        print("music name?")
                        m = input("")
                        music = pygame.mixer.Sound(f"Os/Data/Music/{m}.mp3")
                        print(f"Playing {music}")
                        menu1()
                elif menu == "cal":
                        n = input("")
                        
                if menu == "ver":
                        with open("Os/Data/data.json", "r") as f:
                                vers = json.load(f)
                        version = vers["Version"]
                        print(f"Os version {version}")
                        menu1()
                elif menu == "test":
                        try:
                                with open("Os/Data/data.json", "r") as f:
                                        dir2 = json.load(f)
                        except:
                                print("System detected data lose! Running setup.")
                                check()
                        dir1 = dir2["Function"]
                        if dir1 == "gaming":
                                for filename in os.listdir("Os/Data/Pygames"):
                                        if filename.endswith(".py"):
                                                print(filename)
                                                menu1()
                        elif dir1 == "normal":
                                print("Disabled due to set function!")
                                menu1()
                        else:
                                print("System detected A wrong information! Running setup.")
                                check()
                if menu == "dinfo":
                        print(os.ram.usage)
                elif menu == "passchange":
                        pch()
                        time.sleep(2)
                        subprocess.run("clear")
                        menu1()
                if menu == "note create":
                        nt = input("Put your note: ")
                        if nt is None:
                                print("Note not saved. Cant save empty things!")
                        elif nt is not None:
                                num = input("Note num. (dont put used note number bc it will delete the note) ")
                                try:
                                        with open(f"Os/Data/Notes/Note{num}.json", "w") as f:
                                                json.dump(nt, f)
                                except:
                                        n = input("Uh oh! Looks like ur os is old and needs resetup. Do you want to run setup? [y/n] ")
                                        if n == "y":
                                                print("Running setup...")
                                                time.sleep(2)
                                                setup()
                                        elif n == "n":
                                                print("Ok.")
                                                print("Running menu...")
                                                pass        
                                menu1()
                elif menu == "notes":
                        num = input("Note number? ")
                        try:
                                os.listdir("Os/Data/Notes")
                                try:
                                        with open(f"Os/Data/Notes/Note{num}.json", "r") as f:
                                                nt = json.load(f)
                                        print(nt)
                                except:
                                        print("File not found")
                                        menu1()
                        except:
                                n = input("Uh oh! Looks like ur os is old and needs resetup. Do you want to run setup? [y/n] ")
                                if n == "y":
                                        print("Running setup...")
                                        time.sleep(2)
                                        setup()
                                elif n == "n":
                                        print("Ok.")
                                        print("Running menu...")     
                                        menu1()
                else:
                        print(Fore.RED + "Unknown Command.")
                        menu1()
        check()
except:
        try:
                from colorama import Fore
                import os
                pass
        except:
                os.system("pip install colorama")
                pass
        print(Fore.RED + "THERE IS SOMETHING WRONG WITH YOUR PRODUCT! PLEASE CONTACT SUPPORT TO AVOID DATA LOSE!")
        exit()
