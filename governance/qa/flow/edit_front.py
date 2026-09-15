"""Apply the front-matter consolidation; scientific source text remains in Git."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[3]
sections=root/'manuscript/sections'
p=sections/'01_INTRODUCTION.tex'
s=p.read_text(encoding='utf-8')
s=s.replace('Figure~\\ref{fig:oisac_platform_overview} illustrates these physical settings\nand the resources used by both functions.\nIts common design question is how choices of power and waveform, together\nwith timing and receiver design, affect communication and sensing performance.',
'''The common design question is how the shared resource changes the signal
available to each receiver, and therefore the communication and sensing
performance. Section~\\ref{sec:signal_paths_observations} develops these paths
in one physical diagram.''')
s=re.sub(r'\\begin\{figure\*\}.*?\\label\{fig:oisac_platform_overview\}\s*\\end\{figure\*\}\s*','',s,count=1,flags=re.S)
s=s.replace('The fiber result illustrates a power-dependent tradeoff, whereas the\nvisible-light result shows how sensing information can guide transmission.\n','')
s=s.replace('A researcher selecting an O-ISAC approach needs to know which integration\nmechanism fits the application and how it affects both functions.\nReported rates and sensing errors become useful for that choice when they\nare linked to the shared design and its operating conditions.\nThese links can explain why a method is effective in one setting and what\nmust be tested before adapting it to another.\nA synthesis of the literature should therefore connect physical architectures\nto joint performance and to the experiments needed for further development.',
'''These different responses make resource reuse an insufficient basis for
selecting an architecture. The relevant question is which physical mechanism
connects the two outcomes and whether it remains useful under the application's
power, geometry, traffic, and timing constraints. This survey follows that
connection from architecture through performance and validation to the tests
needed for further development.''')
s=s.replace('\\item \\begin{minipage}[t]{\\linewidth}\n','\\item ')
s=s.replace('\\end{minipage}\n','')
s=s.replace('\n\\FloatBarrier\n','\n')
p.write_text(s,encoding='utf-8')
p=sections/'02_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex'
s=p.read_text(encoding='utf-8')
s=s.replace('Numerical examples show how a shared setting connects the resulting\nperformance, providing a basis for the architectures and design relationships in\nSections~\\ref{sec:optical_modality_families} and~\\ref{sec:tradeoffs}.\n','')
s=s.replace('figures/fig_section2_signal_paths_icons_2026-09-10.png','figures/paths.pdf')
s=s.replace('figures/fig_section2_resource_sharing_icons_2026-09-11.png','figures/sharing.pdf')
s=s.replace('electrical signal-to-noise\nratio (SNR) after receiver processing,','electrical signal-to-noise\nratio (SNR) at the stated electrical receiver plane,')
s=s.replace('Receiver icons represent functional roles with shared or separate hardware.',
'''Receiver icons represent functional roles with shared or separate hardware.
Panel (a) illustrates a laser and external modulator; an intensity-driven LED
can supply the optical waveform in an IM/DD implementation.''')
s=s.replace('Figure~\\ref{fig:bandwidth_resolution} shows this physical scale using the\n6.2~GHz sweep reported in a photonic-THz experiment\n\\cite{OISAC_SCR00083}.\n','')
s=re.sub(r'\\begin\{figure\}\[!t\].*?\\label\{fig:bandwidth_resolution\}\s*\\end\{figure\}\s*','',s,count=1,flags=re.S)
s=s.replace('The same\n6.2~GHz experiment reports a maximum ranging error of 0.55~cm for static\ntargets at 20--45~cm \\cite{OISAC_SCR00083}.',
'''For example, a 6.2~GHz sweep gives a nominal resolution of about 2.4~cm,
whereas the experiment reports a maximum ranging error of 0.55~cm for static
targets at 20--45~cm \\cite{OISAC_SCR00083}.''')
start=s.index('\\begin{table*}')
end=s.index('\\end{table*}',start)+len('\\end{table*}')
s=s[:start]+r'''\begin{table*}[!t]
\caption{Three examples of metric interpretation under source-specific test conditions}
\label{tab:section2_quantitative_examples}
\centering
\footnotesize
\setlength{\tabcolsep}{5pt}
\renewcommand{\arraystretch}{1.12}
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.25\textwidth}
>{\raggedright\arraybackslash}p{0.40\textwidth}>{\raggedright\arraybackslash}X@{}}
\toprule
\textbf{Configuration} & \textbf{Reported communication and sensing measures} & \textbf{Interpretation} \\
\midrule
Fiber \cite{OISAC_SCR00057}: 40~km; two 30~GBaud 16-QAM subcarriers;
500~MHz LFM probe; 200~Hz vibration on a 1~m segment. &
$2\times120$~Gbit/s during concurrent sensing; nominal spatial resolution
1~m with a 10~m gauge length. Probe pre-compensation improves vibration-spectrum
SNR by 2.4~dB. &
Gauge length differs from spatial resolution. The 2.4~dB gain is a
pre-compensation result, separate from the probe-power sweep, which fixes
communication launch power at 0~dBm rather than total power. \\
\addlinespace[4pt]
Visible light \cite{OISAC_SCR00196}: 225~mW white laser; 1~GHz receiver;
$0.6\times0.6$~m illumination area at 2~m. &
Estimated rate averages 3.35~Gbit/s (3.16--3.52 across patterns).
Separate tests resolve 1~mm lateral and approximately 4~cm depth displacements;
dynamic localization runs at 39~frames/s. &
Estimated rate is not delivered throughput. Pattern averages, static spatial
tests and dynamic localization describe different evaluations. \\
\addlinespace[4pt]
Photonic THz \cite{OISAC_SCR00083}: 262.1--268.3~GHz ASK/FMCW signal;
6.2~GHz sweep in 400~ns; communication distance 1~m. &
15~Gbit/s with BER $2.97\times10^{-3}$; approximately 36.2~GHz occupied
bandwidth. Nominal range resolution 2.4~cm; maximum error 0.55~cm for static
targets at 20--45~cm in a separate receiver configuration. &
Sweep and occupied bandwidth differ. Range error is distinct from resolution;
target range is distinct from communication distance. \\
\bottomrule
\end{tabularx}
\vspace{3pt}
\parbox{\textwidth}{\footnotesize Values in a row may come from separate tests
and do not by themselves define one jointly measured operating point.
QAM: quadrature amplitude modulation; LFM: linear frequency modulation;
ASK: amplitude-shift keying; FMCW: frequency-modulated continuous wave.}
\end{table*}'''+s[end:]
start=s.index('The clearest performance link is a controlled change')
end=s.index('Once both outcomes can be evaluated',start)
s=s[:start]+'''A shared waveform can support both tasks while their reported numerical
results come from different receiver configurations or tests, as in the
photonic-THz and visible-light examples. A controlled sweep instead links a
specific change to both responses. Section~\\ref{sec:tradeoffs} examines such
within-study relationships, including the fiber probe-power sweep, and
distinguishes them from benefits obtained by sharing receiver information.

'''+s[end:]
start=s.index('The same condition set also determines what further evaluation')
s=s[:start]+'''The architecture analysis in Section~\\ref{sec:optical_modality_families}
now identifies which shared choices each physical platform makes available.
Their measured or modeled consequences follow in Section~\\ref{sec:tradeoffs}.
'''
p.write_text(s,encoding='utf-8')
print('Updated Introduction and Foundations; source and evidence conditions retained.')
