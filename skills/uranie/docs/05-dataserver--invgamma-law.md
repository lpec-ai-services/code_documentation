# The DataServer module — The TAttribute class — Introducing the TStochasticAttribute classes — InvGamma law … Composing law
<!-- source PDF pages 55-60 -->

<!-- page 48 (PDF 55) -->
Figure 2.27: Example of PDF, CDF and inverse CDF for a Gamma truncated distribution.

#### 2.2.5.16 InvGamma law

The inverse-Gamma distribution is a two-parameter family of continuous probability distributions. It depends on a shape
parameter 𝛼and a scale parameter 𝛽. The function is usually defined for 𝑥greater than 0, but the distribution can be
shifted thanks to the third parameter called location (𝜉) which should be positive.
𝑓(𝑥) = 𝛽𝛼(𝑥−𝜉)−𝛼−1𝑒−𝛽/(𝑥−𝜉)
Γ(𝛼)
1I]𝜉,+∞](𝑥)
Uranie code to simulate a inverse-Gamma random variable is:

```python
tds = DataServer.TDataServer("tdssampler", "Sampler Uranie demo")
tds.addAttribute(DataServer.TInvGammaDistribution("ing", 2.0, 0.5, 0.0))
fsamp = Sampler.TSampling(tds, "lhs", 300)
fsamp.generateSample()
                        # Create a representative sample
tds.Draw("ing")
```

Figure 2.28 shows the PDF, CDF and inverse CDF generated for different sets of parameters.

<!-- page 49 (PDF 56) -->
Figure 2.28: Example of PDF, CDF and inverse CDF for InvGamma distributions.
Is it also possible to set boundaries to the infinite span of this distribution to create a truncated InvGamma law. This can
be done by calling the following method:

```python
tds.getAttribute("ing").setBounds(-3.0,8.0)
                                             # truncate the law
```

The resulting PDF, CDF and inverse CDF, with and without truncation, can be seen, in this case, in Figure 2.29 for a
given set of parameters and various boundaries.
Figure 2.29: Example of PDF, CDF and inverse CDF for a InvGamma truncated distribution.

#### 2.2.5.17 Student Law

Exclamation-Triangle Warning
This distribution is available only if the ROOT “mathmore” feature has been installed when your ROOT version was
brought (you can check this by running root-config --has-mathmore. If not found, this law cannot be used.

<!-- page 50 (PDF 57) -->
The Student law is simply defined with a single parameter: the degree-of-freedom (DoF). The probability density function
is then set as
𝑓(𝑥) =
√
𝑘𝜋
Γ
(︀𝑘+1
)︀
Γ
(︀𝑘
)︀
(︂
1 + 𝑡2
𝑘
)︂−𝑘+1
where Γ is the Euler’s gamma function.
Uranie code to simulate an student random variable is:

```python
tds = DataServer.TDataServer("tdssampler", "Sampler Uranie demo")
tds.addAttribute(DataServer.TStudentDistribution("stu", 5))
fsamp = Sampler.TSampling(tds, "lhs", 300)
fsamp.generateSample()
                        # Create a representative sample
tds.Draw("stu")
```

Figure 2.30 shows the PDF, CDF and inverse CDF generated for different sets of parameters.
Figure 2.30: Example of PDF, CDF and inverse CDF for Student distributions.
Is it also possible to set boundaries to the infinite span of this distribution to create a truncated Student law. This can be
done by calling the following method:

```python
tds.getAttribute("stu").setBounds(-1.4,2.0)
                                             # truncate the law
```

The resulting PDF, CDF and inverse CDF, with and without truncation, can be seen, in this case, in Figure 2.31 for a
given set of parameters and various boundaries.

<!-- page 51 (PDF 58) -->
Figure 2.31: Example of PDF, CDF and inverse CDF for a Student truncated distribution.

#### 2.2.5.18 Generalized normal law

This law describes a generalized normal distribution depending on the location 𝜇, the scale 𝛼and the shape 𝛽, as
𝑓(𝑥) =
𝛽
2𝛼Γ (1/𝛽) × 𝑒
−
(︁
𝑥−𝜇
𝛼
)︁𝛽
Both 𝛼and 𝛽should be greater than 0.
Uranie code to simulate a generalized normal random variable is:

```python
tds = DataServer.TDataServer("tdssampler", "Sampler Uranie demo")
tds.addAttribute(DataServer.TGeneralizedNormalDistribution("gennor", 0.0, 1.0, 3.0) )
fsamp = Sampler.TSampling(tds, "lhs", 300)
fsamp.generateSample()
                        # Create a representative sample
tds.Draw("gennor")
```

Figure 2.32 shows the PDF, CDF and inverse CDF generated for different sets of parameters.

<!-- page 52 (PDF 59) -->
Figure 2.32: Example of PDF, CDF and inverse CDF for GeneralizedNormal distributions.
Is it also possible to set boundaries to the infinite span of this distribution to create a truncated generalized normal law.
This can be done by calling the following method:

```python
tds.getAttribute("gennor").setBounds(-0.8,1.6) # truncate the law
```

The resulting PDF, CDF and inverse CDF, with and without truncation, can be seen, in this case, in Figure 2.33 for a
given set of parameters and various boundaries.
Figure 2.33: Example of PDF, CDF and inverse CDF for a generalized normal truncated distribution.

#### 2.2.5.19 Composing law

It is possible to imagine a new law, hereafter called composed law, by combining different pre-existing laws in order to
model a wanted behaviour. This law would be defined with 𝑁pre-existing laws whose densities are noted {𝑓𝑗}1≤𝑗≤𝑁,
along with their relative weights {𝜔𝑗}1≤𝑗≤𝑁∈(R+)𝑁and the resulting density is then written as
𝑓(𝑥) =
𝑁
∑︁
𝑗=1
𝜔𝑗𝑓𝑗(𝑥)

<!-- page 53 (PDF 60) -->
Uranie code to simulate a composition of three normally-distributed laws (with their own statistical properties):

```python
tds = DataServer.TDataServer("tdssampler", "Sampler Uranie demo")
comp = DataServer.TComposedDistribution("compo")
comp.addDistribution(DataServer.TNormalDistribution("n1", -1.5, 0.2), 1.2)
comp.addDistribution(DataServer.TNormalDistribution("n2", 0, 0.5), 1.0)
comp.addDistribution(DataServer.TNormalDistribution("n3", 1.5, 0.2), 0.8)
tds.addAttribute(comp)
fsamp = Sampler.TSampling(tds, "lhs", 300)
fsamp.generateSample()
                        # Create a representative sample
tds.Draw("compo")
```

Figure 2.34 shows the PDF, CDF and inverse CDF generated for different sets of parameters.
Figure 2.34: Example of PDF, CDF and inverse CDF for a composed distribution made out of three normal distributions
with respective weights.
Is it also possible to set boundaries to the infinite span of this distribution, if it is created from at least one infinite-based
law, to create a truncated composed law. This can be done by calling the following method:

```python
tds.getAttribute("compo").setBounds(-1.6,1.8) # truncate the law
```

The resulting PDF, CDF and inverse CDF, with and without truncation, can be seen, in this case, in Figure 2.35 for a
given set of parameters and various boundaries.
