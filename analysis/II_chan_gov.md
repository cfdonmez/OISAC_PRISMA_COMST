# Section II-B: Channel Model Governance
    
## 1. Symbol Conventions
- **Atmospheric Loss**: Prefer $h_{atm}$ or $L_{atm}$.
- **Turbulence**: Prefer $h_{tur}$ or $h_{turb}$.
- **Pointing Error**: Prefer $h_{p}$.
- **Structure Parameter**: $C_n^2$ (avoid conflating with scintillation index $\sigma_I^2$).

## 2. Do-Not-Conflate Rules
- **Gamma-Gamma vs Log-Normal**: Verify turbulence regime. Log-Normal is weak turbulence ($<1$ km or low $C_n^2$), Gamma-Gamma covers weak-to-strong.
- **Path Loss includes Pointing?**: Explicitly check if geometric loss $h_{geo}$ includes pointing error $h_{p}$.
- **Attenuation vs Fading**: Attenuation is deterministic (Beer-Lambert); Fading is stochastic (Turbulence).

## 3. Detected Usage Statistics (from Corpus)
- **multipath_nlos**: 725 occurrences
- **noise_regime**: 327 occurrences
- **pointing_error**: 130 occurrences
- **turbulence_general**: 61 occurrences
- **attenuation_beer_lambert**: 55 occurrences
- **turbulence_gamma_gamma**: 44 occurrences
- **turbulence_log_normal**: 32 occurrences
- **turbulence_malaga**: 1 occurrences
