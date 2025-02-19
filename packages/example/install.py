import os
import sys
import subprocess

def install_dependencies():
    """Install necessary dependencies."""
    dependencies = ["requests"]  # Example dependencies
    for dep in dependencies:
        subprocess.run([sys.executable, "-m", "pip", "install", dep])

def main():
    print("Installing Example Package...")
    install_dependencies()
    print("Installation complete!")

if __name__ == "__main__":
    main()
