import logging
import subprocess

logging.basicConfig(filename='logs.log', level=logging.INFO, format=('%(asctime)s - %(levelname)s - %(message)s'))

logger = logging.getLogger()

while(True):
    #test gitignore
    print("Enter a choice: ")
    print("1-make a new file")
    print("2-delete a file")
    print("3-see the current directory")
    print("4-quit")

    choice = int(input())

    if(choice == 1):
        name = input("Enter the name of the file you want to make: ")
        subprocess.run(['touch', name])
        logging.info(f"A new file was made by name: {name}")
    elif(choice == 2):
        try:
            name = input("Enter the name of the file you want to delete: ")
            subprocess.run(['rm', name], check=True)
            logging.warning(f"{name} file was deleted")
        except subprocess.CalledProcessError:
            print("no such file or directory")
            logger.error("no file name was found")
    elif(choice == 3):
       result = subprocess.run(['pwd'],capture_output=True, text=True)
       print(f"The current directory is: {result.stdout}")
       logging.info("Current directory was seen by the user")
    elif(choice == 4):
        print("Goodbye")
        logging.info("The program was quit")
        break
    else:
        print("Invalid input")
        