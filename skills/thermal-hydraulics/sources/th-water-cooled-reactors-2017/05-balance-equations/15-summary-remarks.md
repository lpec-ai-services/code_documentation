# Summary remarks
<!-- source PDF pages 75-78 -->

<!-- page 241 (PDF 75) -->
5.15
Summary remarks
The equations at the basis of computational tools adopted for transient analysis of
water-cooled nuclear reactors have been presented. Those equations have a broad
validity which derives from their origin, i.e., the principles of thermodynamics and
mechanics. Continuum body assumption is invoked in order to translate the principles
into workable equations for fluids either single- or multiple phase.
The process for development of the equations has been outlined in this chapter
starting from the fundamentals and involving steps of increasing complexity. The
set of six PDEs dealing with steam and water mixture is also known as unequal velocity
unequal temperature (UVUT): qualified sets of UVUT-PDE, including the constitutive
/closure equations (Chapter 9), which are implemented in current system
thermal-hydraulic codes, shall be considered the key outcome of decades of research
in nuclear thermal-hydraulics (Chapter 2); the same equations also constitute a synthesis
of knowledge and the state of the art in the area.
Time and space averaging constitute at the same time unavoidable processes for
achieving a solution and sources of approximations in the results of the numerical integration
which are difficult to be quantified.
Nevertheless the translation of the equations into the algebraic form necessary for
numerical computation and the solution of the algebraic equations have been marginally
considered in this chapter (more information is given in Chapter 11).
The distinction between open and porous media modeling approaches is discussed:
the former deals with the CFD-like codes and includes the DNS codes; the latter deals
with system thermal-hydraulics and may be characterized by the amount and type of
closure models (i.e., including constitutive equations) which are needed for achieving
a solution. Actually, only in the case of single-phase DNS, closure models can be
avoided for predicting fluid transient evolutions at the expenses of computational
power that is impractical for NPP applications. More information about current
CFD models can be found in Chapter 12.
Special topics related to the nature and the structure of the balance equations are
also considered in the present chapter. These are listed below together with summary
notes:
(a) The HEM also called equal velocity equal temperature (EVET): steam and liquid form a
compressible fluid.
(b) The drift flux model: this can be considered an attempt to establish a relationship between
liquid and steam velocities in a gravity environment; the drift flux model, as conceived in
the 1960s, can be derived by introducing approximations to the UVUT momentum equation.
(c) The hyperbolicity of the solution: the issue of hyperbolicity is connected with the numeric
solution of the UVUT set of equations and has been thoroughly investigated for the case
of 1-D models. Nonhyperbolicity or lack of hyperbolicity of a set of equations implies
non-realrootsforthecharacteristicequationandmaycauseabortionofacalculationprocess.
(d) The CFD modeling: this is considered by the paragraph above and included in this list for
the sake of completeness.

