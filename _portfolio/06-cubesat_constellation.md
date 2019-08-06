---
title: "CubeSat Constellation Separation"
excerpt: "Optimal Control Theory Course Project:<br/>Simulated CubeSat constellation separation using nonlinear programming to maximize constellation lifetime<br/><img src='/files/cubesat_constellation/NonlinearOptimization.png' width='500'><br/><br/>Image: Simulation of Satellite Constellation Separation using Nonlinear Programming"
collection: portfolio
---

This project was for a graduate-level course on optimal control theory. In this project, I and a team of two other students attempted to replicate and extend upon a method of separating a CubeSat constellation using differential drag - controlling the speed and altitude of a satellite by varying the satellite's orientation (and therefore its exposed surface area to air resistance) - to create even spacing in the constellation with the goal of maximizing the constellation's lifetime before the CubeSats dropped too low and burned up in Earth's atmosphere. This method of constellation separation has been sucessfully used by [Planet Labs](https://www.planet.com/) in the past.

Sin et. al. studied this separation method in [their 2017 paper](https://arxiv.org/abs/1710.00104) by approximating the complex nonlinear atmospheric dynamics as a linear process. My team was interested in evaluating how much accuracy the researchers lost with this approximation, and attempted to perform a nonlinear optimization in MATLAB.  

For more detail, our project report is available [here](/files/cubesat_constellation/Linear_and_Nonlinear_Optimization_of CubeSat_Constellation_Lifetime_Using_Differential_Drag_Control.pdf).

The MATLAB simulation code for this project can be found [here](https://github.com/jdwapman/SmallSatSeparation).

