# Debugging tips 

## Launching gdb

1. `export LD_LIBRARY_PATH=/nfs/data41/software/Xilinx/Vitis_HLS/2022.2/tps/lnx64/gcc-8.3.0/lib64/`
    - We got this path from `find $XILINX_HLS -regex ".*libstdc\+\+.so.*"`
2. `gdb csim.exe`
3. In gdb prompt: `run t` (the `t` is the command-line argument)
