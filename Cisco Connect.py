from cisco_backup import nxos
import getpass


if __name__ == "__main__":

    username = input("Username? ")
    myIP = input("Host IP? ")
    password = getpass.getpass("Password? ")
    myInstance = nxos(username, password, myIP, "cisco_xe")
    myInstance.full_backup()

    # print (myInstance.username)
    #myInstance.full_backup()
    
