from all_functions import *
import os

def train_objective_function():
    read_file = 0
    files = []

    directory = str(input('Input directory path with pdb files: '))

    if os.path.isdir(directory):
        for path in os.listdir(directory):
            full_path = os.path.join(directory, path)

            if full_path.endswith(".pdb"):
                files.append(path)
            else:
                read_file += 1

        if read_file == 0:
            name_directory = str(input('Output directory path: '))
            nom_folder = str(input('Folder name : '))
            print("done")

            score = compute_RNA_pseudo_energy(directory)[0]
            save(nom_folder, name_directory, score)

        else:
            print('Error')

if __name__ == "__main__":
    train_objective_function()
