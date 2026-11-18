# THE CADIS VARIANCE REDUCTION TECHNIQUE
<!-- source PDF pages 275-284 -->

<!-- page 275 -->
Chapter 20
THE CADIS VARIANCE REDUCTION
TECHNIQUE
Many variance-reduction techniques, including TRIPOLI-4’s exponential transform (Chapter 17), require the
use of an importance map. For several techniques, it can be proved that the optimal importance map is given
by the adjoint flux, i.e. the solution to the adjoint Boltzmann equation.
This chapter describes the CADIS technique, its implementation in TRIPOLI-4, and the input syntax that is
required to use it.

## 20.1 PRINCIPLE OF THE CADIS METHOD

The CADIS (Consistent Adjoint-Driven Importance Sampling) technique consists in using a deterministic
solver to solve the adjoint Boltzmann equation for the adjoint flux, and using it as an importance map in a
direct Monte Carlo calculation. The detector acts as a source for the adjoint equation; thus, different detectors
(and different detector response functions) result in different importance maps. On the other hand, the particle
source does not appear in the adjoint Boltzmann equation; therefore, CADIS importance maps for a given
detector can be used for any particle source.
In TRIPOLI-4, the CADIS technique is implemented via a coupling with the IDT deterministic solver [104].
IDT is developed at CEA/SERMA. It is a multi-group, SN solver that uses the method of short characteristics.
Starting with version 12, it is shipped together with TRIPOLI-4. IDT can be used for photon calculations and
neutron calculations; coupled neutron-photon calculations are not supported yet. The code is shipped with
a photon file and a neutron file in the HDF5 format containing microscopic multi-group cross sections. The
photon cross sections use a 94-group energy grid, while the neutron cross sections use a 281-group grid. The
HDF5 schemes used by these files are documented in technical notes [82, 83].
In the current implementation of the CADIS scheme, TRIPOLI-4 uses the exponential transform as a variancereduction
method by default (see Chapter 17). Other variance-reduction methods may be used by writing the
generated importance map to a file and using it as an external map.

<!-- page 276 -->
## 20.2 MODELLING AND APPROXIMATIONS

In the IDT solver, mesh cells are assumed to be homogeneous. In practice, a mesh cell can overlap with
more than one TRIPOLI-4 volume, with possibly different compositions. It is important to stress that IDT
will assume that cells are filled with the material that is found at the center of the cell. This admittedly crude
approximation will be improved upon in future versions of the code. For the moment we recommend users
to adapt the coarseness of the space mesh to the complexity of the geometry.

## 20.3 SYNTAX

VARIANCE_REDUCTION
NAME <biasing_name>
<PARTICLE_TYPE>
GRID
Grid data
MINIMAL_IMPORTANCE <importance>
∗
MESH
Uniform mesh data
END_MESH
∗
MESH_VARIABLE
Nonuniform mesh data
END_MESH_VARIABLE
IDT
IDT data
END_IDT
STORE_IN_FILE <format>
END_VARIANCE_REDUCTION
The CADIS scheme uses a slightly modified version of the standard VARIANCE_REDUCTION block. The
syntax and the semantics of the GRID, MESH and MESH_VARIABLE keywords are the same as in the
VARIANCE_REDUCTION block, described in Chapter 17, with the following caveats:
• the recommended way to set the energy grid with the GRID keyword is to read it from the default IDT
microscopic cross section file (see below). The syntax is the following:
GRID FROM_IDT_XS_T4PATH
where the string T4PATH refers to the path file using the new path file format (see Section 3.1.2) with
the idt_photon_xs_file and idt_neutron_xs_file keywords.
Alternatively, the cross section grid can be read from another HDF5 microscopic cross section file with
the following syntax:

