
def selection(prompt: str = "Please select an option", options: list[str] = []) -> int | str:
    """
    Method
    ------
    Allows user to select from a list of elements\n
    This method is blocking

    Parameters
    ---------
    prompt : string
        Question to give to user
    options : string[]
        List of selectable options

    Returns
    -------
    Resulting index then element's value
    """
    
    # Prompt user
    if not prompt:
        print("Please select an option");
    else:
        print(prompt);

    # Display options
    index = 0;
    for option in options:
        index += 1;
        print(f"> ({index}) {option}");

    # Collect input
    while True:
        userInput_ = input(f"Please select an option ({index}): ");

        # Type cast
        userInput = 0;
        try:
            userInput = round(int(userInput_));
        except:
            userInput = None;

        # Continue if userInput is invalid
        if not userInput or userInput == 0 or userInput > index:
            continue;

        # Return value
        return userInput, options[userInput - 1];




def allocations(prompt: str = "Please choose allocations", options: list[str] = [], points: int = 0) -> dict:
    """
    Method
    ------
    Prompts user to distribute points to several options\n
    This function is blocking

    Parameters
    ---------
    prompt  : string
        Question to give to user
    options : string[]
        List of allocatable options
    points  : integer
        Number of points available to spend

    Returns
    -------
    A dictionary with the options as the keys and the allocated points as the value
    """
    
    # Prompt user
    print(prompt);

    # Display options
    for option in options:
        print(f"> {option}");

    # Collect input
    while True:

        available = points;
        returnObject = {};

        for option in options:

            # Check if available points
            if available <= 0:
                print("All points have been allocated");
                break;

            # Display
            userInput_ = input(f"You have {available} points available to spend on {option}: ");

            # Type cast
            userInput = 0;
            try:
                userInput = round(int(userInput_));
            except:
                print("This value was defaulted to 0 as the inputed value was invalid!");
                userInput = 0;

            # Append to object
            returnObject[option] = userInput;

            # Update available
            available -= userInput;
        
        # Saved
        if available > 0:
            print(f"Your remaining {available} points will be saved!");
            returnObject["saved"] = available;

        # Check if all points have been used
        if available < 0:
            print(f"You have exceeded the allocated points by {-available}");
            continue;
        
        # Return value on completion
        return returnObject;




def spend(prompt: str = "Please choose allocations", options: list = [], points: int = 0) -> dict:
    """
    Method
    ------
    Prompts user to distribute points to several options\n
    This function is blocking

    Parameters
    ---------
    prompt  : string
        Question to give to user
    options : list[ string, integer, int ]
        List of allocatable options, with the respective values corresponding to the displayed name, its cost and whether the option can only be bought once (0 = false; 1 = true; -1 = unavailable)
    points  : integer
        Number of points available to spend

    Returns
    -------
    Two values; the first is the remaining number of points; the second is a dictionary with key-value pairs which have the index of the option paired with the given truplet option
    """
    
    # Prompt user
    print(prompt);
    print("Input 0 if you wish to not purchase anything!");

    # Return Object
    returnObject = {};

    # Display options
    index = 0;
    for option in options:
        print(f"> ({index + 1}) {option[0]} : {option[1]}");
        index += 1;
    
    # Track
    available = points;

    # Collect input
    while True:

        # Select option
        userInput = input(f"You have {available}, please input which option you wish to purchase: ");
        userInput_ = -1;
        try:
            userInput_ = round(int(userInput));
        except:
            userInput_ = None;
        
        # Cancelling
        if userInput.strip() and userInput_ != 0 and userInput != "":

            # Error check
            if userInput_ > len(options) or userInput_ < 0:
                print("Invalid input! Either your selected value was not a number or beyond the scope of options!");
                continue;
            
            # Get option
            chosenOption = options[userInput_ - 1];

            # Check Balance
            if available < chosenOption[1]:
                print("Your balance is too low!");
                continue;

            # Check validity
            if chosenOption[2] == -1:
                print("This option is currently unavailable!");
                continue;

            # Update & Append
            available -= chosenOption[1];
            if chosenOption[2] == 1:
                chosenOption[2] = -1;
                print(f"Successful purchase! This option can no longer be selected again. You have {available} left.");
            else:
                print(f"Successful purchase! You have {available} left.")
            returnObject[userInput_ - 1] = chosenOption;

        # Collect Confirmation
        shouldContinue = input("Have you finished (Y/N)? ");
        if shouldContinue.strip().lower() in [ "y", "yes", "true" ] or available <= 0:
            return available, returnObject;