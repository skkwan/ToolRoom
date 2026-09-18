# Helpful Condor commands

* Increase the memory of currently held jobs to 10000 MB
    ```bash
    condor_qedit -constraint "JobStatus == 5" RequestMemory 10000
    ```