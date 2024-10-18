import os
import subprocess

# Create a Conda environment from environments.yml
def create_conda_env():
    if os.path.isfile("environments.yml"):
        print("Creating Conda environment from environments.yml...")
        subprocess.run(["conda", "env", "create", "-f", "environments.yml"], check=True)
    else:
        print("environments.yml not found. Please ensure the file exists in the project directory.")

# Initialize a Git repository
def initialize_git():
    print("Initializing Git repository...")
    subprocess.run(["git", "init"], check=True)
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)

# Main script where user decides whether to create a Conda environment or not
def main():
    print("Do you want to create a Conda environment using environments.yml? (y/n)")
    choice = input("Enter y or n: ").strip().lower()

    if choice == "y":
        create_conda_env()
    elif choice == "n":
        print("Skipping environment setup.")
    else:
        print("Invalid choice, please run the script again and choose y or n.")

    # Initialize Git after the decision
    initialize_git()

if __name__ == "__main__":
    main()
