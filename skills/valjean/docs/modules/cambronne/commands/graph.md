<!-- source: modules/cambronne/commands/graph.rst -->

# `graph` — The `graph` subcommand

Module for the `graph` subcommand.

### `class valjean.cambronne.commands.graph.GraphCommand  — bases: JobCommand`

Command class for the `build` subcommand.

#### `GraphCommand.register(self, parser)`

Register options for this command in the parser.

#### `GraphCommand.execute(args, _config)`

Execute the `graph` command.

#### `GraphCommand.merge_graph_str(solid_graph, dashed_graph)`

Merge two strings representing graphviz graphs into one graph. The graphs are merged in such a way that the edges of `solid_graph` and `dashed_graph` are respectively represented as solid and dashed.

merge_graph_str

\>\>\> solid_graph = ('digraph {n node1 -\> node2;n' ... ' node2 -\> node3;n}') \>\>\> dashed_graph = 'digraph {n node1 -\> node3;n}'

For example:

\>\>\> print(solid_graph) digraph { node1 -\> node2; node2 -\> node3; } \>\>\> print(dashed_graph) digraph { node1 -\> node3; } \>\>\> print(GraphCommand.merge_graph_str(solid_graph, dashed_graph)) digraph { subgraph G1 { node1 -\> node2; node2 -\> node3; } subgraph G2 { edge \[style=dashed\]; node1 -\> node3; } }

param str solid_graph  
a graph, as produced by `to_graphviz`.

param str dashed_graph  
another graph, as produced by `to_graphviz`.

returns  
the merged graph.

rtype  
str
