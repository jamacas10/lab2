#Lab2(Option-B)
#Jebel Macias
#Last date modified 10/18/2018

#Node class
#Each node object conatins, a password, count,
#and a pointer(next). The object class contains
#multiple functions, getters, and setters.
import time
class Node(object):
    password = ""
    count = 0
    next = None
    def _init_(self, password, count, next):
        self.password = password
        self.count = count
        self.next = next
    #Getters
    def getPassword(self):
        return self.password
    def getCount(self):
        return self.count
    def getNext(self):
        return self.next
    #Setters
    def setPassword(self,password):
        self.password = password
    def setCount(self, count):
        self.count = count
    def setNext(self,next):
        self.next = next

#Linked List class
#Each node in this object class, contains a root,
#tail, and size. Furthermore, the class contains
#four functions, printList(), bubbleSort(), add(),
#and find().
class linkedList(object):
    root = None
    tail = None

    def _init_(self, root, tail):
        self.root = root
        self.tail = tail
    #The function print list, takes 2 parameters,
    #self, and iterate. Self is a reference to the
    #list, and iterate is used to determine how many
    #of the most used passwords will be displayedself.
    #This function does not return anything, as it is
    #simply printing a specific node.
    def printList(self, counter):
        temp = self.root
        i = 0#How many of the most used passwords will be displayed
        print("Count" + " " + "Password")
        while temp and i<counter and temp!=None:
            print(str(temp.getCount()) + "     " + str(temp.getPassword()))
            temp = temp.getNext()
            i+=1

    #The function bubbleSort, takes 1 parameter, self.
    #This method sorts any linked list using the bubble
    #sort method. This function has no return, as it
    #is only sorting any given list. The functions
    #run is O(n^2)
    def bubbleSort(self):
        passAgain = True
        try:
            while passAgain:
                passAgain = False#Will not pass again, if any node is not moved
                current = self.root
                next = current.getNext()
                while next!=None:
                    if current.getCount() < next.getCount():
                        tempCount = current.getCount()
                        tempPassword = current.getPassword()
                        current.setCount(next.getCount())
                        current.setPassword(next.getPassword())
                        next.setCount(tempCount)
                        next.setPassword(tempPassword)
                        passAgain = True#If a node was moved, check if node needs to move again by making another pass
                    current = current.getNext()
                    next = next.getNext()
        except AttributeError as e:
            print("The linked list that called bubble sort is empty, please check the file.")
            return

    #The function add, takes 2 parameters, self, and
    #newNode. Newnode is the object that will be added
    #to the end of the linked list. This function sets
    #the tail of any given list to the newnode.
    def add(self,newNode):
        if self.root == None:
            self.root = newNode
        if self.tail != None:
            self.tail.setNext(newNode)
        self.tail = newNode

    #The function find, takes 2 parameters, self, and
    #password. Password is used to check against each password
    #of each node in the linked list. If the password already
    #exist in a node in the linkedlist, a new node will not be
    #created. The functions run is O(n).
    def find(self, password):
        temp = self.root
        while temp:
            if temp.getPassword() == password:#If password is already in the list, increase the node by 1.
                temp.setCount(temp.getCount()+1)
                return False
            temp = temp.getNext()
        return True

#The fucntion findInDict, takes 2 parameters, dictionary, and
#password. Dictionary holds a list of nodes, with keys, and this
#fucntion will check if password is in exisitng key in the
#dictionary. The functions runtime is O(1)
def findInDict(dictionary, password):
    if password in dictionary:
        dictionary[password].setCount(dictionary[password].getCount()+1)
        return False
    return True

#The function readFromFile,takes 2 parameters, fileName, and searchUsingDict.
#This function takes any given file(assuming the file is formatted as expected)
#and creates a linked list of nodes,in which each new node is created with
#a password from the file, and count is set to 1.
def readFromFile(fileName, searchUsingDict, numberOfUsers):
    numberOfNodes = 1
    head = Node()
    ll = linkedList()
    dict = {}
    try:
        with open(fileName, 'r') as file:
            for line in file:
                if numberOfNodes == numberOfUsers:#How many passwords to look through
                    return ll
                if numberOfNodes == 1:#If its the first pass, create the head
                    head.setPassword(line.split()[1])
                    head.setCount(1)
                    ll.add(head)
                    dict[line.split()[1]] = head
                else:#Begin adding new nodes to the linked list
                    password = ""
                    bool = False
                    if len(line.split()) > 1:#In the instance of users without a password
                        password = line.split()[1]
                    bool = findInDict(dict, password) if searchUsingDict == True else ll.find(password)#Find any exisiting passwords, using a dictionary or iterate through list
                    if bool:
                        newNode = Node()
                        newNode.setPassword(password)
                        newNode.setCount(1)
                        ll.add(newNode)
                        dict[password] = newNode
                numberOfNodes +=1
    except Exception as e:
        print("Failed to load file " + fileName + " in method readFromFile.")
        return None
    return ll

def main():
    tryAgain = True
    while tryAgain:
        fileName = input("What is the name of the file, containing the list of password?\n")

        maxNumberOfUsers = input("How many user passwords would you like to check in the file?\n")
        while not maxNumberOfUsers.isdigit() or int(maxNumberOfUsers) < 1:#Used to check if user input is a number
            maxNumberOfUsers = input("Please enter a positive integer")

        maxNumberOfDisplayedPassword = input("How many of the most used passwords would you like to see displayed?\n")
        while not maxNumberOfDisplayedPassword.isdigit() or int(maxNumberOfDisplayedPassword) < 1:#Used to check if user input is a number
            maxNumberOfDisplayedPassword = input("Please enter a positive integer")

        searchUsingDict = True if input("Search for duplicates in the linked list using a dictionary? Type Yes or No\n").lower() == "yes" else False

        ll = readFromFile(fileName, searchUsingDict, int(maxNumberOfUsers))
        if ll != None:
            ll.bubbleSort()
            ll.printList(int(maxNumberOfDisplayedPassword))
        else:
            print("Unable to print list and perform bubbleSort on the linked list.")
        tryAgain = True if input("Would you try using the program again? Type Yes or No\n").lower() == "yes" else False

main()
