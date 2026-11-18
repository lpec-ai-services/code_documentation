# Key equations

Transcribed in LaTeX from the rendered pages of *Thermal Hydraulics of Water-Cooled Nuclear Reactors* (D'Auria ed., 2017). Pages are printed page numbers; equation numbers are the book's. **P** = physics, **M** = methods. The IAEA fast-reactor report (F) gives no explicit correlations.

Notation (book, ch. 5): phase $k\in\{v,l\}$ (vapour, liquid); $\alpha_k$ void/phase fraction; $\varrho_k$ phase density; $V_k$ phase velocity; $H_k$ phase enthalpy; $A$ flow area; $\Gamma_k$ interfacial mass transfer; $\tau_{wk}$, $q_{wk}$ wall friction and heat flux; $C_k$ heated/wetted perimeter.

---

## P1 — Two-phase averaged quantities, qualities, drift flux (pp. 224, 228)

$$
\varrho_m=\alpha_v\varrho_v+\alpha_l\varrho_l,\qquad G_k=\alpha_k\varrho_kV_k,\qquad G=G_v+G_l,\qquad
H_m=\frac{\alpha_v\varrho_vH_v+\alpha_l\varrho_lH_l}{\varrho_m}
$$
Three qualities:
$$
x=\frac{\alpha_v\varrho_v}{\varrho_m}\ \text{(static)},\qquad
X=\frac{G_v}{G}\ \text{(dynamic, flow quality)},\qquad
X_{th}=\frac{\hat H_m-h_{lsat}}{h_{vl}}\ \text{(thermodynamic / equilibrium)}
$$
Superficial velocities $j_k=\alpha_k v_k$, $J=J_v+J_l$. The distribution parameter and drift velocity are
$$
C_0=\frac{\langle\alpha_v j\rangle}{\langle\alpha_v\rangle\langle j\rangle},\qquad
V_{gj}=\frac{\langle\alpha_v(v_v-j)\rangle}{\langle\alpha_v\rangle}
$$
which give the **drift-flux identity** $\;V_v=C_0J+V_{gj}$. $C_0\neq1$ captures void and velocity profile effects; $V_{gj}\neq0$ captures local slip.

## P2 — Single-phase pressure drop (eqs. 8.2–8.7, p. 497)

$$
\Delta p=f\,\frac{L}{D_h}\,\frac{W^2}{2\rho A^2},\qquad D_h=\frac{4\,\text{flow area}}{\text{wetted perimeter}}
$$
- Laminar: $f=64/Re$ for $Re<2320$.
- Blasius: $f=0.3164\,Re^{-0.25}$ for $3000<Re<10^5$.
- Herman: $f=0.0054+0.33964\,Re^{-0.3}$ for $2\times10^4<Re<2\times10^6$.
- Colebrook–White (smooth and rough, $Re>3000$), standard form: $\dfrac{1}{\sqrt f}=-2\log_{10}\!\Big(\dfrac{e/D}{3.7}+\dfrac{2.51}{Re\sqrt f}\Big)$. The book prints it as $0.86\ln(\ldots)$ (the same, since $0.86\ln = 2\log_{10}$) without the minus sign and with "2.5L"; use the standard form.
- Filonenko (smooth tubes, $4\times10^3<Re<10^{12}$): $\dfrac{1}{\sqrt f}=1.82\log(Re)-1.64$.
- Bare rod bundles (Kays): $f=f_{cir}K_1$, where $K_1$ depends on pitch/diameter (eq. 8.8, p. 498).

## P3 — Two-phase friction multipliers (eq. 8.9, p. 498)

$$
\Big(\frac{\Delta p}{\Delta z}\Big)_{TPF}=\Big(\frac{\Delta p}{\Delta z}\Big)_{L}\Phi_L^2=\Big(\frac{\Delta p}{\Delta z}\Big)_{G}\Phi_G^2=\Big(\frac{\Delta p}{\Delta z}\Big)_{LO}\Phi_{LO}^2=\Big(\frac{\Delta p}{\Delta z}\Big)_{GO}\Phi_{GO}^2
$$
Reference is the liquid alone (L), the gas alone (G), or the whole mixture flowing as liquid (LO) or as gas (GO). Models are either homogeneous (modified single-phase friction factor) or separated-flow multiplier correlations (Lockhart–Martinelli, Friedel…, pp. 499–501).

## P4 — Heat conduction (eqs. 7.5–7.9, p. 365)

$$
q=k\,\Delta T,\qquad c_p\rho\,\frac{\partial T}{\partial\tau}=\operatorname{div}(\lambda\,\operatorname{grad}T)+q_V
$$
With constant properties, $\dfrac{\partial T}{\partial\tau}=a\nabla^2T+\dfrac{q_V}{\rho c_p}$, where $a=\lambda/(\rho c_p)$ is the thermal diffusivity (the book's text writes $\lambda/c_p$). At steady state $\nabla^2T+q_V/\lambda=0$; with no source, $\nabla^2T=0$. $1/k$ is the overall thermal resistance (analogy with Ohm's law).

## P5 — Two-phase critical flow (pp. 599–600)

Slip at the choke, from maximizing the flow:
- Moody: $\dfrac{u_g}{u_l}=\Big(\dfrac{\rho_l}{\rho_g}\Big)^{1/3}$
- Fauske: $\dfrac{u_g}{u_l}=\Big(\dfrac{\rho_l}{\rho_g}\Big)^{1/2}$

**Henry–Fauske** (non-equilibrium, relative to the HEM): $x=Nkx_e$, with $N=20x_{eq}$ for $0<x_{eq}<0.05$ and $N=1$ for $x_{eq}>0.05$, and
$$
G_{cr}=\frac{G_{cr,HEM}}{\sqrt{N_{exit}}}
$$
**Henry (1970)**, pipe-length effect: $x_{exit}=x_{LT}\big(1-e^{-B(L/D-12)}\big)$, with $x_{LT}=Nx_{eq}$ and $B=0.0523$, and
$$
G_{cr}^2=\frac{1}{\Big[\dfrac{x}{p\,\rho_g}-\Big(\dfrac{1}{\rho_g}-\dfrac{1}{\rho_l}\Big)N\dfrac{dx_{eq}}{dp}\Big]_{exit}}
$$

---

## M1 — Local instantaneous single-phase balance equations (p. 177)

Total energy, with $\mathcal T$ the viscous stress tensor and $\vec F$ body forces:
$$
\frac{\partial}{\partial t}\Big[\rho\Big(u+\frac{v^2}{2}\Big)\Big]+\nabla\cdot\Big[\rho\vec v\Big(u+\frac{v^2}{2}\Big)\Big]-\rho\vec F\cdot\vec v+\nabla\cdot(p\vec v)-\nabla\cdot(\mathcal T\cdot\vec v)+\nabla\cdot\vec q=q_{ext}
$$
Momentum:
$$
\frac{\partial\rho\vec v}{\partial t}+\nabla\cdot(\rho\vec v\vec v)+\nabla p-\rho\vec F-\nabla\cdot\mathcal T=0
$$
Enthalpy form ($h=u+p/\rho$):
$$
\frac{\partial\rho h}{\partial t}+\nabla\cdot(\rho\vec v h)-\frac{\partial p}{\partial t}-\vec v\cdot\nabla p-\mathcal T:\nabla\vec v+\nabla\cdot\vec q=q_{ext}
$$
The system is closed with an equation of state and expressions for $\vec q$ and $\mathcal T$.

## M2 — 1-D two-fluid 6-equation model (pp. 221–222)

Principal variables $\alpha_v, P, V_v, V_l, H_v, H_l$. For each phase $k$:

**Mass:**
$$A\frac{\partial\alpha_k\varrho_k}{\partial t}+\frac{\partial A\alpha_k\varrho_kV_k}{\partial z}=A\Gamma_k$$
**Momentum:**
$$
A\frac{\partial\alpha_k\varrho_kV_k}{\partial t}+\frac{\partial A\alpha_k\varrho_kV_kV_k}{\partial z}+A\alpha_k\frac{\partial P}{\partial z}+Af_i\frac{\partial\alpha_k}{\partial z}+g_k\frac{\partial A}{\partial z}
=A\alpha_k\varrho_kg_z+\frac{\partial AR_k(T^t_{kz}+T^d_{kz})}{\partial z}-A\tau_{ik}-C_k\tau_{wk}-A\alpha_k\frac{\delta P_{ksing}}{\delta z}+AF_k^{AM}+A\Gamma_kV_i
$$
**Total enthalpy:**
$$
\begin{aligned}
A\frac{\partial\alpha_k\varrho_k\big(H_k+\frac{V_k^2}{2}\big)}{\partial t}+\frac{\partial A\alpha_k\varrho_kV_k\big(H_k+\frac{V_k^2}{2}\big)}{\partial z}-A\alpha_k\frac{\partial P}{\partial t}
={}&-\frac{\partial A\alpha_k(q_{kz}+q^t_{kz}+q^d_{kz})}{\partial z}+A\alpha_k\varrho_kg_zV_k+C_kq_{wk}\\
&+Aq_{ik}+A\Gamma_k\Big(H_k+\frac{V_i^2}{2}\Big)+A\tau_{ik}V_i+Aq_{kext}
\end{aligned}
$$
**Interface jump conditions and closure:**
$$\sum_k\alpha_k=1;\ \sum_k\Gamma_k=0;\ \sum_k\tau_{ik}=0;\ \sum_kF_k^{AM}=0;\ \sum_k[q_{ik}+\Gamma_kH_k]=0$$
Equations of state $\varrho_k(P,H_k)$, $T_k(P,H_k)$, plus closure laws for $\tau_{ik}$, $T^t_{kz}$, $T^d_{kz}$, $q_{ik}$, $C_k$, $\tau_{wk}$, $q_{wk}$, $\delta P_{ksing}$, $F_k^{AM}$, $\lambda_k^{eff}$. Those closure laws are chapter 9's subject.

System codes (CATHARE, RELAP5) often use the non-conservative momentum form (p. 222):
$$
A\alpha_k\varrho_k\frac{\partial V_k}{\partial t}+A\alpha_k\varrho_kV_k\frac{\partial V_k}{\partial z}+A\alpha_k\frac{\partial P}{\partial z}+Af_i\frac{\partial\alpha_k}{\partial z}+g_k\frac{\partial A}{\partial z}
=A\alpha_k\varrho_kg_z-A\tau_{ik}-C_k\tau_{wk}-A\alpha_k\frac{\delta P_{ksing}}{\delta z}+AF_k^{AM}+A\Gamma_k(V_i-V_k)
$$

## M3 — Model hierarchy (table 5.6, p. 225)

| Model | Mass | Momentum | Energy | Thermal equilibrium | Mechanical equilibrium |
|---|---|---|---|---|---|
| 3-eq. HEM | 1 mixture | 1 mixture | 1 mixture | both phases saturated | no slip |
| 3-eq. + drift flux | 1 mixture | 1 mixture | 1 mixture | both saturated | algebraic slip |
| 4-eq. + drift flux | 2 | 1 mixture | 1 mixture | 1 phase saturated, 1 not | algebraic slip |
| 5-eq. + drift flux | 2 | 1 mixture | 2 | both out of equilibrium | algebraic slip |
| 6-eq. two-fluid | 2 | 2 | 2 | both out of equilibrium | none |

## M4 — 1-D HEM and drift-flux closure (pp. 226–228)

**HEM** (variables $P$, $G$, $\hat H_m$):
$$
A\frac{\partial\varrho_m}{\partial t}+\frac{\partial AG}{\partial z}=0,\qquad
A\frac{\partial G}{\partial t}+\frac{\partial\big(AG^2/\varrho_m\big)}{\partial z}+A\frac{\partial P}{\partial z}=A\varrho_mg_z-C\tau_w-A\frac{\delta p_{sing}}{\delta z},\qquad
A\varrho_m\frac{\partial\hat H_m}{\partial t}+AG\frac{\partial\hat H_m}{\partial z}-A\frac{\partial P}{\partial t}=Cq_w
$$
In the saturated region ($h_{lsat}\le\hat H_m\le h_{vsat}$), $X_{th}=X=x=(\hat H_m-h_{lsat})/h_{lv}$ and
$$
\alpha_v=\frac{(\hat H_m-h_{lsat})\varrho_{lsat}}{(h_{vsat}-\hat H_m)\varrho_{vsat}+(\hat H_m-h_{lsat})\varrho_{lsat}},\qquad
\varrho_m=\frac{\varrho_{lsat}\varrho_{vsat}h_{lv}}{(h_{vsat}-\hat H_m)\varrho_{vsat}+(\hat H_m-h_{lsat})\varrho_{lsat}}
$$
Subcooled ($X_{th}<0$) and superheated ($X_{th}>1$) regions reduce to single-phase liquid and vapour. Limitations of the HEM: no slip, equilibrium, regime-dependent closures (p. 227).

**Drift-flux closure** replacing one momentum equation (p. 228):
$$V_v(1-C_0\alpha_v)=C_0(1-\alpha_v)V_l+V_{gj}$$
