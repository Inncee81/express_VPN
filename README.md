# express VPN
Python script for express VPN on windows. It cycles between the three locations on the VPN dashboard until a connection is established. 

## Path
The script requires express VPN to be added as windows path environment variable.

## Python version
The python script makes use of pywinauto which currently only runs in python version 3.3-3.7.6. Pywinauto must run in the same bits as the automised .exe. As there is is only a 32-bit express VPN app you are required to use 32-bit python. For conda users:

``set CONDA_FORCE_32BIT=1``

``conda create --name venv python=3.x``



