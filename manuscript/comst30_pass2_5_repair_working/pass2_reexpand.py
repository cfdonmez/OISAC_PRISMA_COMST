from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TEX = ROOT / "bare_jrnl_new_sample4.tex"
BIO = ROOT / "biographies_moved_for_submission.tex"


BODY = r"""
\section{Introduction}
\label{introduction}

Integrated sensing and communication (ISAC) has become a central 6G theme because future networks are expected to exchange data, infer geometry, localize users and objects, monitor infrastructure, and adapt to environmental context within the same operating fabric \cite{O_ISAC_070,O_ISAC_162}. Optical integrated sensing and communication (O-ISAC) extends this joint-service idea into optical carriers, guided fiber links, free-space optical links, visible-light/LiFi deployments, and photonics-assisted mmWave/THz chains \cite{O_ISAC_021,O_ISAC_068,O_ISAC_303}. This move is not simply RF-ISAC at a higher carrier frequency. Optical systems expose much larger nominal spectral resources, strong spatial directionality, and mature photonic multiplexing, but they also introduce medium-specific constraints: fiber is guided and often monitored through distributed sensing granularity, FSO is weather- and pointing-sensitive, VLC/LiFi is intensity-domain and illumination-constrained, and photonic-THz systems couple optical generation/distribution to high-frequency wireless propagation \cite{O_ISAC_006,O_ISAC_023,O_ISAC_039,O_ISAC_070}.

The attraction of the optical domain is visible in representative demonstrations. Photonic-THz and fiber-wireless systems report very high data rates together with ranging or radar-style sensing, while multicore and coherent fiber studies show that communication capacity and distributed monitoring can coexist in guided infrastructure \cite{O_ISAC_016,O_ISAC_029,O_ISAC_043,O_ISAC_044,O_ISAC_046,O_ISAC_105}. VLC and LiFi studies, in contrast, often couple indoor data access with positioning, gesture, occupancy, or pose estimation through direct-detection and lighting-aware channels \cite{O_ISAC_009,O_ISAC_022,O_ISAC_039,O_ISAC_050,O_ISAC_062}. These examples motivate O-ISAC as a family of architectures rather than a single pooled performance category.

\begin{figure*}[!t]
    \centering
    \includegraphics[width=\linewidth]{figures/fig1.jpg}
    \caption{O-ISAC landscape across optical spectrum resources and the main fiber, FSO/photonic-THz, and VLC/LiFi branches.}
    \label{fig:fig1}
\end{figure*}

Fig.~\ref{fig:fig1} provides the opening landscape. It separates the broad optical resource argument from the cross-modality synthesis problem. Wide optical bandwidth can support high-rate and fine-delay measurements, yet a fiber \(\Delta z\), a wireless \(\Delta r_{\min}\), an estimator RMSE, a CRB/FIM bound, an optical OSNR value, and an electrical SNR value are not interchangeable evidence objects. This review is built around that distinction. Instead of ranking papers by headline rate or sensing number, it asks when cross-paper comparison is admissible and which reporting fields are needed to make such comparison defensible.

The related survey landscape remains fragmented. RF-ISAC surveys and standardization-oriented discussions establish the broader 6G context but do not resolve optical-plane measurement issues \cite{O_ISAC_161,O_ISAC_162}. VLC/VLP surveys explain visible-light positioning and indoor optical channels, yet usually remain single-modality \cite{O_ISAC_068,O_ISAC_303,O_ISAC_327}. Fiber-oriented reviews emphasize distributed fiber-optic sensing, cabled infrastructure, or optical communication coexistence rather than cross-modality optical ISAC \cite{O_ISAC_006,O_ISAC_041,O_ISAC_090}. Photonic-THz and fiber-wireless reviews highlight high-frequency generation and integrated waveforms but do not fully bridge fiber, FSO, VLC/LiFi, and hybrid platforms under one metric contract \cite{O_ISAC_021,O_ISAC_035,O_ISAC_058,O_ISAC_070}. Table~\ref{tab:axis_comparison} summarizes the gap.

\begin{table*}[!t]
    \caption{Related survey landscape and the contribution of this review.}
    \label{tab:axis_comparison}
    \centering
    \scriptsize
    \setlength{\tabcolsep}{2.4pt}
    \renewcommand{\arraystretch}{1.08}
    \begin{tabularx}{\textwidth}{@{}p{1.25cm}p{0.58cm}p{1.55cm}Xc c c c c@{}}
        \toprule
        Work & Year & Scope & Main emphasis & Syst. & Cross-med. & Tax. & Metric gov. & CRQ \\
        \midrule
        \cite{O_ISAC_161} & 2025 & RF/6G ISAC & RF-centric survey framing and standardization context & No & No & Part & No & No \\
        \cite{O_ISAC_068} & 2024 & VLC & Visible-light JCS prospects and indoor positioning links & No & No & Part & No & No \\
        \cite{O_ISAC_327} & 2024 & VLC/VLP & VLC/VLP channel and localization survey & No & No & Part & No & No \\
        \cite{O_ISAC_006} & 2024 & Fiber & Fiber-sensing ISAC challenges & No & No & Part & No & No \\
        \cite{O_ISAC_021} & 2024 & Optical ISAC & Architecture, potential, and challenge tutorial & No & Part & Part & Part & No \\
        \cite{O_ISAC_070} & 2026 & Photonic THz & Photonic THz-ISAC waveform/system view & No & Part & Part & No & Part \\
        \cite{O_ISAC_163} & 2025 & RIS/ISAC & RIS-enabled ISAC enabler context & No & No & Part & Part & No \\
        This review & 2026 & All optical & PRISMA $N=220$, taxonomy, metric contract, governed tradeoff, enablers, applications, roadmap & Yes & Yes & Yes & Yes & Yes \\
        \bottomrule
    \end{tabularx}
\end{table*}

Four fragmentation mechanisms motivate the review. First, terminology is unstable: optical papers use O-ISAC, LiSAC, optical JCS, photonic ISAC, fiber-ISAC, fiber sensing/communication coexistence, and THz-over-fiber labels for overlapping ideas \cite{O_ISAC_021,O_ISAC_033,O_ISAC_041,O_ISAC_053,O_ISAC_068}. Second, the dominant metrics are not isomorphic across modalities. Third, the communities cite and benchmark within separate silos even when waveforms, calibration, or receiver concepts might transfer \cite{O_ISAC_042,O_ISAC_074,O_ISAC_080,O_ISAC_097,O_ISAC_113}. Fourth, application studies often show domain-specific feasibility without stating which evidence can generalize to other optical media \cite{O_ISAC_084,O_ISAC_123,O_ISAC_129,O_ISAC_143,O_ISAC_155,O_ISAC_160}.

This review contributes five items. First, it builds a PRISMA/TQAF evidence base over \(N=220\) peer-reviewed studies. Second, it defines a cross-modality taxonomy covering fiber, FSO, VLC/LiFi, photonic-THz, and hybrid platforms. Third, it introduces a metric-governance contract that separates \(\Delta r_{\min}\), \(\sigma_r\)/RMSE, CRB/FIM, \(\Delta z\), and OSNR/SNR/ESNR planes. Fourth, it performs a governed rate--resolution and CRQ synthesis that shows the CRQ-valid subset is sparse. Fifth, it links enablers, applications, and open challenges into a roadmap for reproducible, modality-aware O-ISAC research.

\section{Background and Metric-Governance Contract}
\label{sec:background_metric_contract}

An O-ISAC system can be represented as a source, modulation and waveform resources, a propagation medium, receiver observables, and communication/sensing estimators. This abstraction is useful only if the receiver and propagation planes remain explicit. Coherent optical receivers preserve complex-field information and therefore support phase-sensitive observability, carrier recovery, and optical-plane signal-quality measures. IM/DD receivers expose intensity-domain observations after photodetection, so their noise, SNR, and estimator behavior are normally electrical-plane quantities \cite{O_ISAC_001,O_ISAC_022,O_ISAC_028,O_ISAC_029,O_ISAC_039,O_ISAC_132}. Treating these observation modes as equivalent would erase a primary source of metric mismatch.

\begin{figure*}[!t]
    \centering
    \includegraphics[width=\linewidth]{figures/fig_ii_1.png}
    \caption{Unified O-ISAC source--channel--observation abstraction with modality-specific propagation and receiver planes retained.}
    \label{fig:fig_ii_1}
\end{figure*}

Fig.~\ref{fig:fig_ii_1} summarizes the common chain while retaining modality-specific branches. In guided fiber, the signal propagates through a dispersive and nonlinear medium, and sensing often emerges through distributed fiber-optic sensing, vibration monitoring, strain, temperature, or co-route infrastructure monitoring \cite{O_ISAC_006,O_ISAC_013,O_ISAC_024,O_ISAC_032,O_ISAC_046,O_ISAC_076}. In FSO, atmospheric loss, turbulence, pointing, and geometry shape both rate and ranging behavior \cite{O_ISAC_005,O_ISAC_023,O_ISAC_035,O_ISAC_048}. In VLC/LiFi, Lambertian emission, LoS/NLoS composition, illumination constraints, and direct detection dominate the receiver-level model \cite{O_ISAC_009,O_ISAC_022,O_ISAC_039,O_ISAC_054}. In photonic-THz or hybrid systems, optical carriers may generate, distribute, or coherently receive high-frequency signals while wireless propagation occurs at mmWave/THz bands \cite{O_ISAC_026,O_ISAC_029,O_ISAC_047,O_ISAC_065,O_ISAC_070,O_ISAC_077}.

\begin{table*}[!t]
    \caption{Modality-aware O-ISAC abstraction.}
    \label{tab:ii1}
    \centering
    \scriptsize
    \setlength{\tabcolsep}{2.7pt}
    \renewcommand{\arraystretch}{1.08}
    \begin{tabularx}{\textwidth}{@{}p{1.65cm}p{2.05cm}p{2.15cm}p{2.0cm}X@{}}
        \toprule
        Modality & Channel basis & Receiver/observable & Typical task & Governance warning \\
        \midrule
        Fiber & Guided dispersive/nonlinear link; DAS/DFOS granularity & Coherent or direct optical/electrical plane & Vibration, strain, intrusion, co-route monitoring & Report $\Delta z$ and OSNR plane; do not call it wireless range resolution \\
        FSO & LoS optical wireless with turbulence and pointing & Direct or coherent photodetection & Ranging, tracking, link adaptation & Geometry and weather condition admissibility dominate comparison \\
        VLC/LiFi & Lambertian LoS/NLoS indoor optical wireless & Mostly IM/DD, sometimes camera-assisted & Localization, gesture, indoor sensing & Electrical SNR/RMSE cannot be merged with optical OSNR or CRB without model disclosure \\
        Photonic-THz/hybrid & Optical generation/distribution plus mmWave/THz or mixed links & Coherent photonic, electronic, or hybrid chains & High-rate ranging and fiber-wireless transfer & Separate optical generation, wireless propagation, and post-detection measurement planes \\
        \bottomrule
    \end{tabularx}
\end{table*}

The metric contract in Table~\ref{tab:ii2} is the main guardrail. Bandwidth-limited range resolution is
\begin{equation}
    \Delta r_{\min}=\frac{v}{2B_{\mathrm{eff}}},
    \label{eq:range_resolution}
\end{equation}
where \(v=c\) for free-space two-way propagation and \(v\approx c/n_g\) for guided media under the corresponding convention. This expression is a physical resolution limit tied to effective bandwidth. It is not the same as estimator accuracy, localization RMSE, or an empirical standard deviation. Accuracy terms such as \(\sigma_r\) and RMSE depend on SNR, geometry, estimator design, and the data model; CRB/FIM quantities are lower bounds under an explicit observation model and cannot be treated as measured error \cite{O_ISAC_050,O_ISAC_056,O_ISAC_061,O_ISAC_062}.

\begin{table*}[!t]
    \caption{Metric contract for admissible O-ISAC comparison.}
    \label{tab:ii2}
    \centering
    \scriptsize
    \setlength{\tabcolsep}{2.8pt}
    \renewcommand{\arraystretch}{1.08}
    \begin{tabularx}{\textwidth}{@{}p{2.15cm}p{2.15cm}p{2.7cm}X@{}}
        \toprule
        Metric object & Valid role & Must report & Forbidden shortcut \\
        \midrule
        $\Delta r_{\min}$ & Bandwidth-limited resolution & $B_{\mathrm{eff}}$, propagation convention, scenario & Replacing RMSE or CRB with resolution \\
        $\sigma_r$/RMSE & Estimator-level accuracy & estimator, SNR plane, geometry, dataset/simulation setup & Treating as bandwidth-only resolution \\
        CRB/FIM & Bound context & observation model, parameters, noise statistics & Treating as measured accuracy \\
        $\Delta z$ & Fiber spatial granularity & gauge length/segment, interrogator assumptions & Treating as wireless range resolution \\
        OSNR/SNR/ESNR & Signal-quality plane & optical/electrical/reference location and bandwidth & Mixing planes without receiver/noise model \\
        $\mathrm{CRQ}_{\Delta}$ & Rate per bandwidth-limited resolution & matched $R$ and $\Delta r_{\min}$ in one scenario record & Combining unmatched rate and sensing entries \\
        \bottomrule
    \end{tabularx}
\end{table*}

The OSNR/SNR distinction is especially important. Coherent optical studies frequently report OSNR before or around optical reception, while VLC and many OWC studies report electrical SNR after photodetection \cite{O_ISAC_028,O_ISAC_061,O_ISAC_100,O_ISAC_132}. Converting one plane into another requires receiver bandwidth, noise-equivalent power, responsivity, filtering, and detection model assumptions. Without those fields, OSNR and SNR are contextual signal-quality indicators rather than a common axis.

Fiber spatial granularity is a second frequent source of unsafe comparison. Distributed fiber systems report gauge length, segment spacing, or spatial granularity \(\Delta z\). These quantities describe how a guided fiber is interrogated along its length; they do not directly describe free-space range resolution. Conversely, wireless optical \(\Delta r_{\min}\) follows a delay/ranging convention tied to \(B_{\mathrm{eff}}\). A fiber study can be highly valuable for O-ISAC without being a point on the same range-resolution plane as an FSO or photonic-THz ranging record \cite{O_ISAC_006,O_ISAC_013,O_ISAC_046}.

For the governed synthesis, the capacity-resolution quotient is retained only as
\begin{equation}
    \mathrm{CRQ}_{\Delta}=\frac{R}{\Delta r_{\min}},
    \label{eq:crq_delta}
\end{equation}
and only when rate \(R\) and \(\Delta r_{\min}\) are reported for the same scenario record. This is a conservative rule: it excludes tempting but invalid combinations of one paper's rate with another paper's sensing resolution or one experiment's throughput with a different mode's sensing metric. Section~\ref{sec:tradeoff} uses this rule to show that the CRQ-valid subset is sparse, which is a reporting finding rather than a statement that O-ISAC lacks high-performing systems.

\section{Review Methodology}
\label{sec:methodology}

This review follows PRISMA 2020 and PRISMA-S search-reporting principles. The protocol was registered with OSF on February 12, 2026 (Registration ID: \texttt{7f6wb}), and the formal database search used IEEE Xplore, Scopus, and Web of Science. The canonical search was frozen on November 30, 2025. Supplementary preprint monitoring and version tracing were retained for audit purposes, but the canonical PRISMA flow reported here is based on the peer-reviewed database record.

The search blocks combined optical-domain terms, ISAC/JCS terminology, modality-specific terms for fiber, FSO, VLC/LiFi, LiDAR, photonic-mmWave, and photonic-THz systems, and sensing/communication terms. Full search strings are kept in the supplementary evidence package to avoid spending main-text pages on reproducibility mechanics. The main manuscript instead reports the database set, freeze date, eligibility rationale, extraction fields, and the corpus-level synthesis logic.

\begin{table*}[!t]
    \caption{Compact eligibility criteria used for study selection.}
    \label{tab:iii1}
    \centering
    \scriptsize
    \setlength{\tabcolsep}{3pt}
    \renewcommand{\arraystretch}{1.08}
    \begin{tabularx}{\textwidth}{@{}p{2.4cm}X X@{}}
        \toprule
        Criterion & Include & Exclude \\
        \midrule
        Topical scope & Optical, fiber, FSO, VLC/LiFi, photonic-mmWave/THz, or hybrid systems with both sensing and communication relevance & Pure communication, pure sensing, or non-optical RF-only ISAC without optical relevance \\
        Evidence type & Peer-reviewed articles, conference papers, and survey/review works needed for context & Editorial-only, incomplete metadata, inaccessible, or duplicate records outside the audit ledger \\
        Synthesis value & Reports architecture, metric, modality, experiment/simulation, or application information usable for taxonomy/TQAF extraction & No usable O-ISAC extraction fields after full-text assessment \\
        \bottomrule
    \end{tabularx}
\end{table*}

\begin{figure}[!t]
    \centering
    \fbox{\begin{minipage}{0.92\linewidth}
        \centering
        \footnotesize
        IEEE Xplore + Scopus + Web of Science search frozen on Nov. 30, 2025\\[2pt]
        $\downarrow$ deduplication and title/abstract screening\\[2pt]
        222 full texts assessed\\[2pt]
        $\downarrow$ 2 full-text exclusions\\[2pt]
        Final PRISMA corpus: $N=220$ peer-reviewed studies
    \end{minipage}}
    \caption{Compressed PRISMA flow for the final O-ISAC corpus.}
    \label{fig:fig_iii_1}
\end{figure}

Eligibility was intentionally broad enough to capture the fragmented vocabulary of the field but narrow enough to exclude pure optical communications, pure sensing, and RF-only ISAC papers that do not inform optical modality synthesis. During full-text assessment, 222 papers were assessed and 2 were excluded, giving a final included corpus of \(N=220\) peer-reviewed studies. The two full-text exclusions and their reasons are preserved in the structured exclusion ledger.

The TQAF appraisal used five dimensions: topical fit, metric transparency, modality/implementation clarity, methodological reproducibility, and contribution relevance to cross-modality synthesis. This appraisal was not used to create a single quality score that ranks papers; instead, it informed how strongly each record could support taxonomy, metric-governance, enabler, application, or roadmap claims. Simulation-only, experiment-only, and review-style records can all be useful, but they support different kinds of statements.

No statistical meta-analysis is attempted. O-ISAC studies do not yet report enough matched scenarios, common endpoints, uncertainty fields, or receiver-plane details to support pooled effect sizes. The appropriate synthesis is therefore structured and governed: the extraction ledger feeds the taxonomy in Section~\ref{sec:taxonomy}, while scenario-level rate and sensing metrics feed the governed tradeoff synthesis in Section~\ref{sec:tradeoff}. The complete 220-study included-corpus ledger, extraction sheet, and supplementary evidence records are provided in the public repository / Zenodo package.

\section{Unified O-ISAC Taxonomy}
\label{sec:taxonomy}

The taxonomy is designed to make cross-modality comparison possible without hiding ambiguity. Each paper \(p\) is mapped as
\begin{equation}
    T(p)=\bigl(m(p),i(p),d(p),s(p)\bigr),
    \label{eq:taxonomy_vector}
\end{equation}
where \(m\) is medium class, \(i\) is integration class, \(d\) is detection/observability class, and \(s\) is sensing task. These axes were selected because they determine whether two reported performance points can be compared at all. Medium captures the propagation substrate. Integration captures how communication and sensing share waveform, hardware, resource, or processing layers. Detection/observability captures whether the receiver sees direct intensity, coherent field information, camera/Rydberg/other observations, or a mixed chain. Sensing task captures what is being estimated.

\begin{figure*}[!t]
    \centering
    \includegraphics[width=\linewidth,trim=0.8cm 0.7cm 0.8cm 1.1cm,clip]{figures/fig_iv_1.jpg}
    \caption{Semantic taxonomy map retained as the single main-text taxonomy figure.}
    \label{fig:fig_iv_1}
\end{figure*}

\begin{table*}[!t]
    \caption{Compact taxonomy summary across the $N=220$ corpus.}
    \label{tab:taxonomy_compact}
    \centering
    \scriptsize
    \setlength{\tabcolsep}{2.7pt}
    \renewcommand{\arraystretch}{1.08}
    \begin{tabularx}{\textwidth}{@{}p{2.0cm}p{1.65cm}p{2.25cm}p{2.2cm}X@{}}
        \toprule
        Medium & Corpus share & Dominant detection & Dominant task & Governance warning \\
        \midrule
        Fiber & 45/220 & Coherent-leading, with direct tail & Range/vib. monitoring & Compare using guided-channel and $\Delta z$/OSNR semantics \\
        FSO & 19/220 & Mixed direct/coherent & Ranging-heavy & Condition on geometry, turbulence, and pointing assumptions \\
        VLC/LiFi & 25/220 & Direct IM/DD & Localization and ranging & Electrical-plane accuracy dominates; do not infer optical OSNR behavior \\
        Photonic-THz / hybrid & 116/220 hybrid; 39 photonic-THz anchors & Near-balanced coherent/direct & Ranging-heavy with broad multi-task tail & Separate optical generation/distribution from wireless propagation and receiver plane \\
        \bottomrule
    \end{tabularx}
\end{table*}

The medium axis is the first filter. Fiber O-ISAC is the guided anchor of the corpus, with 45 records. It includes distributed acoustic sensing, OFDR/DFOS-style monitoring, coherent communications with embedded sensing pilots, multicore or co-wavelength coexistence, and cabled infrastructure monitoring \cite{O_ISAC_006,O_ISAC_013,O_ISAC_020,O_ISAC_038,O_ISAC_041,O_ISAC_046,O_ISAC_069,O_ISAC_090}. The key interpretation rule is that fiber evidence is not a wireless ranging baseline. It is a guided-medium integration story in which OSNR, gauge length, spatial granularity, and interrogator assumptions often carry more meaning than free-space \(\Delta r_{\min}\).

FSO O-ISAC contains a smaller but important group of wireless optical records. It is strongly ranging-oriented and highly sensitive to link geometry, weather, turbulence, pointing, and blockage. FSO studies include DCO-OFDM, OCDM/FMCW-style waveform design, power allocation, remote phase-shift LiDAR with communication, retroreflective links, and UAV-aided or mixed FSO-RF designs \cite{O_ISAC_005,O_ISAC_023,O_ISAC_035,O_ISAC_040,O_ISAC_048,O_ISAC_051,O_ISAC_055,O_ISAC_099,O_ISAC_106}. Because FSO observability may be direct or coherent, its comparisons must remain receiver-model conditioned.

VLC/LiFi O-ISAC is the most direct-detection-heavy class. It includes indoor positioning, visible-light positioning and communication, LED-based joint systems, camera-assisted variants, gesture recognition, and multi-task learning under visible-light constraints \cite{O_ISAC_009,O_ISAC_022,O_ISAC_030,O_ISAC_039,O_ISAC_050,O_ISAC_054,O_ISAC_062,O_ISAC_068,O_ISAC_092,O_ISAC_110,O_ISAC_303,O_ISAC_327}. The evidence is often rich for localization and indoor services, but it is tied to illumination geometry, Lambertian channel assumptions, electrical SNR, and direct-detection noise. Those assumptions make VLC/LiFi valuable but not directly poolable with coherent fiber or photonic-THz records.

Photonic-THz and hybrid O-ISAC form the bridge class. The optical carrier may drive high-frequency generation, local oscillator distribution, fiber-wireless transport, coherent de-chirping, or THz-over-fiber operation, while the sensing target may lie in a high-frequency wireless channel \cite{O_ISAC_002,O_ISAC_016,O_ISAC_026,O_ISAC_029,O_ISAC_043,O_ISAC_044,O_ISAC_047,O_ISAC_057,O_ISAC_065,O_ISAC_070,O_ISAC_077,O_ISAC_105}. This class is especially tempting for rate--resolution headlines, so it requires strict plane separation: optical generation/distribution evidence, wireless propagation evidence, and post-detection signal-quality evidence are not the same object.

The integration axis distinguishes shared waveform, shared hardware, shared resources, and shared processing. Shared-waveform papers include OFDM/LFM/OCDM/OTFS-like structures where the same waveform carries communication and sensing information \cite{O_ISAC_035,O_ISAC_060,O_ISAC_075,O_ISAC_117,O_ISAC_188,O_ISAC_219,O_ISAC_259,O_ISAC_272}. Shared-hardware records expose common apertures, front-ends, photonic chips, or fiber links \cite{O_ISAC_036,O_ISAC_045,O_ISAC_061,O_ISAC_164,O_ISAC_324,O_ISAC_354,O_ISAC_360}. Shared-resource and shared-processing records express integration through time/frequency/power scheduling, beamforming, or inference pipelines \cite{O_ISAC_049,O_ISAC_052,O_ISAC_083,O_ISAC_086,O_ISAC_102,O_ISAC_134,O_ISAC_138,O_ISAC_140,O_ISAC_242,O_ISAC_340}.

The detection/observability axis prevents receiver-plane collapse. Direct IM/DD and coherent detection dominate the corpus, but the residual categories matter because they show that the field is not limited to a binary receiver taxonomy \cite{O_ISAC_001,O_ISAC_028,O_ISAC_029,O_ISAC_122,O_ISAC_136}. The sensing-task axis similarly separates ranging, localization, vibration/strain, environmental monitoring, object/gesture detection, and multi-task perception. Ambiguous records are retained with explicit tags rather than forced into a single dominant bucket. As a result, the taxonomy reports evidence concentration, not superiority.

\section{Communication-Sensing Tradeoff Synthesis}
\label{sec:tradeoff}

The governed tradeoff synthesis is the core analytical contribution. The extraction produced 225 scenario points from the \(N=220\) paper corpus. Raw metric coverage initially appears broad because many papers report at least one communication metric and at least one sensing metric. Under the governance contract, however, a point is usable only when the relevant metrics belong to a compatible scenario record and the metric role is clear. After filtering, only 20 scenario records support rate plus \(\Delta r_{\min}\), only 16 support rate plus \(\sigma_r\)/RMSE, and only 13 support the full rate--\(\Delta r_{\min}\)--\(\sigma_r\) triplet. This attrition is the central result.

\begin{table*}[!t]
    \caption{Governance attrition from reported metrics to admissible synthesis.}
    \label{tab:governance_attrition}
    \centering
    \scriptsize
    \setlength{\tabcolsep}{3pt}
    \renewcommand{\arraystretch}{1.08}
    \begin{tabularx}{\textwidth}{@{}p{2.8cm}p{2.0cm}p{2.2cm}X@{}}
        \toprule
        Evidence layer & Available count & Main retained use & Main attrition cause \\
        \midrule
        Scenario records & 225 & Corpus-level context & Heterogeneous reporting and modality planes \\
        Rate + $\Delta r_{\min}$ & 20 & CRQ-admissible resolution view & Missing matched bandwidth-limited resolution \\
        Rate + $\sigma_r$/RMSE & 16 & Accuracy-conditioned operating view & Missing estimator/SNR/geometry detail \\
        Full triplet & 13 & Most conservative cross-metric subset & Rate, resolution, and accuracy rarely co-reported \\
        \bottomrule
    \end{tabularx}
\end{table*}

\begin{figure*}[!t]
    \centering
    \includegraphics[width=\linewidth]{figures/fig_v_1.png}
    \caption{Governed rate--resolution and rate--accuracy operating clouds after metric-role filtering.}
    \label{fig:fig_v_1}
\end{figure*}

The first governed view uses rate and \(\Delta r_{\min}\). This view is admissible for records that disclose a bandwidth-limited resolution quantity tied to the same scenario as the reported rate. Photonic-THz and fiber-wireless demonstrations are prominent in this view because they often report high rates and fine delay/ranging resolution in one experiment \cite{O_ISAC_016,O_ISAC_026,O_ISAC_029,O_ISAC_043,O_ISAC_044,O_ISAC_065,O_ISAC_070,O_ISAC_077,O_ISAC_105}. Yet even here, the evidence is sparse compared with the full corpus, and the view should not be interpreted as a universal frontier.

The second governed view uses rate and \(\sigma_r\)/RMSE. This view is different because it is estimator-level and often geometry- or SNR-dependent. VLC/LiFi localization and FSO resource-allocation studies can be important here, but only when the estimation metric, scenario, and signal-quality plane are clear \cite{O_ISAC_009,O_ISAC_023,O_ISAC_039,O_ISAC_050,O_ISAC_052,O_ISAC_054,O_ISAC_061,O_ISAC_062}. A small \(\sigma_r\) value is not automatically comparable with a small \(\Delta r_{\min}\), and a CRB/FIM bound is not a measured RMSE. Fig.~\ref{fig:fig_v_1} therefore separates the operating clouds rather than overlaying all sensing values.

\begin{table*}[!t]
    \caption{Governed fiber, wireless, and hybrid slices.}
    \label{tab:comparative_slices}
    \centering
    \scriptsize
    \setlength{\tabcolsep}{2.8pt}
    \renewcommand{\arraystretch}{1.08}
    \begin{tabularx}{\textwidth}{@{}p{1.7cm}p{2.0cm}p{2.1cm}X@{}}
        \toprule
        Slice & Strong evidence & Weakness for pooling & Main reading \\
        \midrule
        Fiber & Tb/s-class aggregate links and distributed sensing \cite{O_ISAC_046} & $\Delta z$ and OSNR differ from wireless range/ESNR & Guided infrastructure and monitoring anchor \\
        Wireless optical & FSO/VLC ranging/localization and OPA-controlled optical wireless links \cite{O_ISAC_023,O_ISAC_061} & Geometry, turbulence, ambient light, and estimator differences & Scenario-conditioned sensing/communication tradeoff \\
        Photonic-THz/hybrid & High-rate photonic generation plus mmWave/THz ranging \cite{O_ISAC_029,O_ISAC_105} & Optical and wireless planes can be conflated & Bridge class, not a single medium \\
        \bottomrule
    \end{tabularx}
\end{table*}

Table~\ref{tab:comparative_slices} highlights why naive pooling is unsafe. Fiber records can dominate communication capacity or infrastructure monitoring relevance, but their sensing granularity and OSNR semantics differ from wireless range/accuracy metrics \cite{O_ISAC_038,O_ISAC_041,O_ISAC_046,O_ISAC_069,O_ISAC_074}. Wireless optical records often expose clearer ranging/localization tasks but are more sensitive to geometry, channel, and receiver assumptions \cite{O_ISAC_003,O_ISAC_005,O_ISAC_023,O_ISAC_035,O_ISAC_039,O_ISAC_048}. Photonic-THz/hybrid records provide many high-rate, high-frequency anchors, but they mix optical and wireless stages and must be read through the measurement-plane contract \cite{O_ISAC_026,O_ISAC_029,O_ISAC_047,O_ISAC_065,O_ISAC_077,O_ISAC_105}.

The CRQ-valid subset is therefore sparse and illustrative. CRQ is informative when \(R\) and \(\Delta r_{\min}\) are matched, but it is not a stable design envelope for the field. The current evidence says more about reporting practice than about ultimate physical limits: many O-ISAC studies do not report the rate, bandwidth-limited resolution, estimator-level accuracy, receiver plane, and scenario fields needed for full cross-metric synthesis. A future benchmark culture should close this reporting gap before broad optical-ISAC frontiers are claimed.

\section{Enabling Technologies and System-Level Co-Design}
\label{sec:enablers}

O-ISAC enablers matter because they determine whether the metric-governed taxonomy can become deployable systems. The main enabler families are ORIS/optical RIS, OPA, PIC and photonic integration, photonics-assisted mmWave/THz generation, and ML/security-aware adaptation. Table~\ref{tab:vi_a_enablers} keeps the synthesis compact while the surrounding prose explains what each family contributes and what must be reported.

\begin{table*}[!t]
    \caption{Compact enabler synthesis for O-ISAC.}
    \label{tab:vi_a_enablers}
    \centering
    \scriptsize
    \setlength{\tabcolsep}{2.8pt}
    \renewcommand{\arraystretch}{1.08}
    \begin{tabularx}{\textwidth}{@{}p{2.15cm}p{2.65cm}p{2.3cm}X@{}}
        \toprule
        Enabler & Main O-ISAC role & Evidence center & Reporting risk \\
        \midrule
        ORIS / optical RIS & Programmable reflection, beam control, spatial reuse & Optical wireless and RIS-adjacent ISAC \cite{O_ISAC_163} & Geometry and control overhead must be disclosed \\
        OPA & Beam steering and joint communication/sensing aperture & OPA-based optical wireless ISAC \cite{O_ISAC_061,O_ISAC_091} & Beam pattern, scan schedule, and sensing estimator must be linked \\
        PIC / photonic integration & Compact source/modulator/receiver integration & Fiber-wireless and chip-scale demonstrations \cite{O_ISAC_036,O_ISAC_045} & Device results need system-level metric planes \\
        Photonics-assisted mmWave/THz & High-frequency generation/distribution and coherent reception & W-band, D-band, and THz-over-fiber systems \cite{O_ISAC_029,O_ISAC_070} & Separate optical generation from wireless propagation \\
        ML/security adaptation & Inference, calibration, robustness, and attack-aware control & Learning-assisted VLC/fiber-wireless studies \cite{O_ISAC_039,O_ISAC_242} & Dataset, generalization, and threat model must be explicit \\
        \bottomrule
    \end{tabularx}
\end{table*}

ORIS and optical RIS concepts promise programmable optical reflection, beam shaping, and spatial reuse. They are most naturally connected to optical wireless deployments where geometry, blockage, or coverage can be controlled by reconfigurable surfaces \cite{O_ISAC_112,O_ISAC_145,O_ISAC_156,O_ISAC_163,O_ISAC_200}. Their O-ISAC value depends on reporting the surface model, phase/amplitude control assumptions, alignment burden, and whether sensing observes the same controlled path as communication.

OPA technologies provide aperture-level beam steering for optical wireless ISAC. OPA-based optical wireless studies show how beamforming, target direction, and communication performance can be coupled in one front-end \cite{O_ISAC_008,O_ISAC_061,O_ISAC_091,O_ISAC_120}. The reporting challenge is that beam pattern, scan schedule, receiver aperture, estimator, and communication link budget must be tied to the same scenario. Otherwise a beam-steering gain may not support a sensing claim.

PIC and photonic integration provide the device and packaging path for practical O-ISAC. Heterogeneous integration, micro-ring and chip-scale demonstrations, photonic transmitters, and integrated coherent front-ends can reduce size and improve stability, but device-level performance is not automatically system-level sensing/communication evidence \cite{O_ISAC_036,O_ISAC_045,O_ISAC_063,O_ISAC_073,O_ISAC_354,O_ISAC_360}. The metric contract should therefore accompany PIC claims with source, modulator, receiver, calibration, and measurement-plane disclosure.

Photonics-assisted mmWave/THz generation is a key bridge for high-rate high-frequency O-ISAC. Optical carriers can support generation, distribution, coherent reception, de-chirping, or THz-over-fiber transport, enabling W-band, D-band, and THz demonstrations \cite{O_ISAC_026,O_ISAC_029,O_ISAC_031,O_ISAC_043,O_ISAC_044,O_ISAC_047,O_ISAC_057,O_ISAC_065,O_ISAC_070,O_ISAC_077}. The governance issue is that optical and wireless stages must not be collapsed: a high-quality optical generation chain still needs wireless propagation, receiver, and estimator fields for sensing claims.

ML and security-aware adaptation appear across VLC/LiFi localization, fiber-wireless reception, beam management, channel prediction, and robustness studies \cite{O_ISAC_017,O_ISAC_039,O_ISAC_098,O_ISAC_103,O_ISAC_127,O_ISAC_134,O_ISAC_138,O_ISAC_140,O_ISAC_242,O_ISAC_379}. ML can help with calibration, nonlinear compensation, inference, resource allocation, or semantic/context-aware control, but it also introduces dataset dependence, generalization risk, attack surfaces, and privacy concerns. O-ISAC reporting should therefore include data origin, train/test separation, channel variation, threat model, and uncertainty.

\begin{figure*}[!t]
    \centering
    \includegraphics[width=\linewidth]{figures/fig_vi_2.jpg}
    \caption{Deployment-oriented systems map linking optical enablers, impairments, control, and benchmark discipline.}
    \label{fig:fig_vi_2}
\end{figure*}

\begin{table}[!t]
    \caption{Minimum reproducible reporting fields.}
    \label{tab:vi_d_reporting}
    \centering
    \scriptsize
    \setlength{\tabcolsep}{2.5pt}
    \renewcommand{\arraystretch}{1.05}
    \begin{tabularx}{\linewidth}{@{}p{1.8cm}X@{}}
        \toprule
        Field & Required disclosure \\
        \midrule
        Scenario & medium, geometry, range, mobility, weather/ambient state \\
        Link & rate, BER/throughput method, bandwidth, modulation, multiplexing \\
        Sensing & task, $\Delta r_{\min}$ or $\Delta z$, RMSE/$\sigma_r$, CRB/FIM if used \\
        Plane & OSNR/SNR/ESNR reference point and conversion model if any \\
        Evidence & simulation/experiment, data/code availability, uncertainty reporting \\
        \bottomrule
    \end{tabularx}
\end{table}

Fig.~\ref{fig:fig_vi_2} and Table~\ref{tab:vi_d_reporting} convert the enabler discussion into a reporting contract. Programmable optical hardware, photonic high-frequency generation, and ML adaptation are not enough on their own. They become comparable O-ISAC evidence only when the channel, scenario, metric plane, estimator, and benchmark workflow are disclosed together.

\section{Applications and Use Cases Across Domains}
\label{sec:applications}

Application evidence is treated as a deployment map rather than a maturity scorecard. The corpus spans smart infrastructure, indoor VLC/LiFi localization, automotive and optical V2X, underwater or harsh OWC, and space/NTN or satellite-oriented photonic systems. Table~\ref{tab:section7_portfolio} compresses these domains into five motifs while preserving the transfer warning for each.

\begin{table*}[!t]
    \caption{Application portfolio compressed to five macro-domains.}
    \label{tab:section7_portfolio}
    \centering
    \scriptsize
    \setlength{\tabcolsep}{2.8pt}
    \renewcommand{\arraystretch}{1.08}
    \begin{tabularx}{\textwidth}{@{}p{2.35cm}p{2.6cm}p{2.55cm}X@{}}
        \toprule
        Macro-domain & Communication motif & Sensing motif & Transfer warning \\
        \midrule
        Smart infrastructure / cabled-fiber corridor & High-capacity transport and monitoring overlays & Vibration, strain, intrusion, seismic/corridor awareness & Strong for guided infrastructure; weak as wireless baseline \\
        Indoor VLC/LiFi localization & Lighting/data access and room-scale links & Positioning, gesture, occupancy, camera-assisted sensing & Direct-detection and ambient-light assumptions dominate \\
        Automotive / optical V2X & Short-range optical links and beam-controlled access & Ranging, pose, cooperative perception & Geometry, eye safety, weather, and blockage must be disclosed \\
        Underwater or harsh OWC & Optical wireless where RF is limited & Salinity, environmental, and link-state monitoring & Medium absorption/scattering makes transfer highly conditional \\
        LEO/satellite or space photonic O-ISAC & Space/NTN optical backhaul and hybrid network support & Tracking, ranging, situational awareness & Evidence is roadmap-oriented and needs deployment validation \\
        \bottomrule
    \end{tabularx}
\end{table*}

Smart infrastructure and cabled-fiber corridors are natural O-ISAC domains because installed fiber can carry data while sensing vibration, strain, temperature, intrusion, or environmental events along the route \cite{O_ISAC_013,O_ISAC_020,O_ISAC_038,O_ISAC_064,O_ISAC_069,O_ISAC_074}. Their value is strongest for guided infrastructure and transport monitoring. Transfer to wireless optical ISAC is conditional because the sensing object is a distributed guided medium rather than a free-space target.

Indoor VLC/LiFi localization uses lighting infrastructure, room-scale data access, and direct-detection observability to support positioning, gesture recognition, occupancy, and multi-task sensing \cite{O_ISAC_009,O_ISAC_011,O_ISAC_022,O_ISAC_030,O_ISAC_039,O_ISAC_050,O_ISAC_054,O_ISAC_060}. The deployment motif is compelling because luminaires are already spatially structured, but the results remain tied to room geometry, ambient light, receiver orientation, camera or photodiode assumptions, and electrical-plane metrics.

Automotive and optical V2X records connect O-ISAC to short-range optical links, beam-controlled access, cooperative perception, and ranging/pose estimation \cite{O_ISAC_003,O_ISAC_021,O_ISAC_034,O_ISAC_071,O_ISAC_089,O_ISAC_109,O_ISAC_137}. The transfer warning is stronger here: weather, blockage, eye safety, mobility, synchronization, and field-of-view constraints must be explicit before a laboratory optical link can be interpreted as deployment evidence.

Underwater and harsh OWC cases appear where RF propagation is limited or environmental sensing is part of the communication mission. Representative records include underwater or harsh-medium optical links, salinity/environmental monitoring, and hybrid OWC designs \cite{O_ISAC_005,O_ISAC_027,O_ISAC_055,O_ISAC_108,O_ISAC_187,O_ISAC_252}. These applications are highly medium-specific because absorption, scattering, turbulence, and alignment dominate both communication and sensing performance.

LEO, satellite, and space photonic O-ISAC are more roadmap-oriented. Optical backhaul, NTN integration, tracking, ranging, and space/airborne network control suggest a future O-ISAC role in multi-layer networks \cite{O_ISAC_059,O_ISAC_070,O_ISAC_127,O_ISAC_130,O_ISAC_164,O_ISAC_220,O_ISAC_248,O_ISAC_276,O_ISAC_291}. The evidence should not be read as mature across all space deployments; it is a transfer map showing where photonic links, pointing, tracking, and network orchestration may converge.

\section{Open Challenges and Research Roadmap}
\label{sec:roadmap}

The roadmap is organized around five challenge domains: standardization/interoperability, hardware scalability, channel modeling/evaluation, security/privacy/reliability, and deployment convergence. Fig.~\ref{fig:fig_viii_1} links these domains back to the metric contract, enablers, and application motifs.

\begin{figure*}[!t]
    \centering
    \includegraphics[width=\linewidth]{figures/fig_viii_1.jpg}
    \caption{Challenge-to-roadmap dependency map for taxonomy, metrics, benchmarks, hardware, security, and deployment validation.}
    \label{fig:fig_viii_1}
\end{figure*}

\begin{table*}[!t]
    \caption{Compressed O-ISAC challenge domains.}
    \label{tab:challenge_compact}
    \centering
    \scriptsize
    \setlength{\tabcolsep}{2.8pt}
    \renewcommand{\arraystretch}{1.08}
    \begin{tabularx}{\textwidth}{@{}p{2.4cm}p{3.0cm}X@{}}
        \toprule
        Domain & Bottleneck & Roadmap response \\
        \midrule
        Std./interoperability & Terminology, taxonomy, and reporting fields remain inconsistent & Shared O-ISAC taxonomy, PRISMA-style ledgers, metric-governed templates \\
        Hardware scalability & OPA/ORIS/PIC/photonic-THz demonstrations are promising but unevenly integrated & Co-design aperture, source, receiver, calibration, and packaging metrics \\
        Channel modeling/evaluation & Fiber, FSO, VLC, and photonic-THz assumptions are often mixed & Scenario-tagged benchmark channels and plane-aware signal-quality reporting \\
        Security/reliability & ML, sensing data, and narrow-beam control add new attack and failure surfaces & Threat-modeled evaluation with robustness and privacy fields \\
        Deployment convergence & Application claims outpace cross-domain validation & Domain-aware pilots tied to reproducible evaluation workflows \\
        \bottomrule
    \end{tabularx}
\end{table*}

Standardization and interoperability are the first bottleneck. O-ISAC currently spans multiple naming conventions, channel models, and reporting cultures. A common vocabulary should not erase modality differences; it should require authors to declare medium, integration mechanism, detection/observability class, sensing task, metric role, and signal-quality plane \cite{O_ISAC_161,O_ISAC_162,O_ISAC_327}. The most practical near-term step is a reporting template aligned with Table~\ref{tab:ii2} and Table~\ref{tab:vi_d_reporting}.

Hardware scalability is the second bottleneck. OPA, ORIS, PIC, and photonics-assisted mmWave/THz systems are promising, but they are not yet evaluated under a shared deployment and benchmark protocol \cite{O_ISAC_008,O_ISAC_036,O_ISAC_061,O_ISAC_091,O_ISAC_145,O_ISAC_163}. Future prototypes should report aperture, beam-control, calibration, packaging, thermal, synchronization, and receiver-plane details together with communication and sensing metrics.

Channel modeling and evaluation remain fragmented. Fiber, FSO, VLC/LiFi, and photonic-THz systems require different channel assumptions, and a benchmark should not pretend that one model covers all of them \cite{O_ISAC_005,O_ISAC_023,O_ISAC_035,O_ISAC_039,O_ISAC_041,O_ISAC_050}. The roadmap should therefore define scenario families: guided infrastructure, indoor visible light, atmospheric FSO, photonic-THz/fiber-wireless, underwater/harsh OWC, and NTN/space optical links. Each family needs common reporting fields and uncertainty treatment.

Security, privacy, and reliability become more important as O-ISAC moves from link demonstrations to sensing-rich deployments. Optical beams offer spatial isolation, but narrow beams, reflected paths, sensing data, ML inference, and programmable surfaces create attack and failure modes that differ from conventional optical communications \cite{O_ISAC_093,O_ISAC_112,O_ISAC_133,O_ISAC_134,O_ISAC_151,O_ISAC_381}. The field needs threat-modeled benchmarks rather than security claims attached only as future work.

Deployment convergence is the final challenge. O-ISAC must connect physical-layer metrics, network orchestration, application requirements, and reproducible evidence. Smart infrastructure, indoor LiFi, vehicular optical links, harsh OWC, and NTN/space photonics each define different success criteria \cite{O_ISAC_025,O_ISAC_059,O_ISAC_064,O_ISAC_127,O_ISAC_164,O_ISAC_220,O_ISAC_237}. The roadmap is therefore not a single technology ladder; it is a set of domain-conditioned validation paths.

\begin{table*}[!t]
    \caption{Five-item prioritized research agenda.}
    \label{tab:viii_f_2}
    \centering
    \scriptsize
    \setlength{\tabcolsep}{2.8pt}
    \renewcommand{\arraystretch}{1.08}
    \begin{tabularx}{\textwidth}{@{}p{0.55cm}p{2.7cm}X p{2.15cm}@{}}
        \toprule
        Pri. & Agenda item & Concrete deliverable & Risk if deferred \\
        \midrule
        1 & Metric-governed reporting & Required fields for rate, $\Delta r_{\min}$, $\sigma_r$/RMSE, CRB/FIM, $\Delta z$, OSNR/SNR plane & Persistent unsafe comparisons \\
        2 & Reproducible corpus workflow & Public ledgers, search strings, extraction sheets, and code for figures/tables & Weak systematic-review traceability \\
        3 & Cross-modality benchmarks & Fiber/FSO/VLC/photonic-THz scenario templates with uncertainty reporting & Non-transferable performance claims \\
        4 & Scalable hardware evidence & OPA/ORIS/PIC/photonic-THz prototypes evaluated with shared fields & Enabler claims remain isolated \\
        5 & Deployment validation & Domain pilots for infrastructure, indoor, vehicle, harsh OWC, and space/NTN cases & Application map remains aspirational \\
        \bottomrule
    \end{tabularx}
\end{table*}

The resulting COMST roadmap is methodological and technological at the same time. O-ISAC needs better hardware, but it also needs interoperable taxonomy, metric-governed reporting, reproducible workflows, benchmark channels, and domain-aware validation before cross-modality performance claims become robust.

\section{Conclusions}
\label{sec:conclusion}

This review synthesized optical integrated sensing and communication as a family of architectures rather than a monolithic interchangeable design space. Using a PRISMA-grounded corpus of 220 studies, it organized fiber, FSO, VLC/LiFi, photonic-THz, and hybrid work through a cross-modality taxonomy and a metric-governed comparison contract. The central lesson is that comparability requires explicit modality, metric role, measurement plane, and deployment context: \(\Delta r_{\min}\) is not \(\sigma_r\)/RMSE, CRB/FIM is a bound-level statement, fiber \(\Delta z\) is not wireless range resolution, and OSNR and electrical SNR cannot be exchanged without a receiver/noise model. Under that governed reading, the rate--resolution evidence is informative but sparse: only small subsets of the 225 extracted scenario records support admissible CRQ or full triplet synthesis. Future progress therefore depends as much on reporting practice as on hardware advances. Reproducible workflows, benchmark definitions, scalable OPA/ORIS/PIC and photonic-THz hardware, security-aware adaptation, and domain-aware validation are the necessary path from promising O-ISAC demonstrations to credible 6G systems.

"""


