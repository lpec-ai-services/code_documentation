# 6. THERMAL HYDRAULICS OF ACCIDENTS AND TRANSIENTS IN LIQUID METAL FAST REACTORS
<!-- source PDF pages 47-51 -->

<!-- page 35 (PDF 47) -->
# 6. THERMAL HYDRAULICS OF ACCIDENTS AND TRANSIENTS IN LIQUID METAL FAST REACTORS

## 6.1. DEFENCE IN DEPTH AND THERMAL HYDRAULICS

Six papers were presented in Track 4 of the IAEA Technical Meeting on
State-of-the-art Thermal Hydraulics of Fast Reactors [2]. Three of them were
devoted to liquid heavy metal cooled fast reactors (lead and lead bismuth) and
three to sodium cooled fast reactors (SFRs). This section is focused on thermal
hydraulics under transient conditions in LMFRs.3
The IAEA defines the concept of ‘defence in depth’ (DiD) as
“a comprehensive approach to safety that has been developed by nuclear
power experts to ensure with high confidence that the public and the
environment are protected from any hazards posed by the use of nuclear
power for the generation of electricity” [120].
The thermal hydraulics phenomena of a nuclear reactor are usually defined
in its phenomena identification and ranking table (PIRT) for each accident or
transient scenario. Some important phenomena are highlighted in this section.

## 6.2. OPERATIONAL TRANSIENTS

The first level of DiD, ‘prevention of abnormal operation and failures’,
involves the implementation of measures to prevent accidents from occurring in
the first place. This includes the use of high quality components and materials,
strict design and construction standards, and regular maintenance and inspections.
The second level of DiD, ‘control of abnormal operation and detection of
failures,’ detects failures and avoids or controls abnormal operation [120]. If it
is successful, the plant will return to normal operation after recovery from the
failure. Operational transients of plants belong to the second level of DiD.
The thermal hydraulics of operational transients include the following:
— Single phase circulation of coolants;
— Heat exchange in primary and secondary systems;
— Thermal stresses in reactor structures;
— Operation of control systems.
3	 Gas cooled and molten salt reactors are not covered in this section.

<!-- page 36 (PDF 48) -->
## 6.3. DESIGN BASIS ACCIDENTS

The third level of DiD, ‘control of accidents within the design basis’ [120],
involves the use of active or passive safety systems, procedures and human
intervention to mitigate the consequences of accidents that may occur despite the
preventive measures in place. This includes the use of emergency response plans,
backup power systems and redundant safety systems.
In spite of the dependence of the thermal hydraulics of design basis
accidents (DBAs) on the reactor design and its safety systems, there are common
representative phenomena, which include the following:
— Transition from forced to natural convection in the primary and secondary
systems;
— Operation of passive reactor shutdown systems, activated by temperature
increase or flow rate decrease;
— Fuel bundle heat transfer during power excursion.
As an example of DBA modelling, Lee et al. [121] performed an analysis
of several DBAs, including protected station blackout and protected transient
overpower for the Westinghouse lead cooled fast reactor (LFR), using the
SAS4A/SASSYS-1 code for reactor primary system modelling and the GOTHIC
package for passive heat removal systems.
Activities that are important for creating new knowledge in the area of DBA
thermal hydraulics include coupled neutronic and thermal hydraulic modelling
of various initiating events, as well as experimental studies providing data for
validating the modelling tools. As an example of the latter, Mariani et al. [122]
reported the experimental and numerical activities performed to investigate
thermal hydraulic phenomena occurring in response to hypothetical accident
scenarios (protected loss of heat sink and protected loss of flow) and the heat
transfer in the LBE cooled fuel pin bundle simulator of the CIRCE facility.

## 6.4. SEVERE ACCIDENTS

The fourth level of DiD, ‘mitigation of radiological consequences of
accidents beyond the design basis’ [120], involves measures to limit the release
of radioactive material into the environment in the event of a severe accident that
exceeds the design basis. This includes the use of passive safety systems, such
as containment structures and radiation shielding, as well as off-site emergency
response plans and communication with the public. Severe accidents vary

<!-- page 37 (PDF 49) -->
between SFRs and LFRs, even among reactors of the same type, because of the
design differences among the reactors and variations in their mitigation systems.
Although severe accident scenarios among different reactors may not be
similar, some representative thermal hydraulics phenomena found in severe
accidents could be considered, such as the following:
— Fuel assembly blockage;
— Coolant boiling (sodium cooled reactors);
— Fuel and cladding melting and relocation;
— Fuel–coolant interaction;
— Corium behaviour (sodium cooled reactors);
— Source term evaluation;
— Vapour bubble entrainment to core (LFRs).
As an example of a flow blockage study, prototypical tests were carried
out by Martelli et al. [123] to address flow blockage in the fuel subassemblies
of ALFRED — a pool type LFR designed to demonstrate the safety and
competitiveness of Generation IV LFR technology. CFD numerical simulations
were used to validate the results. Both experiments and simulations showed two
main effects of blockage: a local maximum in temperature behind the blockage
and an overall maximum at the end of the active region. Unsteady RANS
simulations provided better agreement with the experimental data, indicating
that a more accurate approach, like a LES simulation, could further reduce the
difference from the experimental results.
Concerning the phenomenology of sodium boiling, Sorokin et al. [124]
conducted experiments at a three circuit liquid metal facility to study Na and
NaK liquid metal boiling in model fuel assemblies under natural convection
regimes. Although steady, bubbly boiling is observed only in a limited region
of heat fluxes, transitions to unstable pulsed plug boiling are determined by
various factors. Decreases in surface roughness promote boiling instabilities
and heat transfer crises. The hydrodynamic interaction of circuits can lead to a
significant increase in the amplitude of flow rate fluctuations, thereby increasing
the probability of a heat transfer crisis. Boiling heat transfer coefficients in fuel
rod lattices are similar to those in pipes and pools. The modified SABENA-3D
code can simulate heat transfer and hydrodynamic stability.
Modelling of fuel and cladding melting and relocation, as well as
fuel–coolant interactions, has been conducted by Chen and Rineiski [125]
using the SIMMER-III code. This code was developed mainly for simulation of
hypothetical reactor accidents after core melting, but it can also be applied to
accident initiation phase simulations in sodium and other LMFRs. New thermal
hydraulic and neutronic simulation approaches and models have been developed