<!-- page 277 -->
GRID FROM_IDT_XS_FILE <filename>
Finally, the grid can be explicitly specified, following the standard syntax of Chapter 17.
Note that, in all cases, the given energy grid must match the grid stored in the microscopic cross section
file that is actually used by the solver (see below). No cross section condensation takes place at the
moment, and an error is emitted if the given energy grid does not match the cross section grid.
Note also that the lower simulation energy bound must be greater than or equal to the lower energy
bound of the energy grid used by IDT. Likewise, the upper simulation energy bound must be less than
or equal to the upper energy bound of the IDT energy grid. These rules are not specific to CADIS
simulations; they also apply to other variance-reduction techniques (see Sec. 17.2.1). However, in the
case of CADIS, the energy grid is essentially imposed by the IDT cross-section file. Therefore, the user
may need to adjust the energy simulation domain to match the cross-section grid (see Sec. 22.2 for the
syntax).
• the optional MINIMAL_IMPORTANCE keyword sets the smallest value that is accepted in the generated
importance map; values below this threshold are truncated to the threshold value. In problems with
strong attenuation, the use of MINIMAL_IMPORTANCE is recommended with a very small value (e.g.
1e-30).
• the MESH/MESH_VARIABLE keywords follow the syntax of Section 17.2.4 and define the space mesh for
the importance map as seen by TRIPOLI-4. For use with IDT, the frame type of the space mesh must be
CARTESIAN. The actual space mesh used internally by the IDT solver may be finer (see CONVERGENCE
keyword below). Although this possibility exists, it is generally recommended that IDT and TRIPOLI-4
use the same space mesh: the TRIPOLI-4 importance map is anyway smaller than the memory required
for the IDT calculation, so there is little gain in homogenizing it on a coarser mesh.
• as with INIPOND, the IDT importance map can be stored in a file for further analysis or reused with the
STORE_IN_FILE keyword (see Chapter 17).

### 20.3.1 IDT PARAMETERS

The IDT block has the following syntax:

<!-- page 278 -->
IDT
TARGET <target data>
SPECTRUM <spectrum data>
CONVERGENCE <convergence parameters>
MICROSCOPIC_CROSS_SECTIONS
<microscopic cross section data>
END_MICROSCOPIC_CROSS_SECTIONS
MAX_INNERS <max inner iterations>
MAX_THERMALS <max thermal iterations>
∗
CHARACTERISTICS CONSTANT
∗
CHARACTERISTICS LINEAR
ALLOW_IDT_IN_PARALLEL
IDT_SOLVER_OPTIONS
<IDT solver options>
END_IDT_SOLVER_OPTIONS
END_IDT
The TARGET, SPECTRUM, and CONVERGENCE keywords are required.

#### 20.3.1.1 TARGET keyword

TARGET describes the spatial location of the adjoint source, i.e. of the detector. The arguments of the TARGET
keyword are names of scores, as defined in the SCORE block. The syntax is
TARGET <number of scores> <score name 1> ...<score name n>
The scores must be defined over a list of volumes (possibly consisting on only one volume), a sum of volumes
or an extended mesh. The location of all the scores is jointly taken as the location of the adjoint source.

#### 20.3.1.2 SPECTRUM keyword

SPECTRUM describes the energy response of the detector, i.e. the energy spectrum of the adjoint source. The
spectrum can be given as a constant (energy-independent) response, it can be given as a tabulated response or
it can be automatically extracted from one of the TRIPOLI-4 responses, defined in the RESPONSES block.
In the first case the spectrum of the adjoint source is given as
SPECTRUM CONSTANT <response value>
For example, SPECTRUM CONSTANT 1.0 can be used to represent a flux detector (which is characterized by a
response function that is equal to 1 for all energies).

<!-- page 279 -->
For the second case (tabulated response), the syntax is
SPECTRUM LIST <response value> <response value> ...
Here the response values must be given on the energy grid specified in the VARIANCE_REDUCTION block. If
the grid has length N, exactly N −1 values are expected here.
Finally, for the case of an existing response, the SPECTRUM syntax is
SPECTRUM RESPONSE NAME <response name>
where <response name> must be the name of one of the responses defined in the RESPONSES block (see
Chapter 13).

