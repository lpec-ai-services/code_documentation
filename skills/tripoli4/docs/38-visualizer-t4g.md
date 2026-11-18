# VISUALIZER T4G
<!-- source PDF pages 421-440 -->

<!-- page 421 -->
Chapter 38
VISUALIZER T4G

## 38.1 INTRODUCTION TO T4G

T4G is a tool to visualize and check the data interpreted by Tripoli-4 or Root.
T4G window is divided in two areas (figure 38.1): the left pane contains the picture of the data, while the
right pane contains some information about the data set or the data pointed by the mouse.
T4G manages color policy. Each policy is the representation of a same kind of parameters. One color depicts
a parameter to make it easily recognizable among the others.
The available color policies are:
- "volumes", exactly 1 color per volume;
- "compositions", exactly 1 color per composition;
- "colors", colors defined by the user for some or all volumes in a *.colors file;
"Compositions", "scores" and "colors" policies are optional.

<!-- page 422 -->
Figure 38.1: T4G window

## 38.2 HOW TO LAUNCH T4G

To run T4G with the data set data_set, type the following command:
./static_visutripoli4 <data_set> [--<option_1> <value_1> [--<option_2> <value_2> ...]]
where data_set can be a Tripoli-4 or a Root data set. The type of geometry is deduced from the file
extension of the data set: *.t4 for Tripoli-4 geometries, *.root for root ones. Other extensions will lead to
the execution stop.
The accepted options keywords and associated values are described below:
--lang
: language (0 -> english, 1 -> french, 2 -> old).
--fromfile
: name of commands file
--title
: title of the GUI window
--screensize
: heigth of the window
--para
: parallel flag followed by number of tasks
--window
: list of values defining the frame of the window :
[ox oy oz ux uy uz vx vy vz lu lv] (see section \ref{win})
--3D
: 3D visualization (if not set : 2D visu)
--help
: print the help
--expert
: disable the automatic load of the files .colors, .vvls,
.scores, .meshes and .points.
If the option --expert is used then the following keywords can be used :
--colors
: to load a "colors" file

<!-- page 423 -->
--vvls
: to load a "volumes values" file
--scores
: to load a "*.dat scores" file
--meshes
: to load a "*.general meshes" file
--points
: to load a "*.general points" file
followed by the name of the file.
Default values are:
• lang : old;
• window : -1 -1 0.5 1 0 0 0 1 0 100 100 (see section 38.3.4);
Parallel flag
The parallel flag only concerns the native geometry of Tripoli-4 (the CERN/ROOT is not concerned).
It is followed by the number of tasks to use. T4G uses OpenMP for shared memory parallelisation. The screen
is decomposed into multiple horizontal frames each slave process is filling with geometry. As different frames
do not necessarily take similar durations to complete, do not hesitate to ask for more tasks (no more than a
factor 2 though) than really available cores (or CPU threads). It allows task stealing and better handling of
tail effect (tasks not finishing at the same time), so a better parallelism efficiency.

<!-- page 424 -->
## 38.3 2D VISUALIZATION

### 38.3.1 GEOMETRY RETRIEVAL

In 2D, a geometry can be plotted in three modes: line by line volumes ("pursuit"), point by point volumes
("position"), or frontier ("contours") modes (figure 38.2).
The default mode is "pursuit".
To switch between "pursuit" and "frontier" modes, press the V key. To switch between "pursuit" and "position"
modes, press the E key.

#### 38.3.1.1 "Pursuit" mode

This is the default mode. The volumes are plotted with different colors in different volumes.

#### 38.3.1.2 "Position" mode

This volume mode displays the same data than the previous one, but the algorithm used is different. This
visualization mode is slower than the "pursuit" one but should show the same plot. However, incorrect
geometries may lead to differencies between these plots. A good use is then to navigate through the geometry
in "pursuit" mode and switch to "position" mode from time to time to check the coherency of the geometry.

#### 38.3.1.3 "Contours" mode

The frontier mode displays the frontiers between different volumes by a black line.
Figure 38.2: From left to right: geometry visualization in "pursuit", "position" and "contours" modes