<!-- page 242 (PDF 76) -->
(e) The Transport of Interfacial Area: efforts in the last two decades attempting to introduce an
additional equation (and additional unknown) to the existing set of balance equations did
not demonstrate yet to be able to catch the complex two-phase phenomena even in a limited
range of conditions, noticeably droplet and bubbly flows, considered in modeling. The
polydispersed modeling approach may reveal more promising in this area.
(f ) The 3-D modeling: all major thermal-hydraulic system codes have a three-dimensional
modeling capability; however, systematic and comprehensive validation demonstrations
are not achieved. Differences in relation to 3-D open media and porous media approaches
are important, as discussed in the chapter.
(g) The multifield modeling: the complex nature of two-phase flow imposes the consideration
of multifields in modeling. The capability appears important for modeling of reflood, with
main reference to the flow configuration from the quench front where droplets are entrained
up to upper plenum, hot legs, and steam generators where they can deposit and vaporize.
This complex behavior has an important impact on the overall reflooding process.
It may be noted that the last three topics constitute areas for current research in relation
to which industrial applications are not fully mature at the time of this writing.
Furthermore, a problem common to the TIA approach, the 3-D modeling (at least
in porous media) and the multifield modeling, derives from the difficulty in utilizing
the huge and expensive experimental data base available in nuclear thermalhydraulics
(see Chapter 6): the same level of information from experiments which
is suited for 1-D modeling needs to be extended to more complex modeling approach.
New experimental programs with advanced local measurement techniques are then
necessary.
This chapter constitutes a hinge, or has the pivot role, for all the chapters. Namely,
the development of equations is the technology response to needs established in
Chapter 4 within the framework in nuclear thermal-hydraulics set by Chapters 1–3.
The equations in this chapter are supplemented by constitutive/closure equations in
Chapter 9 and constitute the basis for the code discussed in Chapter 11. The code must
have the capability to predict phenomena in Chapter 6 and shall undergo the process of
validation discussed in Chapter 13. The envisaged framework for code applications
and the results from calculation of transient scenarios are discussed in Chapters 14
and 15, respectively.
References
Bestion, D., 1990. The physical closure laws in the Cathare code. Nucl. Eng. Des. 124, 229–245.
Bestion, D., 2014. The difficult challenge of a two-phase CFD model for all flow regimes. Nucl.
Eng. Des. 279, iv–v.
Bestion, D., Serre, G., 2012. On the modelling of two-phase Flow in horizontal legs of a PWR.
Nucl. Eng. Technol. 44, 8.
Bestion, D., Serre, G., 2013. Transport of interfacial area in system codes: status and perspectives
. In: NURETH-15, Pisa, 12–15 May.
Bestion, D., Coste, P., Niceno, B., Mimouni, S., Lakehal, D., Bartosiewicz, Y., 2011.
Two-phase CFD: the various approaches and their applicability to each flow regime. Multiph
. Sci. Technol. 23 (2–4), 101–128.

