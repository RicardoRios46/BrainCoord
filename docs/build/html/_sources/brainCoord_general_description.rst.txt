.. _description-sheet:

*******************************
BrainCoord general description
*******************************

BrainCoord is a program designed to deliver the optimal coordinates for a particular nucleus analyzed through microinjection techniques in mouse.

It computes the target coordinates instantly and error free, improving the researchers work and the whole experiment result.

BrainCoord was built in reference to the Mouse Brain Paxinos Atlas.
This program allows to calculate the optimal coordinates to reach any brain nucleus in the mouse, delivering the resultant coordinates points (AP, ML, DV) from a coordenate 0 (bregma or lambda), previously entered by the user.
In addition, this script allows the importing of a datbase of any particular nucleus.

.. _how-does-it-work:

=================
How does it work?
=================


This tool we is focused on cerebellar nuclei: medial vestibular parvocellular (**MVePC**), medial nucleus (**MN**), lateral vestibular (**LVe**), Interpositus anterior (**IntA**).
It computes the final coordinates using as a reference a database that contains information of several plates, which indicates the position of the target nucleus in such plate.
BrainCoord choose the bigger area of the nucleus in those plates and according to the middle point of such area, computes the coordinates where the needle must be moved to perform the microinjection.


===============
Considerations
===============

Coordinates are computed using as a reference the coronal plane and considering a stereotaxic apparatus tower positioned at the left side.

===================
Inputs requirements
===================

This tool accepts 5 arguments:

#. name of one of the 4 target nucleus (as indicated in the keywords in black in (see :ref:`how-does-it-work`) section.

#. reference point (bregma or lamda)

#. AP coordinate 0 (in **mm**)

#. ML coordinate 0 (in **mm**)

#. DV coordinate 0 (in **mm**)

Optionally, this tool accepts .cvs files containing the following ordered coordinates (in mm), per each imported nucleus:

* point reference lambda

* point reference bregma

* lateral limit

* medial limit

* dorsal limit

* vetral limit
