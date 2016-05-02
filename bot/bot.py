import os
import aiml
import fbchat
import random

kernel = aiml.Kernel()

print ("Choose a brain file:")
print ("[1] Standard")
print ("[2] Project")
print ("[3] Both")
print ("[4] None\n")

invalidSelection = True
path = "notafile.brn"

while invalidSelection:
    
    print("Please select a number between 1 and 4")
    
    inp = input(": ")
    
    if inp == "1":
        path = "brains\\_standard.brn"
        
        if os.path.isfile(path):
            kernel.bootstrap(brainFile = path)
        else:
            kernel.bootstrap(learnFiles = "std-standard.xml", commands = "load aiml b")
            kernel.saveBrain(path)

        invalidSelection = False
    
    elif inp == "2":
        path = "brains\\_project.brn"
        
        if os.path.isfile(path):
            kernel.bootstrap(brainFile = path)
        else:
            kernel.bootstrap(learnFiles = "std-project.xml", commands = "load aiml b")
            kernel.saveBrain(path)

        invalidSelection = False
    
    elif inp == "3":
        path = "brains\\_both.brn"
        
        if os.path.isfile(path):
            kernel.bootstrap(brainFile = path)
        else:
            kernel.bootstrap(learnFiles = "std-project.xml", commands = "load aiml b")
            kernel.bootstrap(learnFiles = "std-standard.xml", commands = "load aiml b")
            kernel.saveBrain(path) 
        
        invalidSelection = False

    elif inp == "4":
        print ("No brain loaded")
        invalidSelection = False

    elif inp == "5":
        print(";)")
        kernel.bootstrap(learnFiles = "std-project.xml", commands = "load aiml b")
        
        invalidSelection = False


class Commands:

    def __init__(self, path):
        self.path = path
        
    def command_ping(self):
        # Tests responsiveness
        print("ping")
    
    def command_quit(self):
        # Quits the bot
        exit(0)
        
    def command_learntest(self):
        # Loads the aiml files for the project folder
        kernel.bootstrap(learnFiles = "std-project.xml", commands = "load aiml b")
        
    def command_learnstandard(self):
        # Loads the aiml files for the standard folder
        kernel.bootstrap(learnFiles = "std-standard.xml", commands = "load aiml b")
            
    def command_save(self):
        # Saves the currently loaded aiml files to the brain file
        # assuming one was selected at the beginning)
        # if not then you are asked to name the new brain file
        
        if os.path.isfile(self.path): 
            kernel.saveBrain(self.path)
        else:
            print("Name new brain file")
            inp = input(": ")
            self.path = "brains\\%s.brn" % inp
            kernel.saveBrain(self.path)
            
            
    def command_tlr(self):
        # Test location responses
        
        inp = ""
        for question in questionList:
            print(question)
            print(kernel.respond(question))
            print()
                                      
    def command_(self):
        bot_response = kernel.respond(message)

c = Commands(path)

api = fbchat.Client("13393724@students.lincoln.ac.uk", "group9")

while True:
    metadata = api.listen()

    if metadata != None :
        if 'message' in metadata:
            mid     = metadata['message']['mid']
            message = metadata['message']['body']
            fbid    = metadata['message']['sender_fbid']
            name    = metadata['message']['sender_name']
            
            if 'thread_fbid' in metadata['message']:
                tid = metadata['message']['thread_fbid']
            else:
                tid = None
                
        elif 'delta' in metadata and 'messageMetadata' in metadata['delta']:
            mid     = metadata['delta']['messageMetadata']['messageId']
            message = metadata['delta']['body']
            fbid    = metadata['delta']['messageMetadata']['threadKey']['threadFbId']
            tid     = fbid
            name    = metadata['delta']['messageMetadata']['actorFbId']

        else:
            mid     = None
            message = None
            fbid    = None
            tid     = None
            name    = None
            
        print (mid)
        print (message)
        print (fbid)
        print (name)
        print (metadata)            

        if tid != None:
            try:
                command = getattr(c, "command_" + message)()
                response = ""
            except:
                response = kernel.respond(message)
                
            if response != "" and tid == "963983477056732":
                print (response)
                api.send(tid, response)
            elif tid != "963983477056732":
                print("tid != '963983477056732'")
    
        else:
            print("tid == None")
    