<!-- page 243 (PDF 77) -->
Bois, G., Jamet, D., Lebaigue, O., 2010. Towards large eddy simulation of two-phase flow with
phase-change: direct numerical simulation of a pseudo-turbulent two-phase condensing
flow. In: 7th International Conference on Multiphase Flow, ICMF 2010, Tampa, FL,
30 May–4 June.
Boure, J.A., 1975. On a unified presentation of the non-equilibrium two-phase flow model. In:
Lahey Jr., R.T., Wallis, G.B. (Eds.), ASME Annual Winter Meeting, Houston, TX.
de Crecy, F., 1986. Modeling of stratified two-phase flow in pipes, pumps and other devices. Int.
J. Multiphase Flow 12, 307–323.
Delhaye, J.M., Giot, M., Riethmuller, M.L., 1981. Thermohydraulics of Two-Phase Systems for
Industrial Design and Nuclear Engineering. McGraw-Hill, New York.
Dhotre, M.T., Smith, B., Niceno, B., 2007. CFD simulation of bubbly flows: random dispersion
model. Chem. Eng. Sci. 62, 7140–7150.
Dhotre, M.T., Niceno, B., Smith, B., 2008. Large eddy simulation of a bubble column using
dynamic sub-grid scale model. Chem. Eng. J. 136, 337–348.
Ishii, M., Hibiki, T., 2011. Thermo-Fluid Dynamics of Two-Phase Flow, second ed. Springer,
New york.
Koncar, B., Morel, C., Mimouni, S., Vyskocil, L., Galassi, M.C., 2011. CFD modeling of boiling
bubbly flow for DNB investigations. Multiph. Sci. Technol. 23(2–4).
Krepper, E., Morel, C., Niceno, B., Ruyer, P., 2011. CFD modelling of adiabatic bubbly flow.
Multiph. Sci. Technol. 23, 2–4.
Lahey Jr., R.T., Moody, F.J., 1993. The Thermal-hydraulics of a Boiling Water Reactor. ANS
Monograph, Hinsdale, IL.
Lakehal, D., 2002. On the modelling of multiphase turbulent flows for environmental and
hydrodynamic applications. Int. J. Multiphase Flow 28, 823–863.
Lakehal, D., 2008. LEIS for the prediction of turbulent multifluid flows applied to thermal
hydraulics applications. In: Int. Meet XCFD4NRS, Grenoble, 10–12 September.
Lakehal, D., 2010. LEIS for the prediction of turbulent multifluid flows applied to thermalhydraulics
applications. Nucl. Eng. Des. 240, 2096–2106.
Lakehal, D., Labois, M., 2011. A new modelling strategy for phase-change heat transfer in turbulent
. Int. J. Multiphase Flow 37, 627–639.
Lakehal, D., Fulgosi, M., Banerjee, S., Yadigaroglu, G., 2008. Turbulence and heat transfer in
condensing vapor-liquid flow. Phys. Fluids 20.
Lerchl, G., Austcberegesilo, H., 2013. ATHLET Mod 3.0 Cycle A.—models and methods.
In: GRS-P-1/Vol. 4, Garching, July.
Lilly, D.K., 1991. A proposed modification of the Germano Subgrid-Scale Closure Method.
Phys. Fluids A 4 (3), 633–635.
Lucas, D., Coste, P., H€ohne, T., Lakehal, D., Bartosiewicz, Y., Bestion, D., Scheuerer, M.,
Galassi, M.C., 2011. CFD modeling of free surface flow with and without condensation.
Multiph. Sci. Technol. 23(2–4).
Magdeleine, S., Mathieu, B., Lebaigue, O., Morel, C., 2010. DNS up-scaling applied to volumetric
interfacial area transport equation. In: 7th International Conference on Multiphase
Flow (ICMF 2010), Tampa, FL, 30 May–4 June.
Mahaffy, J. (Ed.), 2007. Best Practice Guidelines for the Use of CFD in Nuclear Reactor Safety
Applications.OECD,NuclearEnergy Agency,Paris Technical Report, NEA/CSNI/R(2007)5.
Morel, C., 2015. Mathematical Modelling of Disperse Two-Phase Flow. Springer-Verlag,
Cham, Switzerland.
Niceno, B., Dhotre, M.T., Deen, N.G., 2008. One equation sub-grid scale (SGS) modeling for
Euler-Euler large eddy simulation (EELES) of dispersed bubbly flow. Chem. Eng. Sci.
63, 3923–3931.

<!-- page 244 (PDF 78) -->
Nicˇeno, B., Boucker, M., Smith, B.L., 2009. Euler-Euler large eddy simulation of a square
cross-sectional bubble column using the neptune CFD code. Sci. Technol. Nucl. Ins.
RELAP5/MOD3, 1998. Code manual volume I: code structure, system models and solution procedure
. In: NUREG/CR-5535. USNRC, Washington, DC.
Stuhmiller, J.H., 1977. The influence of interfacial pressure forces on the character of two-phase
flow model equations. Int. J. Multiphase Flow 3, 551–560.
Toutant, A., Chandesris, M., Jamet, D., Lebaigue, O., 2009a. Jump conditions for filtered quantities
at an under resolved interface. Part 1: theoretical development. Int. J. Multiphase
Flow 35 (12), 1100–1118.
Toutant, A., Chandesris, M., Jamet, D., Lebaigue, O., 2009b. Jump conditions for filtered quantities
at an under resolved interface. Part 2: a priori tests. Int. J. Multiphase Flow 35 (12),
1119–1129.
TRACE V5.0, 2007. Theory Manual—Field Equations, Solution Methods and Physical Models,
USNRC, Washington, DC.
Valette, M., Pouvreau, J., Bestion, D., Emonot, P., 2009. Revisiting large break LOCA with the
CATHARE 3 three field model. In: NURETH 13, Kanazawa, 27 September–2 October.
Zaepffel, D., Morel, C., Lhuillier, D., 2012. A multi-size model for boiling bubbly flows. Multiph
. Sci. Technol. 24 (2), 105–179.
Zuber, N., Findlay, J.L., 1965. Average volumetric concentration in two-phase systems. J. Heat
Transf. 453–468.
