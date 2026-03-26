# VII-E Supplement (Merged Evidence Excerpts)

## Context/Takeaways
| cite_key | excerpt (<=25 words) | locator | used_for |
|---|---|---|---|
| `O_ISAC_089` | "The introduction of inter-satellite links (ISLs) can significantly improve the throughput of the satellite network." | `data/proc_markdowns/O_ISAC_089/O_ISAC_089.md`; HeadingPath: `Abstract`; line span: `9-9` | ISL communication-plane scope |
| `O_ISAC_089` | "the system requires a coarse pointing assembly (CPA) with a broad detection range" | `data/proc_markdowns/O_ISAC_089/O_ISAC_089.md`; HeadingPath: `ACQUISITION, POINTING, AND TRACKING`; line span: `75-75` | motion and alignment constraints |
| `O_ISAC_195` | "in Earth observation and satellite communication applications, ISAC-enabled payloads leverage multiple radar beams to construct multi-dimensional remote sensing channels" | `data/proc_markdowns/O_ISAC_195/O_ISAC_195.md`; HeadingPath: `2. Framework of ISAC systems based on multi-beamforming`; line span: `35-35` | vertical scope cue |

## Scenario 1
| cite_key | excerpt (<=25 words) | locator | used_for |
|---|---|---|---|
| `O_ISAC_089` | "The satellites in the LEO layer are connected by ISLs in a mesh and realize the network access." | `data/proc_markdowns/O_ISAC_089/O_ISAC_089.md`; HeadingPath: `SATELLITE NETWORK SYSTEM ARCHITECTURE`; line span: `45-45` | mesh topology factor |
| `O_ISAC_089` | "each satellite has four laser ISLs to connect the neighboring satellites in the same orbit plane (OP) and adjacent OPs" | `data/proc_markdowns/O_ISAC_089/O_ISAC_089.md`; HeadingPath: `Introduction`; line span: `37-37` | deployment geometry factor |

## Scenario 2
| cite_key | excerpt (<=25 words) | locator | used_for |
|---|---|---|---|
| `O_ISAC_187` | "A 16.3-17.826 GHz IM-LFM waveform is experimentally generated and demonstrated for ISAC purposes." | `data/proc_markdowns/O_ISAC_187/O_ISAC_187.md`; HeadingPath: `Abstract`; line span: `7-7` | shared waveform evidence |
| `O_ISAC_187` | "platforms like LEO satellites with dynamic Doppler shifts as large as hundreds of kilohertz have not been considered" | `data/proc_markdowns/O_ISAC_187/O_ISAC_187.md`; HeadingPath: `1. Introduction`; line span: `19-19` | mobility and Doppler factor |

## Scenario 3
| cite_key | excerpt (<=25 words) | locator | used_for |
|---|---|---|---|
| `O_ISAC_137` | "Measurement by laser beam, artificial satellites, satellite communication, space debris." | `data/proc_markdowns/O_ISAC_137/O_ISAC_137/O_ISAC_137.md`; HeadingPath: `ABSTRACT (Index Terms)`; line span: `23-23` | space lexical cue |
| `O_ISAC_137` | "the system can transfer information from the ground to the satellite or receiving SLR station" | `data/proc_markdowns/O_ISAC_137/O_ISAC_137/O_ISAC_137.md`; HeadingPath: `3. INTEGRATION OF LASER RANGING AND OPTICAL COMMUNICATION`; line span: `77-77` | station-to-satellite deployment |
| `O_ISAC_137` | "the pulse repetition rate has the largest impact on the achievable bitrate of PPM communication system" | `data/proc_markdowns/O_ISAC_137/O_ISAC_137/O_ISAC_137.md`; HeadingPath: `3. INTEGRATION OF LASER RANGING AND OPTICAL COMMUNICATION`; line span: `81-81` | comm-plane metric cue |

## Scenario 4
| cite_key | excerpt (<=25 words) | locator | used_for |
|---|---|---|---|
| `O_ISAC_195` | "capable of simultaneously synthesizing five squint-free beams directed at distinct angles across the entire Ku-band spectrum." | `data/proc_markdowns/O_ISAC_195/O_ISAC_195.md`; HeadingPath: `Abstract`; line span: `5-5` | multi-beam deployment factor |
| `O_ISAC_195` | "The bit error rate (BER) of the signal transmission is 8.15 × 10−<sup>7</sup> , and the EVM is 6.74%." | `data/proc_markdowns/O_ISAC_195/O_ISAC_195.md`; HeadingPath: `3.2. Verification test of the ISAC system`; line span: `122-122` | comm-plane metric evidence |
| `O_ISAC_195` | "wireless communication is realized by receiving 16-QAM signal with 2.4 Gbps data rate at the same time" | `data/proc_markdowns/O_ISAC_195/O_ISAC_195.md`; HeadingPath: `4. Conclusion`; line span: `126-126` | concurrent comm support |

## Math Anchor
| cite_key | excerpt (<=25 words) | locator | used_for |
|---|---|---|---|
| `O_ISAC_187` | "A 29.99-Mbps rate communication is achieved with a 500 kHz Doppler frequency shift." | `data/proc_markdowns/O_ISAC_187/O_ISAC_187.md`; HeadingPath: `Abstract`; line span: `7-7` | supports `R_comm` |
| `O_ISAC_187` | "the bit error rate (BER) is maintained below the 7% pre-forward error correction (pre-FEC) threshold" | `data/proc_markdowns/O_ISAC_187/O_ISAC_187.md`; HeadingPath: `1. Introduction`; line span: `23-23` | supports BER reliability constraint |
| `O_ISAC_195` | "The calculated range resolution is 14.9 cm with a peak sidelobe ratio (PSLR) of 11.61 dB" | `data/proc_markdowns/O_ISAC_195/O_ISAC_195.md`; HeadingPath: `3.2. Verification test of the ISAC system`; line span: `120-120` | supports `J_sense` |
| `O_ISAC_187` | "The sensing range resolution is better than 0.146 meters with a probability larger than 86%." | `data/proc_markdowns/O_ISAC_187/O_ISAC_187.md`; HeadingPath: `Abstract`; line span: `7-7` | supports sensing-quality constraint |
| `O_ISAC_187` | "low-Earth-orbit (LEO) satellite networks offer broad coverage and low communication latency" | `data/proc_markdowns/O_ISAC_187/O_ISAC_187.md`; HeadingPath: `1. Introduction`; line span: `13-13` | supports `s` element (`s_LEO`) |
| `O_ISAC_195` | "includes multiple groups of transmission signal generators and receiving signal processors, along with a shared multi-beamformer and antenna array" | `data/proc_markdowns/O_ISAC_195/O_ISAC_195.md`; HeadingPath: `2. Framework of ISAC systems based on multi-beamforming`; line span: `43-43` | supports `s` element (`s_mb`) |
