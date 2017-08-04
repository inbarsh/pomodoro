import datetime

counter = 0
choise = 1
tasks=[]
el = "\n"
f = open("C:\Users\inbarsh\Desktop\sikuli\scripts\pomodoro.sikuli/log.txt", "a");
myOptions = ("start", "skip")
        
popup("Welcome! What are your tasks for today?")
while choise == 1:
    temp = inputText("")
    tasks.append(temp)
    choise = popAsk("Do you have more tasks?")
for task in tasks:
    choise = 0
    while choise == 0:
        #popup("Your task is " + task + "\nStart pomodoro!")
        counter = counter + 1
        result = select("Your task is " + str(counter) + "-" + task + "\nStart pomodoro!", options = myOptions)
        now = datetime.datetime.now()
        value = now.strftime("%Y-%m-%d %H:%M")+" "+task
        myString = str(value+el)
        f.write(myString)
        if result == "start":
            sleep(1500)
        else:
            now = datetime.datetime.now()
            value = now.strftime("%Y-%m-%d %H:%M")+" skip"
            myString = str(value+el)
            f.write(myString)
        #popup("Break Time!")
        now = datetime.datetime.now()
        if counter == 4:
            counter = 0
            value = now.strftime("%Y-%m-%d %H:%M")+" Long Break"
            myString = str(value+el)
            f.write(myString)
            result = select("Long Break Time!", options = myOptions)
            if result == "start":
                sleep(1800)
            else:
                value = now.strftime("%Y-%m-%d %H:%M")+" skip"
                myString = str(value+el)
                f.write(myString)            
        else:
            value = now.strftime("%Y-%m-%d %H:%M")+" Break"
            myString = str(value+el)
            f.write(myString)
            result = select("Break Time!", options = myOptions)
            if result == "start":
                sleep(300)
            else:
                value = now.strftime("%Y-%m-%d %H:%M")+" skip"
                myString = str(value+el)
                f.write(myString)
        choise = popAsk("Did you finish "+task+"?")
f.close()    
    
