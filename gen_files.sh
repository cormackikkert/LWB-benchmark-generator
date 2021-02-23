# The following script has been modified to use the python3 lwb-generator
# instead of the lwb executable. Changes were also made so that each class
# has 56 problems (previously some classes had more).
# Everything else is unchanged - Cormac 

################################################################################
#
# Script to generate the LWB-benchmarks
# for modal logics K, KT and S4.
#
#   - Modal Logic S4 : ~13GB | 1008 benchmarks | 504 SAT | 504 UNSAT | 9 cat.
#   - Modal Logic KT : ~18GB | 1008 benchmarks | 504 SAT | 504 UNSAT | 9 cat.
#   - Modal Logic K  : ~14GB | 1008 benchmarks | 504 SAT | 504 UNSAT | 9 cat.
#
# It was performed by Ullrich Hustadt and Valentin Montmirail
# Apache License 2017
#
################################################################################

# S4 : {s4_45, branch, grz, ipc, md, path, ph, s5, t4p}
# This script will generate 1008 benchmarks for the modal logic S4.
# There will be 504 benchmarks   satisfiable in S4;
# There will be 504 benchmarks unsatisfiable in S4.

  # ---------------------------------

    python3 generate.py s4_45_n 2 18 2
    python3 generate.py s4_45_n 20 940 20
    python3 generate.py s4_45_p 2 18 2
    python3 generate.py s4_45_p 20 940 20

  # ---------------------------------

    python3 generate.py s4_branch_n 1 30 1
    python3 generate.py s4_branch_n 32 78 2
    python3 generate.py s4_branch_n 80 88 8
    python3 generate.py s4_branch_p 1 30 1
    python3 generate.py s4_branch_p 32 78 2
    python3 generate.py s4_branch_p 80 88 8

  # ---------------------------------

    python3 generate.py s4_grz_n 10 90 10
    python3 generate.py s4_grz_n 100 4000 100
    python3 generate.py s4_grz_n 4500 7500 500
    python3 generate.py s4_grz_p 10 90 10
    python3 generate.py s4_grz_p 100 4000 100
    python3 generate.py s4_grz_p 4500 7500 500

  # ---------------------------------

    python3 generate.py s4_ipc_n 1 56 1
    python3 generate.py s4_ipc_p 1 56 1

  # ---------------------------------

    python3 generate.py s4_md_n 1 56 1
    python3 generate.py s4_md_p 1 56 1

  # ---------------------------------

    python3 generate.py s4_path_n 2 18 2
    python3 generate.py s4_path_n 20 390 10
    python3 generate.py s4_path_n 400 1200 100
    python3 generate.py s4_path_p 2 18 2
    python3 generate.py s4_path_p 20 390 10
    python3 generate.py s4_path_p 400 1200 100

  # ---------------------------------

    python3 generate.py s4_ph_n 1 56 1
    python3 generate.py s4_ph_p 1 56 1

  # ---------------------------------

    python3 generate.py s4_s5_n 1 56 1
    python3 generate.py s4_s5_p 1 56 1

  # ---------------------------------

    python3 generate.py s4_t4p_n 10 90 10
    python3 generate.py s4_t4p_n 100 2900 100
    python3 generate.py s4_t4p_n 3000 7500 500
    python3 generate.py s4_t4p_n 8000 15000 1000
    python3 generate.py s4_t4p_p 10 90 10
    python3 generate.py s4_t4p_p 100 2900 100
    python3 generate.py s4_t4p_p 3000 7500 500
    python3 generate.py s4_t4p_p 8000 15000 1000

  # ---------------------------------

################################################################################

