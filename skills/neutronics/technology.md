# Technology branch: how a PWR is built and operated

Source: **P** = `sources/marguet-technologie-rep-2019/`: S. Marguet, *La technologie des réacteurs à eau pressurisée* (EDF R&D scientific publishing, 2019, 1161 pages), in French, focused on the French fleet (CP0 to N4, EPR). Pages are printed pages, with every section in the source's `TOC.md`. Reactor-type overviews in English: Stacey (S) ch. 7.

French acronyms (RCV, RIS, RRA, ASG…) are defined in the dictionary of acronyms (Annexe 1, p. 1053) and listed in §7.22, *Trigrammes des circuits* (p. 968).

| Topic | Where |
|---|---|
| **History of the PWR line**: naval reactors, Shippingport, Yankee Rowe, BR3, Tihange, Sizewell B, **VVER**, the French fleet, plutonium recycling (MOX), **EPR** | P ch. 1, pp. 3–186 |
| **Buildings**: French plant series (paliers), nuclear island, reactor building and containment, fuel building, **fuel handling**, contamination hot spots, auxiliaries building, **control room** | P ch. 2, pp. 187–282 |
| **Primary circuit**: layout, temperature/pressure/flow/power, **primary chemistry** (boron, lithium, hydrogen), activity, **reactor coolant pumps**, **pressurizer**, **steam generators (primary side)**, nozzles and thermal sleeves, primary regulations | P ch. 3, pp. 283–444 |
| **Reactor vessel and internals**: nozzles, supports, head, lower/upper internals, bypass, baffle, thermal shield, bottom penetrations, **surveillance programme** (irradiation embrittlement), water level, opening for refuelling, in-service inspection | P ch. 4, pp. 445–534 |
| **Core and fuel**: loading/unloading, active core, **fuel (pellets, rods, assemblies)**, **control rod system (RGL)**, start-up sources, **core monitoring (in-core and ex-core instrumentation)**, **fuel management**, **loading-pattern search** | P ch. 5, pp. 535–690 |
| **Secondary circuit**: water chemistry, steam generator secondary side, turbine (steam aspects), moisture separator reheaters, valves, **condenser**, feedwater heaters, deaerator, turbine bypass, feed pumps, **flow-accelerated corrosion**, heat sink | P ch. 6, pp. 691–842 |
| **Main auxiliary and safety systems**: chemical and volume control (RCV), boron/water make-up (REA), **residual heat removal (RRA)**, **safety injection (RIS)**, component cooling (RRI), sampling, main steam (VVP), atmospheric dump, feedwater (ARE), **auxiliary feedwater (ASG)**, **containment spray (EAS)**, pool cooling, effluents, ventilation, I&C (KIC), circuit acronyms | P ch. 7, pp. 843–978 |
| **Turbine-generator and electricity**: machine hall, turbine, alternator, transformers, auxiliary power, **emergency diesel generators**, example of loss of power (Dampierre 2007) | P ch. 8, pp. 979–1050 |
| Annexes: acronyms; performance of French units by series (CP0, CPY, P4, P'4, N4); pressure-equipment regulations | P Annexe, pp. 1053–1094 |

## How to use it

- Physics questions (k_eff, feedback, xenon) belong to `physics.md`. This branch answers "what is this component, how is it designed, how is it operated, what are its parameters".
- For transients and accident thermal-hydraulics (LOCA, SGTR, SBO), use the `thermal-hydraulics` skill. This book describes the systems involved (RIS, ASG, EAS…).
- Answer in the user's language. Keep French system acronyms and give the English equivalent (e.g. RIS = safety injection system).
