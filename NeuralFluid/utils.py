import streamlit as st
import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

class NeuralFluid:
    def __init__(self, state, e, noise=1e-2, dt=0.01, alpha=0.04):
        self.state = state
        self.e = e
        self.noise = noise
        self.dt = dt
        self.alpha = alpha
        self.delta = np.zeros(self.state.shape)
        self.delta_e = np.zeros(self.e.shape)
    
    def step(self,exp1,exp2):
        #apply the diffusion equation via convolution (convolve2d)
        self.delta=self.alpha*convolve2d(self.state,[[0,1,0],[1,-4,1],[0,1,0]],mode='same',boundary='symm') + self.noise*np.random.randn(*self.state.shape)

        ds,de=dsde(self.state,self.e,exp1,exp2)
        self.delta+=ds
        self.delta_e=de

        self.state+=self.delta*self.dt
        self.e+=self.delta_e*self.dt

        #smoothly clip the values
        state_clipped=np.clip(self.state,0,1)
        e_clipped=np.clip(self.e,0,1)
        self.state=state_clipped*0.2+self.state*0.8
        self.e=e_clipped*0.2+self.e*0.8

    def stepn(self,n,exp1,exp2):
        for i in range(n):
            self.step(exp1,exp2)

    def init_plot(self):
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(15, 7))
        self.im1 = self.ax1.imshow(self.state, cmap='jet', vmin=0, vmax=1, animated=True)
        self.im2 = self.ax2.imshow(self.e, cmap='jet', vmin=-1, vmax=1, animated=True)
        plt.colorbar(self.im1, ax=self.ax1, shrink=0.6)
        plt.colorbar(self.im2, ax=self.ax2, shrink=0.6)
        self.ax1.set_xticks([])
        self.ax1.set_yticks([])
        self.ax2.set_xticks([])
        self.ax2.set_yticks([])
        #set titles for the plots
        self.ax1.set_title('State')
        self.ax2.set_title('Energy')

    def update_plot(self):
        self.im1.set_data(self.state)
        self.im2.set_data(self.e)

def dsde(s,e,exp1,exp2):
    ds=eval(exp1)
    de=eval(exp2)
    return ds,de

def generate_video(states, energies):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))
    ax1.set_title('State')
    ax2.set_title('Energy')
    im1 = ax1.imshow(states[0], cmap='jet', vmin=0, vmax=1, animated=True)
    im2 = ax2.imshow(energies[0], cmap='jet', vmin=-1, vmax=1, animated=True)
    plt.colorbar(im1, ax=ax1, shrink=0.6)
    plt.colorbar(im2, ax=ax2, shrink=0.6)
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax2.set_xticks([])
    ax2.set_yticks([])

    def update(num, states, energies, im1, im2):
        im1.set_array(states[num])
        im2.set_array(energies[num])
        return im1, im2,

    ani = animation.FuncAnimation(fig, update, len(states), fargs=[states, energies, im1, im2],
                                  interval=50, blit=True)
    

    # Save the video
    temp_filename = "temp_output_video.mp4"
    ani.save(temp_filename)

    return temp_filename