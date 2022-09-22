from k_branch_n import k_branch_n
from k_branch_p import k_branch_p
from k_d4_n import k_d4_n
from k_d4_p import k_d4_p
from k_dum_n import k_dum_n
from k_dum_p import k_dum_p
from k_grz_n import k_grz_n
from k_grz_p import k_grz_p
from k_lin_n import k_lin_n
from k_lin_p import k_lin_p
from k_path_n import k_path_n
from k_path_p import k_path_p
from k_ph_n import k_ph_n
from k_ph_p import k_ph_p
from k_poly_n import k_poly_n
from k_poly_p import k_poly_p
from k_t4p_n import k_t4p_n
from k_t4p_p import k_t4p_p

from kt_45_n import kt_45_n, kt_45_n_f
from kt_45_p import kt_45_p, kt_45_p_f
from kt_branch_n import kt_branch_n, kt_branch_n_f
from kt_branch_p import kt_branch_p, kt_branch_p_f
from kt_dum_n import kt_dum_n, kt_dum_n_f
from kt_dum_p import kt_dum_p, kt_dum_p_f
from kt_grz_n import kt_grz_n, kt_grz_n_f
from kt_grz_p import kt_grz_p, kt_grz_p_f
from kt_md_n import kt_md_n, kt_md_n_f
from kt_md_p import kt_md_p, kt_md_p_f
from kt_path_n import kt_path_n, kt_path_n_f
from kt_path_p import kt_path_p, kt_path_p_f
from kt_ph_n import kt_ph_n, kt_ph_n_f
from kt_ph_p import kt_ph_p, kt_ph_p_f
from kt_poly_n import kt_poly_n, kt_poly_n_f
from kt_poly_p import kt_poly_p, kt_poly_p_f
from kt_t4p_n import kt_t4p_n, kt_t4p_n_f
from kt_t4p_p import kt_t4p_p, kt_t4p_p_f

from s4_45_n import s4_45_n, s4_45_n_f
from s4_45_p import s4_45_p, s4_45_p_f
from s4_branch_n import s4_branch_n, s4_branch_n_f
from s4_branch_p import s4_branch_p, s4_branch_p_f
from s4_grz_n import s4_grz_n, s4_grz_n_f
from s4_grz_p import s4_grz_p, s4_grz_p_f
from s4_ipc_n import s4_ipc_n, s4_ipc_n_f
from s4_ipc_p import s4_ipc_p, s4_ipc_p_f
from s4_md_n import s4_md_n, s4_md_n_f
from s4_md_p import s4_md_p, s4_md_p_f
from s4_path_n import s4_path_n, s4_path_n_f
from s4_path_p import s4_path_p, s4_path_p_f
from s4_ph_n import s4_ph_n, s4_ph_n_f
from s4_ph_p import s4_ph_p, s4_ph_p_f
from s4_s5_n import s4_s5_n, s4_s5_n_f
from s4_s5_p import s4_s5_p, s4_s5_p_f
from s4_t4p_n import s4_t4p_n, s4_t4p_n_f
from s4_t4p_p import s4_t4p_p, s4_t4p_p_f
target_dir = r"/home/users/u6427001/Provers/lwbS4"

import sys
if len(sys.argv[1:]) != 4:
    print("Usage  : python generate.py <benchmark_class> <start_index> <end_index> <step>")
    print("Example: python generate.py k_branch_p 30 88 2")
    exit()

base, *nums = sys.argv[1:]
start, end, step = map(int, nums)

import os
for i in range(start, end+1, step):
    if os.path.isfile(rf"{target_dir}/{base}.{str(i).rjust(4, '0')}.intohylo") and (len(open(rf"{target_dir}/{base}.{str(i).rjust(4, '0')}.intohylo").readlines()) == 3): continue
    print("DOING", rf"{target_dir}/{base}.{str(i).rjust(4, '0')}.intohylo")

    fileVar=  open(rf"{target_dir}/{base}.{str(i).rjust(4, '0')}.intohylo", "w")
    fileVar.write("begin\n~(")
    fileVar.write(str(eval(f"{base}({i})")))
    fileVar.write(")\nend\n")


