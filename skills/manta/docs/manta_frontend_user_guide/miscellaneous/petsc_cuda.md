<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/miscellaneous/petsc_cuda.html -->

# Running a simulation using PETSc CUDA capabilities

In order to use the CUDA capabilities of the PETSc library, you need to have compiled MANTA with
CUDA support enabled for PETSc. See the [Installation guide](../../get_started/installation_guide.md#installation-guide) section for details about this.

Once this is done, you may run a simulation using CUDA enabled preconditionners or solvers by setting the appropriate
options directly in your `petscrc` file.

Here is an example to run on a single MPI rank (and also single GPU) :

> ```
> # [ General options ]
> -vec_type cuda
> -mat_seqaij_type seqaijcusparse  # Only use when pure sequential run (=1 MPI rank)
> #-mat_type aijcusparse
> -use_gpu_aware_mpi 0
> -blocksize 3       # To be set when solving vectioral equation
>
> # [ Logging / Help ]
> #-help
> #-log_view
> #-fieldsplit_u_ksp_monitor
> #-fieldsplit_u_ksp_monitor_true_residual
>
> # [ Solver ]
> -fieldsplit_u_ksp_type cg
> -fieldsplit_u_ksp_rtol 1.e-3
>
> ##
> ## Several preconditionners are available.
> ## On GPU, Hypre BoomerAMG is the efficient one.
> ##
>
> # [ Precond BlockJacobi ]
> # -fieldsplit_u_pc_type bjacobi
> # -fieldsplit_u_pc_bjacobi_local_blocks 3
>
> # [ Precond ILU ]
> #-fieldsplit_u_pc_type ilu
>
> # [ Precond Hypre ]
> -fieldsplit_u_pc_type hypre
> -fieldsplit_u_pc_hypre_boomeramg_strong_threshold 0.85    # THIS IS THE KEY PARAMETER!!
> ```

and now a more involved example to run on multiple MPI ranks and multiple GPUs (example taken from a Topaze A100 run):

> ```
> # [ General options ]
> -vec_type cuda
> -mat_type aijcusparse
> -mat_seqaij_type seqaijcusparse
> -use_gpu_aware_mpi 0
> -blocksize 3
>
> # [ Logging / Help ]
> #-help
> #-log_view
> #-fieldsplit_u_ksp_monitor
> #-fieldsplit_u_ksp_monitor_true_residual
>
> # [ Solver ]
> -fieldsplit_u_ksp_type cg
> -fieldsplit_u_ksp_rtol 1.e-8
> -fieldsplit_u_ksp_atol 1.e-12
>
> # [ Precond Hypre ]
> -fieldsplit_u_pc_type hypre
> -fieldsplit_u_pc_hypre_boomeramg_strong_threshold 0.9    # THIS IS THE KEY PARAMETER!!
> -fieldsplit_u_pc_hypre_boomeramg_coarsen_type PMIS
> -fieldsplit_u_pc_hypre_boomeramg_interp_type ad-wts
> -fieldsplit_u_pc_hypre_boomeramg_relax_type_all l1scaled-Jacobi
> ```
