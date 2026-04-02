The Pricing and Hedging of
Mortgage-Backed Securities
A MULTIVARIATE DENSITY
ESTIMATION APPROACH
Jacob Boudoukh, Matthew Richardson, Richard Stanton,
and Robert F. Whitelaw
The mortgage-backed security (MBS) market plays a special role in
the U.S. economy. Originators of mortgages (S&Ls, savings and com-
mercial banks) can spread risk across the economy by packaging
these mortgages into investment pools through a variety of agen-
cies, such as the Government National Mortgage Association
(GNMA), Federal Home Loan Mortgage Corporation (FHLMC), and
Federal National Mortgage Association (FNMA). Purchasers of
MBS are given the opportunity to invest in virtually default-free
This chapter is based closely on the paper, “Pricing Mortgage-Backed Securities in a
Multifactor Interest Rate Environment: A Multivariate Density Estimation Ap-

proach,” Review of Financial Studies (Summer 1997, Vol. 10, No. 2, pp. 405-446).
265

---

| { 266 OTHER RISK FACTORS
: interest-rate contingent claims that offer payoff structures different
i from U.S. Treasury bonds. Due to the wide range of payoff patterns
| J offered by MBS and their derivatives, the MBS market is one of the
| i largest as well as fastest growing financial markets in the United
5 States. For example, this market grew from approximately $100 mil-
i | lion outstanding in 1980 to about $1.5 trillion in 1993.
{Hh Pricing of mortgage-backed securities is a fairly complex task,
it and investors in this market should clearly understand these com-
plexities to fully take advantage of the tremendous opportunity
‘ | offered. Pricing MBS may appear fairly simple on the surface. Fixed-
! I rate mortgages offer fixed nominal payments; thus, fixed-rate MBS
i . .
i prices will be governed by pure discount bond prices. The complex-
ii ity in pricing of MBS is due to the fact that typically residential
| mortgage holders have the option to prepay their existing mort-
id gages; hence, MBS investors are implicitly writing a call option on a
( corresponding fixed-rate bond. The timing and magnitude of cash
Hi flows from MBS are therefore uncertain. While mortgage prepay-
# ments occur largely due to falling mortgage rates, other factors such
§ as home owner mobility and home owner inertia play important
1 roles in determining the speed at which mortgages are prepaid.
i Since these non-interest rate related factors that affect prepayment
bi (and hence MBS prices) are difficult to quantify the task of pricing
i MBS is quite challenging.
: This chapter develops a non-parametric method for pricing MBS.
i Much of the extant literature (e.g., Schwartz & Torous, 1989) employs
id parametric methods to price MBS. Parametric pricing techniques re-
quire specification and estimation of specific functions or models to
i describe interest rate movements and prepayments. While paramet-
ric models have certain advantages, any model for interest rates and
: prepayments is bound to be only an approximation of reality. Non-
: parametric techniques such as the multivariate density estimation
(MDE) procedure that we propose, on the other hand, estimates the
relation between MBS prices and fundamental interest rate factors
directly from the data. MDE is well suited to analyzing MBS be-
cause, although financial economists have good intuition for what
the MBS pricing fundamentals are, the exact models for the dynam-
ics of these fundamentals is too complex to be determined precisely
i from a parametric model. For example, while it is standard to assume
at least two factors govern interest rate movements, the time series

---

THE PRICING AND HEDGING OF MORTGAGE-BACKED SECURITIES 267
dynamics of these factors and the interactions between them are not
well understood. In contrast, MDE has the potential to capture the
effects of previously unrecognized or hard to specify interest rate
dynamics on MBS prices.

In this chapter, we first describe the MDE approach. We present
the intuition behind the methodology and discuss the advantages
and drawbacks of non-parametric approaches. We also discuss the
applicability of MDE to MBS pricing in general and to our particular
application.

We then apply the MDE method to price weekly TBA (to be an-
nounced) GNMA securities! with coupons ranging from 7.5% to
10.5% over the period 1987-1994. We show that at least two interest
rate factors are necessary to fully describe the effects of the prepay-
ment option on prices. The two factors are the interest rate level,
which proxies for the moneyness of the prepayment option, the ex-
pected level of prepayments, and the average life of the cash flows;
and the term structure slope, which controls for the average rate
at which these cash flows should be discounted. The analysis also
reveals cross-sectional differences among GNMAs with different
coupons, especially with regard to their sensitivities to movements
in the two interest rate factors. The MDE methodology captures the
well-known negative convexity of MBS prices.

Finally, we present the methodology for hedging the interest
rate risk of MBS based on the pricing model in this chapter. The
sensitivities of the MBS to the two interest rate factors are used to
construct hedge portfolios. The hedges constructed with the MDE
methodology compare favorably to both a linear hedge and an alter-
native non-parametric technique. As can be expected, the MDE
methodology works especially well in low interest rate environ-
ments when the GNMAs behave less like fixed maturity bonds.
MORTGAGE-BACKED SECURITY PRICING: PRELIMINARIES
Mortgage-backed securities represent claims on the cash flows from
mortgages that are pooled together and packaged as a financial
A TBA contract is just a forward contract, trading over the counter. More details are
provided in the next section.

---

> N
268 OTHER RISK FACTORS
asset. The interest payments and principal repayments made by
mortgagees, less a servicing fee, flow through to MBS investors.
MBS backed by residential mortgages are typically guaranteed by
; government agencies such as the GNMA and FHLMC or private
H agencies such as FNMA. Because of the reinsurance offered by these
| agencies MBS investors bear virtually no default risk. Thus, the pric-
ing of an MBS can be reduced to valuing the mortgage pool's cash
flows at the appropriate discount rate. MBS pricing then is very
much an issue of estimating the magnitude and timing of the pool's
cash flows.
i However, pricing an MBS is not a straightforward discounted
i cash flow valuation. This is because the timing and nature of a
| pool's cash flows depends on the prepayment behavior of the hold-
i ers of the individual mortgages within the pool. For example, mort-
i gages might be prepaid by individuals who sell their homes and
! relocate. Such events lead to early repayments of principal to the
| MBS holders. In addition, MBS contain an embedded interest rate
i option. Mortgage holders have an option to refinance their property
i and prepay their existing mortgages. They are more likely to do so
§ as interest rates, and hence refinancing rates, decline below the rate
i of their current mortgage. This refinancing incentive tends to lower
¢ the value of the mortgage to the MBS investor because the mort-
i gages’ relatively high expected coupon payments are replaced by an
; immediate payoff of the principal. The equivalent investment alter-
‘ native now available to the MBS investor is, of course, at the lower
h coupon rate. Therefore, the price of an MBS with, for example, a 8%
; coupon is roughly equivalent to owning a default-free 8% annuity
: bond and writing a call option on that bond (with an exercise price
: of par). This option component induces a concave relation between
H the price of MBS and the price of default-free bonds (the so called
i “negative convexity”).
MBS Pricing: An MDE Approach
Modeling and pricing MBS involves two layers of complexity:
: (1) modeling the dynamic behavior of the term structure of interest
rates, and (2) modeling the prepayment behavior of mortgage holders.
The standard procedure for valuation of MBS assumes a particular

---

THE PRICING AND HEDGING OF MORTGAGE-BACKED SECURITIES 269
stochastic process for term structure movements and uses specific
statistical models of prepayment behavior. The success of this ap-
proach depends crucially on the correct parameterization of prepay-
ment behavior and on the correct model for interest rates. We
propose here a different approach that directly estimates the rela-
tion between MBS prices and various interest rate factors. This ap-
proach circumvents the need for parametric specification of interest
rate dynamics and prepayment models.

The basic intuition behind the MDE pricing technique we pro-
pose is fairly straightforward. Let a set of m variables, denoted by x,
be the underlying factors that govern interest rate movements and
prepayment behavior. The vector x, includes interest rate variables
(e.g, the level of interest rates) and possible prepayment specific
variables (e.g., transaction costs of refinancing). The MBS price at
time f, denoted as P,, , is a function of these factors and can be writ-
ten as

P.,.=V(x, 6)

where V(x,,0) is a function of the state variables x, and the vector 6
is a set of parameters that describe the interest rate dynamics and
the relation between the variables x, and the prepayment function.
The vector 8 includes variables such as the speed with which inter-
est rates tend to revert to their long run mean values and the sen-
sitivity of prepayments to changes in interest rates. Parametric
methods in the extant literature derive the function V based on
equilibrium or no-arbitrage arguments and determine MBS prices
using estimates of 8 in this function. The MDE procedure, on the
other hand, aims to directly estimate the function V from the data
and is not concerned with the evolution of interest rates or the spe-
cific forms of prepayment functions.

The MDE procedure starts with a similar basic idea as parametric
methods: That MBS prices can be expressed as a function of a small
number of interest rate factors. MBS prices are expressed as a func-
tion of these factors plus a pricing error term. The error term allows
for the fact that model prices based on any small number of pricing
factors will not be identical to quoted market prices. There are sev-
eral reason why market prices can be expected to deviate from model
prices. First, bid prices may be asynchronous with respect to the

---

{4
| | 270 OTHER RISK FACTORS
|
| interest rate quotes. Furthermore, the bid-ask spreads for the MBS
| in this chapter generally range from %s2nd to #:2nds, depending on
the liquidity of the MBS. Second, the MBS prices used in this chap-
| ter refer to prices of unspecified mortgage pools in the marketplace
(see p. 277). To the extent that the universe of pools changes from
tl period to period, and its composition may not be in the agent's in-
| | formation set, this introduces an error into the pricing equation. Fi-
Hl nally, there may be pricing factors that are not specified in the
i | model. Therefore, we assume observed prices are given by
i PL.=V(x) +e (9.1)
| | where g, represent the aforementioned pricing errors. A well-
i specified model will yield small pricing errors. Examination of ¢,
i based on our model will therefore enable us to evaluate its suitabil-
i ity in this pricing application.
i The first task in implementing the MDE procedure is to specify
the factors that determine MBS prices. To price MBS we need factors
i that capture the value of fixed cash flow component of MBS and re-
ii financing incentives. The particular factors we use here are the yield
iH on 10-year Treasury notes and the spread between the 10-year yield
| and the 3-month T-bill yield. There are good reasons to use these
i factors for capturing the salient features of MBS. The MBS analyzed
§ in this paper have 30 years to maturity; however, due to potential
i prepayments and scheduled principal repayments, their expected
3 lives are much shorter. Thus, the 10-year yield should approximate
gl the level of interest rates which is appropriate for discounting the
i MBS’s cash flows. Further, the 10-year yield has a correlation of
Hl 0.98 with the mortgage rate (see Table 9.1 and Figure 9.1). Since the
M spread between the mortgage rate and the MBS’s coupon deter-
: mines the refinancing incentive, the 10-year yield should prove use-
ful when valuing the option component.
The second variable, the slope of the term structure (in this case,
the spread between the 10-year and 3-month rates) provides infor-
mation on two factors: the market's expectations about the future
: path of interest rates, and the variation in the discount rate over

short and long horizons. Steep-term structure slopes imply lower
: discount rates for short-term cash flows and higher discount rates
B for long-term cash flows. Further, steep-term structures may imply

---

THE PRICING AND HEDGING OF MORTGAGE-BACKED SECURITIES 271
TABLE 9.1. Summary Statistics
Coupon: 7.5% 8.0% 85% 9.0% 9.5% 10.0% 10.5%
GNMA Prices
Mean 93.132 95.578 97.876 100.084 102.204 104.347 106.331
Max. 105.156 106.563 107.500 108.281 109.469 110.938 112.719
Min. 78.375 81.625 83.656 86.531 89.531 92.688 95.750
Vol. 6.559 6.287 5.831 5.260 4.722 4.294 3.978
Correlations
7.5% 1.000 0.998 0.993 0.986 0.981 0.983 0.977
8.0% 0.998 1.000 0.997 0.992 0.987 0.987 0.979
8.5% 0.993 0.997 1.000 0.998 0.995 0.993 0.982
9.0% 0.986 0.992 0.998 1.000 0.999 0.995 0.983
9.5% 0.981 0.987 0.995 0.999 1.000 0.997 0.985
10.0% 0.983 0.987 0.993 0.995 0.997 1.000 0.994
10.5% 0.977 0.979 0.982 0.983 0.985 0.994 1.000
Long Rate Spread Mortgage Rate
Interest Rates
Mean 7.779 2.119 9.337
Max. 10.230 3.840 11.580
Min. 5.170 -0.190 6.740
Vol. 1.123 1.101 1.206
Correlations
Long rate 1.000 0.450 0.980
Spread -0.450 1.000 -0.518
Mortgage rate 0.980 -0.518 1.000
Note: Summary statistics for prices of TBA contracts on 7.5% to 10.5%
GNMAs, the long rate (10-year), the spread (10-year minus 3-month), and the
average mortgage rate. All data are weekly from January 1987 through May
1994. Interest rates are in percent per year.

---

J
: 272 OTHER RISK FACTORS
|
| FIGURE 9.1. Mortgage Rates and Interest Rates
; ©
] | .
ii |
i A |
i |
8 of
i 3
i 5 w
is <
| {
i \
i EE 1
i . — 0vear Pete ]
i | =——— Mortgage Rate
H [
2 wl a ]
§ il 1987 1988 1988 1980 1991 1982 19e3 1994 1895
§ Date
ii - OO OO OO OOOO
5 Note: The yield on the “on-the-run” 10-year treasury note and the average
Hi 30-year mortgage rate, from January 1987 to May 1994.
i
E increases in future mortgage rates, which should decrease the likeli-
F hood of mortgage refinancing.
i
i Multivariate Density Estimation Issues
: This subsection explains the details of the multivariate density esti-
. mation technique proposed in this chapter. To understand the is-
iB sues involved, suppose that the error term in Equation (9.1) is
i uniformly zero and that we have unlimited data on the past history
of MBS prices. Now suppose that we are interested in determining
the fair price for a MBS with a particular coupon and prepayment
history at a particular point in time when, for example, the 10-year
yield is 8% and the slope of the term structure is 1%. In this case, all
; we have to do is look back at the historical data and pick out the
i price of an MBS with similar characteristics at a point in time his-
i torically when the 10-year yield was 8% and the slope of the term
t

---

THE PRICING AND HEDGING OF MORTGAGE-BACKED SECURITIES 273
structure was 1%. While this example illustrates the simplicity of
the underlying idea behind the MDE procedure, it also highlights
the sources of potential problems in estimation. First, for reasons
discussed in the last subsection, it is unrealistic to assume away the
error terms. Second, in practice we do not have unlimited historical
data, and a particular economic scenario, such as an 8% 10-year
yield and a 1% term structure slope, may not have been played out
in the past. The estimation technique therefore should be capable of
optimally extracting information from the available data.

The MDE procedure characterizes the joint distribution of the
variables of interest, in our case the joint distribution of MBS prices
and interest rate factors. We implement MDE using a kernel estima-
tion procedure. In our application, the kernel estimator for MBS
prices as a function of interest rate factors simplifies to:

Tp AAPA TN
. PYRLW { h, Ji [hn
Buper—r)s——m—mm—F"F (9:2)
5. fend
ul =r i
where T is the number of observations, K(-) is a suitable kernel
function and h is the window width or smoothing parameter.
Bb, (rr, —r,) is our model price for a MBS with coupon ¢ when the
long rate is r, and the term structure slope is 7, 7. P_, is the mar-
ket price of the t observation for the price of a MBS with coupon c.
Note that the long rate at the time of observation t is r,, and the term
structure slopeisr, — 7, ’

The econometrician has at his or her discretion the choice of
K() and h. It is important to point out, however, that these choices
are quite different from those faced by researchers employing
parametric methods. Here, the researcher is not trying to choose
?For examples of MDE methods for approximating functional forms in the empirical
asset pricing literature, see Pagan and Hong (1991), Harvey (1991), and Ait-Sahalia
(1996). An alternative approach to estimating nonlinear functionals in the derivatives
market is described by Hutchinson, Lo, and Poggio (1994). They employ methods as-
sociated with neural networks to estimate the nonlinear relation between option
prices and the underlying stock price.

---

I}
i 274 OTHER RISK FACTORS
i
| functional forms or parameters that satisfy some goodness-of-fit
criterion (such as minimizing squared errors in regression meth-
ods), but is instead characterizing the joint distribution from which
the functional form will be determined.

i One popular class of kernel functions is the symmetric beta den-
! | sity function, which includes the normal density, the Epanechnikov
iH (1969) “optimal” kernel, and the commonly used biweight kernel as
| i special cases. Results in the kernel estimation literature suggest that
iil any reasonable kernel gives almost optimal results, though in small
li | 1 samples there may be differences (Epanechnikov, 1969). In this
| | chapter, we employ an independent multivariate normal kernel,
! i though it should be pointed out that our results are relatively insen-
Bt sitive to the choice of kernel within the symmetric beta class. The
{ i specific functional form for the K( - ) that we use is:

i i 1 12
i K@)= (2m) 2e™
! 3

i where z is the appropriate argument for this function.

4 The other parameter, the window width, is chosen based on the

i dispersion of the observations. For the independent multivariate
normal kernel, Scott (1992) suggests the window width
i h, =k,G, Tm
ji
i where S, is the standard deviation of the ith variable (i.e., i may de-
i note either variable r, or r,—=rJ), mis the dimension of the variables,
i which in our case is 2, and k; is a scaling constant often chosen via a
a cross-validation procedure. In our application we need to choose two

i such scaling constants, one for the long rate r, and one for the term

Hy structure slope r, — r . Note that the window width is larger when the

‘ variance of the variable under consideration is larger in order to com-

i pensate for the fact that observations are, on average, further apart.

i; This window width (with k; = 1) has the appealing property that, for

i certain joint distributions of the variables, it minimizes the asymp-

& totic mean integrated squared error of the estimated density func-

i tion. Unfortunately, our data are serially correlated and therefore

Hl the necessary distributional properties are not satisfied.

i We employ a cross-validation procedure to find the k; that min-

L imizes the estimation error. To implement cross-validation, the

---

THE PRICING AND HEDGING OF MORTGAGE-BACKED SECURITIES 275
implied MDE price at each data point is estimated using the entire
sample, except for the actual data point and its nearest neighbors.?
We identify the k's that minimize the mean-squared error between
the observed price and the estimated kernel price. Once the k/'s are
chosen based on cross-validation, the actual estimation of the MBS
prices and analysis of pricing errors involves the entire sample.

To gain further intuition into the estimation procedure, note
that Equation (9.2) takes a special form; the estimate of the MBS
price can be interpreted as a weighted average of observed prices:

~ I
Poy (11 = 10) = D0, (0) Pub 9.3)
t=1
where
PAAR A a)
hi hi
w(t) =—m———————
5" { [= = In, - 2
ho. he
nm nr

Note that to determine the MBS price when the interest rate fac-
tors are (1,1, — 1.) the kernel estimator assigns to each observation ¢
a weight w (t) that is proportional to the “distance” (measured via
the kernel function) between the interest rate factors at the time of
observation £(r,,r,, — ro) and the current interest rate factors. The
attractive idea behind MDE is that these weights are not estimated
in an ad hoc manner, but instead depend on the true underlying dis-
tribution (albeit estimated) of the relevant variables. Thus, if the
current state of the world, as measured by the state vector (1, —1,),
is not close to a particular point in the sample, then this sample
price is given little weight in estimating the current price. Note,
however, that MDE can give weight (possibly inconsequential) to all
observations, so that the price of the MBS with (n,n —r,) also takes
into account MBS prices at surrounding interest rates. This will help
3Due to the serial dependence of the data, we performed the cross-validation omitting
one year of data, for example, six months in either direction of the particular data
point in question.

---

i
i 4
i if
i 276 OTHER RISK FACTORS
i
average out the different € errors in Equation (9.1) from period to
| period. Although our application utilizes only two factors, MDE
! will average out effects of other factors if they are independent
| of the two interest rate factors. Thus, for any given long rate r’
it and a given short rate r,, there is a mapping to the MBS price
i | P(r ,n =r). These prices can then be used to evaluate how MBS
i prices move with fundamental interest rate factors.
i H While the MDE procedure has the advantage that it does not re-
| 1 quire explicit functional specification of interest rate dynamics and
: i prepayment models, it does have certain drawbacks. The most seri-
H ous problem with MDE is that it is data intensive. Much data are re-
| l quired in order to estimate the appropriate weights which capture
i the joint density function of the variables. The quantity of data
Hl which is needed increases quickly in the number of conditioning
i | variables used in estimation. How well MDE does at estimating the
| : relation between MBS prices and the interest-rate factors is then an
i open question, since the noise generated from the estimation error
{ can be substantial.*
Another problem with MDE is that the procedure requires co-
i variance stationarity of the variables of interest. For example, when
Ei we use only two interest rate factors, the MDE procedure does not
b account for differences in prices MBS when the underlying pools
Hi have different prepayment histories. For this reason the MBS proce-
i dure is most suitable for pricing TBA securities which are most com-
: monly used for new originations rather than for seasoned MBS.
i Accounting for seasoning of a mortgage or a mortgage pool's burnout
i will require additional factors that are beyond the scope of this
Hl chapter.
i A few comments are in order, however, to provide some guid-
1 ance on how these factors could be accounted for when one is in-
Bi terested in pricing seasoned MBS. First, one could potentially take
Bl account of a mortgage pool's seasoning by nonlinearly filtering out
: any time dependence. Estimation error aside, this filtering would be
; effective as long as the seasoning is independent of the other state
. variables. Second, in order to incorporate path dependence due to a
1 +Boudoukh, Richardson, Stanton, and Whitelaw (1997) perform simulation exercises
Ll in an economy governed by two factors and some measurement error in reported
5 prices. Within this (albeit simple) environment, the MDE methodology performs
fi quite well.

---

THE PRICING AND HEDGING OF MORTGAGE-BACKED SECURITIES 277
pool’s burnout, the only viable way would be to employ a state vari-
able which captures this dependence. For example, Boudoukh,
Richardson, Stanton, and Whitelaw (1997) and Richard and Roll
(1989) describe several variables that might be linked closely with
burnout. Because the strength of the MDE procedure estimation of
nonlinear relations, all that is required is that these variables span
the appropriate state space.

DATA DESCRIPTION

Mortgage-backed security prices were obtained from Bloomberg Fi-
nancial Markets covering the period January 1987 to May 1994.
Specifically, we collected weekly data on 30-year fixed-rate Govern-
ment National Mortgage Association (GNMA) MBS, with coupons
ranging from 7.5% to 10.5%.” The prices represent dealer-quoted bid
prices on GNMAs of different coupons traded for delivery on a to be
announced (TBA) basis.

The TBA market is most commonly employed by mortgage
originators who have a given set of mortgages that have not yet
been pooled. However, trades can also involve existing pools on an
unspecified basis. Rules for the delivery and settlement of TBAs
are set by the Public Securities Association (PSA); (see, for exam-
ple, Bartlett, 1989, for more details). For example, an investor might
purchase $1 million worth of 8% GNMAs for forward delivery next
month. The dealer is then required to deliver 8% GNMA pools
within 2.5% of the contracted amount (i.e., between $975,000 and
$1,025,000), with specific pool information to be provided on a
TBA basis (just prior to settlement). This means that, at the time
of the agreed-upon-transaction, the characteristics of the mortgage
pool to be delivered (e.g., the age of the pool and its prepayment
history) are at the discretion of the dealer. Nevertheless, for a
majority of the TBAs, the delivered pools represent newly issued
pools.
® Careful filters were applied to the data to remove data reporting errors using prices
reported in the Wall Street Journal. Furthermore, data are either not available or sparse
for some of the GNMA coupons during the period. For example, in the 1980s, 6%
coupon bonds represent mortgages originated in the 1970s, and not the more recent is-
sues which are the focus of this paper. Thus, data on these MBS were not used.

---

t 278 OTHER RISK FACTORS
| With respect to the interest rate series, weekly data for the
! 1987-1994 period were collected on the average rate for 30-year
mortgages (collected from Bloomberg Financial Markets),® and the
yields on the 3-month Treasury bill and 10-year Treasury note (pro-
i vided by the Board of Governors of the Federal Reserve).
i Data Characteristics
| Before describing the pricing results and error analysis for MBS
t using the MDE approach, we briefly describe the environment for in-
HH terest rates and mortgage rates during the sample period, 1987-1994.
| Since the mortgage rate represents the available rate at which
i homeowners can refinance, it plays an especially important role
i with respect to the prepayment incentive. Figure 9.1 graphs the
t mortgage rate for 1987 through 1994. From 1987 to 1991, the mort-
i gage rate varied from 9% to 11%. In contrast, from 1991 to 1994, the
Hi. mortgage rate generally declined from 9.5% to 7%.7
i For pricing GNMA TBAs, it is most relevant to understand the
| characteristics of the universe of pools at a particular point in time.
i That is, the fact that a number of pools have prepaid considerably
h may be irrelevant if newly originated pools have entered into the
H MBS market since the MBS from new originations are the one typi-
i cally delivered in TBA contracts. To get a better idea of the time
E series behavior of the GNMA TBAs during this period, Figure 9.2
5 graphs an artificially constructed index of all the originations of
i 7.5% to 10.5% GNMA pools from January 1983 to May 1994.
There is a wide range of origination behavior across the
5 coupons. As mortgage rates moved within a 9% to 11% band be-
i tween 1987 to 1991, Figure 9.2 shows that GNMA 9s, 9.5s, 10s, and
¢Bloomberg’s source for this rate is “Freddie Mac's Primary Mortgage Market Sur-
of vey,” which reports the average rate on 80% of newly originated 30-year, first mort-
Gi gages on a weekly basis.
Note that the MBS coupon rate is typically 50 basis points less than the interest rate
. on the underlying mortgage. The 50 basis points are retained to cover the servicing fee
id and reinsurance cost.
i $The dollar amount outstanding for each coupon is normalized to 100 in January
i 1987. Actual dollar amounts outstanding in that month were $10,172, $27,096,
fe $10,277, $63,392, $28,503, $15,694, and $5,749 (in millions) for the 7.5%-10.5%
| coupons, respectively.
i

---

THE PRICING AND HEDGING OF MORTGAGE-BACKED SECURITIES 279
FIGURE 9.2. GNMA Originations
-_—
8 -
t [— woman |
s| — 7.5% GNMA |
2 | m——g% GNMA |
" 8.5% GNMA |
= ee 8% GNMA ERY AAR
5] deen 9.5% GNMA
= 10% GNMA —m = —
Pa. —— 10.5% GNMA oT
El ral |
gs ’ — —
A
FE} a / ammm-
i 1H
ha Cee JRE
° 18983 “ees 1887 188 18391 1993 1995
Date
-_—
Note: Originations of 7.5% to 10.5% GNMAs from January 1983 to April
1994. The dollar amount outstanding is normalized to 100 in January 1987.
10.5s were all newly originated during this period. Consistent with
the decline in mortgage rates in the post-1991 period, GNMA 7.5s,
8s, and 8.5s originated while the GNMA 9s to 10.5s became sea-
soned issues. Thus, in terms of the seasoning of the pools most likely
to be delivered in the TBA market, there are clearly cross-sectional
differences between the coupons.

Figure 9.2 shows that there are several reasons for choosing the
TBA market during the post-1986 time period to investigate MBS
pricing using the MDE methodology. First, during 1985 and 1986, in-
terest rates dramatically declined, leading to mortgage originations
for a wide variety of coupon rates. Thus, the GNMA TBAs in
1987-1994 correspond to mortgage pools with little prepayment his-
tory (i.e, no burnout) and long maturities. In contrast, prior to this
period, the 7.5% to 10.5% GNMAs were backed by mortgages origi-
nated in the 1970s and thus represented a different security (in both
maturity and prepayment levels). Second, MDE pricing requires
joint stationarity between MBS prices and the interest rate variables.

---

|
280 OTHER RISK FACTORS

i

i

hi This poses a potential problem in estimating the statistical proper-

i ties of any fixed maturity security, since the maturity changes over

ih time. Recall that the TBA market refers to unspecified mortgage

i i pools available in the marketplace. Thus, to the extent that there are

il originations of mortgages in the GNMA coupon range, the maturity
i of the GNMA TBA is less apt to change from week to week. Fig-
If ure 9.2 shows that this is the case for the higher coupon GNMAs
i pre-1991, and for the low coupon GNMAs post-1991. Of course,
h when no originations occur in the coupon range (e.g., the GNMA
| 10s in the latter part of the sample), then the maturity of the avail-
ii able pool will decline. In this case, the researcher may need to add
it variables to capture the maturity effect and possibly any prepay-
i ment effects. In our analysis, we choose to limit the dimensionality
I of the multivariate system, and instead focus on the relation be-

{ I tween MBS prices and the two interest rate factors.

i iB Table 9.1 provides ranges, standard deviations, and cross-

ii Pp 8

H i correlations of GNMA prices and mortgage and interest rates dur-

| i ing the 1987-1994 period. Absent prepayments, MBS are fixed-rate

| 18 annuities, and the dollar volatility of an annuity increases with the

Ii y y

i coupon. In contrast, from Table 9.1, we find that the lower coupon

15 . .

| H GNMAs are more volatile than the higher coupon GNMAs. The

Ih: lower volatility of the higher coupon GNMAs is due to the embed-

& ded call option of MBS. The important element of the option com-
i P p! p

3H ponent for MBS valuation is the refinancing incentive. For most of

E: the sample (especially 1990 on), the existing mortgage rate lies

of below 10.5% and the prepayment option is at- or in-the-money.’
! Historically, given the costs associated with refinancing, a spread
: of approximately 150 basis points between the old mortgage rate

pp y P gag

By and the existing rate is required to induce rapid prepayments.’

Ei

i

§ ? Figure 9.1 also graphs one of the interest rate factors, the 10-year yield. There is a dif-
zn ference in the level between the two series (i.e., on average 1.56%), representing the
d cost of origination, the option value, and the bank profits, among other factors.

See Bartlett (1989) and Breeden (1991) for some historical evidence of the relation

H between prepayment rates and the mortgage spread. Note that in the 1990s the thresh-

: old spread required to induce refinancing has been somewhat lower—in some cases,

B 75 to 100 basis points. Some have argued that this is due to the proliferation of new

i types of mortgage loans (and ensuing marketing efforts by the mortgage companies)

i (Bartlett, 1989), though it may also be related to aggregate economic factors, such as

I the implications of a steep term structure.

---

THE PRICING AND HEDGING OF MORTGAGE-BACKED SECURITIES 281
The lack of seasoning aside, this would suggest that the higher
coupon GNMAs began to prepay in the early 1990s.

As mentioned, Figure 9.1 graphs the 10-year yield against the
mortgage rate. During the 1987 to 1994 period, there are multiple
observations of particular interest rates. Since these multiple obser-
vations occur at different points of the sample, this will help MDE
isolate the potential impact of additional interest rate factors, as
well as reduce maturity effects not captured by the MDE pricing
(see Characteristics of Mortgages above). Similarly, while the spread
between the 10-year yield and the 3-month rate is for the most part
positive, there is still variation of the spread during the period of an
order of magnitude similar to the underlying 10-year rate (see
Table 9.1). Moreover, the correlation between these variables is only
—0.45, indicating that they potentially capture independent infor-
mation, which may be useful for pricing GNMAs.

EMPIRICAL RESULTS

This section implements the MDE procedure and investigates how
well the model prices match market prices.

One-Factor Pricing

As a first pass at the MBS data, we describe the functional relation
between GNMA prices and the level of interest rates (the 10-year
yield). As an illustration, Figure 9.3 graphs the estimated 9% GNMA
price with the actual data points. The smoothing factor, which is
chosen by cross-validation, is 0.35 (i.e., k; = 0.35).

Several observations are in order. First, the figure illustrates the
well-known negative convexity of MBS. Specifically, the MBS price
is convex in interest-rate levels at high interest rates (when it be-
haves more like a straight bond), yet concave at low interest rates (as
the prepayment option becomes in-the-money). Second, the esti-
mated functional relation is not smooth across the entire range of
sample interest rates. Specifically, between 10-year yields of 7.1% to
7.8%, there is a bump in the estimated relation. While this feature is
most probably economically spurious, it reflects the fact that the

---

3
| 282 OTHER RISK FACTORS
I FIGURE 9.3. Market Prices and One-Factor Model Prices
| :
if fr EERE 5
i pase] ot 28
i e Ts Ee Cad So
| sl NCE
i ot FF Rg 1
i 2 8 E NTE =
| < EAS Bac
i £8 oo
i E - pS
it x Bf SHEER a
Ji L SENG
il o TEEN ]
b Or iy
| Cl TEEN
i =
iH Bos 8.0 8.5 7.0 B 7.5 8.0 8.5 Teo 8.5
4 10-Year Rate
I$ OO OO OO OOOO
i Note: Observed weekly prices and estimated prices from a one-factor (long
|i rate) MDE model for a 9% GNMA for the period January 1987 to May 1994.
iE
i observed prices in this region are high relative to the prices at
hi nearby interest rates. Increasing the degree of smoothing eliminates
4 this bump at the cost of increasing the pricing errors. The source of
5 this variation, which could be missing factors, MDE estimation
4 error, or structural changes in the mortgage market, is investigated
ik further below. Third, there is a wide range of prices at the same level
48 of interest rates. For example, at a 10-year yield of 8%, prices of
i GNMA 9s vary from 98% to 102% of par. Is this due to the impact of
4 additional factors, measurement error in GNMA prices, MDE esti-
| mation error, or some other phenomenon?
Id Table 9.2 provides some preliminary answers to this question,
b reporting summary statistics on the pricing errors (defined as the
i difference between the MDE estimated price and the observed MBS
i price) for the 7.5% to 10.5% GNMAs. As seen from a comparison be-
= tween Tables 9.1 and 9.2, most of the volatility of the GNMA price
& can be explained by a 1-factor kernel using the interest rate level. For
i example, the volatility of the 9% GNMA is $5.26, but its residual
£

