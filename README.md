# ComputerNetworksPythonPractical
This repository includes all of my practicals of computer networks implimented in python and ns2 implementations.

You can install numpy, matplotlib, etc. for each python3 file using:
sudo pip3 install libraryfilename             (also see pypi.org)

For using the python3 files use:
python3 filename.py

For using the tcl files for network simulation you need to install Network Simulator ns2. Use it using:
ns filename.tcl
nam yournamfile.nam

To plot xgraph or use the awk files:
awk -f filename.awk tracefile.tr
awk -f filename.awk tracefile.tr > filename.txt|xrg (chose any one of the two formats)
xgraph filename.txt|xgr