#### 20.3.1.3 CONVERGENCE keyword

The CONVERGENCE keyword describes the space and angular discretization of the mesh used by IDT for
solving the adjoint Boltzmann equation. The syntax is
CONVERGENCE FIXED <max optical thickness> <SN order>
The max optical thickness parameter is used to control the coarseness of the IDT internal calculation mesh:
IDT starts by considering the mesh provided by the user with one of the MESH/MESH_VARIABLE keywords.
It computes the optical thickness of each mesh cell, defined as the product of the total cross section for
the (homogenized) cell and the cell size. If the optical thickness is larger than the max optical thickness
value given by the user, then IDT will automatically refine the internal calculation mesh to meet the optical
thickness criterion. See Section 20.4 below for a discussion of the optimal value for this parameter.
The SN order parameter is the order of the SN angular quadrature to be used by IDT. Larger values of this
parameter improve the accuracy of the angular quadrature formulas and help with mitigating ray effects in
the importance map; however, note that the memory footprint of IDT is mildly dependent on the value of this
parameter. The CPU time also increases when this parameter is increased. A value of 8 is a good starting
point.

#### 20.3.1.4 MICROSCOPIC_CROSS_SECTIONS block

The optional MICROSCOPIC_CROSS_SECTIONS block provides the parameters for the computation of the
macroscopic cross sections from the microscopic multi-group photon/neutron cross sections. The syntax
is the following:

<!-- page 280 -->
MICROSCOPIC_CROSS_SECTIONS
ORDER <order>
∗
PARTICLE <particle type> FILE <HDF5 file name> ALL
∗
PARTICLE <particle type> FILE <HDF5 file name> NUCLEI
<number of nuclei> <nucleus> <nucleus>...
END_MICROSCOPIC_CROSS_SECTIONS
The ORDER keyword represents the maximum order of the development of the angular distribution of microscopic
cross sections over Legendre polynomials. For the default microscopic cross-section files provided
with the installation, this parameter can range from 0 to 6 (inclusive); the default value is 1. It is recommended
to use larger values for high-energy neutron problems and for photon problems. Note also that the
memory footprint of the IDT solver and the required CPU time scale as the square of this parameter.
The PARTICLE and FILE keywords can be used to customize the microscopic cross section files that should
be used by IDT. By default, all nuclei in the geometry will use the files defined by the idt_photon_xs_file
and idt_neutron_xs_file keywords in the dictionary file (see Chapter 3). This choice can be overridden
on a nucleus-by-nucleus basis with the NUCLEI syntax, or globally with the ALL keyword. Multiple FILE
keywords may be given for the same PARTICLE; if the ALL syntax is used together with one or more NUCLEI
lines, then the filename specified by the ALL keyword only applies to the nuclei that were not explicitly
specified.

### 20.3.2 OTHER KEYWORDS

There are a few other optional keywords that can be used in the IDT block:
• MAX_INNERS can be used to set the maximum number of inner iterations performed by IDT. By default
this number is 1000. Reducing this number to a smaller value may speed up the IDT calculation but it
might also prevent the code from converging.
• MAX_THERMALS sets the maximum number of thermal iterations in neutron problems. The default value
is 50. Reducing this value might prevent IDT from converging.
• CHARACTERISTICS sets the type of characteristics to use. Possible values are CONSTANT and LINEAR,
with CONSTANT being the default. Linear characteristics are more precise than constant characteristics
for a given mesh size, but their memory footprint is four times larger and they may lead to negative
importances in unconverged meshes.
• the IDT_SOLVER_OPTIONS block can be used to pass any option understood by IDT to the solver. The
content of this block is copied verbatim into the IDT input file (filename <input_file>_idt.d). A
partial list of useful IDT options follows:
– FissionIntegralPrecision <float>: convergence criterion for the fission integral during outer