---

THE PRICING AND HEDGING OF MORTGAGE-BACKED SECURITIES 283
TABLE 9.2. One-Factor GNMA Pricing
Coupon: 7.5% 8.0% 85% 9.0% 9.5% 10.0% 10.5%
Pricing Errors
Mean 0.003 0.006 0.007 0.010 0.010 0.010 0.009
Mean Abs. 0.529 0.605 0.649 0.679 0.660 0.597 0.666
Vol. 0.703 0.747 0.800 0.832 0.824 0.767 0.841
Autocorr. 0.861 0.898 0.918 0.927 0.921 0.917 0916
Pricing Error Regression Analysis
Const. 3.226 3.613 3.887 3.857 3.721 3.249 2.755
(3.190) (3.413) (4.133) (4.419) (4.402) (4.028) (4.320)
Long rate -0.963 -1.062 -1.130 -1.117 -1.074 -0.942 -0.805
(0.887) (0.941) (1.135) (1.216) (1.210) (1.119) (1.216)
(Long rate)? 0.069 0.075 0.080 0.078 0.075 0.066 0.057
(0.059) (0.063) (0.075) (0.081) (0.080) (0.075) (0.082)
R? 0.028 0.026 0.023 0.020 0.018 0.017 0.011
Joint test 2.795 2.157 1.709 1.441 1327 1.228 0.707
p-value 0.247 0.340 0.426 0.487 0.515 0.541 0.702
AC(e) 0.853 0.891 0.913 0.923 0.916 0.912 0.914
Const. 0.491 0.236 0.411 0.607 0.887 1.137 1.494
(0.148) (0.194) (0.212) (0.211) (0.194) (0.165) (0.135)
Spread -0.673 -0.373 -0.446 -0.605 -0.948 -1.234 -1.582
(0.275) (0.330) (0.365) (0.374) (0.342) (0.286) (0.261)
(Spread)? 0.165 0.098 0.095 0.120 0.199 0.261 0.328
(0.074) (0.090) (0.101) (0.103) (0.094) (0.079) (0.072)
R? 0.072 0.020 0.033 0.068 0.145 0.276 0.401
Joint test 6.480 1.281 2.608 5.916 14.102 34.899 79.195
p-value 0.039 0.527 0.271 0.052 0.001 0.000 0.000
AC(e) 0.848 0.895 0.914 0.920 0.904 0.877 0.847
Note: Summary statistics and regression analysis for the pricing errors from a
one-factor (long rate) MDE GNMA pricing model. The regression analysis in-
volves regressing the pricing errors on linear and squared explanatory vari-
ables. Heteroscedasticity and autocorrelation consistent standard errors are
reported in parentheses below the corresponding regression coefficient.
AC(e) is the autocorrelation of the residuals from the regression.

