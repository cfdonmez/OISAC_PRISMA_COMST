# Section 4 Axis Definitions (v2)

This file freezes taxonomy axes using Section II schema/metric contract and Section IV evidence extraction.

## Axis 1: Medium
Normalized labels: cabled_fibre, hybrid, other, retroreflective, retroreflective_optical, terahertz, wireless, wireless_fso, wireless_retroreflective, wireless_rf, wireless_uv, wireless_vlc

## Axis 2: Integration Mechanism
Normalized labels: separate_frontends, shared_frontend

## Axis 3: Detection / Signal Plane
Normalized labels: coherent, direct, envelope_detection, mimo, other, unknown

## Axis 4: Sensing Task Class
Normalized labels: direction_of_arrival, fault_localization, hand_gesture_recognition, localization, localization_2d, localization_2d|_localization_3d, localization_2d|_target_detection, motion_detection, none, other, ranging, ranging|_localization, ranging|_localization_2d, ranging|_localization_2d|_velocity, ranging|_turbulence_sensing, ranging|_vibration, target_detection, temperature, temperature_sensing, vibration, volcanic_ash_detection

## Contract Notes
- Keep optical-plane and electrical-plane metrics separated.
- Keep resolution and accuracy as separate fields.