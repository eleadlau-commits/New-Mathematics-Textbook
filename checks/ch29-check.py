# Chapter 29 check: waves on the circle (numerical, numpy).
import numpy as np
K = 1 << 14; t = (np.arange(K) + 0.5) / K
w = lambda s: np.exp(2j*np.pi*s)
coef = lambda f, n: np.mean(f * w(-n*t))
print("P1 <e_m,e_n>:", all(abs(np.mean(w(m*t)*np.conj(w(n*t))) - (m == n)) < 1e-9 for m in range(-4, 5) for n in range(-4, 5)))
f = np.exp(np.sin(2*np.pi*t)) + np.cos(6*np.pi*t)**3; a = 0.137
fa = np.exp(np.sin(2*np.pi*(t - a))) + np.cos(6*np.pi*(t - a))**3
print("P3 turning:", all(abs(coef(fa, n) - w(-n*a)*coef(f, n)) < 1e-9 for n in range(-6, 7)))
fp = np.exp(np.sin(2*np.pi*t))*2*np.pi*np.cos(2*np.pi*t) - 3*np.cos(6*np.pi*t)**2*np.sin(6*np.pi*t)*6*np.pi
print("P4 derivative:", all(abs(coef(fp, n) - 2j*np.pi*n*coef(f, n)) < 1e-6 for n in range(-6, 7)))
e1 = w(t); print("P5 (e1*e1)^(2) = 1, e1^(2)^2 = 0:", abs(coef(e1*e1, 2) - 1) < 1e-9, abs(coef(e1, 2)) < 1e-9)
sq = np.where(t < 0.5, 1.0, -1.0); N = 400
c = {n: coef(sq, n) for n in range(-N, N + 1)}
tt = np.linspace(0, 0.02, 4001)
SN = np.real(sum(c[n]*w(n*tt) for n in range(-N, N + 1)))
print("P6 overshoot of S_400 near the jump: %.4f" % SN.max())
def fejer(Nf, s): return np.abs(sum(w(k*s) for k in range(Nf + 1)))**2/(Nf + 1)
FN = fejer(20, t); DN = np.real(sum(w(n*t) for n in range(-20, 21)))
print("T2 F_20 >= 0, total 1, D_20 negative somewhere:", FN.min() >= -1e-12, abs(FN.mean() - 1) < 1e-9, DN.min() < 0)
# T2 formula: sigma_N = average of S_0..S_N  equals convolution with F_N (compare coefficients: weight (N+1-|n|)/(N+1))
Nn = 20; ok = True
for n in range(-Nn, Nn + 1):
    ok &= abs(np.mean(FN*w(-n*t)) - (Nn + 1 - abs(n))/(Nn + 1)) < 1e-9
print("T2 coefficients of F_N are (N+1-|n|)/(N+1), the weights of the average:", ok)
sig = np.real(sum((N + 1 - abs(n))/(N + 1)*c[n]*w(n*tt) for n in range(-N, N + 1)))
print("T3 sigma_400 of the square wave stays within [-1,1]: max %.6f" % sig.max(), sig.max() <= 1 + 1e-9)
d = 0.1; s = t[(t >= d) & (t <= 0.5)]
print("T4 F_N <= 1/((N+1) sin^2(pi delta)) for N=5,20,80:", all(fejer(Nf, s).max() <= 1/((Nf + 1)*np.sin(np.pi*d)**2) + 1e-9 for Nf in (5, 20, 80)))
for name, g in (("|sin|", np.abs(np.sin(2*np.pi*t))), ("triangle", 1 - 2*np.abs(t - 0.5)), ("sqrt|t-1/2|", np.sqrt(np.abs(t - 0.5)))):
    cs = {n: coef(g, n) for n in range(-200, 201)}
    errs = []
    for Nf in (10, 50, 200):
        sg = np.real(sum((Nf + 1 - abs(n))/(Nf + 1)*cs[n]*w(n*t) for n in range(-Nf, Nf + 1)))
        errs.append(np.abs(sg - g).max())
    print("T5 %s: largest gap of sigma_N at N=10,50,200:" % name, ["%.4f" % e for e in errs], errs[0] > errs[1] > errs[2])
g = np.exp(np.cos(2*np.pi*t)); g2 = np.exp(np.cos(2*np.pi*t))*((2*np.pi*np.sin(2*np.pi*t))**2 - 4*np.pi**2*np.cos(2*np.pi*t))
nrm = np.sqrt(np.mean(np.abs(g2)**2))
print("T7 |g^(n)| <= ||g''||/(4 pi^2 n^2):", all(abs(coef(g, n)) <= nrm/(4*np.pi**2*n*n) + 1e-12 for n in range(1, 30)))
saw = t - 0.5
print("E4 sawtooth coefficient i/(2 pi n):", all(abs(coef(saw, n) - 1j/(2*np.pi*n)) < 1e-6 for n in (1, 2, 5)), " E5 bound sum 1/n^2 <= pi^2/6:", sum(1/n**2 for n in range(1, 100000)) <= np.pi**2/6)