---

1
| 284 OTHER RISK FACTORS
volatility is only $0.83. However, while 1-factor pricing does well, it
i clearly is not sufficient as the pricing errors are highly autocorre-
It lated (from 0.861 to 0.927) for all the GNMA coupons. Though this
i autocorrelation could be due to measurement error induced by the
Hi MDE estimation, it does raise the possibility that there is a missing
i factor. In addition, the residuals are highly correlated across the
i seven different coupon bonds (not shown in the table). Thus, the
I pricing errors contain substantial common information.
i This correlation across different GNMAs implies that an expla-
i nation based on idiosyncratic information (such as measurement
1 error in prices) will not be sufficient. Combined with the fact that
il the magnitude of the bid-ask spreads in these markets lies some-
i where between sand and #3nds, clearly measurement error in ob-
i served prices cannot explain either the magnitude of the pricing
| | errors with 1-factor pricing (e.g., $2 — $3 in some cases) or the sub-
i stantial remaining volatility of the errors (e.g., $0.70 to $0.84 across
it the coupons).
It Table 9.2 investigates the impact of additional interest rate fac-
a tors. We run a regression of the pricing errors on the level and
kb squared level to check whether any linear or nonlinear effects re-
ti main. For the most part, the answer is no. The level has very little ex-
i planatory power for the pricing errors, with R%s ranging from 1.1%
ki to 2.8%. Moreover, tests of the joint significance of the coefficients
i cannot reject the null hypothesis of no explanatory power at stan-
i dard significance levels. Motivated by our earlier discussion, we also
aH run a regression of the pricing errors for each GNMA on the slope of
id the term structure (the spread between the 10-year yield and the 3-
E month yield) and its squared value. The results strongly support the
b existence of a second factor, with Rs increasing with the coupon
I from a low of 2.0% to 40.1%. Furthermore, this second factor comes
i in nonlinearly as both the linear and nonlinear terms are large and
i significant.
i Most interesting is the fact that the slope of the term structure
: has its biggest impact on higher coupon GNMAs. This suggests an
i important relation between the prepayment option and the term
4 structure slope. Due to the relatively lower value of the prepayment
i option, low coupon GNMAs behave much like straight bonds. Thus,
LC the 10-year yield may provide enough information to price these
3 MBS. In contrast, the call option component of higher coupon
i$
3

