
def selection(prompt = "Please select an option", options = []) -> int | str:
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
            userInput = int(userInput_);
        except:
            userInput = None;

        # Continue if userInput is invalid
        if not userInput or userInput == 0 or userInput > index:
            continue;

        # Return value
        return userInput, options[userInput - 1];




def allocations(prompt = "Please choose allocations", options = [], points = 0) -> dict:
    
    # Prompt user
    print(prompt);

    # Display options
    for option in options:
        print(f"> {option}");

    # Separator
    print("\n");

    # Collect input
    while True:

        available = points;
        returnObject = {};

        for option in options:

            # Check if available points
            if available <= 0:
                print("All points have been allocated; remaining options will be set to 0");
                break;

            # Display
            userInput_ = input(f"You have {available} points available to spend on {option}: ");

            # Type cast
            userInput = 0;
            try:
                userInput = int(userInput_);
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
