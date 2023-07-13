powershell -ExecutionPolicy ByPass -NoExit -Command "& '~\anaconda3\shell\condabin\conda-hook.ps1' ; conda activate '~\anaconda3' "

conda update -n base -c defaults conda 