---

|
THE PRICING AND HEDGING OF MORTGAGE-BACKED SECURITIES 285
GNMAs is substantial enough that the duration of the bond is
highly variable. Clearly, the slope of the term structure provides in-
formation about the variation in yields across these maturities;
hence, its additional explanatory power for higher coupon GNMAs.
The negative coefficient on the spread implies that the 1-factor MDE
is underpricing when the spread is high. In other words, when
spreads are high, and short rates are low for a fixed long-rate, high-
coupon GNMAs are more valuable than would be suggested by a
1-factor model. The positive coefficients on the squared spread sug-
gest that the relation is nonlinear, with a decreasing effect as the
spread increases. Note that in addition to information about varia-
tion in discount rates across maturities, the spread may also be
proxying for variation in expected prepayment rates that is not cap-
tured by the long rate.
Two-Factor Pricing
Motivated by the results in Table 9.2, it seems important to consider
a second interest rate factor for pricing MBS. Therefore, we describe
the functional relation between GNMA prices and two interest rate
factors, the level of interest rates (the 10-year yield) and the slope of
the term structure (the spread between the 10-year yield and the
3-month yield). In particular, we estimate the pricing functional
given in Equation (9.1) for each of the GNMA coupons. For compar-
ison purposes with Figure 9.3, Figure 9.4 graphs the 9% GNMA
against the interest rate level and the slope. The smoothing factor
for the long rate is fixed at the level used in the one-factor pricing
(i.e. 0.35), and the cross-validation procedure generates a smooth-
ing factor of 1.00 for the spread.

