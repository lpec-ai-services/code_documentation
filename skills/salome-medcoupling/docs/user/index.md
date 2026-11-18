<!-- source: index.rst -->

# medcoupling user's manual

medcoupling gathers several powerful functionalities around the input and output data of field-physics-oriented simulation codes. Data manipulated by medcoupling are objects relative to fields for simulation codes.

medcoupling functionalities are accessible through python modules.

medcoupling functionalities can be split into 4 categories:  
1.  `Data movement`: read/write from/to file, reduce, extract, duplicate, aggregate, compare, exchange data memory to memory across process (image of multifile to file)
2.  `Data analysis`: extract/gather information in data to transform it in a condensate workable data (not necessarely field linked) for further use.
3.  `Data conversion`: interpolate, project, repare, decimate, format convertion to make discuss simulation codes each other
4.  `Data optimization` for simulation code : renumbering, partition for multiprocessor codes

First, this documentation introduces `fundamental concepts/objects` of medcoupling for a better understanding of examples.

- `basic_concepts` (`basic_concepts.md`)
- `data_movement` (`data_movement.md`)
- `data_analysis` (`data_analysis.md`)
- `data_conversion` (`data_conversion.md`)
- `data_optimization` (`data_optimization.md`)