def replace_between(text: str, start_pat: str, end_pat: str, replacement: str) -> str:
    start = re.search(start_pat, text, flags=re.S)
    end = re.search(end_pat, text, flags=re.S)
    if not start or not end or start.start() >= end.start():
        raise RuntimeError("Could not locate body replacement anchors")
    return text[: start.start()] + replacement + text[end.start() :]


def main() -> None:
    text = TEX.read_text(encoding="utf-8")
    text = replace_between(text, r"\\section\{Introduction\}", r"\\bibliographystyle\{IEEEtran\}", BODY)
    text = text.replace("\n\\nocite{*}\n", "\n")

    bio_match = re.search(r"\\newpage\s*(\\begin\{IEEEbiography\}.*)\\end\{document\}", text, flags=re.S)
    if bio_match:
        BIO.write_text(
            "% Biographies moved out of the submission-length build during Pass 2.\n\n"
            + bio_match.group(1).strip()
            + "\n",
            encoding="utf-8",
        )
        text = text[: bio_match.start()] + (
            "\n\n% Biographies are omitted from the submission-length build and can be restored for final production if required.\n"
            "\\end{document}\n"
        )
    else:
        BIO.write_text("% No IEEEbiography blocks found to move.\n", encoding="utf-8")

    TEX.write_text(text, encoding="utf-8")
    print("Pass 2 re-expansion applied.")
    print(f"Biographies file: {BIO.name}")


if __name__ == "__main__":
    main()
