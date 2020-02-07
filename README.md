# BrainCoord

It was built in reference to the coronal plates from the Mouse Brain Paxinos Atlas. This script allows to calculate the optimal coordinates to reach any brain nucleus in the mouse, giving the resultant coordinates points (AP, ML, DV) from a coordinate 0 (bregma or lambda) previously entered by the user. In addition, this script is open to import datbase of any particular nucleus. The actual version 0.1 includes the cerebellar nuclei: medial (MN), lateral vestibular (LVe), medial vestibular parvocelular (MVePc) and anterior Interpositus (IntA).

This tool accepts .cvs files which requires to contain the following ordered coordinates (in mm), per each imported nucleus: 
    * point reference bregma
    * point reference lambda
    * lateral limit 
    * medial limit
    * dorsal limit
    * vetral limit
    
This script requires that `NumPy` be installed within the actual Python environment.

## How to use it?

Run the script at your terminal. Fill the varibles as they are requested, all must be entered in millimeters, choose a reference point (bregma or lambda) and select the nuceli to target. Notice the "reference0" is the AP, ML, DV coordinates from the point references at the mouse.
If the nuceli is not in database, upload it as a .cvs file with the format previously mentioned. At the end, the script will rise a list with the resultant coordinates (AP, ML, DV), which indicates the point to move at the stereotaxic frame. 
