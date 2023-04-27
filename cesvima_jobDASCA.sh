#!/bin/bash
##----------------------- Start job description -----------------------
#SBATCH --ntasks=1
#SBATCH --partition=standard-gpu
#SBATCH --gres=gpu:a100#
#SBATCH --job-name=t5_test
#SBATCH --mem-per-cpu=120G
#SBATCH --time=100:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=a.vogel@alumnos.upm.es
#SBATCH --output=out-%j.log
##------------------------ End job description ------------------------

module load GLib && module load CUDA


source /home/s730/s730251/projects/t5env/bin/activate
 
srun python3 /home/s730/s730251/projects/t5-spanish-news-summarization/train_t5base_NASES.py 

deactivate
