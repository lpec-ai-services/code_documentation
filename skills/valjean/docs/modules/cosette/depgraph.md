<!-- source: modules/cosette/depgraph.rst -->

# `depgraph` — Dependency graphs

The `DepGraph` class encapsulates a number of useful methods to deal with interdependent items. It represents the workhorse for the scheduling algorithms in the `scheduler` module.

A dependency graph is a directed acyclic graph which may be represented as follows:

depgraph

"bacon" -\> "spam"; "sausage" -\> "eggs", "spam";

The convention here is that if an edge goes from `A` to `B`, then `A` depends on `B`.

## Building

You can create a `DepGraph` in of two ways. Either you pass a dictionary representing the dependencies between items to the `from_dependency_dictionary()` class method:

> \>\>\> from valjean.cosette.depgraph import DepGraph \>\>\> from pprint import pprint \>\>\> deps = {'bacon': \['spam'\], 'sausage': \['eggs', 'spam'\]} \>\>\> pprint(deps) {'bacon': \['spam'\], 'sausage': \['eggs', 'spam'\]} \>\>\> g = DepGraph.from_dependency_dictionary(deps)

or you create an empty graph and add nodes and dependencies by hand:

> \>\>\> h = DepGraph().add_dependency('bacon', on='spam') ... .add_dependency('sausage', on='eggs') ... .add_dependency('sausage', on='spam') \>\>\> g == h True

In these examples, `sausage` depends on `eggs` and `spam`, and `bacon` depends on `spam`; `spam` and `eggs` have no dependencies. Note that the dependency dictionary may be seen as a sparse representation of the graph adjacency matrix.

You can recover the dependency dictionary by passing the graph to `dict()`:

> \>\>\> pprint(dict(g)) \# doctest: +SKIP {'bacon': {'spam'}, 'eggs': set(), 'sausage': {'eggs', 'spam'}, 'spam': set()}

If you print the dictionary, you will notice that `spam` and `eggs` have been added as nodes with no dependencies:

> \>\>\> print(g) \[('bacon', \['spam'\]), ('eggs', \[\]), ('sausage', \['eggs', 'spam'\]), ('spam', \[\])\]

What if a node has no dependencies and no other node depends on it? Just add it to the dictionary with the empty list as a value:

> \>\>\> free = DepGraph.from_dependency_dictionary({'kazantzakis': \[\]})

You can also add it after creating the graph:

> \>\>\> also_free = DepGraph().add_node('kazantzakis') \>\>\> free == also_free True

## Querying

You can inspect the nodes of the graph:

> \>\>\> sorted(g.nodes()) \['bacon', 'eggs', 'sausage', 'spam'\]

or ask for the dependencies of a node:

> \>\>\> sorted(g.dependencies('sausage')) \['eggs', 'spam'\] \>\>\> sorted(g\['sausage'\]) \# equivalent, shorter syntax \['eggs', 'spam'\]

or ask for the nodes that depend on another node (careful though, this operation has `O(N)` time complexity, `N` being the number of nodes in the graph):

> \>\>\> sorted(g.dependees('spam')) \['bacon', 'sausage'\]

You can also iterate over graphs:

> \>\>\> for k, vs in sorted(g): ... for v in sorted(vs): ... print(f"You can't have {k} without {v}!") You can't have bacon without spam! You can't have sausage without eggs! You can't have sausage without spam!

Finally, you can check if a graph is a subgraph of another one:

> \>\>\> sub_g = DepGraph().add_dependency('bacon', on='spam') ... .add_dependency('sausage', on='eggs') \>\>\> sub_g \<= g True

## Merging, sorting and other operations

Given two graphs, possibly sharing some nodes and edges, you can construct the *union* `g12` as follows:

> \>\>\> g1 = sub_g \>\>\> g2 = DepGraph().add_dependency('sausage', on='spam') \>\>\> g12 = g1 + g2 \>\>\> g12 == g True \>\>\> \_ = g2.merge(g1) \# in-place merge \>\>\> g2 == g True \>\>\> g2 += g1 \# equivalent syntax \>\>\> g2 == g True