### 38.3.2 DISPLAY OF THE COLOR POLICY

In 2D, T4G can handle several color policies which are :
- "volumes";

<!-- page 425 -->
- "compositions", if they are available in the data set;
- "colors", if the data_set.colors file exists and is not empty.
Pressing N selects a policy between the available ones. In the information pane, at the line "info", the name
or value of the policy at the place pointed by the mouse is then displayed.
Pressing C refreshes the display in the left pane: the current policy is displayed (figure 38.3). Its name is
indicated in the right pane at the line "color" by the matching keyword:
Policies
Keyword
volumes(geometry)
GEOM
compositions
COMPOS
colors
INFOCOLORS
A volume may be undefined for "colors" policy. In that case, it is painted black.
The following picture (figure 38.3) shows an example of the visualization for each policy:
Figure 38.3: From left to right: visualization of "volumes", "compositions" and "colors" policies
"Compositions" and "colors" policies are always drawn using "pursuit" mode.
It is possible to add the contours of the geometry to the current policy by pressing key f.

#### 38.3.2.1 "Volumes values" file

The association of a volume and its value is defined in the "vvls" file. Its structure is the following:
<name of a volume>
<volume value>
<name of another volume> <volume value>
...
This file may be provided be a Tripoli-4 run. See section 23.1 for details. If T4G find such a file, volume
score will the score defined previously divided by the value of the volume.

<!-- page 426 -->
#### 38.3.2.2 "Colors" file

The association of volumes and colors is defined in the "colors" file. Its structure is the following:
<name of a color>
<number of volumes> <list of volume names>
<name of another color> <number of volumes> <list of volume names>
...
The color names can be written in lower or uppercase. They are the ones defined in X11 library file rgb.txt.

### 38.3.3 TRIPOLI-4 SCORES, MESHES AND POINTS PLOT

Data such as scores on volumes or values on meshes or points may be provided by a Tripoli-4 run. The
generated files are respectively named data_set.scores,data_set.meshes and data_set.points files.
They contain the list of the *.dat or *.general files that contain the data.
The data_set.scores,data_set.meshes and data_set.points files have the same structure: each line
must start with the keyword name and then contains the name of the *.dat or *.general file.
In the meshes file, each mesh must be defined on exactly one line. The user can set different parameters of
the mesh :
• the frame (frame)
• special color legend (colorlegend)
• min and max values (minmax)
• reversing the color legend (neg)
• a multiplying coefficient (coeff)
All of these parameters are optional. The user can disable the rest of the line options with the # keyword.
name <name of a *.general file>
[keyword <definition of option >] ...
name <name of another *.general file> [keyword <definition of option >] ...
..
For meshes and points the definition of the frame in the geometry is available and given after the keyword
frame.If no frame is defined, the frame is the same as the geometry’s one. A frame is defined by its origin o
and two unit vectors u and v:
frame <ox oy oz ux uy uz vx vy vz>
For meshes the definition of the mesh’s color legend is available and given after the keyword colorlegend.If
no color legend is defined, the standard color legend is setted. A color legend is defined by a set of three types
of parameters : the number of colors ncolors, the treshold of each color lim and the name of the color
color.

<!-- page 427 -->
colorlegend < ncolors min color0 lim1 color1 ... lim(n-1) color(n-1) max colorn >
The user can set the values of the min and the max of the current mesh with the following keyword : minmax
and the values of min and max.
minmax < min max >
The user can reverse the color scale. Usually, high values are in red and low values in blue. With this mode,
low values are in red and high values in blue.
neg
This option may be useful if the user wants high importances in red and low importances in blue. The
quantity dumped when using the STORE_IN_FILE keyword is −log(I) with I the importance function. Thus,
using the neg keyword, high importances can appear in red and low importances in blue.
The user can set a multiplying coefficient for the current mesh with the following keyword : coeff and the
value of the multiplying coefficient.
coeff <coeff>
Note that the data plotted here will be added to the current plot, but will disappear after a call to a move or
an update.
The list of available actions on meshes and points are given in section 38.3.5. The main features are described
below.

