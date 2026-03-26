# II Section II Gapfill Plan

## Trigger
ESNR (electrical SNR plane) evidence is WEAK based on current anchors.

## Pattern expansions (exact keywords/regex)
- /(?i)received\s+SNR/
- /(?i)SNR\s+at\s+(the\s+)?(photodiode|PD)\s+output/
- /(?i)after\s+(photodetection|PD|photodiode)/
- /(?i)photodetector\s+output/
- /(?i)electrical\s+domain\s+SNR/
- /(?i)post[-\s]?detection\s+SNR/
- /(?i)IM\/DD\s+SNR/

## Targeted manual verification candidates (<=12)
Rationale: VLC/IMDD-likely (visible/UV carrier + direct detection + SNR fields in extraction JSON).
- O_ISAC_003: medium=wireless_vlc, carrier=visible, rx_detection_type=direct, snr_db_present=True; scan sections: metrics, receiver/detection, experimental setup.
- O_ISAC_009: medium=wireless_vlc, carrier=visible, rx_detection_type=direct, snr_db_present=True; scan sections: metrics, receiver/detection, experimental setup.
- O_ISAC_015: medium=wireless_vlc, carrier=visible, rx_detection_type=direct, snr_db_present=True; scan sections: metrics, receiver/detection, experimental setup.
- O_ISAC_022: medium=wireless_vlc, carrier=visible, rx_detection_type=direct, snr_db_present=True; scan sections: metrics, receiver/detection, experimental setup.
- O_ISAC_039: medium=wireless_vlc, carrier=visible, rx_detection_type=direct, snr_db_present=True; scan sections: metrics, receiver/detection, experimental setup.
- O_ISAC_049: medium=vlc, carrier=visible, rx_detection_type=direct_detection, snr_db_present=True; scan sections: metrics, receiver/detection, experimental setup.
