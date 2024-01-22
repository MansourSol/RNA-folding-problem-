from train_script import train_objective_function
from plot_script import plot_scoring_profiles

if __name__ == "__main__":
    print("Executing Part 1: Training script...")
    train_objective_function()
    print("Part 1 completed.\n")

    print("Executing Part 2: Plot training script...")
    plot_scoring_profiles()
    print("Part 2 completed.")