It is also possible to compute the transitive reduction of the graph. Let `g` be an acyclic graph. The transitive reduction `tr(g)` is the minimal (in the number of edges), provably unique subgraph of `g` over the same vertices with the following property: for each pair of nodes `A` and `B`, `A` is reachable from `B` within `g` iff it is reachable within `tr(g)`.

> \>\>\> g_redundant = DepGraph() ... .add_dependency('eggs', on='bacon') ... .add_dependency('bacon', on='spam') ... .add_dependency('eggs', on='spam') \# this edge is redundant \>\>\> g_tr = g_redundant.copy() \>\>\> print(g_tr.transitive_reduction()) \[('bacon', \['spam'\]), ('eggs', \['bacon'\]), ('spam', \[\])\] \>\>\> 'spam' in g_tr.dependencies('eggs') False

You can also do a topological sort of the graph. The result is a list of the graph nodes, with the property that each node is guaranteed to appear after all the nodes it depends on. Note that in general there are several possible topological sorts for a given graph.

> \>\>\> g.topological_sort() \# doctest: +SKIP \['eggs', 'spam', 'bacon', 'sausage'\]

## Grafting sub-graph nodes into the graph itself

A nice feature of `DepGraph` is that you can have graph nodes that are themselves instances of `DepGraph`! Consider the following graph:

depgraph

compound=true; "Spanish Inquisition" -\> "surprise" \[lhead=cluster1\]; subgraph cluster1 { label="chief weapons" "surprise" -\> "fear"; "surprise" -\> "efficiency"; "fear" -\> "devotion"; "efficiency" -\> "devotion"; } "devotion" -\> "nice red uniforms" \[ltail=cluster1\];

Here is the code that generates it:

> \>\>\> spanish_inq = 'Spanish Inquisition' \>\>\> surprise, fear, efficiency = 'surprise', 'fear', 'efficiency' \>\>\> devotion, uniforms = 'devotion', 'nice red uniforms' \>\>\> chief_weapons = DepGraph.from_dependency_dictionary({ ... surprise: \[fear, efficiency\], ... fear: \[devotion\], ... efficiency: \[devotion\] ... }) \>\>\> spanish = DepGraph() ... .add_dependency(spanish_inq, on=chief_weapons) ... .add_dependency(chief_weapons, on=uniforms)

Here `chief_weapons` is a `DepGraph` itself, but it is also a node of `spanish`. You can graft `chief_weapons` inside `spanish` like so:

> \>\>\> spanish.graft(chief_weapons) DepGraph(...)

This yields the following graph

depgraph

compound=true; "Spanish Inquisition" -\> "surprise"; "surprise" -\> "fear"; "surprise" -\> "efficiency"; "fear" -\> "devotion"; "efficiency" -\> "devotion"; "devotion" -\> "nice red uniforms";

as you can verify yourself:

> \>\>\> full_graph = DepGraph.from_dependency_dictionary({ ... spanish_inq: \[surprise\], ... surprise: \[fear, efficiency\], ... fear: \[devotion\], ... efficiency: \[devotion\], ... devotion: \[uniforms\] ... }) \>\>\> full_graph == spanish True

The nice thing about this feature is that it makes it easier (more modular) to build complex graphs. Just build smaller subgraphs and assemble them together as if they were nodes! The `flatten` method will recursively graft all graph nodes into the main graph.

