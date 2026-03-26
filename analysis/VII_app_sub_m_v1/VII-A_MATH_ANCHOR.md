VII-A. Smart Infrastructure & Outdoor Urban Sensing-Communication (MATH_ANCHOR)

```latex
\max_{u,\pi,T}\ \alpha R_{\mathrm{comm}}(u,\pi;s) - (1-\alpha) J_{\mathrm{sense}}(u,T;s)
```
```latex
\text{s.t.}\ \mathbb{E}\{|x_u(t)|^2\} \le P_{\mathrm{avg}},\quad \max_t\{|x_u(t)|^2\} \le P_{\mathrm{peak}},
```
```latex
\mathrm{BER}(u,\pi;s) \le \beta_{\max}.
```

In this conventional optical-ISAC anchor, `u` denotes waveform and link-adaptation settings, while scenario vector `s` captures deployment state such as distance, user load, and atmospheric condition [O_ISAC_034] [O_ISAC_048]. The communication plane is represented by `R_comm` (achievable rate or spectral efficiency), and the sensing plane is represented by `J_sense` (distance-estimation error, e.g., RMSE or MSE) [O_ISAC_034] [O_ISAC_048]. The average-power, peak-power, and BER constraints encode deployment limits on transmitter budget and service reliability [O_ISAC_034] [O_ISAC_048].
