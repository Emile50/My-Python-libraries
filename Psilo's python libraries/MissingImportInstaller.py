import importlib
import subprocess
import sys

def import_or_install(package, specific_function = None):
    """Attempt to import the module (or a specific function of it). download it if missing
        Example usage:
        from package import specific_function1 as SomeName1, SomeName2
        Becomes:
        someName1, someName2 = import_or_install(math, specific_function1)
        
        CANNOT HANDLE MUTIPLE SPECIFIC FUNCTIONS YES
"""
    try:
        # Try to import the package
        mod = importlib.import_module(package)
        
        if function:
            # If a specific function is specified, get it from the module
            return getattr(mod, function)
        
        return mod  # Return the module itself if no function is specified
    except ImportError as e:
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


def install_packages(packages):
    """Meant to be used like so:
    try:
        import x
        from import y import a,b,c as f, g, h
        import z
    except importError:
        install_packages("x", "y", "x")

    ***Allows complex subimports with names unlike import_or_install***
"""
    for package in packages:
        try:
            # Install the missing package using pip
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"{package} installed successfully.")
            
            # Reattempt the import after installation
            importlib.import_module(package)
            print(f"{package} imported successfully after installation.")
        except subprocess.CalledProcessError as install_error:
            print(f"Failed to install {package}. Error: {install_error}")

"""#Example usage
package_name = "requests"  # Replace with the package you want to use
#you need to create a variable to use the module, one isnt created by default with importlib.import_module
requests = import_or_install(package_name) 

"""