#### 38.3.3.1 Scores plot

If T4G finds a data_set.scores file in the working directory, it will load all the related scores files.
A score file defines the association of volumes and scores. Its structure is the following:
<name of a volume>
<score value>
<name of another volume> <score value>
...
Pressing left parenthesis key “)" switches between the available scores files. The name of the current scores
file *.dat appears in the right pane of the T4G window in the SCORES section.
Pressing the key "O" displays the current scores (figure 38.4).
Note that the scale that is plotted at the bottom left side of the plot area is computed so as to take into account
the values in all the loaded geometry. A volume may be undefined: in this case, it is painted white. Scores
are drawn using “pursuit" mode.

<!-- page 428 -->
Figure 38.4: Scores on volumes

#### 38.3.3.2 Meshes plot

If T4G finds a data_set.meshes file in the working directory, it will load all the related meshes.
Pressing m switches between the available meshes. The name of the current mesh file *.general appears in
the right pane of the T4G window in the MESHES section.
Pressing T selects the mesh frame type that will be used to convert the mesh positions into the cartesian
geometry’s frame. The selected frame type is indicated in the T4G window just before the mesh file. It can
be one of:
Frame type
Keyword
cartesian
CART
cylindrical
CYL
spherical
SPH
spherical(r,µ,φ)
SPH_MU
As there is no way to recognize a mesh type, it is the responsibility of the user to select the right one. If the
selected type does not match the mesh type, the display will be incoherent. However, the mesh type is now
included in the comments of the .general file format as long as a possible change of frame:
#frame_type = <frame_type>
#origin = <ox>, <oy>, <oz>
#vectors = <ux>, <uy>, <uz>, <vx>, <vy>, <vz>

<!-- page 429 -->
T4G is able to interpret these comments to set a proper default.
The available possibilities for the frame type are CARTESIAN, CYLINDRICAL, SPHERICAL, SPHER-
ICAL_MU and TRIANGLE_Z. SPHERICAL_MU is the same as spherical, but with a cosθ instead of θ.
It allows to easily represent isotropic data. TRIANGLE_Z is related to meshes with prismatic cell (see
extended meshes, section 15.8) used to score, in particular, hexagonal structures.
Pressing M superimposes the current mesh’s display over previously displayed geometrical elements (figure
38.5).
Pressing space redraws with the current color policy (re-initialized the display). Hence to display only the
current mesh, one should press space then M.
Figure 38.5: Data mesh with grid
Note that the scale that is plotted at the top right side of the plot area is computed so as to take into account
the values in all the loaded meshes.
The mesh grid can be enabled/disabled with the key B.
A logarithmic scale can be used by pressing L. In this case, the keyword "Log" appears in the right part of the
T4G window, under the line "color".

#### 38.3.3.3 Points plot

If T4G finds a data_set.points file in the working directory, it will load all the related points files.
Pressing p switches between the available files. The name of the current file *.general appears in the right
pane of the T4G window in the POINTS section.

<!-- page 430 -->
Pressing R switches between the different fields of points available in the current file. The field’s name is
indicated in the T4G window at the line "value". See section 31.4.2 for a description of available fields.
Pressing P superimposes the current field’s display over previously displayed geometrical elements (figure
38.6). As it is likely to get very few points in the current plane, the plotted points are the ones located at a
distance lower to the one indicated at the line "Max. distance to plane:". This distance can be lowered (key
J) or increased (key K) by a factor two. The default distance is 128 cm.
Figure 38.6: Data points
Note that, unlike the behaviour for meshes scale, T4G will plot a scale at the bottom right side of the representation
pane that takes into account only the data of the current points set.

### 38.3.4 WINDOW

#### 38.3.4.1 Definition

The plot frame or "window" defines the frame in which the geometry will be drawn.
The required informations to define it are:
- o : the origin position;

<!-- page 431 -->
- u : the first vector of the system;
- v : the second vector;
- lu : the width, along the first vector;
- lv : the height, along the second vector;
T4G admits three ways to define a window. Here they are, in order of priority:
• using the option --window in the command line;
• loading the file data_set.window from the current working directory;
• using the default frame (no option --window, no file data_set.window).
In 2D, when the user closes T4G, the last characteristics are saved in the file data_set.window.

