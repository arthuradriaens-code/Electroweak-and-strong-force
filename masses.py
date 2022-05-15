import numpy as np
import matplotlib.pyplot as plt

m_e = [0.5109*10**6,1.0]
m_mu = [105.658*10**6,2]
m_tau = [1776.86*10**6,3]
m_u = [2.16*10**6,1]
m_d = [4.67*10**6,1]
m_s = [93*10**6,2]
m_c = [1.27*10**9,2]
m_b = [4.18*10**9,3]
m_t = [172.76*10**9,3]
plt.scatter(m_e[0],m_e[1],label="e",c='black')
plt.annotate("e", (m_e[0], m_e[1]+0.05))
plt.scatter(m_tau[0],m_tau[1],label="tau",c='black')
plt.annotate("$τ$", (m_tau[0], m_tau[1]+0.05))
plt.scatter(m_mu[0],m_mu[1],label="mu",c='black')
plt.annotate("$u$", (m_u[0], m_u[1]+0.05))
plt.scatter(m_d[0],m_d[1],label="d",c='black')
plt.scatter(m_u[0],m_u[1],label="u",c='black')
plt.annotate("$\mu$", (m_mu[0]+10**7, m_mu[1]+0.05))
plt.scatter(m_mu[0],m_mu[1],label="mu",c='black')
plt.annotate("d", (m_d[0], m_d[1]+0.05))
plt.scatter(m_s[0],m_s[1],label="s",c='black')
plt.annotate("s", (m_s[0]-11**7, m_s[1]+0.05))
plt.scatter(m_c[0],m_c[1],label="c",c='black')
plt.annotate("c", (m_c[0], m_c[1]+0.05))
plt.scatter(m_b[0],m_b[1],label="b",c='black')
plt.annotate("b", (m_b[0], m_b[1]+0.05))
plt.scatter(m_t[0],m_t[1],label="t",c='black')
plt.annotate("t", (m_t[0], m_t[1]+0.05))
plt.title("fermion masses")
plt.xlabel("eV")
plt.ylim(0,4)
plt.xlim(10**3,10**12)
plt.xscale('log')
plt.axvline(x=10**6, color='black', linestyle='--')
plt.axvline(x=10**9, color='black', linestyle='--')
plt.show()

