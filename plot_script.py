from all_functions import *
import os
import sys

def plot_scoring_profiles():
    read_file = 0
    directory = str(input('Input directory path with pdb files: '))
    if os.path.isdir(directory):
        if read_file == 0:
            score = compute_RNA_pseudo_energy(directory)[0]
            plot_folder = str(input('Output directory path plot: '))
            print("done")
                
            if os.path.exists(plot_folder):
                plot(score, plot_folder)
            else:
                print('Error ')
        else:
            print('Error')

if __name__ == "__main__":
    plot_scoring_profiles()