#### 38.3.4.2 Default window

The default frame characteristics are:
- o : [-1., -1., 0.5];
- u : [1., 0., 0.];
- v : [0., 1., 0.];
- lu : 100;
- lv : 100.

#### 38.3.4.3 Command line option

The same frame would be defined using the following command line option :
--window
[ox oy
oz ux uy uz vx vy vz
lu
lv]
--window
-1 -1 0.5
1
0
0
0
1
0 100 100

#### 38.3.4.4 Window file

The matching data_set.window file would contain :
o -1 -1 0.5
a 1 0 0
b 0 1 0
la 100
lb 100

### 38.3.5 AVAILABLE KEYS IN 2D MODE

2D features are given in the following tables:

<!-- page 432 -->
Key
General
q or Q
Quit
?
Display the help
space or a
Redraw with the current color policy (re-initialized the display)
G
Draw grid
=
Reload meshes and points
H
Hide the right pane of the T4G window
F
Export image: generates .tiff and .bmp pictures of the T4G window.
Key
Drawing policy
N
Loop over the color policy
C
Call the display of the current color policy
E
Toggle between "pursuit" and "position" drawing methods
V
Toggle between "pursuit" and "contours" drawing methods
Key
Memorize in stack
<
Add the mouse position in the stack
>
Remove the last position from the stack
!
Set position in the stack from console input
Key
Information at the console
v
Display the name of the current volume, its color RGB and the current
mesh value under the mouse pointer
I
Window definition
*
Enable/disable drawing of the scale
,
Draw a legend on the plot area : the name of the current policy under
the mouse pointer (score value in scores case)
r
Display the ray between the mouse positions kept in stack
t
Display the ray from center to volume next to cursor

<!-- page 433 -->
Key
Move
h or left
Translation towards x -
l or right
Translation towards x +
j or down
Translation towards y -
k or up
Translation towards y +
n or Next Page
Translation towards z -
i or Previous
page
Translation towards z +
d or -
Unzoom
D or Shift+-
Unzoom more
s or +
Zoom
S or Shift++
Zoom more
W
Zoom from positions in stack
x, y, z
Compute a plane cut along the specified direction
X, Y, Z
Rotate 90 deg around X, Y and Z axis
w
Rotation defined by the center of the plot and the mouse position
c
Center the plot to the mouse position
Key
Actions on Scores
O
Display the current scores
b
Change current scores
Key
Actions on Meshes
M
Superimpose the current mesh’s display over previously displayed geometrical
elements
m
Change current mesh
A
Select / unselect all the meshes as current mesh
B
Plot / do not plot the mesh grid
U
Increment number of isovalues
u
Decrement number of isovalues
o
Display the isovalues of the current mesh
_
Load all mesh files (.meshes, .resultmeshes, .sourcemeshes and .importancemeshes
) of the current working directory
L
Use / do not use the logarithmic mode
T
Change mesh type (cartesian, cyclindrical, spherical, spherical mu)

<!-- page 434 -->
Key
Actions on Points
P
Superimpose the current point field’s display over previously displayed
geometrical elements
p
Change current points file
R
Change points field
J
Divide by 2 the maximum distance between current plane and points to
plot
K
Multiply by 2 the maximum distance between current plane and points
to plot
Key
Common to Meshes and Points
f
Display the contours of the geometry
Key
Commands file
g
Stop file input

<!-- page 435 -->
## 38.4 3D VISUALIZATION

This mode allows some kind of 3D representation of the geometry. It is considered as experimental and it is
not currently known if further enhancement will be possible on this concept.

### 38.4.1 LAUNCH 3D VISUALIZATION

In order to get a 3-dimensional view of a geometry, type the command:
./static_visutripoli4 data_set --3D
where data_set is the name of a *.t4 or *.root file.

### 38.4.2 BASIC FEATURES

