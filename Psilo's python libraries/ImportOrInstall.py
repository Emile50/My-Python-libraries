import importlib
import subprocess
import sys

def import_or_install(package):
    try:
        # Try to import the package
        return importlib.import_module(package)
    except ImportError:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"{package} installed successfully.")
        except subprocess.CalledProcessError:
            print(f"Failed to install {package}. Install it manually.")
            print("---Error details---")
            print(f"Error message: {e}")  # Print the error message
            print(f"Return code: {e.returncode}")  # Print the error return code
            print(f"Command: {e.cmd}")  # Print the command that was attempted
        return importlib.import_module(package)

"""#Example usage
package_name = "requests"  # Replace with the package you want to use
#you need to create a variable to use the module, one isnt created by default with importlib.import_module
requests = import_or_install(package_name) 

"""
