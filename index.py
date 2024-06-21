# Import Libraries
import os;
import json;
import utility;

from objects import Instance;



# Global mutatable values (these values will be mutated globally; BEWARE!)
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
    print("Loading instance...");

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
    print("Importing file...");

elif selected == 3:
    print("Creating new instance...");



# DEBUG
print(instanceRaw);
print(instanceJson["name"]);
print(instance.name);



# GAME LIFECYCLE
while True:
    
    # General Points

    # General Allocations

    # Nuclear Win Condition

    # Commander Points

    # Commander Distributions

    # Update Sectors

    # Push Wind Condition

    # End of lifecycle
    break;





# Terminate program
if not instanceRaw:
    instanceRaw.close();
