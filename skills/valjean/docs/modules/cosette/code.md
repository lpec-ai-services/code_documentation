<!-- source: modules/cosette/code.rst -->

# `code` — Tools for checking out and building code

This submodule contains a few useful tasks for checking out, configuring, and building arbitrary code.

The `CheckoutTask` task class checks out a version-controlled repository. For the moment, only `git` repositories are supported. The path to the `git` executable may be specified through the `CheckoutTask.GIT` class variable.

Implement `svn` and `cvs` checkout; `copy` checkout (i.e. copy a directory from somewhere) may also be useful.

The `BuildTask` task class builds code from a given source directory. A build directory must also be specified and will be created if necessary. For the moment, `BuildTask` only supports <span class="title-ref"> </span><span class="title-ref">cmake</span><span class="title-ref"> builds, but there are plans to add support for </span><span class="title-ref">autoconf</span><span class="title-ref">/</span><span class="title-ref">configure</span><span class="title-ref">/</span><span class="title-ref">make</span><span class="title-ref"> builds. The path to the </span><span class="title-ref">cmake</span><span class="title-ref"> executable may be specified through the </span><span class="title-ref">BuildTask.CMAKE</span>\` class variable.

Implement `autoconf`/`configure`/`make` builds.

code

\>\>\> from valjean.cosette.code import CheckoutTask, BuildTask \>\>\> import subprocess \>\>\> work_dir = getfixture('tmp_path') \>\>\> repo_dir = work_dir / 'repo' \>\>\> repo_dir.mkdir() \>\>\> subprocess.check_call(\[CheckoutTask.GIT, 'init', str(repo_dir)\]) 0 \>\>\> cmakelists_path = repo_dir / 'CMakeLists.txt' \>\>\> with cmakelists_path.open('w') as cmake_file: ... print('project(TestCodeTasks C)n' ... 'cmake_minimum_required(VERSION 2.6)n' ... 'set(SOURCE_FILENAME "\${PROJECT_BINARY_DIR}/test.c")n' ... 'file(WRITE "\${SOURCE_FILENAME}" "int main(){return 0;}")n' ... 'add_executable(test_exe "\${SOURCE_FILENAME}")n', ... file=cmake_file) \>\>\> git_dir = repo_dir / '.git' \>\>\> subprocess.check_call(\[CheckoutTask.GIT, '--git-dir', str(git_dir), ... 'config', 'user.email', '<sblinda@antani.com>'\]) 0 \>\>\> subprocess.check_call(\[CheckoutTask.GIT, '--git-dir', str(git_dir), ... 'config', 'user.name', 'Conte Mascetti'\]) 0 \>\>\> subprocess.check_call(\[CheckoutTask.GIT, '--git-dir', str(git_dir), ... '--work-tree' , str(repo_dir), ... 'add', 'CMakeLists.txt'\]) 0 \>\>\> subprocess.check_call(\[CheckoutTask.GIT, '--git-dir', str(git_dir), ... '--work-tree', str(repo_dir), ... 'commit', '-a', '-m', 'Test commit'\]) 0

To describe the usage of `CheckoutTask` and `BuildTask`, let us assume that `repo_dir` contains a `git` repository with a CMake project. We use a temporary directory `work_dir` for our test:

> \>\>\> checkout_dir = work_dir / 'checkout' \>\>\> build_dir = work_dir / 'build' \>\>\> log_dir = work_dir / 'log'

Now we can build checkout and build tasks for this repository:

> \>\>\> from valjean.cosette.code import CheckoutTask, BuildTask \>\>\> from pprint import pprint \>\>\> ct = CheckoutTask(name='project_checkout', ... repository=repo_dir, ... checkout_root=checkout_dir, ... log_root=log_dir) \>\>\> bt = BuildTask(name='project_build', ... source=ct, ... build_root=build_dir, ... build_flags=\['--' ,'-j4'\], ... log_root=log_dir)

Note how we passed the `ct` object directly to the `source` argument of the `BuildTask` constructor: we are telling the `BuildTask` to look for the sources to build in the checkout directory. You can also pass a normal path to the `source` argument instead.

> \>\>\> from valjean.cosette.env import Env \>\>\> env = Env() \>\>\> ct_up, ct_status = ct.do(env, config=None) \>\>\> print(ct_status) TaskStatus.DONE \>\>\> pprint(ct_up) {'project_checkout': {'checkout_log': '.../log/project_checkout.log', 'elapsed_time': ..., 'output_dir': '.../checkout/project_checkout', 'repository': '.../repo'}} \>\>\> env.apply(ct_up) \# apply CheckoutTask's environment update ... \# for this example, this is actually optional \>\>\> bt_up, bt_status = bt.do(env=env, config=None) \>\>\> print(bt_status) TaskStatus.DONE \>\>\> pprint(bt_up) {'project_build': {'build_log': '.../log/project_build.log', 'elapsed_time': ..., 'output_dir': '.../build/project_build'}}

### `class valjean.cosette.code.CheckoutTask(name, *, repository, checkout_root=None, log_root=None, flags=None, ref=None, vcs='git', deps=None, soft_deps=None)  — bases: PythonTask`

Task to check out code from a version-control system. The actual code checkout is performed when the task is executed.

### `class valjean.cosette.code.BuildTask(name, source, *, build_root=None, log_root=None, targets=None, build_system='cmake', configure_flags=None, build_flags=None, deps=None, soft_deps=None)  — bases: PythonTask`

Task to build an existing source tree. The build is actually performed when the task is executed.

#### `BuildTask.cmake_build_sys(self, targets, configure_flags, build_flags)`

Return a function that builds a project using cmake.
