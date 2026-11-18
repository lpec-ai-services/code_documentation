<!-- source: https://manta-project.gitlab.io/manta/theory_manual/fluid_mechanics/critical_flow.html -->

# Critical flow

Pipe rupture causes a sudden depressurization of the fluid in the circuit. During the transient phase, pressure waves propagate through the circuit. At the same time, the fluid velocity increases gradually. The fluid flow rate depends on the upstream conditions and those at the break. Under certain conditions, a critical regime can occur, limiting the flow rate. When the downstream pressure at the leak decreases, the upstream pressure being fixed, the fluid flow rate increases gradually until the pressure at the leak equals a **critical pressure**. If the downstream pressure at the leak continues to decrease, the flow rate remains constant.

In the case of a two-phase flow, the phenomena can lead to important phase change (from liquid to vapor in the case of water) that modifies the mass of the moving fluid impacting the motion of the broken pipe ends (pipe whipping). This phenomena must be modeled with care to help designing the facilities and ensure their safety. To that end, in the case of wireframe (1D) pipe models, it is necessary to use critical flow models to enforce the correct boundary condition. These models are presented hereafter for perfect gas and for two-phase flow and for liquid.

Note

This document is a slightly modified English translation of §2, §3 and §4 of [[Lep97](../../references/references.md#id55)].

## [Perfect gas](#id24)

### [Problem definition and assumptions](#id25)

The objective is to determine the properties of perfect gas flow through a modeled break at the end of a pipe, discharging into a large reservoir. The following assumptions are made :

- Steady-state flow is established
- One-dimensional flow i.e. the velocity \(V\), the pressure \(P\), the density \(\rho\), the temperature \(T\) in the gas over the whole cross section area \(A\) are constant
- The gas is perfect so that \(P=\rho R_s T\) (\(R_s\) is specific gas constant)
- Adiabatic flow without wall friction or heat input
- Body forces such as gravity are negligible

Indices are used as follows :

- Index \(1\) denotes fluid properties upstream of the break
- Index \(0^-\) denotes properties at the break

[![figure](https://manta-project.gitlab.io/manta/_images/critical_flow_break_schematic.png)](../../_images/critical_flow_break_schematic.png)

Fig. 113 Schematic of the break

The break is shown in [Fig. 113](#fig-critical-flow-break-schematic). There are two regions depicted :

- Upstream from \(A_1\) to \(A_0\)
- Downstream from \(A_{0^+}\) to \(A_2\)

### [Conservation equations](#id26)

In each of these regions and under the previously made assumptions, one can write the following conservation equations :

- **Conservation of mass** (here, the mass flow rate \(w\))
  :   (244)\[\text{d}w = 0\]

  Where the mass flow rate is \(w=\rho A V\).
- **Conservation of energy** (in fact Bernouilli's equation)
  :   (245)\[\text{d} \left( h + \frac{1}{2}V^2 \right) = 0\]

  Where, for a perfect gas, the enthalpy is \(h=\frac{\gamma}{\gamma-1} \frac{P}{\rho}\) and the adiabatic index (or isentropic coefficient) \(\gamma = 1.4\) for a diatomic gas.
- **Conservation of entropy**
  :   (246)\[\text{d} s = 0\]

  Where, for a perfect gas, the entropy is \(s=\frac{P}{\rho^\gamma}\). This is a strong assumption on the flow that implies that the process is reversible and adiabatic.

### [Upstream region](#id27)

In the upstream region, it leads to the following equations :

- **Conservation of mass** (from Eq. (244))
  :   (247)\[w = \rho_1 A_1 V_1 = \rho_{0^-} A_0 V_{0^-}\]
- **Conservation of energy** (from Eq. (245))
  :   (248)\[h_1 + \frac{V_1^2}{2} = h_{0^-} + \frac{V_{0^-}^2}{2}\]

      Where \(h\) is the specific internal enthalpy of the fluid and \(V\) is the fluid velocity.

      Where \(ρ\) is the fluid density. \(A_1\) is the cross-section of the fluid upstream of the break
      and \(A_0\) is the section corresponding to the size of the break.
- **Conservation of entropy** (from Eq. (246))
  :   (249)\[\frac{\rho_{0^-}}{\rho_1} = \left(\frac{P_{0^-}}{P_1}\right)^{\frac{1}{\gamma}}\]

After some mathematical manipulations using Eqs. [(245)](#equation-cenergy0), [(248)](#equation-cenergy) and [(249)](#equation-centropy), we can derive the fluid velocity at the break as a function of the upstream state (*Relation de Barré de Saint Venant*) :

(250)\[V_{0^-}^2 - V_1^2 = \frac{2\gamma}{\gamma-1} \frac{P_1}{\rho_1} \left[1 - \left(\frac{P_{0^-}}{P_1}\right)^{\frac{\gamma-1}{\gamma}}\right]\]

#### [Looking for the critical regime](#id28)

Let \(r\) be the opening ratio, defined as the ratio between the area at the outlet and the area of the upstream duct:

\[r = \frac{A_0}{A_1}, \quad r \in ]0, 1]\]

Let \(x\) be the ratio representing the depressurization at the break :

\[x = \frac{\rho_{0^-}}{\rho_1} = \left(\frac{P_{0^-}}{P_1}\right)^{\frac{1}{\gamma}}\]

Using Eq. [(247)](#equation-cmass), it leads \(\frac{V_{0^-}}{V_1} = \frac{\rho_1}{r\rho_{0^-}}\). Eq [(250)](#equation-veldiff) can then be expressed in terms of \(r\) and \(x\) as follows :

\[V_1^2 = \frac{2\gamma}{\gamma-1} \frac{P_1}{\rho_1} \frac{1 - {\frac{P_{0^-}}{P_1}}^{\frac{\gamma-1}{\gamma}}}{\frac{1}{r^2}\frac{\rho_1^2}{\rho_{0^-}^2}-1}\]

\[V_1^2 = \frac{2}{\gamma-1} C_1^2 r^2 x^2 \left(\frac{1-x^{\gamma-1}}{1-r^2 x^2} \right)\]

Where \(C_1 = \sqrt{\gamma \frac{P_1}{\rho_1}}\) is the speed of sound upstream of the break.

Assuming a fixed opening ratio \(r\), the desired mass flow rate \(w\) becomes a function that depends only on \(x\):

(251)\[\boxed{w = A_0 \rho_1 C_1 \sqrt{\frac{2}{\gamma - 1}}Z(x)}\]

Where :

(252)\[Z^{2}(x) =x^2\frac{1-x^{\gamma-1}}{1-r^2 x^2}\]

Mathematical analysis shows that :

- \(\lim_{x\to 0} Z(x) = 0\)
- \(\lim_{x\to 1} Z(x) = 0\)

Note

There is a particular case when \(r \to 1\) for a total opening, then the denominator tends towards infinity. In this case, it suffices to refer to Eqs [(247)](#equation-cmass), [(248)](#equation-cenergy) and [(249)](#equation-centropy). In that case, the outlet conditions are the same as upstream.

Therefore, there exists a value \(x_c\in ]0,1[\) such that the flow rate is maximal. This value must cancel the numerator of the derivative of \(Z^{2}(x)\) :

\[\frac{dZ^{2}(x)}{dx} = 0\]

\[\frac{dZ^{2}(x)}{dx} = \frac{d}{dx} \left( x^2\frac{1-x^{\gamma-1}}{1-r^2 x^2} \right) = \frac{(\gamma - 1) r^2 x^{\gamma + 2} - (\gamma + 1) x^\gamma + 2 x}{\left(1 - r^2 x^2 \right)^2} = 0\]

\[\Leftrightarrow (\gamma - 1) r^2 x^{\gamma + 2} - (\gamma + 1) x^\gamma + 2 x = 0\]

(253)\[\Leftrightarrow (\gamma - 1) r^2 x^{\gamma + 1} - (\gamma + 1) x^{\gamma-1} + 2 = 0\]

For small \(r\) (\(r\to 0\)), this equation can be easily solved :

(254)\[x_c \approx \left(\frac{2}{1+\gamma}\right)^{\frac{1}{\gamma-1}}\]

Once \(x_c\) is known, the **critical pressure** \(P_c\) (pressure in \(A_0\) for \(x=x_c\)) can be obtained using the definition of \(x\) :

\[P_c = P_1 x_c^\gamma\]

The **critical pressure** \(P_c\) is then :

(255)\[P_c \approx P_1 \left(\frac{2}{1+\gamma}\right)^{\frac{\gamma}{\gamma-1}}\]

For general \(r\), Eq [(253)](#equation-zsquared) is solved iteratively. In MANTA, following [[Lep97](../../references/references.md#id55)], the calculation is initialized with the approximate solution given in Eq [(254)](#equation-xc) :

\[x_{0} = \left(\frac{2}{1+\gamma}\right)^{\frac{1}{\gamma+1}}\]

The next iteration value is calculated by extracting \(x^{\gamma-1}\) in the Eq. [(253)](#equation-zsquared), obtaining :

\[\left((\gamma - 1) r^2 x^2 - (\gamma + 1)\right) x^{\gamma-1} + 2 = 0\]

\[x^{\gamma - 1} = \frac{2}{\gamma + 1 + (\gamma - 1) r^2 x^2}\]

It leads to a formula \(x_{i+1}=f(x_i)\) that can be used in a fixed point algorithm :

\[x_{i+1} = \left(\frac{2}{(\gamma + 1) - (\gamma - 1) r^2 x_i^2}\right)^{\frac{1}{\gamma-1}}\]

For this algorithm to converge, \(f'(x)\) must have a majorant \(M<1\). We have

\[f(x) = 2^{\frac{1}{\gamma-1}} \left( (\gamma + 1) - (\gamma - 1) r^2 x^2 \right)^{\frac{-1}{\gamma-1}}\]

\[f'(x) = 2^{\frac{1}{\gamma-1}} \left( - 2 (\gamma - 1) r^2 x \right) \left( \frac{-1}{\gamma-1} \right) \left( (\gamma + 1) - (\gamma - 1) r^2 x^2 \right)^{\frac{-\gamma}{\gamma-1}}\]

\[f'(x) = 2^{\frac{\gamma}{\gamma-1}} \left( r^2 x \right) \left( (\gamma + 1) - (\gamma - 1) r^2 x^2 \right)^{\frac{-\gamma}{\gamma-1}}\]

\[f'(x) = \left[\left(\frac{2}{(\gamma + 1) - (\gamma - 1) r^2 x^2}\right)^{\frac{1}{\gamma-1}}\right]^\gamma r^2 x\]

Using Eq [(253)](#equation-zsquared), it comes :

\[f'(x) = r^2 x^{\gamma+1}\]

Since \(r \in ]0,1[\) and \(x \in ]0,1[\), this condition is satisified. Note that the convergence will be faster if \(r\to 0\).

The expression for \(Z^{2}(x_c)\) in Eq. [(252)](#equation-zsquared0) can be simplified by solving Eq. [(253)](#equation-zsquared). By multiplying both sides by \(x_c^2\) :

\[r^2 x_c^2 (\gamma - 1) x_c^{\gamma+1} - (\gamma + 1) x_c^{\gamma+1} + 2 x_c^2 = 0\]

This simplifies to:

\[(1 - r^2 x_c^2)(\gamma - 1) x_c^{\gamma+1} = 2 x_c^2 (1 - x_c^{\gamma-1})\]

Which further simplifies to:

\[\frac{x_c^2 (1 - x_c^{\gamma-1})}{1 - r^2 x_c^2} = Z^{2}(x_c) = \frac{\gamma-1}{2}x_c^{\gamma+1}\]

Therefore, substituting the new expression for \(Z(x_c)\) into Eq. [(251)](#equation-massflow) :

(256)\[\boxed{w = \rho_1 C_1 A_0 x_c^{\frac{\gamma+1}{2}}}\]

Let's compute the velocity \(V_c\) at the break. Combining the definitions of \(C_1 = \sqrt{\gamma \frac{P_1}{\rho_1}}`\) and \(C_0 = \sqrt{\gamma \frac{P_c}{\rho_c}}\) and the fact that \(x_c=\frac{\rho_c}{\rho_1}\), it leads to

(257)\[C_1^2 = C_0^2 \frac{P_1}{P_c}\frac{\rho_c}{\rho_1} = C_0^2 x^{1-\gamma}\]

Using Eq. [(256)](#equation-debitcritique) and Eq. [(257)](#equation-c1carre), we can simplify the following expression :

\[V_c^2 = \frac{w^2}{\rho_c^2 A_0^2} = \left(\frac{\rho_1}{\rho_c}\right)^2 C_1^2 x_c^{\gamma+1}\]

\[V_c^2 = x_c^{-2} C_0^2 x_c^{1-\gamma} x_c^{1+\gamma} = C_0^2\]

\[V_c = C_0\]

We have recovered a classic result : the maximum flow rate is reached when the velocity matches the speed of sound at the break.

Note

For the upstream region, we recall that we made a strong assumption of isentropic flow.

Note

The maximum flow rate is not always reached, it depends on the downstream conditions.

### [Downstream region](#id29)

The downstream flow conditions are suppoed to be known and we seek to find the flow properties in \(A_0\).

It is possible to apply the same conservation laws than for the upstream region between \(A_0^+\) and \(A_2\). This implies that the flow is still isentropic in the downstream region.

This situation can be encountered in the case of nozzles, where the flow passes from medium 1 to medium 2 through a converging and then a diverging section. The conditions at the throat then impose the flow rate.

[![figure](https://manta-project.gitlab.io/manta/_images/tuyere.png)](../../_images/tuyere.png)

Fig. 114 Pressure along a convergent-divergent nozzle

In our case, where a pipeline failure causes a break in a circuit, we are very far from this situation. Indeed, we can consider that the pressure of the fluid near the break (downstream side) is almost \(P_2\), and the decompression then occurs irreversibly.

Note

The same is certainly true for the upstream region. However, assuming an isentropic (reversible) decompression maximizes the flow rate at the breach. This is the reason why we maintain this hypothesis to remain conservative about the consequences on the circuit.

Two distinct flow regimes

Thus, when the downstream pressure \(P_2\) decreases, the upstream pressure \(P_1\) remains constant, and the flow rate at the break will increase progressively until \(P_2\) becomes equal to the **critical pressure** \(P_c\). If \(P_2\) decreases further, the flow rate remains constant, and an irreversible decompression occurs between \(P_c\) and \(P_2\). This distinguishes two regimes:

- \(P_2 > P_c\) : subsonic regime.
- \(P_2 \leq P_c\) : supersonic regime.

### [Summary](#id30)

We assume that upstream conditions are known, as well as the downstream pressure and the complete set of geometric characteristics.

We then calculate the **critical pressure** \(P_c\) :

(258)\[P_c = P_1 x_c^\gamma\]

The critical factor \(x_c\) is obtained by successive iterations from the equation :

(259)\[x_c = \left( \frac{2}{(\gamma + 1) \left( 1 - \frac{\gamma - 1}{\gamma + 1} x_c^2 \right)} \right)^{\frac{1}{\gamma - 1}}\]

We then compare this pressure \(P_c\) with the downstream pressure \(P_2\).

- **Case 1 : Supersonic regime** (\(P_2 \leq P_c\))

  The regime is supersonic. The flow rate is maximal and is expressed as :

  (260)\[\boxed{w_m = \rho_1 C_1 A_0 x_c^{\frac{\gamma+1}{2}}}\]
- **Case 2 : Subsonic regime** (\(P_2 > P_c\))

  The regime is subsonic, and the flow rate is less than \(w_{m}\) :

  (261)\[\boxed{w = A_0 \rho_1 C_1 \sqrt{\frac{2}{\gamma - 1}}Z(x)}\]

  with

  (262)\[Z^{2}(x) =x^2\frac{1-x^{\gamma-1}}{1-r^2 x^2}\]

  and

  (263)\[x = \left( \frac{P_2}{P_1} \right)^{\frac{1}{\gamma}}\]

Conclusion

In conclusion, analytical formulas for mass flow rates based on upstream and downstream gas conditions, as well as geometric characteristics at the exit, have been established. These are valid assuming the fluid is a perfect gas.

### [Case of low velocities](#id31)

We take the Barré de Saint-Venant Eq. [(250)](#equation-veldiff) (dropping the "\({0^-}\)" subscript for a simpler "\(0\)" subscript) :

(264)\[V_0^2 - V_1^2 = \frac{2}{\gamma - 1} C_1^2 \left[ 1 - \left( \frac{P_{0-}}{P_1} \right)^{\frac{\gamma - 1}{\gamma}} \right]\]

where it has been noted that :

(265)\[ C_1^2 = \gamma \frac{P_1}{\rho_1}\quad\text{and}\quad C_0^2 = \gamma \frac{P_0}{\rho_0}\]

Moreover, we introduce the Mach number :

(266)\[ M_1 = \frac{V_1}{C_1}\quad\text{and}\quad M_0 = \frac{V_0}{C_0}\]

Note that Eq. [(249)](#equation-centropy) can be rewritten as :

(267)\[\frac{P_0}{\rho_0} = \frac{P_1}{\rho_1} \left(\frac{P_{0^-}}{P_1}\right)^{\frac{\gamma + 1}{\gamma}}\]

Using Eqs [(265)](#equation-recallc1c0), [(266)](#equation-recallmach) and [(267)](#equation-centropybis), we can rewrite Eq. [(264)](#equation-barre2) as follows :

\[\left( \frac{P_0}{P_1} \right)^{\frac{\gamma - 1}{\gamma}} = 1 - \frac{(\gamma - 1)}{2} \left[ M_0^2 \left( \frac{P_0}{P_1} \right)^{\frac{\gamma - 1}{\gamma}} - M_1^2 \right]\]

If we assume that the break has small dimensions :

\[M_1^2 \ll M_0^2 \ll 1\]

Then :

\[\left( \frac{P_0}{P_1} \right)^{\frac{\gamma - 1}{\gamma}} \approx 1 - \frac{(\gamma - 1)}{2} M_0^2 \left( \frac{P_0}{P_1} \right)^{\frac{\gamma - 1}{\gamma}}\]

\[\frac{P_1}{P_0} \approx \left( 1 + \frac{\gamma - 1}{2} M_0^2 \right)^{\frac{\gamma}{\gamma - 1}}\]

or

\[\frac{P_1 - P_0}{P_0} \approx \frac{\gamma M_0^2}{2} \left( 1 + \frac{M_0^2}{4} \right)\]

But, using Eqs [(265)](#equation-recallc1c0) and [(266)](#equation-recallmach) :

\[\gamma P_0 M_{0}^2 = \rho_0 V_{0}^2\]

Therefore :

(268)\[ \boxed{\frac{P_1 - P_0}{\frac{1}{2} \rho_0 V_0^2} \approx \left( 1 + \frac{1}{4} M_0^2 \right)}\]

Thus, for low velocities (\(M_0^2 \ll 1\)), we find ourselves in the case of incompressible fluids, where Bernoulli’s relation applies :

(269)\[ \frac{P_1 - P_0}{\frac{1}{2} \rho_0 V_0^2} = 1\]

This property allows for resolving difficulties that could arise when upstream and downstream pressures are close.

Note

For example, for \(M_0 = 0.2\), the discrepancy between the two formulas [(268)](#equation-lowvel1) and [(268)](#equation-lowvel1) is only 1%. In the case of air under normal conditions (1 bar and 0°C), \(M_0 = 0.2\) corresponds to a velocity \(V_0 \approx 65\text{m/s}\) and a pressure difference of 28 millibars.

## [Two-phase flow](#id32)

Among the numerous existing models, four models (available in MANTA) will be discussed :

1. The Homogeneous Model,
2. The Moody Model [[Moo65](../../references/references.md#id57)],
3. The Fauske Model [[Fau62](../../references/references.md#id58)],
4. The Henry-Fauske Model [[HF71](../../references/references.md#id60)],

These models are based on similar assumptions and mainly differ in how they handle the parameter \(K\) which represents the slip coefficient between the phases, defined as the ratio of the vapor phase velocity to the liquid phase velocity. Another well-known model is the Henry model [[Hen70](../../references/references.md#id59)].

The objective is once again to establish a formulation of the flow rate as a function of the conditions at the break and the state of the fluid upstream in order to determine the condition that maximizes the flow rate.

Note

We will present the key points of the Moody model [[Moo65](../../references/references.md#id57)]. The homogeneous and Fauske models [[Fau62](../../references/references.md#id58)] will then be presented as special cases.

### [Problem definition and assumptions](#id33)

The objective is to determine the properties of two-phase flow through a modeled break at the end of a pipe, discharging into a large reservoir. The following assumptions are made :

- Steady-state flow is established
- One-dimensional flow i.e. in the whole cross section area \(A\), the velocity \(V\), the pressure \(P\), the density \(\rho\), the temperature \(T\) in the gas are constant in the vapor phase and also in the liquid phase
- The liquid phase and the vapor phase are in a mechanical and thermal equilibrium (\(P_{\text{vapor}} = P_{\text{liquid}}\), \(T_{\text{vapor}} = T_{\text{liquid}}\))
- The transformation is isentropic
- Total energy is conserved
- Fluid flow is anular (i.e. a flow characterized by the presence of a liquid film flowing on the pipe wall and with the gas flowing in the gas core)
- The break orifice is perfect (no additional friction or headloss is considered due to the configuration of the orifice)

### [Moody's model](#id34)

[![figure](https://manta-project.gitlab.io/manta/_images/critical_flow_break_schematic2.png)](../../_images/critical_flow_break_schematic2.png)

Fig. 115 Schematic of an anular two-phase flow at the break (velocity is denoted \(u\) instead of \(V\))

The subscript \(g\) denotes quantities for the vapor phase, and \(f\) for the liquid phase. We define the following parameters:

- **Mass fraction of vapor** passing through the nozzle cross-section per unit time :

  \[x = \frac{w_g}{w}\]

  where \(w_g\) is the mass flow rate of the vapor, and \(w\) is the total mass flow rate.
- **Area ratio** of the vapor phase to the total breach area :

  \[\alpha = \frac{A_g}{A}\]

  where \(A_g\) is the area occupied by the vapor, and \(A\) is the total area of the breach.
- **Slip factor**: the ratio of the velocity of the vapor phase to that of the liquid phase :

  \[K = \frac{V_g}{V_f}\]

  where \(V_g\) is the velocity of the vapor phase, and \(V_f\) is the velocity of the liquid phase.

Using the fact that the fluid is at rest upstream \(V_1 = 0\) (see [Fig. 115](#fig-critical-flow-break-schematic2)) and the flow is isentropic :

(270)\[s_1 = x s_g + (1 - x) s_f\]

(271)\[h_1 = x \left( h_g + \frac{1}{2} V_g^2 \right) + (1 - x) \left( h_f + \frac{1}{2} V_f^2 \right)\]

Moreover, the mass flow rate per unit area \(G\) is written as :

\[G = \frac{w}{A}\]

Therefore :

\[G = \frac{\alpha w_g}{x A_g}\]

Using the definition of the specific volume \(v = \frac{1}{\rho}\) :

\[G = \frac{\alpha}{x} \frac{V_g}{v_g} = \frac{(1 - \alpha)}{(1 - x)} \frac{V_f}{v_f}\]

It is possible to express \(\alpha\) as a function of \(K\) and \(x\). Indeed :

\[K = \frac{V_g}{V_f} = \frac{w_g}{w_f}\frac{v_g}{v_f} \frac{A_f}{A_g} = \left(\frac{1 - \alpha}{\alpha}\right)\left(\frac{x}{1-x}\right)\left(\frac{v_g}{v_f}\right)\]

Thus :

\[\frac{1 - \alpha}{\alpha} = K \left(\frac{1 - x}{x}\right) \frac{v_f}{v_g}\]

(272)\[\boxed{\alpha = \frac{1}{1 + K \left(\frac{1 - x}{x}\right) \frac{v_f}{v_g}}}\]

We aim to express the mass flow rate per unit area as a function of the thermodynamic conditions of the upstream medium (denoted by index \(1\)) and the conditions at the nozzle throat (denoted by index \(0\)).

We have :

(273)\[G = \frac{\alpha}{x} \frac{V_g}{v_g}\]

From Eq. [(271)](#equation-enth) :

\[h_1 - x h_g - (1 - x) h_f = \frac{1}{2} \left[ x V_g^2 + (1 - x) V_f^2 \right]\]

Phase slip is defined by :

\[V_g = K V_f\]

Thus :

\[2 \left( h_1 - x h_g - (1 - x) h_f \right) = x V_g^2 + (1 - x) \frac{V_g^2}{K^2}\]

and :

\[V_g^2 = 2 \frac{\left( h_1 - x h_g - (1 - x) h_f \right)}{x \left( 1 + \left( \frac{1 - x}{x} \right) \frac{1}{K^2} \right)}\]

Substituting this expression into Eq. [(273)](#equation-unitmassflow) :

(274)\[\boxed{G^2 = \frac{\alpha^2}{x^2 v_g^2} \frac{2 \left[ h_i - x h_g - (1 - x) h_f \right]}{x\left( 1 + \left( \frac{1 - x}{x} \right) \frac{1}{K^2} \right)}}\]

Eq. [(272)](#equation-alphamoody) provides an expression for \(\alpha\). To express \(x\), we use Eq. [(270)](#equation-entrop) :

(275)\[x = \frac{s_1 - s_f}{s_g - s_f}\]

Next, we adopt Moody's notation :

\[s_{fg} = s_g - s_f\quad\text{and}\quad h_{fg} = h_g - h_f\]

Thus :

\[x = \frac{s_1 - s_f}{s_{fg}} \quad \text{and} \quad 1 - x = \frac{s_g - s_f}{s_{fg}}\]

Before substituting the expressions for \(\alpha\) and \(x\) in Eq. [(274)](#equation-gsquared), using Eq. [(272)](#equation-alphamoody), we note that :

(276)\[\frac{\alpha}{x v_g} = \frac{1}{x v_g + K (1 - x) v_f}\]

It follows that :

(277)\[\boxed{G = \sqrt{\frac{2\left[ \left( h_1 - h_f \right) s_{fg} - (s_1 - s_f) h_{fg}\right]}
{\left[\frac{s_1-s_f}{s_{fg}}v_g + \frac{s_g - s_1}{s_{fg}} v_f K\right]^2
\left[ \left( s_1 - s_f\right) + \frac{s_g - s_1}{K^2} \right]}}}\]

Note

Eq. [(277)](#equation-moodyg) is Moody's original formula.

The unit mass flow rate \(G\) is expressed as a function of the thermodynamic quantities of the upstream medium (\(h_1\), \(s_1\)) and those of each phase (\(v\), \(h\), \(s\)) and the slip phase \(K\).

The two phases are in mechanical equilibrium (same pressure \(P\)). Furthermore, if we are at saturation, all variables related to each phase are expressed as a function of the pressure \(P\) :

\[v_f (P); v_g (P); h_f (P); h_g (P); s_f (P); s_g (P)\]

Since the upstream conditions are imposed (\(h_1\) and \(s_1\)), the unit mass flow rate \(G\) is expressed only as a function of the two variables \(P\) and \(K\) :

\[G = f(P, K)\]

However, these two variables may not be independent.

If we assume that \(P\) and \(K\) are independent variables (**Supplementary Hypothesis**), the maximum mass flow rate \(G\) is obtained for :

\[\left( \frac{\partial G}{\partial K} \right)_P = 0 \quad \text{and} \quad \left( \frac{\partial G}{\partial P} \right)_K = 0\]

Taking the derivative of Eq. [(277)](#equation-moodyg) with respect to \(K\) at constant \(P\), we get :

(278)\[\frac{G'}{G} = - \frac{\frac{\left( s_g - s_1 \right)}{s_{fg}} v_f}{\frac{\left( s_1 - s_f \right)}{s_{fg}} v_g + \frac{\left( s_g - s_1 \right)}{s_{fg}} v_f K} - \frac{1}{2} \frac{\left( s_g - s_1 \right)\frac{-2}{K^3}}{\left( s_1 - s_f \right)+ \frac{\left( s_g - s_1 \right)}{K^2}}\]

It simplifies as :

(279)\[ \frac{G'}{G} = - \frac{(s_g - s_1) v_f}{(s_1 - s_f) v_g + (s_g - s_1) v_f K} + \frac{\frac{\left(s_g - s_1\right)}{K^3}}{\left( (s_1 - s_f) + \frac{s_1 - s_f}{K^2} \right)}\]

The condition for an extremum becomes :

\[0 = - v_f \left[ \left( s_1 - s_f \right) + \frac{s_g - s_1}{K^2} \right] + \frac{1}{K^3} \left[ \left( s_1 - s_f \right) v_g + \left(s_g - s_1 \right) v_f K \right]\]

Therefore :

\[\left( s_1 - s_f \right) v_f + \frac{\left( s_g - s_1 \right)}{K^2} v_f = \left( s_1 - s_f \right) \frac{v_g}{K^3}+ v_f \frac{\left( s_g - s_1 \right) }{K^2}\]

It follows that :

(280)\[\boxed{K_m = \left( \frac{v_g}{v_f} \right)^{\frac{1}{3}}}\]

The phase slip corresponding to maximal flow is associated with the mass volume ratio. This ratio is known as soon as the pressure is fixed. Hence, the value of the maximal flow \(G_m\) can be obtained by iterating over the tables of thermodynamic properties for different values of \(P\).

The pressure corresponding to maximal flow is called the **critical pressure** analogous to the perfect gas case.

In [[Moo65](../../references/references.md#id57)], this value of \(G\) is said to be a maximum and to be unique, but it is not proven. For the rest of this document, we will assume that it is indeed the case.

Note

The assumption of considering an isentropic (reversible) flow in the upstream section amounts to overestimating the flow rate through the break. This hypothesis allows for conservative estimatation of the effects on the circuit.

### [Fauske's Model](#id35)

Consider the reaction force associated with the diphasic jet. We have :

\[F = w_g V_g + w_f V_f\]

or equivalently :

\[F = w (x V_g + (1 - x) V_f)\]

But according to Eq. [(272)](#equation-alphamoody) and Eq. [(273)](#equation-unitmassflow), we have :

\[G = \frac{\alpha V_g}{x v_g} \quad \text{and} \quad K = \frac{V_g}{V_f}\]

Thus :

\[F = w V_g \left( x + \frac{1 - x}{K} \right)\]

and, using [(276)](#equation-truc) :

\[V_g = \frac{x G}{\alpha} v_g = G (x v_g + K (1 - x) v_f)\]

Finally :

\[\boxed{F = w G \left( x + \frac{1 - x}{K} \right) (x v_g + K (1 - x) v_f)}\]

The expression of \(x\) is the same as in Eq. [(275)](#equation-moodyx) :

\[x = \frac{s_1 - s_f}{s_g - s_f}\]

Fauske's hypothesis is that the maximum flow rate is obtained when \(F\) reaches an extremum as \(K\) varies at constant \(P\) :

\[\left( \frac{\partial F}{\partial K} \right)_P = 0\]

In practice, Fauske only considers the quantity \(B\) :

\[B = \frac{F}{w G} = \left( x + \frac{1 - x}{K} \right) (x v_g + K (1 - x) v_f)\]

and imposes the condition \(\left( \frac{\partial B}{\partial K} \right)_P = 0\).

In this case :

\[0 = \left( x + \frac{1 - x}{K} \right) (1 - x) v_f - \left( \frac{1 - x}{K^2} \right) (x v_g + K (1 - x) v_f)\]

which simplifies to :

\[\left( K^2 x + (1 - x) K \right) v_f = x v_g + K (1 - x) v_f\]

and :

\[\boxed{K_m = \left( \frac{v_g}{v_f} \right)^{1/2}}\]

Note

The maximum flow rate is then determined in the same way as the previous case, with the Moody hypothesis.

### [Homogeneous Model](#id36)

By definition, the homogeneous model assumes that there is no slip between phases:

\[\boxed{K = 1}\]

and once again, we use Moody's expression of Eq. [(277)](#equation-moodyg) to determine the maximum flow rate.

### [Henry-Fauske Model](#id37)

The Henry-Fauske model was introduced in 1971 by Henry and Fauske
[[HF71](../../references/references.md#id60)] as an evolution of the Henry
[[Hen70](../../references/references.md#id59)] and Fauske [[Fau62](../../references/references.md#id58)] models.
The objective is to determine the critical mass flow rate through the break,
requiring only the upstream conditions and the geometry. Unlike the models
presented above, it accounts for the **non-equilibrium** nature of the flow
(neither fully frozen nor fully equilibrated heat and mass transfer), and covers
sub-cooled liquid, saturated liquid, two-phase mixtures and saturated vapor.

As in Moody's model, the fluid is assumed to be at rest upstream (\(V_1 =
0\)). The isentropic coefficient \(\gamma\) of the vapor phase is used in
what follows; its definition is recalled in the [Perfect gas](#critical-flow-theory) section above.

The model distinguishes two cases based on the vapor quality at upstream
conditions \(x_1\), relative to a threshold \(x_t\) (set by default to
\(x_t = 10^{-4}\)).

**Case 1 — Sub-cooled or saturated liquid** (\(x_1 \leq x_t\))

The critical mass flow rate per unit area \(G_m\) is given by :

(281)\[\boxed{G_m = \left[ \left( v_{gc} - v_{f1} \right)
\frac{N}{s_{gc} - s_{fc}}
\frac{ds_{fc}}{dP}\rvert_c \right]^{-1}}\]

where \(v_{gc}\) is the specific volume of vapor at critical conditions,
\(v_{f1}\) is the specific volume of liquid at upstream conditions,
\(N\) is a measure of the deviation from equilibrium mass transfer,
\(s_{gc}\) and \(s_{fc}\) are the specific entropies of vapor and
liquid at critical conditions, and \(\frac{ds_{fc}}{dP}\rvert_c\) is the
pressure derivative of liquid specific entropy at critical conditions.

The auxiliary quantities are computed as follows :

\[v_{gc} = \left( v_{g1} \frac{P_c}{P_1} \right)^{-1/\gamma}\]

\[s_1 = x_1 s_{g1} + (1 - x_1) s_{f1}\]

\[x_c = \frac{s_1 - s_{fc}}{s_{gc} - s_{fc}}\]

\[\begin{split}N = \begin{cases}
\frac{x_c}{0.14} & \text{if } x_c > 0 \\
1 & \text{if } x_c \leq 0
\end{cases}\end{split}\]

\[\frac{P_c}{P_1} = 1 - \frac{v_{f1}\, G_m^2}{2\, P_1}\]

\[\frac{ds_{fc}}{dP}\rvert_c = \frac{\Delta s_{fc}}{\Delta P_c}\]

The unknowns \(P_c\), \(x_c\) and \(G_m\) are obtained iteratively
from the system formed by Eq. [(281)](#equation-hf-case1) and the relations above.

**Case 2 — Two-phase mixture** (\(x_1 > x_t\))

The critical mass flow rate per unit area \(G_m\) is given by :

(282)\[\boxed{G_m = \left[ \frac{x_1 v_{gc}}{n P_c}
+ (v_{gc} - v_{f1}) \left( (1-x_1)
\frac{N}{s_{gc}-s_{fc}}
\frac{ds_{fc}}{dP}\rvert_c
- \frac{x_1 c_{pg}(1/n - 1/\gamma)}{P_c (s_{g1}-s_{f1})} \right) \right]^{-1/2}}\]

where \(c_{pg}\) is the vapor specific heat, \(c_{pl}\) is the liquid
specific heat, and \(n\) is the thermal equilibrium polytropic exponent. The
auxiliary quantities \(v_{gc}\), \(s_1\), \(x_c\), \(N\) and
\(\frac{ds_{fc}}{dP}\rvert_c\) are defined as in Case 1, and additionally :

\[\frac{\left[ (1-x_1)\, v_{f1} + x_1\, v_{gc} \right]^2 G_m^2}{2\, P_1}
= \left[ (1-x_1)\, v_{f1} + \frac{\gamma}{\gamma-1} x_1\, v_{g1} \right] P_1
- \left[ (1-x_1)\, v_{f1} + \frac{\gamma}{\gamma-1} x_1\, v_{gc} \right] P_c\]

\[n = \frac{(1 - x_c)\, c_{pl}/c_{pg} + 1}
{(1 - x_c)\, c_{pl}/c_{pg} + 1/\gamma}\]

As in Case 1, the unknowns \(P_c\), \(x_c\) and \(G_m\) are
obtained iteratively from the system formed by Eq. [(282)](#equation-hf-case2) and the
relations above.

Note

As for the other two-phase models, the assumption of isentropic flow in the
upstream region leads to a conservative overestimate of the mass flow rate
through the break.

## [Pure Liquid](#id38)

We saw previously that for low velocities, we would have, for an ideal gas :

\[\frac{P_1 - P_0}{\frac{1}{2} \rho_0 V_0^2} = 1\]

For slightly compressible liquids, we will adopt an analogous formula :

\[\frac{P_1 - P_0}{\frac{1}{2} \rho_1 V_1^2} = \frac{k}{r^2}\]

The transition of values at the break (\(P_0\), \(V_0\)) to upstream values (\(P_1\), \(V_1\)) introduces the term (\(\frac{1}{r^2}\)), defined previously as:

\[r = \frac{\text{Area of the break}}{\text{Upstream section area}}\]

The coefficient \(k\) corresponds to the associated head loss. According to Idel’Cik [[Idelcik69](../../references/references.md#id56)], for the exit of a straight tube through a thin diaphragm (chapter XI):

\[k = \left( 1 + 0.707 \sqrt{1 - r} \right)^2\]

Note

In MANTA, we have retained these formulas for calculating the head loss associated with the break.

## [References](#id39)

- [[Lep97](../../references/references.md#id55)]
- [[Idelcik69](../../references/references.md#id56)]
- [[Moo65](../../references/references.md#id57)]
- [[Fau62](../../references/references.md#id58)]
- [[Hen70](../../references/references.md#id59)]
- [[HF71](../../references/references.md#id60)]
