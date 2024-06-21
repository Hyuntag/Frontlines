
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