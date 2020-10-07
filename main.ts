let numbersArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
let operations = ["+", "-", "x", "/", "="]
let numberLoop = 0
let numbreChoice : any = null
let symbolLoop = 99
let symbolChoice : any = null
let currentActivity = 0
let currentSum = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    
    
    
    
    
    currentActivity = 0
    symbolLoop = 99
    if (numberLoop < numbersArray.length - 1) {
        numberLoop = numberLoop + 1
    } else {
        numberLoop = 0
    }
    
    basic.showString("" + numbersArray[numberLoop])
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    
    
    numberLoop = 99
    currentActivity = 1
    if (symbolLoop < operations.length - 1) {
        symbolLoop = symbolLoop + 1
    } else {
        symbolLoop = 0
    }
    
    basic.showString("" + operations[symbolLoop])
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    
    
    
    
    
    numberLoop = 0
    numbreChoice = 0
    symbolLoop = 0
    symbolChoice = 0
    currentActivity = 0
    currentSum = 0
    basic.showString("Start")
})
//      basic.show_string("" + currentSum)
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    
    
    
    
    //  basic.show_string("" + currentSum)
    if (currentActivity == 0) {
        numbreChoice = numbersArray[numberLoop]
        if (currentSum == 0) {
            currentSum = numbreChoice
        }
        
        if (symbolChoice == "+") {
            //  sum
            currentSum = currentSum + numbreChoice
        }
        
        if (symbolChoice == "-") {
            //  substraction
            currentSum = currentSum - numbreChoice
        }
        
        if (symbolChoice == "x") {
            //  multiplication
            currentSum = currentSum * numbreChoice
        }
        
        if (symbolChoice == "/") {
            //  division
            currentSum = currentSum / numbreChoice
        }
        
    } else {
        //  basic.show_string("Sum: " + currentSum)
        //  basic.show_string("" + currentSum)
        symbolChoice = "" + operations[symbolLoop]
        if (symbolChoice == "=") {
            //  equals
            basic.showString("" + currentSum)
        }
        
    }
    
})