<!-- page 281 -->
iterations. Default: 1e-4. This option is only relevant for FIXED_SOURCES_CRITICALITY calculations
.
– InnersPrecision <float>: convergence criterion for inner iterations (self-scattering). Default:
1e-5.
– ThermalsPrecision <float>: convergence criterion for thermal iterations. Default: 1e-5.
– AccEqPrecision <float>: convergence criterion for acceleration (which drives the convergence
in each group, in the thermals and in the outers).
Default: 1e-4.
The value of this
parameter should be at most, roughly, of the order of the smallest of ThermalsPrecision,
FissionIntegralPrecision and InnersPrecision.
– MaxOuters:
maximum number of outer iterations.
This parameter is only relevant in
FIXED_SOURCES_CRITICALITY mode. Default: 50.
– MaxThermalsBeforeConvergence <integer>: maximum number of thermal iterations before
convergence of outer iterations; after the outer iterations have converged the value of MAX_THERMALS
is used. Default: 1. Good values are in the 1–5 range.
– MaxInnersBeforeConvergence <integer>: maximum number of inner iterations before convergence
of thermal iterations; after the thermal iterations have converged the value of MAX_INNERS is
used. Default: 1. Good values are in the 1–5 range.
• see the next section for the use of the ALLOW_IDT_IN_PARALLEL keyword.

## 20.4 CAVEATS

A few important points about the usage of IDT must be brought to the attention of the reader.
• The mesh cells containing the adjoint source are determined by checking if the center of the cell falls
within the TARGET score region (volume or extended mesh). In the case of a small detector volume, it
is possible that no cell center falls into the detector region. In this case, TRIPOLI-4 will emit an error.
Refining the mesh around the detector region should fix the error. It is often also possible to slightly
displace the whole mesh in such a way that the center of at least one cell falls into the detector.
• If more than one TARGET score is requested, TRIPOLI-4 will not emit an error as long as at least one
detector region contains one cell center. In this case, detectors that do not contain any cell center may
be silently ignored from the adjoint source. If you want to make sure that all your detectors are correctly
picked up by IDT, you can check the generated IDT input file. Alternatively, you can run replace the
list of TARGET scores with one score at a time and check that TRIPOLI-4 is picking it up correctly (i.e.
no error message is emitted).
• It is of the utmost importance to make sure that the space discretization used by IDT is converged.
A coarse calculation mesh will result in inaccurate importance maps at best, and unphysical maps at
worst. The user can ensure that the internal calculation mesh is sufficiently fine either by setting the
max optical thickness parameter to a moderately small value (of the order of 1) or by refining the mesh
by hand. However, in case the max optical thickness parameter is used, the importance map produced
by IDT will be homogenized onto the user-provided TRIPOLI-4 mesh for the transport phase. This

