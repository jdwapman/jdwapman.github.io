---
title: "NASA Jet Propulsion Laboratory"
excerpt: "Planar air-bearing platform used for CubeSat dynamics and control algorithm testing<br/><br/><img src='/files/jpl/marco.jpg' width='500'><br/><br/>Image: Mars as captured by the MarCO-B CubeSat during the InSight landing [(source)](https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA22833)"
collection: portfolio
---

During Summer 2019 I worked as an intern in the Guidance & Control group at NASA's Jet Propulsion Laboratory in Pasadena, CA.

CubeSats are small, relatively cheap satellites that have been successfully used for gathering climate data, imaging distance galaxies, and most recently for relaying telemetry data from the InSight Lander's landing on Mars using the [MarCO CubeSats](https://www.jpl.nasa.gov/cubesat/missions/marco.php).

![MarCO](/files/jpl/marco_bench.jpg)  
[Source](https://photojournal.jpl.nasa.gov/feature/marco)

Since CubeSat mission budgets are typically small, the [Small Satellite Dynamics Testbed](https://scienceandtechnology.jpl.nasa.gov/small-satellite-dynamics-testbed-ssdt) at JPL has been leading an effort to create a suite of test platforms and procedures that can be used by multiple CubeSat missions, thus reducing the need for each individual mission to create and validate test equipment from scratch. One such platform is a planar air-bearing platform, used to simulate zero-gravity dynamics on a flat floor.  

![SSDT](/files/jpl/ssdt.png)  
[Source](https://scienceandtechnology.jpl.nasa.gov/small-satellite-dynamics-testbed-ssdt)

The first iteration of this platform was successfully used to test the MarCO CubeSats before launch. However, there were several limitations to this platform. The first was that it had no onboard position-control functionality. Platform operators had to physically move the platform - limiting its accuracy, repeatability, and the types of tests it could be used for.  

At the time I started my internship, the SSDT had recently procured a second iteration of the planar platform, which included an array of onboard thrusters that could be controlled by an onboard computer to controll the platform's motion. My internship task was to write a software library for this platform that users could access to control its motion, with functions such as PID position and velocity control, arbitrary force generation, thruster ON/OFF manipulation, and telemetry data capture. Additionally, I was tasked with characterizing the platform's mechanical properties (center of mass, moment of inertia, thruster force generation capabilities, etc).

Although the platform is still under development, in the future it will be used to support further CubeSat launches and research. A technical report for this project is currently in peer review with the Journal of Spacecraft and Rockets.