(Fun fact: the `DepGraph` type is a monad, with `flatten` playing the role of `join`. If what I just wrote makes no sense to you, don't worry.)

## Caveats

Some things you should be aware of when using `DepGraph`:

- The type of the items in the graph is irrelevant, but if you want to use the `from_dependency_dictionary()` constructor they need to be stored in a dictionary, and therefore they must be *hashable*;

- You need to use a single-element list if you want to express a single dependency, as in the case of `bacon`. So this is wrong:

  > \>\>\> bad_deps = {0: 1, 7: \[0, 42\]} \# error, should be 0: \[1\] \>\>\> bad = DepGraph.from_dependency_dictionary(bad_deps) Traceback (most recent call last): File "\<stdin\>", line 1, in \<module\> \[...\] TypeError: 'int' object is not iterable

  Here `1` is not iterable, and the test crashed. However, if your graph nodes happen to be iterable, the `DepGraph` constructor will not crash, but you will not get what you expect.

### `class valjean.cosette.depgraph.DepGraphError  — bases: Exception`

An exception raised by `DepGraph`.

### `class valjean.cosette.depgraph.DepGraph(nodes=None, edges=None)`

A dependency graph.

There are two preferred ways to instantiate this class:

- using the `from_dependency_dictionary()` class method;
- constructing an empty graph and repeatedly calling `add_dependency()` and/or `add_node()`.

Alternatively, you may also use the full form of the constructor; in this case, the graph `edges` are represented as a dictionary between integers, with the convention that each node is represented by its index in the `nodes` list. So `nodes` can be seen as a mapping from integers to nodes. The inverse mapping is called `index` and may be passed to the constructor if it is available to the caller as a dictionary; if not, it will be constructed internally.

#### `DepGraph.from_dependency_dictionary(cls, dependencies)`

Generate a `DepGraph` from a dependency dictionary.

#### `DepGraph.isomorphic_to(self, other)`

Returns `True` if this graph is isomorphic to `other`.

#### `DepGraph.add_node(self, node)`

Add a new node to the graph.

param node  
The new node.

#### `DepGraph.remove_node(self, node)`

Remove a node from the graph.

Any edges going in and out of the node will be removed, too.

param node  
The node to be removed.

#### `DepGraph.add_dependency(self, node, on)`

Add a new dependency to the graph.

param node  
The node for which the dependency is specified.

param on  
The node `node` depends on.

#### `DepGraph.remove_dependency(self, node, on)`

Remove a dependency from the graph.

param node  
The node for which the dependency is specified.

param on  
The node `node` depends on.

#### `DepGraph.invert(self)`

Invert the graph.

returns  
A new graph having the same nodes but all edges inverted.

#### `DepGraph.topological_sort(self)`

Perform a topological sort of the graph.

returns  
The nodes of the graph, as a list, with the invariant that each node appears in the list after all the nodes it depends on.

raises DepGraphError  
if the graph is cyclic.

#### `DepGraph.copy(self)`

Return a copy of this graph.

#### `DepGraph.merge(self, other)`

Merge this graph in place with another one.

param DepGraph other  
The graph to merge.

#### `DepGraph.nodes(self)`

Returns the graph nodes.

#### `DepGraph.dependencies(self, node, recurse=False)`

Query the graph about the dependencies of `node`. If `recurse` is `True`, also return indirect dependencies (the transitive closure of the specified node). With `recurse=False`, this operation is `O(1)`.

param bool recurse  
If true, return indirect dependencies as well.

returns  
A list containing the dependencies of `node`.

#### `DepGraph.dependees(self, node)`

Collect the nodes that depend on the given node. This operation is `O(N)`, where `N` is the number of nodes in the graph.

returns  
A set containing the dependees of `node`.

#### `DepGraph.to_graphviz(self)`

Convert the graph to graphviz format.

returns  
A string describing the file in graphviz format.

#### `DepGraph.transitive_reduction(self)`

Perform a transitive reduction of the graph in place.

#### `DepGraph.transitive_closure(self)`

Perform a transitive closure of the graph in place.

#### `DepGraph.initial(self)`

Return the initial nodes of the graph.

The initial nodes are the nodes that have no ingoing edge; i.e., no other node depends on them.

returns  
The list of initial nodes.

#### `DepGraph.terminal(self)`

Return the terminal nodes of the graph.

The terminal nodes are the nodes that have no outgoing edge; i.e., they do not depend on any other node.

returns  
The list of terminal nodes.

#### `DepGraph.graft(self, node)`

Graft the given node into the graph.

param DepGraph node  
A DepGraph embedded as a graph node.

#### `DepGraph.flatten(self, recurse=True)`

Graft all DepGraph nodes into this graph.

param bool recurse  
If true, recursively graft DepGraph nodes until all nodes are flat.

#### `DepGraph.depends(self, node1, node2, recurse=False)`

Return `True` if the node `node1` depends on `node2`.

param node1  
The first node.

param node2  
The second node.

param bool recurse  
If true, look at indirect dependencies, too.

returns  
`True` if `node1` directly (`recurse == False`) or indirectly (`recurse == True`) depends on `node2`.
