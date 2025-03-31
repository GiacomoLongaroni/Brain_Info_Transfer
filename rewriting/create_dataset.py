import numpy as np 

def createDataset(n_simulations, n_of_Trials):

    # Simulation parameters
    n_weights = 10
    w_sig = np.linspace(0,1, num=n_weights)
    w_noise = np.linspace(0, 1, num=n_weights)

    std_X_noise = 2
    std_X_ratio = 0.4
    std_X_signal = std_X_ratio*std_X_noise
    eps = 1e-52          

    # Time parameters 
    simLen = 50                                 # simulation length in units of 10 ms
    stimWindow = [20, 25]                       # time window of the stimulus
    delays = [4,5,6]                            # time delay for Y

    # Binning parameters
    S_values = [1,2,3,4]
    X_bins = 3
    Y_bins = 3

    # dataset initialization
    dataset = np.zeros((n_simulations, n_weights, n_weights, n_of_Trials, 1))


    S = np.random.choice(n_simulations*n_weights*n_weights*n_of_Trials)
    w_sig = np.repeat(w_sig, n_simulations*n_of_Trials ) 
    w_noise = np.repeat(w_sig, n_simulations*n_of_Trials )
    X_noise = npr.normal(0, std_X_noise, size=(n_simulations, n_))









    return S, X_binned, Y_binned, Y_binned_past 




