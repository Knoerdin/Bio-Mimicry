# Bio-Mimicry

## Code:
This project does not make use of any code, as the project is entirely analogue. However, there is a piece of simulation code for determining the deflection of different materials. Below is an explanation of how to use this code:
### Step 1:
To run the code, you'll need to install all dependencies. Do this by installing the requirements.txt file with this command:
```
pip install -r requirements.txt
```
### Step 2:
Now that you can run the code (assuming Python is installed...), go to the directory with the deflection.py in it and run the following command:
```
python3 deflection.py
```
This should start prompting values for these variables:
-   Material **name**
-   Beam **length** in meters
-   Beam **diameter** in centimeters
-   Beam **thickness** in millimeters
-   Material **modulus** of elasticity in pascals
-   Material **density** in kg/m³

After giving these variables a value, the program will ask you if you'd like to enter another entry. **Saying yes** will result in the same six questions and another entry in the data file. **Saying no** will plot all entries in the data file as a bar plot.\
When you are done with the simulation or need to exit, the data of the materials will be saved in deflection_results.txt for ease of use the next time the simulation is run.
## STL Files

This folder contains all 3D-printable parts used in the final prototype of the biomimetic bouldering hold gripper. The system consists of a pole-mounted tool head with a granular-jamming vacuum gripper, integrated drilling capability, onboard vacuum pump, and battery power supply.

### `accu_holder_los_helft.stl`
Single half of the slide-in battery holder that secures the battery pack and prevents connector movement during use.

### `conncection_drill_and_pole.stl`
Connector part that mechanically couples the drill and gripper head assembly to the aluminium pole.

### `filling_rig.stl`
Assembly aid used to hold the silicone membrane and clamping parts upright while filling the gripper with granular material.

### `handvat_half.stl`
One half of the handle shell that clamps around the pole and houses wiring, switches, and the drill trigger mechanism. To get the other half, just mirror this STL file before printing.

### `hinge_drill_connection.stl`
Tool-head-side hinge component that connects the gripper/drill assembly to the hinge mechanism.

### `hinge_pole_connection.stl`
Pole-side hinge component that mounts to the aluminium pole and the other hinge component

### `pump_holder+accu_helf_connected.stl`
Combined mount for the vacuum pump and battery interface that attaches to the pole and acts as a counterweight.

### `silicone_attachement_rings.stl`
Clamping rings used to secure the silicone membrane and create an airtight seal for the vacuum gripper.

### `silicone_cap_vacuum_attachment.stl`
Top cap of the gripper that connects the silicone membrane to the vacuum tubing. There is also a cutout for a ring filter.

### `silicone_mould_final_design.stl`
Mould used for casting the final silicone gripper membrane geometry.

## Miscellaneous:
Under the MISC folder, you'll find the poster used in the poster presentation given in Delft.
You'll also find the drawn electrical circuit connecting the drill and vacuum pump to the battery.


