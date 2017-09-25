# Pipetting-Robot-Instructions

This repository contains a short script commanding a pipetting robot (www.openstrons.com) to perform the actions outlined in the following spec submitted by a lab director:

> Hardware
> - Robot: OT-One S Hood
> - Pipette(s): p200 (20 - 200 uL) (single), p300 (50 - 300 uL) (multi)
> - Labware: 12 row trough,200uL tiprack,1000 uL tiprack,96 well plate (flat)

> Workflow description from survey: 
> - Step 1: Use multichannel pipet to transfer 200 uL of solution A from Trough A1 into wells A1-H1, A2–H2  of Plate 1 (same tips) 
> - Step 2: Use single channel to add 20, 25, 30, 35, 40, 45, 50, and 55 uL of Sample A (Trough A1 ) into  wells A1-H1 
> - Step 3: Use single channel to add 20, 25, 30, 35, 40, 45, 50, and 55uL  of Sample B (Trough A5) into  wells A2-H2 
> - Step 4: Here we would like the robot to wait 30 minutes.
> - Step 5. After 30 minutes, withdraw all solutions from wells A1–H2 from Plate 1 and place into wells A1–H2 of Plate 2.
> - Step 6. Program complete.
