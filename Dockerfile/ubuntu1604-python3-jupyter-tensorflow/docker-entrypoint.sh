#!/bin/sh
# ============================================================
#  Description: Run the jupyter service.
#
#   --ip 0.0.0.0: Allow all IP access.
#   --no-browser: Don't open browser from command line.
# =========================================================== 

jupyter-notebook --ip 0.0.0.0 --no-browser --allow-root --notebook-dir=/home