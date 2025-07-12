# LWB-benchmark-generator
Reimplementation of the scripts in "A benchmark method for the propositional modal logics K, KT, S4" by Heuerding et al. 

## Usage
Make sure python3 is installed. 

First, run ```python3 test.py``` to make sure the generated benchmarks are not different to the originals. 

Then, run ```./gen_files.sh``` to generate all the benchmarks (K, KT, and S4).
If you only want to generate a subset (as they take up alot of space) find the required commands in gen_files.sh and run those. 

``./gen_files_kn.sh`` and ``.\gen_files_global.sh`` works similarly for multimodal benchmarks and global benchmarks.
