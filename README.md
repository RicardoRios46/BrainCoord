# BrainCoord

BrainCoord is a program designed to deliver the optimal coordinates for a particular nucleus analyzed through microinjection techniques in mouse.

It computes the target coordinates instantly and error free, improving the researchers work and the whole experiment result. BrainCoord was built in reference to the Mouse Brain Paxinos Atlas. This program allows to calculate the optimal coordinates to reach any brain nucleus in the mouse, delivering the resultant coordinates points (AP, ML, DV) from a coordenate 0 (bregma or lambda), previously entered by the user. In addition, this script allows the importing of a database of any particular nucleus.

In addition, this script is open to import datbase of any particular nucleus. The actual version 0.1 includes the cerebellar nuclei: medial (MN), lateral vestibular (LVe), medial vestibular parvocelular (MVePc) and anterior Interpositus (IntA).

This tool accepts .cvs files which requires to contain the following ordered coordinates (in mm), per each imported nucleus: 
- point reference bregma
- point reference lambda
- lateral limit 
- medial limit
- dorsal limit
- ventral limit
    

## How to use it?

You can run the script at your terminal in two ways:

- Filling the variables as they are requested, all must be entered in millimeters, choose a reference point (bregma or lambda) and select the nuceli to target (MN, LVe, MVePc or IntA).  Notice the "reference0" is the AP, ML, DV coordinates from the point references at the mouse. For example: 

```bash
python braincoord.py
```

- Type the command with all the entrances in the same line. For example:

```bash
python braincoord.py --database_file MN --reference_point bregma --ap 33 --ml 15 --dv 63.7
```

If the nucleus of your interest is not in this database, upload  your own database as a .cvs file with the format previously mentioned. At the end, the script will rise a list with the resultant coordinates (AP, ML, DV), which indicates the point to move at the stereotaxic frame. 

Is important to notice  that this version only accepts files with a minimun of two rows of coordinates. In the case the user  requires to enter a particular coordinate, load a .csv file with the particular coordinates follow by a second row fill with: [0, 0, 0, 0, 0, 0]. 

### Optional arguments

As optional functions, You can obtain two output files:
- A logbook that it is a text file with the 0 coordinates, the resultant coordinates and the current date. You have to type at the terminal:

```bash
python braincoord.py --logbook True
```

- A log file with the debbug report. You have to type at the terminal:

```bash
python braincoord.py --debug True
```
## Documentation
For further information you will find the documentation in a zip file, open the file "index.html"

## Requirements
You will find a file call "requirements.txt" where is explicit the libraries need run the script.