<!-- page 38 (PDF 50) -->
for the treatment of the initiation phase, and the modified code was used for the
simulation of unprotected loss of coolant flow transients in the ESFR-SMART
and Fast Flux Test Facility (FFTF) reactors. It can be concluded that the SIMMER
code has significant potential for application in initiation phase analyses.

## 6.5. DECAY HEAT REMOVAL

The heat removal safety function is designed to prevent the core from
overheating, which could potentially lead to a meltdown. In normal operation,
the heat generated in the reactor core is transferred by a primary coolant to a
heat exchanger, where it is further transferred to a secondary coolant system.
In addition to the main heat removal path, any reactor is equipped with several
systems for decay heat4 removal. A significant source of heat in a reactor, decay
heat can represent up to 5% of the reactor’s full power heat output immediately
after shutdown. The decay heat gradually decreases over time as the radioactive
isotopes decay, but it can still produce enough heat to potentially cause damage
to the reactor if it is not removed at an acceptable temperature. Important
characteristics of the decay heat removal systems are redundancy, passivity and
backup power sources. In addition, the heat removal safety function includes
various monitoring and control systems to ensure that the heat removal process
is operating correctly. For example, temperature sensors and flowmeters are used
to monitor the temperature and flow rate of the coolant, and if any abnormalities
are detected, the reactor will automatically shut down and/or additional safety
measures will be activated. With the increasing adoption of passive cooling
systems in LMFRs, the thermal hydraulics behaviours of these passive cooling
systems is a focus of R&D, including both testing and analysis.
The following phenomena can be classified as related to the thermal
hydraulic aspects of decay heat removal:
— Activation and operation of passive and active decay heat removal systems;
— Natural circulation of cooling fluid in the passive safety system;
— Instrumentation and control for monitoring the thermal hydraulic
parameters of the coolant during decay heat removal.
As an example of modelling a passive decay heat removal system,
Lee et al. [121] analysed the performance of a passive heat removal system in the
Westinghouse LFR, using the GOTHIC package.
4	 ‘Decay heat’ refers to the heat produced by the radioactive decay of the
fission products and the actinides in the fuel after the reactor has been shut down.

<!-- page 39 (PDF 51) -->
## 6.6. FUNCTIONAL CONTAINMENT THERMAL HYDRAULICS

The functional containment5 safety function in an LMFR is an important
safety feature that is designed to prevent the release of radioactive material
from the reactor in the event of an accident or malfunction. The functional
containment system includes several barriers between the radioactive source and
the environment to prevent the release of radioactive material in the event of a
DBA or severe accident. These barriers include the fuel matrix, fuel cladding,
liquid metal pool, primary system barriers and the containment or confinement
itself, which is typically a large, steel or reinforced concrete structure surrounding
the reactor vessel and associated equipment. Figure 5 illustrates the functional
containment of a representative LMFR. For sodium cooled reactors, since sodium
is highly reactive with air and water and can ignite or explode if it comes into
contact with them, it is especially important to have a robust barrier to prevent
the release of primary radioactive sodium.
The functional containment thermal hydraulics varies among reactors, but
representative phenomena could be related to the following:
— Fission product release from the fuel rods;
— Radionuclide decontamination in the liquid metal pool;
— Transport of radioactive materials in the primary system, in the containment
and in the environment;
— Activation and operation of mitigation devices such as filters;
— Sodium fires.
Louie et al. [126] conducted a numerical study of a sodium discharge
into containment from an SFR vessel. Such an accident can lead to the sodium
spray fire and pool fire phases, which are important to study because of the
heat addition, aerosol generation and potential release of fission products. An
international collaborative research project between Japan and the USA aimed
to enhance the validation basis and modelling capabilities of sodium spray and
pool fires in the MELCOR and SPHINCS codes. The study documents the
validation of the MELCOR and SPHINCS sodium pool fire models against the
Japan Atomic Energy Agency’s sodium pool fire experiments, F7-1 and F7-2,
and proposes the addition of thermal hydraulic and sodium spreading models to
better represent the experimental results.
5	 ‘Functional containment’ represents multiple barriers, that is, more than
traditional containment. It functions for both design basis accidents and beyond
design basis accidents.