The well-known negative convexity of MBS is very apparent in
Figure 9.4. However, this functional form does not hold in the
northwest region of the figure, that is, at low spreads and low in-
terest rates. The explanation is that the MDE approach works well
in the regions of the available data, but extrapolates poorly at the
tails of the data and beyond. Figure 9.5 graphs a scatter plot of the
interest rate level against the slope. As evident from the figure,
there are periods in which large slopes (3%-4%) are matched with
both low interest rates (in 1993-1994) and high interest rates (in

---

H
| 286 OTHER RISK FACTORS
I FIGURE 9.4. Two-Factor Model Prices of 9% GNMA
i ee
i _ I —
i 7 TT
i 7 = —
| _— an A
ee Nie ~~
: eR MEN pd
@ Seen
| IS SEES = SN NsS=N |
| &y Els |
{ H HRY RRR = |
| he]! a RR RR NRE NN f
| > LRERERRS RRR |
| IRIRIRIRS SNS
EY XK RRR RRR NN
OXI RRERRSKS SR >
| ~~ RX ARERR <=
i LL a =
i Teas RRR “_
| = HER A
i Sa PRS Ae
i pen SR 26
i E— a
4 .
3 EEE
tr Note: The price of a 9% GNMA as a function of the pricing factors: the long
rate and the spread. The pricing functional is estimated using the MDE ap-
i proach and weekly data from January 1987 to May 1994.
i 1988). However, few observations are available at low spreads joint
8 with low interest rates. Thus, the researcher needs to be cautious
i when interpreting MBS prices in this range.
i Within the sample period, the largest range of 10-year yields
Bl ple p 8 8 yeary
4 occurs around a spread of 2.70%. Therefore, we take a slice of the
i pricing functional for the 8%, 9%, and 10% GNMAs, conditional on
i this level of the spread. Figure 9.6 graphs the relation between
Hi GNMA prices for each of these coupons against the 10-year yield.
ii P Pp 5 year yield.
th Several observations are in order. First, the negative convexity of
i each MBS is still apparent even in the presence of the second fac-
i tor. Though the bump in the functional form is still visible, it has
i
it
gl

---

THE PRICING AND HEDGING OF MORTGAGE-BACKED SECURITIES 287
FIGURE 9.5. Interest Rates and Spreads
_—

7 —

0 oog®BaP & o o°

BE SE dean” Coq .

& o & = o ©

2 oF oe 0 Bawa E

3 I. © REE 50°
o 3k o 0% Zoey

8 68%
£ 2 ~ ®
& wv Sg = 8, «2

o 8 @o Bq

h 23°

© &2 Sao

Sh Fhe o

= Co

0

El

's 6 7 E] El 10 1

10-Year Rate

Note: A scatter plot of the pairs of data available for the 10-year rate and the
spread between the 10-year rate and the 3-month rate, from January 1987 to
May 1994.

been substantially reduced. Thus, multiple factors do play a key
role in MBS valuation. Second, the price differences between the
various GNMA securities narrow as interest rates fall. This just rep-
resents the fact that higher coupon GNMAs are expected to prepay
at faster rates. As GNMAs prepay at par, their prices fall because
they are premium bonds, thus reducing the differential between the
various coupons. Third, the GNMA prices change as a function of
interest rates at different rates depending on the coupon level, that
is, on the magnitude of the refinancing incentive. Thus, the effective
duration of GNMAs varies as the moneyness of the prepayment op-
tion changes.

The results of the one-factor pricing analysis and Figures 9.5
and 9.6 suggest the possible presence of a second factor for pricing
MBS. To understand the impact of the term structure slope, Fig-
ure 9.7 graphs the various GNMA prices against interest rate levels,

---

i 288 OTHER RISK FACTORS
ji
13
i FIGURE 9.6. GNMA Prices across Coupons
1 EE ———————
1
]

: -

i . ~ - .

: ll Ts is

j N "

| _— ~ EI

: c= ~ BAKE

; z ~ r

: Ea N

: 3 8 ~

4 ~ oo

~
oh ~

Ii — 8% GNMA

i © —_— = 9% GNMA

hi © Coie 10% GNMA

i LL —