<!-- page 282 -->
throws away most of the advantage of using a finely discretized importance map. Since the memory
requirements are anyway dominated by the IDT resolution phase, it is recommended to set the max
optical thickness to a large value, such as 1000. This will practically prevent IDT from automatically
refining the internal calculation mesh and force it to use the user-defined mesh. It is also recommended
to study the convergence of the space discretization by manually refining the mesh and verifying the
stability of the importance map with respect to small changes in the discretization coarseness. Note that
convergence is expected to require cell optical thicknesses of the order of 1. This typically means using
much finer meshes than those required by INIPOND (Chapter 17).
• The energy convergence of the IDT calculation can be studied by inspecting its output file (filename
<input_file>_idt.listing). It is recommended to check the following points:
– The maximum number of inner iterations (MAX_INNERS keyword) should not be reached in any
group, at least during the last thermal iteration, or the last outer iteration for fixed-source problems
with fission (FIXED_SOURCES_CRITICALITY, see Chapter 22). The maximum number is also
echoed at the beginning of the output file.
– The maximum number of thermal iterations (MAX_THERMALS keyword) should not be reached. The
maximum number is also echoed at the beginning of the output file.
– The maximum number of outer iterations (for fixed-source problems with fission) should not be
reached. The maximum number is given at the beginning of the output file.
If any of these numbers are actually reached, it is likely that the IDT calculation has not converged.
A warning message of the form “THERE ARE UNSATISFIED CONVERGENCE CRITERIA”. Increasing the
maximum number of iterations may help.
• In case the max optical thickness parameter is used, note that internal mesh refinement performed by
IDT does not resolve any heterogeneity in the TRIPOLI-4 cell. That is, if a user-provided mesh cell
contains several materials, IDT will still consider the cell as homogeneous (using the material found at
the center), even if the internal calculation mesh is refined.
• In adjoint calculations, the thermal adjoint flux influences the fast adjoint flux. This is the opposite of
what happens in direct calculations. If your detector is sensitive to thermal neutrons, you should pay
careful attention to the convergence of thermal iterations (see MAX_THERMALS and ThermalsPrecision
above).
• By default, IDT uses internal shared-memory parallelism to accelerate the resolution of the adjoint
problem. The number of threads used by IDT is typically equal to 8.
• The maximum number of threads used by IDT can be set with the OMP_NUM_THREADS environment
variable. IDT will never use more threads than the value given in OMP_NUM_THREADS if it is defined, and
it may use fewer. As mentioned above, there is little gain in setting OMP_NUM_THREADS to a value larger
than 8.
• Because of IDT’s shared-memory parallelization, it is forbidden by default to run IDT in a parallel
TRIPOLI-4 calculation (see Chapter 33). The recommended way to run a parallel TRIPOLI-4 calculation

<!-- page 283 -->
with an IDT importance map is to generate the map in a mono-processor calculation, write it to a
file using the STORE_IN_FILE keyword, and reuse it with USE_FILE (Chapter 17). However, if you
know what you are doing, you can use the ALLOW_IDT_IN_PARALLEL keyword to run IDT in a parallel
calculation.
• If the FILE keyword of the MICROSCOPIC_CROSS_SECTIONS block is used, then care must be taken
to ensure that all nuclides use the same microscopic cross-section energy grid.
The correct grid
must also be declared in the GRID keyword of the VARIANCE_REDUCTION block; consider using the
FROM_IDT_XS_FILE keyword.
• The IDT input file is always written to a file (filename <input_file>_idt.d), so that it can be inspected
.
By default, the importance map is not written to a file, unless the user requests it with
STORE_IN_FILE.
• When using the IDT block, TRIPOLI-4 always uses the exponential transform as a variance-reduction
technique. However, importance maps written to external files (STORE_IN_FILE) may be suitable for
the use with other variance-reduction techniques (Adaptive Multilevel Splitting, see Chapter 18; weight
windows, see Chapter 19).
• Weight adjustment of the importance map (MONITORING keyword) is automatically disabled when using
IDT.

## 20.5 EXAMPLE

Here is a full example of the VARIANCE_REDUCTION block for a neutron CADIS calculation:
VARIANCE_REDUCTION
NEUTRON
GRID FROM_IDT_XS_T4PATH
MINIMAL_IMPORTANCE 1e-35
MESH_VARIABLE
60 60 20
0 4 80.001 52 240.001 4 320.002
0 4 80.001 52 240.001 4 320.002
0 20 100.002
3
FRAME CARTESIAN
-160.001 -160.001 -50.001
1 0 0
0 1 0
0 0 1
END_MESH_VARIABLE
IDT
TARGET 1 DOSE_N_SPHERE
CONVERGENCE FIXED 100.0 8

<!-- page 284 -->
MAX_INNERS 200
SPECTRUM RESPONSE NAME DOSE_N
END_IDT
STORE_IN_FILE ASCII
END_VARIANCE_REDUCTION
