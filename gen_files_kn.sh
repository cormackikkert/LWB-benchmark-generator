# Generates K(n) benchmarks
# For UNSAT categories it use the following classes as a base:
#   - k_branch_p
#   - k_path_p
#   - k_ph_p
#   - k_poly_p
#   - k_t4p_p
# For SAT categories it uses the following classes as a base:
#   - k_poly_n
#   - s4_md_n
#   - s4_ph_n
#   - s4_path_n
#   - s4_s5_n
# Each class has 20 instances, each getting progressively more difficult
################################################################################

    python3 generate.py k_branch_p 5 100 5 KnUnsat &
    python3 generate.py k_path_p 85 1700 85 KnUnsat &
    python3 generate.py k_ph_p 1 20 1 KnUnsat &
    python3 generate.py k_poly_p 47 940 47 KnUnsat & 
    python3 generate.py k_t4p_p 190 3800 190 KnUnsat &

  # ---------------------------------

    python3 generate.py k_poly_n 47 940 47 KnSat &
    python3 generate.py s4_md_n 4 80 4 KnSat &
    python3 generate.py s4_ph_n 1 20 1 KnSat &
    python3 generate.py s4_path_n 85 1700 85 KnSat &
    python3 generate.py s4_s5_n 65 1300 65 KnSat

  # ---------------------------------

################################################################################
