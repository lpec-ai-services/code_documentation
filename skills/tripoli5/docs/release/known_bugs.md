<!-- source: https://tripoli5.asnr.dev/documentation/latest-release/release/known_bugs.html -->

# Known bugs

## 0.3.0

## 0.2.0

- [`ROOTGeometry`](../api/patmos-api.md#tripoli5.geometry.root.ROOTGeometry) does not support event based tracking due to a bug in the
  ROOTGeoNavigator system. There is no work around for now.

  This bug is tracked by issue #277
- TRIPOLI-5 can be distributed (among other things) in the form of Python wheels;
  however, the wheels are currently not compatible with ROOT. Compatibility with
  MEDCoupling and MPI has not been verified. If you need to use ROOT, MEDCoupling, or
  MPI, you will have to perform a traditional install from source.

  This bug is tracked by issues #205 and #215.
- There is a problem when applying Branchless collision sampling and splitting.
  A large variance appears when computing fluxes. A workaround is to set a
  very high splitting threshold.

  This bug is tracked by issue #268

## 0.1.0

- [`ROOTGeometry`](../api/patmos-api.md#tripoli5.geometry.root.ROOTGeometry) objects require the number of simulation threads to be
  correctly specified in the constructor (if omitted, 1 thread is assumed). If this
  number is smaller than the number of threads actually used by the simulation or the
  plotter, mayhem will ensue (with a crash being the most likely outcome).

  As a temporary workaround, make sure that the number of threads passed to
  [`ROOTGeometry`](../api/patmos-api.md#tripoli5.geometry.root.ROOTGeometry) always matches the actual number of threads on your machine.

  This bug is tracked by issue #208.
- TRIPOLI-5 can be distributed (among other things) in the form of Python wheels;
  however, the wheels are currently not compatible with ROOT. Compatibility with
  MEDCoupling and MPI has not been verified. If you need to use ROOT, MEDCoupling, or
  MPI, you will have to perform a traditional install.

  This bug is tracked by issues #205 and #215.
- The memory occupation can become quite large in some configurations, because
  it is proportional to the number of neutrons per batch and the particles lives
  length (number of flights and collisions)
  This is due to the “trek” storage that are flushed only at the end of the batch.

  This bug is tracked by issue #253
