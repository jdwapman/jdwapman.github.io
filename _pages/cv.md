---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

PDF available [here](http://jdwapman.github.io/jdwapman/assets/resume.pdf)

# Education
---
## University of California, Davis
* M.S. Electical Engineering
  * September 2018 - Present
  * Advisor: [Dr. John Owens](https://www.ece.ucdavis.edu/~jowens/research.html)
  * Focus: Load-Balancing for GPU-Accelerated Graph Algorithms
  * GPA: 4.00/4.00
* B.S. Electrical Engineering
  * September 2014 - March 2018
  * GPA: 3.96/4.00

# Experience
---

## Owens Research Group
Graduate Student Researcher  
January 2019 - Present  
* Currently researching methods to map GPU graph algorithms and load-balancing methods to a dataflow programming model in collaboration with Nvidia as part of DARPA’s Software-Defined Hardware program.
* Implemented the HITS graph ranking algorithm in the Gunrock open-source parallel graph analytics library.  
[(Link)](https://github.com/gunrock/gunrock/tree/master/gunrock/app/hits)

## NASA Jet Propulsion Laboratory
Guidance & Control Intern  
June 2018 - September 2018
* Developed control algorithms and software drivers to enable automated position and attitude control of a planar air-bearing platform using used for CubeSat formation flying, pointing, and rendezvous experiments.
* Planned and executed a series of laboratory tests to fully characterize the planar platform’s physical properties, software performance, and position-control capabilities. Extensive data analysis performed using MATLAB.


## Lawrence Livermore National Laboratory
Computational Engineering Intern  
March 2018 - June 2018
* Modeled and simulated decentralized multi-agent robotic swarm algorithms for signal detection, information
exchange, and motion planning applied to chemical plume identification and localization.  

Engineering Intern  
June 2017 - September 2017  
* Created a sensor and LabView virtual instrument used to measure and track the capacitance of over 4000 high energy-density capacitors for preventative maintenance. Achieved  accuracy within 3% and repeatability within 1%.


## Yankelevich & Marcu Laboratory
Undergraduate Research Assistant
January 2017 - March 2018
* Implemented low-cost, automated hardware and software systems to capture, analyze, and visualize fluorescence lifetime imaging data for guided surgery applications using C++ and Python on a Raspberry Pi computer.

## Silva Laboratory
Undergraduate Research Assistant  
September 2016 - June 2017  
* Designed circuitry and programmed an Arduino for a digitally-controlled syringe with a team of three students. Used as a low-cost alternative for microfluidic educational and research projects.
* Achieved performance comparable to a \$2000 industrial digitally-controlled syringe for less than \$150.


## Varian Medical Systems
Engineering Intern  
June 2016 - September 2016
* Designed PCBs and software used to validate Multi-Leaved Collimator motors for radiation therapy machines.
* Programmed a GUI-based application to allow engineers to interface with MLC motor test equipment. Features include telemetry data visualizations, command sequence entry, and debugging tools.


## UC Davis C-STEM Center
Research Assistant  
January 2016 - June 2016
* Developed code examples for Arduino robotic platforms such as line-following and maze-solving procedures.
* Created teaching materials for middle-school students to learn basic coding and robotics concepts.


## White Laboratory
Undergraduate Research Assistant  
December 2016  
* Created scale models of LA buildings using foam blocks for use in wind tunnel simulations.



# Conferences
---
* "Gunrock GPU Graph Analytics", UC Davis Indistrial Affiliates Conference, May 2019.  
[poster](http://jdwapman.github.io/jdwapman/assets/posters/ia2019.pdf)
* "UC Undergraduate Research Ambassador Showcase", February 2018.
* “Chemical Plume Detection with Collaborative, Autonomous Sensor Networks,” in 2018 Signal and Image Sciences Workshop, 2018.  
[poster](http://jdwapman.github.io/jdwapman/assets/posters/casis2018.pdf)
* Presentation “Multichannel solid state photodetection system for low-cost fluorescence lifetime spectroscopy (Conference Presentation),” in Advanced Biomedical and Clinical Diagnostic and Surgical Guidance Systems XVI, 2018. (contributed slides)
* "Rocket Imaging Payload: Identification of Ground-Based Targets using Contour Detection and Neural Networks with Bluetooth-Enabled Inertial Measurement Unit", UC Davis Industrial Affiliates Conference, May 2018.  
[poster](http://jdwapman.github.io/jdwapman/assets/posters/ia2018.pdf)


# Skills
---
## Software
* Languages
  * Bash
  * C
  * C++
  * CUDA
  * MATLAB
  * Python
  * Verilog
* Frameworks
  * OpenCV
  * NumPy
  * SciPy
  * Gunrock
* Tools
  * Git
  * Jekyll
  * Linux
  * Mac OS
  * Windows



Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
