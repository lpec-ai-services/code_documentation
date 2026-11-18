# EXAMPLE
<!-- source PDF pages 43-44 -->

<!-- page 43 -->
Chapter 5
EXAMPLE
After each of the different datablocks have been defined (geometrical data, composition data, etc.), the corresponding data for a
test example are given (the dictionary has already been established for this example).
The geometrical configuration of the example (an experiment using cylinders containing a solution of uranyl nitrate), consists of:
• a concrete slab 300 x 300 x 60 cm3;
• two cylindrical containers with conical bottoms (for simplicity, the conical bottoms are not modeled) made of stainless steel
and placed vertically 125 cm above the concrete slab and containing:
– uranyl nitrate solution at the bottom;
– air at the top.
The geometry is shown on the following page.
The data are given for a critical height Hc=28.54 cm and a distance of D=0.5 cm between the containers.
The syntax is given for the following two sources:
• a point source at the center of the uranyl nitrate solution in the left-hand container (as an example of a point source, whereas
convergence would be faster with a diffuse source corresponding to the fissile solution);
• a source corresponding to the uranyl nitrate solution in the right-hand container.
We will show the user how to request:
• the flux, computed using the track length estimator, in the air volumes above the uranyl nitrate solution (volumes 4 and 7);
• surface flux between the air volume (1) and the concrete (2);
• a macroscopic reaction rate for isotope U238, computed using the track length estimator, in the uranyl nitrate volumes
(volumes 5 and 8);
• a macroscopic reaction rate for isotope O16, computed using the track length estimator, in the air volumes (volumes 1, 4 and
7);
• a tabulated reaction rate, computed using the track length estimator, in all the volumes.

<!-- page 44 -->
The calculation is a criticality calculation.
Other geometry examples are given in the appendix. These examples seek to cover the different possible data definitions in
TRIPOLI-4®.
Complete examples of benchmark cases will also be given in the appendix in later versions of this report.
Hc
(5)
(4)
(8)
(7)
3
3
145,5
998
6
(1)
(2)
1250
Uranyl nitrate
Air
Concrete
Stainless steel
600
D
Figure 5.1: Geometrical configuration for the interaction between two uranyl nitrate containers in air
