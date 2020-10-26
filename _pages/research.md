---
permalink: /research/
title: "Research"
author_profile: true
---

My research focuses on accelerating graph algorithms and sparse linear algebra kernels using the Graphics Processing Unit's (GPU) parallel architecture.

## Software-Define Hardware (DARPA)

My current project is a collaboration between UC Davis, NVIDIA, and several other universities as part of DARPA's Software-Defined Hardware (SDH) program within the Electonics Resurgence Initiative (ERI). In short, the ERI seeks to continue advances in computer technology in the post-Moore's-Law era. Within the ERI, the SDH program's goal is to explore reconfigurable computer architectures and programming models optimized for big-data fields such as graph analytics, machine learning, and linear algebra.  

More details about this project coming soon...

[DARPA Press Release](https://www.darpa.mil/news-events/2018-07-24a)  
[Nvidia Press Release](https://blogs.nvidia.com/blog/2018/07/24/darpa-research-post-moores-law/)  

## Gunrock

[Gunrock](https://github.com/gunrock/gunrock/tree/master/) is a GPU-accelerated [graph algorithm](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/) library developed by Dr. Owens's research group.

I implemented the [Hyperlink-Induced Topic Search](https://en.wikipedia.org/wiki/HITS_algorithm) (HITS) web page ranking algorithm. The goal of the HITS algorithm is to assign websites with a hub score and an authority score. Websites with high hub scores are sites that are useful as search engines (example: Google), while sites with high authority scores are websites that contain authoritative information (example: Wikipedia). My Gunrock implementation of HITS is used in NVIDIA's [RAPIDS cuGraph](https://github.com/rapidsai/cugraph) open-source data analytics library.

![HITS Algorithm](/files/owensgroup/hits.png)  
[Source](http://pi.math.cornell.edu/~mec/Winter2009/RalucaRemus/Lecture4/lecture4.html)

More specifically, sites that point to other websites with high authority scores have a high hub score, and websites pointed to by other sites with high hub scores in turn have a high authority score. [(Code)](https://github.com/gunrock/gunrock/tree/master/gunrock/app/hits)

I presented a [Poster](/files/owensgroup/ia2019.pdf) on Gunrock at the UC Davis 2018 Industrial Affiliates Conference.

Other contributions include general Gunrock documentation, bug fixes, and tests.

## Past Projects

Past research projects include:
* Design and characterization of a planar air-bearing platform used for CubeSat guidance & control tests at NASA JPL [(Link)](/portfolio/01-JPL)
* Simulation of distributed detection algorithms applied to chemical plume emissions using autonomous robotic swarms at the Lawrence Livermore National Laboratory [(Link)](/portfolio/02-llnl_swarm)
* Design of a low-cost data capture system for fluorescence lifetime spectroscopy with [Professor Diego Yankelevich](https://faculty.engineering.ucdavis.edu/yankelevich/) and [Professor Laura Marcu](https://marculab.bme.ucdavis.edu/) at UC Davis [(Link)](/portfolio/05-yankelevich)