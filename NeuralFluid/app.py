from utils import *

def main():
    st.title('Neural Fluid Simulation')

    # Sidebar: Parameters Configuration
    st.sidebar.header('Parameters Configuration')

    init_state = st.sidebar.selectbox('Initial State for `s`', ['constant', 'random'])
    if init_state == 'constant':
        state_init_val = st.sidebar.slider('Initial constant value for `s`', 0.0, 1.0, 0.0)
        state = np.ones((50, 50)) * state_init_val
    else:
        state = np.random.uniform(0, 1, (50, 50))

    init_e = st.sidebar.selectbox('Initial State for `e`', ['constant', 'random'])
    if init_e == 'constant':
        e_init_val = st.sidebar.slider('Initial constant value for `e`', 0.0, 1.0, 0.3)
        e = np.ones((50, 50)) * e_init_val
    else:
        e = np.random.uniform(0, 1, (50, 50))
    
    noise = st.sidebar.slider('Noise Level', 1e-4, 0.1, 1e-2)
    dt = st.sidebar.slider('Time Step', 0.001, 0.3, 0.01)
    alpha = st.sidebar.slider('Diffusion Constant', 0.003, 0.2, 0.04)

    steps = st.sidebar.slider('Number of Steps', 0, 1000000, 20000)
    steps_per_frame = st.sidebar.slider('Number of steps per plotting frame', 5, 500, 20)

    # Allow users to input the reaction expressions
    state_reaction_expr = st.sidebar.text_input("Enter the equation expression for the state reaction:", value="0.7*(e-0.5)*s")
    energy_expr = st.sidebar.text_input("Enter the equation expression for the energy \"consumption\":", value="0.3*e*(1-e)- 0.2*s + 0.02")

    # Buttons
    start = st.sidebar.button("Start Simulation")
    stop = st.sidebar.button("Stop Simulation")

    states = []
    energies = []

    # When the "Start" button is pressed, run the simulation
    if start:
        nf = NeuralFluid(state=state, e=e, noise=noise, dt=dt, alpha=alpha)

        progress_bar = st.sidebar.progress(0)
        for t in range(0,steps, steps_per_frame):
            if stop:  # Stop the simulation
                break
            
            nf.stepn(steps_per_frame,state_reaction_expr, energy_expr)
            states.append(nf.state.copy())
            energies.append(nf.e.copy())

            progress_bar.progress((t+1) / steps)
        
        # Generate and save video

        video_file = generate_video(states, energies)
        time.sleep(2)
        st.video(video_file)


if __name__ == '__main__':
    main()