| “ss 8.0 8.5 7.0 75 8.0 8.5 8.0 es
H 10-Year Rate

| Note: Prices of 8%, 9%, and 10% GNMAs for various interest rates, with the
ii spread fixed at 2.70%, as estimated via the MDE approach using weekly data
i from January 1987 to May 1994.

i

i conditional on two different spreads (2.70% and 0.30%)."" Recall that
! the slope of the term structure is defined using the yield on a full-
. P g y

i coupon note, not a 10-year zero-coupon rate. As a result, positive
i spreads imply upward sloping full-coupon yield curves and even
iid more steeply sloping zero-coupon yield curves. In contrast, when the
iE spread is close to zero, both the full-coupon and zero-coupon yield
A curves tend to be flat. Thus, holding the 10-year full-coupon yield
Hl constant, short-term (long-term) zero-coupon rates are lower (higher)
4 for high spreads than when the term structure spread is low.
i In terms of MBS pricing, note that at high interest rate levels,
& the option to prepay is out-of-the-money. Consequently, many of
[£: the cash flows are expected to occur as scheduled, and GNMAs
i have long expected lives. The appropriate discount rates for these
8

H 1The spreads and interest rate ranges are chosen to coincide with the appropriate
bi ranges of available data, to insure that the MDE approach works well.
i
i

---

THE PRICING AND HEDGING OF MORTGAGE-BACKED SECURITIES 289

FIGURE 9.7. GNMA Prices at Different Spreads
-_
< ——-=
=
3 8

Sh - = — 9% GNMA

=~.
PE — ~
8 — 2.7% Spread | } —
| — — 03% Spread | 8% GNMA == -
3 se so es 8.4 8.6 8.8 8.0 8.2 g.4 8.6
10-Year Rates

-_
Note: Prices of 8%, 9%, and 10% GNMAs for various interest rates, with the
spread fixed at 2.70% and 0.30%, as estimated via the MDE approach using
weekly data from January 1987 to May 1994.
cash flows are therefore longer-term zero-coupon rates. Consider
first the effects on the price of an 8% GNMA. Since this security
has its cash flows concentrated at long maturities, its price should
be lower for higher spreads, just as we observe in Figure 9.7. On the
other hand, the option component of the 10% GNMA is much
closer to being at-the-money, even for the highest interest rates
shown in the figure. Hence, at these interest rates, 10% GNMA
prices do not follow the same ordering as 8% GNMAs vis-a-vis the
level of the spread.

As interest rates fall, prepayments become more likely, and the
expected life of the MBS falls for GNMAs of all coupons. As this
life declines, the levels of the shorter-term zero-coupon rates be-
come more important for pricing. In this case, high spreads imply
lower discount rates at the relevant maturities, for a fixed 10-year
full-coupon yield. Consequently, when the GNMAs are priced as
shorter-term securities due to high expected prepayments, high

---

i 290 OTHER RISK FACTORS

i |

i spreads imply higher prices for all coupons. This implication is il-
f lustrated in Figure 9.7. While prices always increase for declining
: long rates, the increase is much larger when spreads are high. For
. the 8% GNMA, this effect causes the prices to cross at a long rate of
i approximately 8.3%, while for the 10% GNMA it causes the pricing
i functionals to diverge further as rates decrease. The effect in Fig-
| ure 9.7 is primarily driven by changes in expected cash flow life.
i The 10-year yield proxies for the moneyness of the option, the ex-
i pected level of prepayments, and the average life of the cash flows.
J The addition of the second factor, the term structure slope, also con-
i trols for the average rate at which these cash flows should be
: discounted.

i To understand the impact of two-factor pricing more clearly,
i Table 9.3 provides an analysis along the lines of Table 9.2 for one-
factor pricing, reporting summary statistics on the pricing errors for

i the 7.5% to 10.5% GNMAs. The addition of a second interest rate
Il factor reduces the pricing error volatility across all the GNMA
| coupons (i.e., from $0.70 to $0.65 for the 7.5s, $0.83 to $0.61 for the
] 9s, and $0.84 to $0.52 for the 10.5s). Most interesting, the largest re-
it duction in pricing error volatility occurs with the higher coupon
{ GNMAs, which confirms the close relation between the slope of the
i term structure and the prepayment option. Table 9.3 also investi-
gates whether there is any remaining level or slope effect on the
kl two-factor MBS prices. We run nonlinear regressions of the pricing
i errors on the level and the slope separately. Neither the level nor the
if slope have any remaining economic explanatory power for the pric-
i ing errors, with R%s ranging from 3.6% to 4.5% for the former and
i R2s under 1.0% for the latter. The tests of joint significance of the
li coefficients exhibit marginal significance for the level, suggesting
Ei that reducing the smoothing parameter will generate a small im-
ft provement in the magnitude of the pricing errors.

<4

ie HEDGING INTEREST RATE RISK

[5

| Hedging Methodology

i This section illustrates how to hedge the interest rate risk of MBS
1 using the pricing model presented here. Since there are two interest

---

THE PRICING AND HEDGING OF MORTGAGE-BACKED SECURITIES 291
TABLE 9.3. Two-Factor GNMA Pricing
-_—
Coupon: 7.5% 8.0% 85% 9.0% 9.5% 10.0% 10.5%
Pricing Errors
Mean 0.018 0.020 0.022 0.023 0.025 0.023 0.018
Mean Abs. 0.503 0.489 0.499 0.494 0.483 0.412 0.396
Vol. 0.646 0.616 0.627 0.623 0.613 0.532 0.523
Autocorr. 0.832 0.843 0.859 0.869 0.864 0.840 0.819
Pricing Error Regression Analysis
Const. 3.470 3.924 4.193 4.183 4.088 3.559 3.002
(2.751) (2.784) (3.112) (3.064) (2.924) (2.228) (1.875)
Long rate -1.036 -1.150 -1.215 -1.207 -1.176 -1.030 -0.878
(0.763) (0.754) (0.830) (0.814) (0.780) (0.605) (0.526)
(Long rate) 0.075 0.082 0.085 0.085 0.082 0.072 0.062
(0.051) (0.049) (0.054) (0.053) (0.051) (0.040) (0.036)
R? 0.041 0.045 0.043 0.040 0.039 0.042 0.036
Joint test 4.775 5.846 5.185 5.059 4.608 5.332 3.792
p-value 0.092 0.054 0.075 0.080 0.100 0.070 0.150
AC(e) 0.825 0.834 0.852 0.865 0.856 0.833 0.814
Const. 0.124 0.096 0.082 0.093 0.117 0.151 0.210
(0.200) (0.182) (0.175) (0.171) (0.178) (0.171) (0.151)
Spread -0.203 -0.158 -0.105 -0.105 =-0.126 -0.183 -0.308
(0.279) (0.265) (0.265) (0.255) (0.243) (0.210) (0.177)
(Spread)? 0.057 0.045 0.028 0.027 0.031 0.046 0.081
(0.072) (0.068) (0.069) (0.065) (0.061) (0.052) (0.043)
R* 0.009 0.006 0.002 0.002 0.003 0.009 0.027
Joint test 0.665 0.486 0.172 0.173 0.270 0.777 3.474
p-value 0.717 0.784 0.917 0.917 0.874 0.678 0.176
AC(e) 0.830 0.841 0.857 0.868 0.862 0.836 0.809
Note: Summary statistics and regression analysis for the pricing errors from a
two-factor (long rate, spread) MDE GNMA pricing model. The regression
analysis involves regressing the pricing errors on linear and squared explana-
tory variables. Heteroscedasticity and autocorrelation consistent standard
errors are reported in parentheses below the corresponding regression coeffi-
cient. AC(e) is the autocorrelation of the residuals from the regression.

---

i 292 OTHER RISK FACTORS
rate factors that are important for pricing MBS we need two fixed-
income assets to hedge out interest rate risk. The hedging instru-
i ments we use are a 3-month T-bill and a 10-year treasury note
| futures contract. Let Oy and og, denote the appropriate posi-
H tions in T-bills and T-note futures contracts respectively to hedge
i the interest rate risk of one unit of a MBS. The hedge position taken
| in each of the instruments should ensure that
0 Po, Pu op,
| t-bill an futures an, an
i OP, OP res dP,
t ©, inp EY D fires TT ——
i Conn) MMA —n) An -1)
; where £ and 525 are the sensitivities of these instruments with
respect to the long rate 7,and slope of the term structure r,—r. The
! equations specify that the sensitivity of MBS price to changes in
i the long rate and the slope of the term structure are exactly offset by
i the corresponding sensitivities of the hedged positions.
| Solving for ®,,., and Ores B1VES
|
| Bu Bp OB, OB,
i o An=r) on 9 Ar-r) 08
1d bill Ser Ty —————— .
4 - IP, yy Burs _ Pwr Bhs
EL an dr-r) An-r) on
i _ Pw Per Pw Pew
El an dr-r) Ar-r) on
bo futures = S535 6-5)
E IP, Bes oF t-bill or futures
A an on-r) Ar-r) an
ia
ih Using Equations (9.4) and (9.5), these hedged portfolios then can
i be constructed ex ante based on the econometrician’s estimate of the
bl partial derivatives of the three fixed-income assets with respect to
lL the two factors. These estimates can be generated from historical
iB
i
pl
pH

