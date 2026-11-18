<!-- source: devs/release_checklist.rst -->

# Release checklist

This page contains a list of things that you should check before issuing a new `valjean` release. In the future, some or all of the things below may (should!) be automated.

1.  Choose the version number of the next release. Use [Semantic Versioning](https://semver.org/).

2.  Create a new branch off the development branch. If you are releasing version `{x.y.z}`, call the branch `releng-v{x.y.z}`. Commit all the following steps on this branch.

3.  Revise this TODO list, if necessary!

4.  Run the code `linters` and fix all the warnings.

5.  Run all the `unit tests`, including the slow ones. Make sure they all pass. Use parallelism:

        $ pytest -m slow -n 4   # for 4 tests in parallel

    Push the `-n` option and overload the test machine a bit (e.g. use `-n 6` if you have 4 cores). If the tests start failing because they run too slowly, they are probably quite close to failing the health checks/deadlines in sequential mode anyway, and they may do so on another machine. Fix them so that they run faster.

    Also, run the command above a few times, in case some tests fail erratically.

    Running `pytest` also runs doctests. Make sure they all pass.

6.  `Build archives` for the code and the documentation

7.  Test `package installation`, with and without optional dependencies (`pip`, `conda` and documentation). Check the install/setup/tests/extras requirements: are they up to date?

8.  Build the HTML documentation `in nitpicky mode`. Fix all the warnings, except the intentional ones.

9.  `Check external documentation links` with the `linkcheck` builder. Fix the broken ones.

10. Check the `TODO list` and update it. Can anything be removed?

11. Update the `changelog`.

12. Commit and make a pull request.

13. Once the pull request is accepted, tag the new version:

        $ git tag vx.y.z  # for appropriate values of x, y and z

    Remember to push the tag to the shared repository.

14. `Create a source tarball and deploy it on the local network`. This requires reinstalling the package and rebuilding the documentation.

15. Remember to merge any release changes back into the development branch.

16. Congratulations, you have made a new `valjean` release!