# KT : {kt_45, branch, dum, md, grz, path, ph, poly, t4p}
# This script will generate 1008 benchmarks for the modal logic KT.
# There will be 504 benchmarks   satisfiable in KT;
# There will be 504 benchmarks unsatisfiable in KT.

  # ---------------------------------

    python3 generate.py kt_45_n 2 18 2
    python3 generate.py kt_45_n 20 940 20
    python3 generate.py kt_45_p 2 18 2
    python3 generate.py kt_45_p 20 940 20

  # ---------------------------------

    python3 generate.py kt_branch_n 1 30 1
    python3 generate.py kt_branch_n 32 78 2
    python3 generate.py kt_branch_n 80 88 8
    python3 generate.py kt_branch_p 1 30 1
    python3 generate.py kt_branch_p 32 78 2
    python3 generate.py kt_branch_p 80 88 8

  # ---------------------------------

    python3 generate.py kt_dum_n 8 40 8
    python3 generate.py kt_dum_n 80 400 40
    python3 generate.py kt_dum_n 480 3760 80
    python3 generate.py kt_dum_p 8 40 8
    python3 generate.py kt_dum_p 80 400 40
    python3 generate.py kt_dum_p 480 3760 80

  # ---------------------------------

    python3 generate.py kt_md_n 1 56 1
    python3 generate.py kt_md_p 1 56 1

  # ---------------------------------

    python3 generate.py kt_grz_n 10 90 10
    python3 generate.py kt_grz_n 100 4000 100
    python3 generate.py kt_grz_n 4500 7500 500
    python3 generate.py kt_grz_p 10 90 10
    python3 generate.py kt_grz_p 100 4000 100
    python3 generate.py kt_grz_p 4500 7500 500

  # ---------------------------------

    python3 generate.py kt_path_n 2 18 2
    python3 generate.py kt_path_n 20 390 10
    python3 generate.py kt_path_n 400 1200 100
    python3 generate.py kt_path_p 2 18 2
    python3 generate.py kt_path_p 20 390 10
    python3 generate.py kt_path_p 400 1200 100

  # ---------------------------------

    python3 generate.py kt_ph_n 1 56 1
    python3 generate.py kt_ph_p 1 56 1

  # ---------------------------------

    python3 generate.py kt_poly_n 2 18 2
    python3 generate.py kt_poly_n 20 940 20
    python3 generate.py kt_poly_p 2 18 2
    python3 generate.py kt_poly_p 20 940 20

  # ---------------------------------

    python3 generate.py kt_t4p_n 10 90 10
    python3 generate.py kt_t4p_n 100 2900 100
    python3 generate.py kt_t4p_n 3000 7500 500
    python3 generate.py kt_t4p_n 8000 15000 1000
    python3 generate.py kt_t4p_p 10 90 10
    python3 generate.py kt_t4p_p 100 2900 100
    python3 generate.py kt_t4p_p 3000 7500 500
    python3 generate.py kt_t4p_p 8000 15000 1000

  # ---------------------------------

################################################################################

# K : {branch, d4, dum, grz, lin, path, ph, poly, t4p}
# This script will generate 1008 benchmarks for the modal logic K.
# There will be 504 benchmarks   satisfiable in K;
# There will be 504 benchmarks unsatisfiable in K.

  # ---------------------------------

    python3 generate.py k_branch_n 1 30 1
    python3 generate.py k_branch_n 32 78 2
    python3 generate.py k_branch_n 80 88 8
    python3 generate.py k_branch_p 1 30 1
    python3 generate.py k_branch_p 32 78 2
    python3 generate.py k_branch_p 80 88 8

  # ---------------------------------

    python3 generate.py k_d4_n 4 16 4
    python3 generate.py k_d4_n 20 200 20
    python3 generate.py k_d4_n 240 1880 40
    python3 generate.py k_d4_p 4 16 4
    python3 generate.py k_d4_p 20 200 20
    python3 generate.py k_d4_p 240 1880 40

  # ---------------------------------

    python3 generate.py k_dum_n 8 40 8
    python3 generate.py k_dum_n 80 400 40
    python3 generate.py k_dum_n 480 3760 80
    python3 generate.py k_dum_p 8 40 8
    python3 generate.py k_dum_p 80 400 40
    python3 generate.py k_dum_p 480 3760 80

  # ---------------------------------

    python3 generate.py k_grz_n 10 90 10
    python3 generate.py k_grz_n 100 4000 100
    python3 generate.py k_grz_n 4500 7500 500
    python3 generate.py k_grz_p 10 90 10
    python3 generate.py k_grz_p 100 4000 100
    python3 generate.py k_grz_p 4500 7500 500

  # ---------------------------------

    python3 generate.py k_lin_n 10 90 10
    python3 generate.py k_lin_n 100 3300 100
    python3 generate.py k_lin_n 3400 6000 200
    python3 generate.py k_lin_p 10 90 10
    python3 generate.py k_lin_p 100 900 100
    python3 generate.py k_lin_p 1000 9000 1000
    python3 generate.py k_lin_p 10000 200000 10000
    python3 generate.py k_lin_p 225000 375000 25000
    python3 generate.py k_lin_p 400000 500000 100000

  # ---------------------------------

    python3 generate.py k_path_n 2 18 2
    python3 generate.py k_path_n 20 390 10
    python3 generate.py k_path_n 400 1200 100
    python3 generate.py k_path_p 2 18 2
    python3 generate.py k_path_p 20 390 10
    python3 generate.py k_path_p 400 1200 100

  # ---------------------------------

    python3 generate.py k_ph_n 2 18 2
    python3 generate.py k_ph_n 20 250 5
    python3 generate.py k_ph_p 1 56 1

  # ---------------------------------

    python3 generate.py k_poly_n 2 18 2
    python3 generate.py k_poly_n 20 940 20
    python3 generate.py k_poly_p 2 18 2
    python3 generate.py k_poly_p 20 940 20

  # ---------------------------------

    python3 generate.py k_t4p_n 10 90 10
    python3 generate.py k_t4p_n 100 2900 100
    python3 generate.py k_t4p_n 3000 7500 500
    python3 generate.py k_t4p_n 8000 15000 1000
    python3 generate.py k_t4p_p 10 90 10
    python3 generate.py k_t4p_p 100 2900 100
    python3 generate.py k_t4p_p 3000 7500 500
    python3 generate.py k_t4p_p 8000 15000 1000

  # ---------------------------------

################################################################################