At the moment, the 3D visualization uses one mode "volume" to draw the geometry. The drawing of "compositions
", "scores" and "colors" policies are not available.

#### 38.4.2.1 Exclusion of volumes

Pressing key - (minus) removes the volume located under the mouse pointer from the visualization (figure
38.7).
Figure 38.7: Left: the geometry from outside. Right: after the exclusion of the main envelop.

#### 38.4.2.2 Manipulation

All operations such as moving, centering, zooming, ... are available (figure 38.8). The related keys are given
in section 38.4.5.

### 38.4.3 HIDING A PART OF A ROOT GEOMETRY WITH A SIMPLE TRIPOLI-4 GEOMETRY

In the case of a Root visualization, it is possible to use a trivial Tripoli-4 geometry to hide the Root geometry
located between the user and the Tripoli-4 geometry (figure 38.9).

<!-- page 436 -->
Figure 38.8: The geometry from different points of view in 3D
This option is activated with key H.
In this case, T4G looks for a file named data_set.hide.t4 in the current working directory. If found, the
Tripoli-4 geometry contained in this file is loaded.
Figure 38.9: 3D Root visualization: two planes, defined by a Tripoli-4 geometry, hide a part of the Root geometry

<!-- page 437 -->
### 38.4.4 VIEW AND SCREEN

3D visualization requires the definition of a "view" and a "screen". Those parameters are equivalent to the
"window" in 2D.

#### 38.4.4.1 View

The view defines the position from where the geometry is observed.
The required informations to define it are:
- o : the position;
- theta : the theta angle;
- phi : the phi angle;
- length : the distance to the geometry;
T4G admits two ways to define a view:
• loading the file data_set.view from the current working directory;
• using the default view (if no file data_set.view);
The default view characteristics are:
- o : [0., 0., 0.];
- theta : 0.;
- phi : 0.;
- length : 200.;
The matching data_set.view file would contain :
o 0 0 0
theta 0
phi 0
length 200

#### 38.4.4.2 Screen

The screen contains the view port properties.
The required informations to define it are:
- screen_distance : the distance;
- pitch : the pitch;
- ilen : the width;

<!-- page 438 -->
- jlen : the height;
T4G admits two ways to define a screen:
• loading the file data_set.screen from the current working directory;
• using the default screen (if no file data_set.screen);
The default screen characteristics are:
- screen_distance : 30. cm;
- pitch : 0.025 cm.
The matching data_set.view file would contain :
screen_distance 30
pitch 0.025
ilen 769
jlen 769

### 38.4.5 AVAILABLE KEYS IN 3D MODE

3D features are given in the following tables:
Key
General
q or Q
Quit
space or a
Redraw
?
Display the help
F
Export image : generates .tiff and .bmp pictures of the T4G window.
Key
Drawing
M
Toggle between drawing methods (only "volume simple" at the moment
)
-
Exclude an object
H
Use the Tripoli-4 hiding geometry (if there is one!). Root visualization
only.
Key
Zoom
d
Unzoom
D or Shift+-
Unzoom more
s
Zoom
S or Shift++
Zoom more

<!-- page 439 -->
Key
Move
l or right
Rotation towards phi -
h or left
Rotation towards phi +
k or down
Rotation towards theta -
j or up
Rotation towards theta +
r
Rotation defined by mouse position
c
Redefine the center of the plot

<!-- page 440 -->
## 38.5 CONFIGURATION FILES

Once T4G is opened, the user can manipulate the geometry by typing keys, but also by passing T4G a
command file. By using the --fromfile option, the user can define a commands file that contains a list of
commands to manipulate the geometry. This file must validate the following conditions:
• it must contain one and only one command per line;
• each special character must be written in english, matching the correspondances below:
Key
Command
space
space
?
question
*
asterisk
,
comma
<
less
>
greater
!
exclam
_
underscore
• when T4G reaches the end of the file, T4G closes. In order to get control of T4G after a key sequence,
add the command g to the command file. When T4G reaches a g key, it stops the configuration file
control, and the user gets back the control of the geometry.
• the commands do not require some user’s action such as keyboarding.
