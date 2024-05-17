# You need to install pwinput for this to work (sudo pip install pwinput)
import pwinput
password = pwinput.pwinput(prompt="Please enter a password: ")
print("You entered: ", password)
