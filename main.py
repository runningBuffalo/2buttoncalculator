numbersArray:List[int] = [0,1,2,3,4,5,6,7,8,9]
operations:List[str] = ["+", "-", "x", "/", "="]
numberLoop:int = 0
numbreChoice:any = None
symbolLoop:int = 99
symbolChoice:any = None

currentActivity:int = 0
currentSum:number = 0

def on_button_pressed_b():
    global symbolLoop
    global currentActivity
    global numberLoop

    numberLoop = 99
    currentActivity = 1

    if symbolLoop < len(operations) - 1:
        symbolLoop = symbolLoop + 1
    else:
        symbolLoop = 0
        
    basic.show_string("" + operations[symbolLoop])

def on_button_pressed_a():
    global numberLoop
    global numbreChoice
    global symbolLoop
    global symbolChoice
    global currentActivity
    global currentSum

    currentActivity = 0
    symbolLoop = 99

    if numberLoop < len(numbersArray) - 1:
        numberLoop = numberLoop + 1
    else:
        numberLoop = 0
    
    basic.show_string("" + numbersArray[numberLoop])
    
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global numberLoop
    global numbreChoice
    global symbolLoop
    global symbolChoice
    global currentActivity
    global currentSum
    
    numberLoop = 0
    numbreChoice = 0
    symbolLoop = 0
    symbolChoice = 0
    currentActivity = 0
    currentSum = 0

    basic.show_string("Start")

input.on_gesture(Gesture.Shake, on_gesture_shake)

def on_button_pressed_ab():
    global currentSum
    global currentActivity
    global numbreChoice
    global symbolChoice
    global symbolLoop

    # basic.show_string("" + currentSum)
    if currentActivity == 0:
        numbreChoice = numbersArray[numberLoop]
        
        if(currentSum == 0):
            currentSum = numbreChoice
        
        if symbolChoice == "+": # sum
            currentSum = currentSum + numbreChoice
        if symbolChoice == "-": # substraction
            currentSum = currentSum - numbreChoice
        if symbolChoice == "x": # multiplication
            currentSum = currentSum * numbreChoice
        if symbolChoice == "/": # division
            currentSum = currentSum / numbreChoice
        # basic.show_string("Sum: " + currentSum)
    else:
        # basic.show_string("" + currentSum)
        symbolChoice = "" + operations[symbolLoop]
        if symbolChoice == "=": # equals
            basic.show_string("" + currentSum)
        
    #     basic.show_string("" + currentSum)
    

input.on_button_pressed(Button.AB, on_button_pressed_ab)
