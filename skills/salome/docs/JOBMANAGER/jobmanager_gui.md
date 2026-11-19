<!-- source: https://docs.salome-platform.org/latest/gui/JOBMANAGER/jobmanager_gui.html -->

# Using the JOBMANAGER GUI

## Job management with the GUI

This section describes the parts 1 and 2 (described in the introduction section) of the JOBMANAGER GUI
dedicated to the management of jobs.

JOBMANAGER provides some buttons to manage the user job list (see figure [Main buttons for job management and job list](#figure-jobmanager-main-buttons)).

![figure](https://docs.salome-platform.org/latest/gui/JOBMANAGER/_images/jobmanager_main_buttons.png)

**Main buttons for job management and job list**

The description of each button (framed in blue in the figure) is given in the table below.

| **Button** | **Condition of activation** | **Description** | **Multi Selection** |
| --- | --- | --- | --- |
| **Create** | Always activated | Launch the job wizard to create a job. | Not matter |
| **Start** | Job selected and job state equals to *Created* | Start a job. | No |
| **Get Results** | Job selected and job state equals to *Finish* or *Failed* | Get job results in the result directory. | Yes |
| **Stop** | Job selected and job state equals to *Queued* or *Running* or *Paused* | Stop the job. If the job is registered into a remote batch manager, it is removed from it. | Yes |
| **Delete** | Job selected | Delete a job. If the job is registered into a remote batch manager, it is removed from it. | Yes |
| **Restart** | Job selected and job state equals to *Finish* or *Failed* | Restart a job. | No |
| **Edit/Clone** | Job selected | Edit a job in *created* or *Error* or *Failed* or *Not Created* state. Clone a job in other state. | No |
| **Refresh jobs** | Always activated | Update jobs states. | Not matter |

**Tip:** You could use the **Auto Refresh** button in GUI part 3 to enable an automatic refresh.

When a job is selected, the part 2 is filled with all the information that the JOBMANAGER has on the job. The figure
[Job widget information](#figure-jobmanager-job-focus) shows this part of the GUI. It contains two tabs. The first tab provides the main
information and the run information. The second tab shows the input and output file list of the job.

![figure](https://docs.salome-platform.org/latest/gui/JOBMANAGER/_images/jobmanager_job_focus.png)

**Job widget information**

## Job creation workflow

This section describes the workflow when a job is created. The jobmanager uses a wizard to create a job.

The first page (see [Create wizard page 1](#figure-jobmanager-job-workflow-1)) of the wizard permits to define the **job name**
and the **job type**. For each job type, the page provides an explanation of what job type refers.

![figure](https://docs.salome-platform.org/latest/gui/JOBMANAGER/_images/jobmanager_job_workflow_1.png)

**Create wizard page 1**

The second page (see [Create wizard page 2](#figure-jobmanager-job-workflow-2)) permits to add two files, the main job file
(in this example a command file). You could also add an environment file that is not mandatory.

![figure](https://docs.salome-platform.org/latest/gui/JOBMANAGER/_images/jobmanager_job_workflow_2.png)

**Create wizard page 2**

The third page (see [Create wizard page 3](#figure-jobmanager-job-workflow-5)) permits to choose the resource where the job
will be executed. You can also define the batch queue that you want to use.

![figure](https://docs.salome-platform.org/latest/gui/JOBMANAGER/_images/jobmanager_job_workflow_5.png)

**Create wizard page 3**

The fourth page (see [Create wizard page 4](#figure-jobmanager-job-workflow-3)) allows to define the resource requirements
and limits for the job. You can define the maximum duration,
the amount of memory needed (per node or per core if the batch manager supports it), the number of
processors/cores for the job, and whether it should use nodes exclusively (not sharing them with other
jobs). Time and memory requirements can be set to a “Default” value, which is the default for the
selected cluster and queue.

![figure](https://docs.salome-platform.org/latest/gui/JOBMANAGER/_images/jobmanager_job_workflow_3.png)

**Create wizard page 4**

The fifth page (see [Create wizard page 5](#figure-jobmanager-job-workflow-4)) permits to add the input and output files.
Input files are files located into the user
computer that have to be transferred into the execution resource. Output files will be copied to the user
computer at the end of the job.
It’s mandatory to define the *Remote working directory* that is the directory where the job will be executed.
Note that if a working directory is defined for the selected resource, the working directory for the job will be
created as a subdirectory of the resource working directory by default. The name of this subdirectory will
contain the current date and time. Of course, you can override this default value.
Input files will be copied in this working directory.
In this page, you can also define the result directory where the job’s results and logs will be copied.

![figure](https://docs.salome-platform.org/latest/gui/JOBMANAGER/_images/jobmanager_job_workflow_4.png)

**Create wizard page 5**

The sixth page (see [Create wizard page 6](#figure-jobmanager-job-workflow-advanced)) can be
used to define some advanced parameters, which are generally optional. The
field “Workload Characterization Key” is used on some clusters to associate
each job with a project for instance. The field “Extra parameters” can be used
to specify some other parameters or environment variables that are not
available through the JOBMANAGER interface. The content of this field is added
“as is” in the job submission file.

![figure](https://docs.salome-platform.org/latest/gui/JOBMANAGER/_images/jobmanager_job_workflow_advanced.png)

**Create wizard page 6**

The last page (see [Create wizard page 7](#figure-jobmanager-job-workflow-6)) finalizes the job creation. You could choose
if you want or not start the job at the end of the wizard.

![figure](https://docs.salome-platform.org/latest/gui/JOBMANAGER/_images/jobmanager_job_workflow_6.png)

**Create wizard page 7**

## Loading and saving job list

The JOBMANAGER permits to save and load the job list.
For some jobs, this feature permits to follow the execution of a job
into a different SALOME session by loading the list.

The figure [Location of load and save job list buttons](#figure-jobmanager-load-save-buttons) shows where are located
the load and save buttons in the JOBMANAGER GUI.

![figure](https://docs.salome-platform.org/latest/gui/JOBMANAGER/_images/jobmanager_load_save_buttons.png)

**Location of load and save job list buttons**

All jobs cannot be followed between two SALOME sessions. Indeed, It’s the *batch* type
of the resource that allows to know if you can or not follow a job. Currently, resources
that use **ssh** for batch configuration cannot be followed. In this case, when the JOBMANAGER
load the job, it will set this kind of job in the **Error** state.
