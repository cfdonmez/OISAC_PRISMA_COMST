Scenario 1
1) Scenario title: Endogenous telecom-fiber monitoring and carriage co-design (smart_infrastructure).
2) Scenario vector s: 10.4 km telecom fiber span, dual-polarization chirp training sequences, coherent payload coexisting with Rayleigh-backscatter sensing probes, and interference-fading conditions [O_ISAC_074].
3) Sensing task + sensing metric: Sensing-plane task is distributed vibration/fading-robust monitoring; reported sensing metric is 1 m spatial resolution, with reduced trace fluctuation under dual chirp probes [O_ISAC_074].
4) Communication task + comm metric: Comm-plane task is fiber data carriage on the same infrastructure; reported communication metric is 50 GBaud 16-QAM transmission over 10.4 km, with BER behavior reported versus SCPR [O_ISAC_074].
5) Dominant component label + evidence justification: Conventional. The opened source describes chirp TS insertion, FrFT processing, and coherent reception, without explicit OPA/ORIS/Hybrid hardware claims [O_ISAC_074].
6) Transfer hook: Working hypothesis: training-sequence reuse for endogenous sensing can transfer to high-mobility photonic ISAC links that already use shared chirp structures [O_ISAC_074] [O_ISAC_187].
7) Representative works: O_ISAC_074.

Scenario 2
1) Scenario title: Photonic Doppler-robust LEO payload ISAC link (space_satellite).
2) Scenario vector s: LEO satellite-network deployment, significant Doppler shifts in high mobility, chirp-multiplexed IM-LFM shared waveform, and photonic dual-polarization up/down conversion chain [O_ISAC_187].
3) Sensing task + sensing metric: Sensing-plane task is target ranging; reported sensing metric is range resolution better than 0.146 m with probability larger than 86% [O_ISAC_187].
4) Communication task + comm metric: Comm-plane task is payload communication under Doppler; reported communication metrics include 29.99 Mbps and BER below 7% pre-FEC at 500 kHz Doppler shift [O_ISAC_187].
5) Dominant component label + evidence justification: Conventional. The source reports photonic up-converter, de-chirp receiver, and FFT-based recovery, with no explicit OPA/ORIS/Hybrid dominance statement [O_ISAC_187].
6) Transfer hook: Working hypothesis: Doppler-robust index-plus-chirp waveform design can transfer to vehicular optical deployments with mobility-induced frequency stress [O_ISAC_187] [O_ISAC_164].
7) Representative works: O_ISAC_187.

