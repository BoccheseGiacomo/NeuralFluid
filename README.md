# NeuralFluid
Emergent behaviour driven Learning

try the app here: https://neuralfluid.streamlit.app/

## 1. Introduction
This is a simulation that uses Reaction-Diffusion to study emergent properties of 2d space + time dynamical systems.

Our aim is to build an emergent system that is able to learn given a reward, inputs and outputs, without an external algorithm that acts as a supervisor or an optimizer. (only needed a meta-optimizer in order to make it "learn how to learn", driven by genetic algorithm or similar methods, once it has converged, we can remove the meta-optimizer).

For making it learn, we think to follow the way of Cortical Labs but in a simulated environment (we set some points as "feedback cells" in these cells we send random, uncoordinated impulses when the reward is negative, this stimulates the system to unlearn, and coordinated, toghether firing cells for giving positive reward to the system, this also allows a kind of meta learning since there can emerge a system where the model self stimulates with coordinated behaviour when thinks it has done right (even without reward), and can fire in a disordered way implementing a kind of pseudo-random algorithm to self-unlearn).

## Other information
The simulation is still in development phase. Nothing has being proved yet.
Try the app here: https://neuralfluid.streamlit.app/

## Authors
- [Giacomo Bocchese] (Deep Learning Engineer, Independent Researcher)
- [You] (If you enjoy the project and want to contribute)
