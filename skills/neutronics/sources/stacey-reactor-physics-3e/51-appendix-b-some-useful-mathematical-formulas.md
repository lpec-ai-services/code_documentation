# Appendix B Some Useful Mathematical Formulas
<!-- source PDF pages 720-721 -->

<!-- page 703 (PDF 720) -->
# Appendix B Some Useful Mathematical Formulas

1) Solution of First-Order Linear Differential Equations:
df
dx + a(x)f (x) = g(x)
(B.1)
f (x) = e−A(x)
∫
x
dx´eA(x´)g(x´) + C

;
A(x) = ∫
x
dx´a(x´)
(B.2)
2) Differentiation of a Definite Integral:
d
dx ∫
a(x)
b(x)
dx´F(x; x´) = F(x; a) da
dx − F(x; b) db
dx + ∫
a(x)
b(x)
dx´ @F(x; x´)
@x
(B.3)
3) Representation of Laplacian ∇2 in Various Coordinate Systems:
a) Cartesian:
∇2 = @2
@x2 + @2
@y2 + @2
@z2
z
y
x
b) Cylindrical:
∇2 = 1
r
@
@r r @
@r + 1
r2
@2
@θ2 + @2
@z2
z
y
r
x
θ
(B.5)
(B.4)
Nuclear Reactor Physics, Third Edition. Weston M. Stacey.
2018 Wiley-VCH Verlag GmbH & Co. KGaA. Published 2018 by Wiley-VCH Verlag GmbH & Co. KGaA.

<!-- page 704 (PDF 721) -->
c) Spherical:
∇2 = 1
r2
@
@r r2 @
@r +
r2sin θ
@
@θ
sin θ @
@θ

+
r2sin2 θ
@2
@ϕ2


z
r
y
x
4) Gauss’ Divergence Theorem:
∫V
d3r∇□ A = ∫
S
dS^es □ A
(B.7)
where ^es is the unit vector normal to the surface element dS.
5) Green’s Theorem:
∫d3r∇ϕ □ ∇ψ = ∫dSϕ^es □ ∇ψ − ∫d3rϕ∇2ψ
(B.8)
∫d3r(ϕ∇2ψ − ψ∇2ϕ) = ∫dS^es □ (ϕ∇ψ − ψ∇ϕ)
(B.9)
6) Taylor Series Expansion:
f (x) = f (x0) + (x − x0)f ´(x0) + (x − x0)2
2!
f ´´(x0) + ∙∙∙
(B.10)
7) Fourier Series Expansion:
f (x) =
X
n=1
ansin nπx
l
+ 1
2 b0 +
X
n=1
bncos nπx
l
(B.11)
where
an ≡ 1
l ∫
l
−1
dx´f (x´)sin nπx´
l
;
bn ≡ 1
l ∫
l
−1
dx´f (x´)cos nπx´
l
(B.12)
(B.6)
