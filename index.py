# Import Libraries
import os;
import json;
import utility;

from objects import Instance;


# "saved" IS A PROTECTED KEYWORD IS ALL SCENARIOS UNLESS IN INTERNAL USAGE
# Global mutatable values (these values will be mutated globally; BEWARE!)
# Should not be written to except start or end of program
instanceRaw = None;
instanceJson: object = {};
instance: Instance;



# Select initial action for user
selected, selected_ = utility.selection(options = [
    "Load instance",
    "Import instance",
    "Create instance"
]);


# Load Instance

if selected == 1:

    print("\nLoading instance...\n");

    # Selection for which file to open
    selectedIndex, selectedFileName = utility.selection(
        "Please select which game instance you wish to open: ",
        os.listdir("./Instances")
    );

    # Read file
    instanceRaw = open("./Instances/" + selectedFileName, "r+");

    # Parse JSON
    instanceJson = json.load(instanceRaw);

    # Serialise
    instance = Instance(instanceJson);


elif selected == 2:

    print("\nImporting file...\n");


elif selected == 3:

    print("\nCreating new instance...\n");


print("\nInitialising the game...\n");

# GAME LIFECYCLE
while True:
    
    # General Points
    for general in instance.players:

        # Check if the player is a general
        if general.position != "general":
            continue;

        # Give general points + saved
        general.allocations.append({
            "available": [ 9, general.points ]
        });
    
        # Notification
        generalPoints = general.allocations[-1]["available"][0];
        generalSaved = general.allocations[-1]["available"][1];
        print(f"The general {general.name} has been allocated {generalPoints} + {generalSaved}");
        print("Please allocate these points to the respective commanders: ");

        # Compile a list of available commanders
        commanders = [];
        for commander in instance.players:

            # Check if player is a commander
            if commander.position != "commander":
                continue;
            
            # Check if player is same faction
            if commander.faction != general.faction:
                continue;
    
            # Append
            commanders.append(commander.name);
    
        # Selection
        allocation = utility.allocations(f"You have recieved {generalPoints} + {generalSaved} Resource Points to spend: ", commanders, generalPoints + generalSaved);
        
        # Apply Allocations
        for name, allocated in allocation.items():
            general.allocations[-1][name] = allocated;
        general.points = allocation["saved"];
    

    # General Abilities
    abilities = utility.spend(options=[
        [ "The Nuclear Option",  ],
        [ "The Test Option" ]
    ]);


    # Commander Points

    # Commander Distributions

    # Update Sectors

    # Push Wind Condition

    # End of lifecycle
    break;





# Terminate program
if not instanceRaw:
    instanceRaw.close();