---

!
THE PRICING AND HEDGING OF MORTGAGE-BACKED SECURITIES 293
data (prior to the forming of the hedge) using kernel estimation.
For example, an estimate of Hue can be calculated from Equation
(9.2) using
(1-r ln =rl-[n, -r,]
> P, LK (i K 1 Y
Pb, pm ( h, hy,
an - (n=) [n=-rl-n,-r,]
> K ! It l{ 1 s Lt st
EA A
EEA (dE) (RANEY
_— rh
[ ( \T
i ite fe] Bim = ln, =n
> Kj A | Hse Thad
. | =H, he)
12
where K’(z)=-(2n) 2ze 7°. Unfortunately, it is difficult to estimate
the derivative accurately (see Scott, 1992); therefore, we average the
estimated derivative with price sensitivities estimated over a range
of long rates or slopes. For example, we calculate the elasticity
AP, _ B= P(r)
Ar, 7 i
for two different pairs of interest rates, (#,1") and average these val-
ues with the kernel derivative. The points are chosen to straddle the
interest rate of interest. Specifically, we use the 10th and 20th near-
est neighbors along the interest rate dimension within the sample, if
they exist, and the highest or lowest interest rates within the sample
if there are not 10 or 20 observations with higher or lower interest
rates. The return on the hedged portfolio is then given by
Pops + © (Py = P, ) + D irires (Por - Py)
Cat AE "et LCA TS SE 724
Py
where it is assumed that the investor starts with one unit of GNMAs
at time t. The hedged portfolio can then be followed through time

---

!
i
I 294 OTHER RISK FACTORS
: and evaluated based on its volatility and correlation with the fixed-
i income factors, as well as other factors of interest.’
|
i . .
Hedging Analysis
| We conducted an out-of-sample hedging exercise over the period
i January 1990 to May 1994 to evaluate the hedge performance. Start-
i ing in January 1987, approximately three years of data (150 weekly
observations) were used on a weekly rolling basis to estimate the
| MBS prices and interest rate sensitivities as described above. For the
i T-bill and T-note futures, we assume that they move one-for-one
i with the short rate and long rate, respectively. This assumption sim-
i plifies the analysis and is a good first-order approximation. For each
i rolling period, several different hedges were formed for comparison
; purposes:
ih
| 1. To coincide with existing practice, a linear hedge of the
Ii GNMAs against the T-note futures was estimated usin
{ 5 8
rolling regressions. The hedge ratio is given by the sensitiv-
ity of the MBS price changes to futures price changes.
| 2. Breeden (1991) suggests a roll-up/roll-down approach to com-
H puting hedge ratios. Specifically, the hedge can be formed for
I a GNMA by computing the ratio between the T-note futures
i price elasticity and the GNMA price elasticity. (The GNMA
i price elasticity of, say, an 8% GNMA is calculated from the
| difference between the prices of 8%2% and a 72% GNMA. We
ii investigate hedging of 8%, 9%, and 10% GNMAs using
E GNMAs with 7.5% through 10.5% coupons.)
i 3. We investigate the two-factor MDE hedge described by the
Eo portfolio weights given in Equations (9.4) and (9.5).
JR 4. To the extent that the second factor (the slope) seems to play
Ei a small role in pricing it is possible that the slope factor may
i not be important for hedging. To evaluate this, we employ a
i 2The method described here forms an instantaneous hedge, which in theory would
13 8 y
8 §! require continuous rebalancing. For an alternative hedge based on horizon length, see
iid Boudoukh, Richardson, Stanton, and Whitelaw (1995).
fre

---

THE PRICING AND HEDGING OF MORTGAGE-BACKED SECURITIES 295
one-factor MDE hedge using the T-note futures and GNMA
as a function of only the 10-year yield.

Table 9.4 compares the performance of the four hedges for the
8%, 9%, and 10% GNMAs over the 1990 to 1994 sample period. Con-
sider first the 10% GNMA. The unhedged GNMA return has a
volatility of 0.414% (41.4 basis points) on a weekly basis. The two-
factor MDE hedge reduces the volatility of the portfolio to 26.1 basis
points weekly. In contrast, the one-factor MDE hedge, the roll-up/
roll-down hedge and linear hedge manage only 30.0, 29.4, and 34.9
basis points, respectively. The 10% GNMA is the most in-the-money
in terms of the refinancing incentive, and it is comforting to find
that, in the GNMA’s most nonlinear region, the MDE approach
works well.

Figure 9.8 illustrates how the volatility of the hedged and un-
hedged returns move through time. While the volatility of the
unhedged returns declines over time, this pattern is not matched
by the hedged returns. To quantify this evidence Table 9.4 breaks
up the sample into four subperiods: January 1990-February 1991,
March 1991-April 1992, May 1992-June 1993, and July 1993-May
1994. The most telling fact is that the MDE approach does very well
in the last subperiod relative to the other hedges (19.2 versus 39.4
basis points for the roll-up/roll-down approach). This is a period in
which massive prepayments occurred in the first part of the period.
Due to these prepayments, 10% GNMAs are much less volatile than
in previous periods. Thus, the linear and roll-up/roll-down ap-
proaches tended to overhedge MBS, resulting in large exposures to
interest rate risks. This might explain some of the losses suffered by
Wall Street during this period.

On the other hand, the MDE approach does not fare as well in
the first two subperiods. For example, the one- and two-factor
hedges have 38.8 and 29.6 basis points of volatility respectively ver-
sus the unhedged GNMA's volatility of 48.1 basis points in the sec-
ond subperiod. In contrast, the roll-up/roll-down hedge has only
26.4 basis points of volatility. The explanation is that the MDE pro-
cedure does not extrapolate well beyond the tails of the data. During
the first and second subperiod, the rolling estimation period faces
almost uniformly higher interest rate levels than the out-of-sample

---

TABLE 9.4. Hedging Results
Roll-Up MDE
| Period GNMA Linear  Roll-Down  1-Factor  2-Factor
| 8% GNMA
1/90--5/94 68.3 35.0 27.6 30.0 29.4
1/90-2/91 85.5 26.9 27.6 27.8 30.1
3/91-4/92 72.2 30.5 31.7 34.8 32.1
i 5/92-6/93 61.3 37.7 25.9 29.3 27.8
i 7/93-5/94 45.5 43.2 24.8 26.9 27.2
i GAr,A (rn ~r) 59.0 15.0 6.8 6.1 43
CA, 59.0 15.0 6.8 6.1 4.2
| MDE
Period GNMA Linear Breeden 1-Factor ~~ 2-Factor
H 9% GNMA
: 1/90-5/94 53.0 36.8 24.6 29.3 25.6
‘ 1/90-2/91 73.9 24.3 23.5 26.0 27.2
. 3/91-4/92 55.2 32.3 25.8 38.1 28.2
i 5/92-6/93 43.8 46.4 25.3 29.3 25.3
i 7/93-5/94 23.8 39.6 23.7 19.7 20.8
| GAr,A(r, =r) 41.1 18.7 1.2 5.5 3.9
i OAr, 41.1 18.6 0.7 5.3 0.1
I!
i 10% GNMA
J 1/90-5/94 41.4 34.9 29.4 30.0 26.1
i 1/90-2/91 58.2 24.0 22.3 27.6 27.8
] 3/91-4/92 48.1 33.8 26.4 38.8 29.6
5/92-6/93 34.8 44.6 29.2 29.5 27.8
| 7/93-5/94 20.3 32.2 39.4 18.8 19.2
i GAA (r, —r) 28.6 16.4 11.3 5.9 5.4
E GAY, 28.6 16.4 1.3 5.7 1.4
i Note: Results of hedging the 8%, 9%, and 10% GNMAs with various meth-
i ods. Each method's hedge ratios are calculated using the past 150 weeks, for
b the next week. Hence the hedging period is January 1990 through May 1994.
ji The methods are (i) GNMA—the total volatility of an open position (no hedg-
i ing) in basis points, (ii) linear—hedging via linear regression on T-note futures
i returns, (iii) roll-up/roll-down-—a method which infers hedge ratios from con-
HH temporaneous market prices of near coupon MBS, (iv) MDE—hedge ratios de-
if termined via a one-factor (long rate only) and two-factor (long rate and
Hi spread) models, trading in T-note futures and T-bills in the corresponding
i hedge ratios. The last two rows provide a measure of the quantity of interest
tt rate risk (two factor risk or one factor risk), which remains using each
i method's hedging results. In all cases the numbers in the tables represent the
Ho standard deviation of weekly returns in basis points.
bt 296
il

---

FIGURE 9.8. Returns under Alternative Hedging Procedures
Em
Unhedged Returns Linear
© o
3 ! 8
|
© | ©
3 f| 3
o 4 Jl 1 i o
Bi | ya ?
« | | o
| | hd
| pe
Teo me me mem mee es kw meme emer me
Roll-Up/Roll-Down 2 Factor MDE
8 3
o a
EH] i 1. 2 if
: |
3 | i | |
< Al
. o
§ ¢
= a
2 :
E] o
few em mse ess mee ess Yeo ww 2 wm fess tess
Nofer Reedlte fro Toor — or oe —————————————
Note: Results from hedging the 10% GNMA using a rolling regression
method, where “Linear” is hedging via linear regression of returns on T-note
futures, “Roll-Up/Roll-Down” infers hedge ratio from market prices of near
coupon MBS, and “2 Factor MDE” uses the two factor MDE approach. The y-
axis is return expressed in percentage.
297

---

298 OTHER RISK FACTORS
] forecast. Thus, hedge ratios were calculated for sparse regions of
the data.
Recall that the MDE two-factor hedge reduces the volatility to
i 65% of the unhedged GNMA's volatility. Since the hedging was per-
| formed on an out-of-sample basis, there is no guarantee that the re-
| maining variation of the GNMA’s return is free of interest-rate
: exposure. Table 9.4 provides results from a linear regression of the
| GNMA unhedged and hedged portfolio’s return on changes in the
i interest rate level (i.e., Ar,,) and movements in the terms structure
! slope (i.e, A(r,, — 7, )). It gives the volatility of each portfolio due to
i interest rate and term structure slope movements. For example, the
i volatility of the explained portion of the 10% GNMA due to the in-
f terest rate level and slope is 28.6 basis points a week; in contrast,
the MDE two-factor hedged 10% GNMA'’s interest rate risk expo-
i sure is only 5.4 basis points. Note that the roll-up/roll-down and
| linear hedges face much more exposure—11.3 and 16.4 basis points,
i respectively.
i So far, we have described the results for hedging the 10%
: GNMA. Table 9.4 also provides results for the 8% and 9% GNMAs.
Essentially, the patterns are very similar to the 10%, except that the
4 MDE approach fares less well relative to the roll-up/roll-down ap-
i proach. To understand why this is the case, note that the 8% and 9%
: GNMAs have a lower refinancing incentive. The bonds therefore be-
4 have more like a straight bond, and are more volatile (see Table 9.1).
i Thus, because the negative convexity of the GNMAs is less preva-
i! lent for the 8% and 9% coupons, one explanation for why the MDE
i approach to hedging GNMAs fares relatively less well with lower
li coupons is that estimation error is more important. In fact, the roll-
i up/roll-down method actually produces a lower volatility of the
i. hedged GNMA portfolio than the MDE two-factor approach for
i both the 8% and 9% GNMAs (27.6 versus 29.4 basis points for the
He 8%s and 24.6 versus 25.6 basis points for the 9%s).
Multiple factors become less important from a hedging perspec-
i . tive as the GNMA coupon falls (e.g., compare the 8% to 10%). This is
i to be expected, since we argued that the term structure slope plays
Hy a role in pricing as the moneyness of the prepayment option changes
A 3 For completeness we also report the volatility of the returns due only to movements
iH in the long rate. These results are very similar to those discussed above, suggesting
Ey that most of the volatility on a weekly basis is attributable to variation in the long rate.
i.

---

THE PRICING AND HEDGING OF MORTGAGE-BACKED SECURITIES 299
through time. The subperiod analysis confirms the intuition based
on our findings for the 10% GNMAs. While the relative hedging
performance of the various approaches is still related to the sub-
periods, it is less prevalent for the lower coupon GNMAs. The MDE
approach fares relatively best in periods with substantial nonlinear-
ities, for example, the 10% GNMAs during July 1993 to May 1994.
The large prepayments which induced 10% GNMA prices to fall (ce-
teris paribus) did not occur for the 8% GNMAs. After all, the 8%
GNMAs are backed by 8.5% mortgages, and the lowest 30-year
fixed-rate mortgage only briefly dropped below 7%.

Of particular interest, both the MDE approach and the roll-
up/roll-down hedges substantially reduce the interest rate expo-
sure of their 8% and 9% GNMA hedge portfolios. For example, for
the 8% (9%) GNMA, the unhedged GNMA has 59.0 (41.1) basis
point of volatility due to the interest rate factors, while the MDE and
roll-up/roll-down approaches have only 4.3 (3.9) and 6.8 (1.2) basis
points respectively.

CONCLUSION

This chapter presents a nonparametric model for pricing mortgage-
backed securities and hedging their interest rate risk exposures. In-
stead of postulating and estimating parametric models for both
interest rate movements and prepayments, as in previous ap-
proaches to mortgage-backed security valuation, we directly esti-
mate the functional relation between mortgage-backed security
prices and the level of economic fundamentals. This approach can
yield consistent estimates without the need to make the strong as-
sumptions about the processes governing interest rates and prepay-
ments required by previous approaches.

We implement the model with GNMA MBS with various
coupons. We find that MBS prices can be well described as a func-
tion of the level of interest rates and the slope of the term structure.
A single interest rate factor, as used in most previous mortgage val-
uation models, is insufficient. The relation between prices and in-
terest rates displays the usual stylized facts, such as negative
convexity in certain regions, and a narrowing of price differentials
as interest rates fall. Most interesting, the term structure slope

---

i : 300 OTHER RISK FACTORS :
|
plays an important role in valuing MBS via its relation to the inter-
i! est rate level and the refinancing incentive associated with a partic-
| ular MBS. We also find that the interest rate hedge established based
i on our model compares favorably with existing methods.
i On a more general note, the MDE procedure will work well (ina
! relative sense) under the following three conditions. First, since
1 density estimation is data intensive, the researcher either needs a
{ large data sample or an estimation problem in which there is little
i disturbance error in the relation between the variables. Second, the
problem should be described by a relative low dimensional system,
i since MDE’s properties deteriorate quickly when variables are
| added to the estimation. Third, and especially relevant for compari-
son across methods, MDE will work relatively well for highly
f nonlinear frameworks. As it happens, these features also describe
li derivative pricing. Hence, while the results we obtain here for
! GNMAs are encouraging, it is likely that the MDE approach would
| fare well for more complex derivative securities. Though the TBA
market is especially suited for MDE analysis due to its reduction of
i the maturity effect on bonds, it may be worthwhile investigating the
: pricing of interest only (10) and principal only (PO) strips, and col-
: lateralized mortgage obligations (CMOs). Since the relation between
i the prices of these securities and interest rates is more highly non-
i linear than that of a GNMA, a multifactor analysis might shed light
i on the interaction between various interest rate factors and the un-
! derlying prices. The advantage of the MDE approach is its ability to
4 capture arbitrary nonlinear relations between variables, making it
: ideally suited to capturing the extreme convexity exhibited by many
3 derivative mortgage-backed securities.
i
kL REFERENCES
i
FE Ait-Sahalia, Y. (1996). “Nonparametric Pricing of Interest Rate Deriva-
i tive Securities,” Econometrica, 64, 527-560.
i Bartlett, W.W. (1989). Mortgage-Backed Securities: Products, Analysis,
I Trading. New York: Institute of Finance.
bl Boudoukh, J., M. Richardson, R. Stanton, and R.F. Whitelaw. (1995). “A
Hi New Strategy for Dynamically Hedging Mortgage-Backed Securi-
i ties,” Journal of Derivatives, 2, 60-77.
i
bi

---

’ THE PRICING AND HEDGING OF MORTGAGE-BACKED SECURITIES 301

Boudoukh, J., M. Richardson, R. Stanton, and R.F. Whitelaw. (1997).
“Pricing Mortgage-Backed Securities in a Multifactor Interest Rate
Environment: A Multivariate Density Estimation Approach,” Re-
view of Financial Studies, 10, 405-446.

Breeden, D.T. (1991). “Risk, Return and Hedging of Fixed Rate Mort-
gages,” Journal of Fixed Income, 1, 85-107.

Epanechnikov, V. (1969). “Nonparametric Estimates of Multivariate
Probability Density,” Theory of Probability and Applications, 14,
153-158.

Harvey, C. (1991). “The Specification of Conditional Expectations,”
working paper, Fuqua School of Business.

Hutchinson, ].M., A.W. Lo, and T. Poggio. (1994). “A Nonparametric
Approach to Pricing and Hedging Derivative Securities via Learn-
ing Networks,” Journal of Finance, 49, 851-889.

. Pagan, A. and Y.S. Hong. (1991). “Non-Parametric Estimation and the
Risk Premium,” in W. Barnett, J. Powell, and G. Tauchen (Eds.),
Semiparametric and Nonparametric Methods in Econometrics and Statis-
tics, Cambridge: Cambridge University Press.

Richard, S.F. and R. Roll. (1989). “Prepayments on Fixed-Rate Mortgage-
Backed Securities,” Journal of Portfolio Management, 15, 74-82.

Schwartz, E.S. and W.N. Torous. (1989). “Prepayment and the Valua-
tion of Mortgage-Backed Securities,” Journal of Finance, 44, 375-392.

Scott, D.W. (1992). Multivariate Density Estimation: Theory, Practice, and
Visualization, New York: John Wiley & Sons.