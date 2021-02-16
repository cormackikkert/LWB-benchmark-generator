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

BENCHMARKS_K = [k_branch_n, k_branch_p, k_d4_n, k_d4_p, k_dum_n, k_dum_p, k_grz_n, k_grz_p, k_lin_n, k_lin_p, k_path_n, k_path_p, k_ph_n, k_ph_p, k_poly_n, k_poly_p, k_t4p_n, k_t4p_p]
BENCHMARKS_KT = [kt_45_n, kt_45_p, kt_branch_n, kt_branch_p, kt_dum_n, kt_dum_p, kt_grz_n, kt_grz_p, kt_md_n, kt_md_p, kt_path_n, kt_path_p, kt_ph_n, kt_ph_p, kt_poly_n, kt_poly_p, kt_t4p_n, kt_t4p_p]
BENCHMARKS_S4 = [s4_45_n, s4_45_p, s4_branch_n, s4_branch_p, s4_grz_n, s4_grz_p, s4_ipc_n, s4_ipc_p, s4_md_n, s4_md_p, s4_path_n, s4_path_p, s4_ph_n, s4_ph_p, s4_s5_n, s4_s5_p, s4_t4p_n, s4_t4p_p]
for (btype, bdir) in [(BENCHMARKS_K, "fmls_k"), (BENCHMARKS_KT, "fmls_kt"), (BENCHMARKS_S4, "fmls_s4")]:
    for item in btype:
        name = item.__name__
        txt = ""
        txt += f"benchmark formulas {name}.txt\n"
        txt += f"begin\n"
        for i in range(1, 22):
            txt += f"{i}: {item(i)}\n"
        txt += f"end\n"

        assert txt == open(f"{bdir}/{name}.txt").read(), f"{name} is different"
        print(f"{name} OK")
    print(f"-> {bdir} OK")
    
