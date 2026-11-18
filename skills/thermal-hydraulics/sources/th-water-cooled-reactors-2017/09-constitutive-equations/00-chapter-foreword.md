# Chapter foreword
<!-- source PDF pages 1-2 -->

<!-- page 549 (PDF 1) -->
J.J. Jeong
Pusan National University, Pusan, South Korea
Abstract
The concept of constitutive equations is strictly linked with the modeling in two-phase
nuclear thermal-hydraulics. This is specifically true for the commonly adopted “unequalvelocity
, unequal-temperature” (UVUT) models. Constitutive equations or closure
models are embedded into balance equations. Here one may distinguish within the broad
category of closure equations (i.e., all the equations needed to solve the balance equations
) the constitutive equations, as those equations derived from experiment. In this case
constitutive equations have an empirical or a semiempirical nature. Closure equations
aim at the numerical simulation of the phenomena in nuclear thermal-hydraulics. Constitutive
equations are discussed in the present chapter making specific reference to
models adopted in the current system thermal-hydraulic codes.
Chapter foreword
The concept of constitutive equations is strictly linked with the modeling in two-phase
nuclear thermal-hydraulics. Balance equations derived from basic principles and discussed
in Chapter 5 of the book cannot be solved without closure and/or constitutive
equations. Here one may distinguish within the broad category of closure equations
(i.e., all the equations needed to solve the balance equations) the constitutive equations
, as those equations derived from experiment. In this case constitutive equations
have an empirical or a semiempirical nature. Constitutive equations are discussed in
the present chapter, making specific reference to models adopted in the current system
thermal-hydraulic codes.
The understanding of this chapter is essential for the reader in order to develop his
own idea in relation to the capabilities and the limitations of the current system
thermal-hydraulics codes discussed in Chapter 11. Constitutive equations and related
modeling are connected with geometry of the system and are part of the scaling issue
in system thermal-hydraulics (also discussed in Chapter 11).
Furthermore, constitutive equations also constitute: (a) one motivation and origin
of uncertainty, discussed in Chapter 13; (b) an area needing continuous development
in the future including planning of new experiments.
9.1
Introduction
There are various mathematical models that have been developed for a two-phase
flow, such as homogeneous equilibrium model, drift-flux model, two-fluid model
Thermal Hydraulics in Water-Cooled Nuclear Reactors. http://dx.doi.org/10.1016/B978-0-08-100662-7.00009-9
© 2017 Elsevier Ltd. All rights reserved.

<!-- page 550 (PDF 2) -->
(known as the unequal-velocity unequal-temperature model or six-equation model),
two-fluid three-field model (Frepoli et al., 2003), and two-fluid four-field model
(Lahey and Drew, 2001). Each of these models was derived from the first principles
of thermodynamics and mechanics under its own assumptions for simplification.
Among these models, the one-dimensional two-fluid six-equation model has
been adopted in most of the state-of-the-art system thermal-hydraulic (TH) codes,
such as RELAP5/MOD3 (USNRC, 1998a,b), RELAP5-3D (Idaho National Lab.,
2001, 2012a,b), TRAC-PF1 (Liles et al., 1988; Spore et al., 1993), TRACE V5
(USNRC, 2013), CATHARE 2 (Bestion, 1990), and MARS (Jeong et al., 1999).
In the two-fluid six-equation model, the mass, energy, and momentum balance
equations for liquid and vapor/gas mixture phases are established separately. The
six equations are represented in differential form, with time and one space dimension
as independent variables, and in terms of time and volume-average dependent variables
. Each phase in the two-fluid model has two interfaces, see Fig. 9.1A:
l
A variable interface between the two phases, where heat, mass, and momentum
transfer occur.
l
An interface with the fixed wall, where heat and momentum transfer occur.
The mathematical models used to represent the interface transfer phenomena in terms
of time and volume-averaged dependent variables are called constitutive equations.
The term “constitutive equations” is associated with a specific set of governing equations
. For the two-fluid model, they link the six governing equations, leading to
“mathematical closure” together with state equations (Meyer et al, 1967; Haar
et al., 1984; Watanabe and Dooley, 1996; Harvey et al., 2000; Lemmon et al., 2010).
In this chapter, the constitutive equations of the two-fluid models, selected from
RELAP5/MOD3 (hereafter, RELAP5), RELAP5-3D, TRACE V5, or CATHARE 2,
are briefly presented and discussed. For the readers who want to compare with those
ofothersystemcodes,includingRELAP-7,WCOBRA/TRAC,TRAC-M,andATHLET,
the review papers by Roth and Aydogan (2014a,b) are recommended. They provided a
systematic comparison of various system TH codes and discussed their governing equations
, closure relations, numerical solutions, and code validation and limitations.
Some system TH codes, such as WCOBRA/TRAC (Thurgood and George, 1983),
SPACE (Ha et al., 2011), and CATHARE 3 (Emonot et al., 2009; Bassenghi, 2013),
use the two-fluid three-field model for two-phase flows, where there are three additional
interfaces, as shown in Fig. 9.1B, because of the separate modeling of entrained
liquid (i.e., droplets). Thus, additional constitutive equations are needed for droplet
Liquid
Vapor/gas
(A)
(B)
Wall
Continuous liquid
Droplets
Vapor/gas
Wall
Fig. 9.1 Interfaces in
(A) the two-fluid model and
(B) the two-fluid
three-field model.
