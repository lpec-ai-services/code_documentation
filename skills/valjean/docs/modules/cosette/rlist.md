<!-- source: modules/cosette/rlist.rst -->

# `rlist` — Reversible lists

A reversible list (`RList` for short) keeps track of the indices of its elements for fast reverse lookup. It has mostly the same semantics as lists:

> \>\>\> from valjean.cosette.rlist import RList \>\>\> dead, stiff, bereft, rests = ('dead', 'stiff', 'bereft of life', ... 'rests in peace') \>\>\> parrot = RList(\[dead, stiff, bereft, rests\]) \>\>\> parrot\[0\] 'dead' \>\>\> parrot\[-2\] 'bereft of life' \>\>\> del parrot\[1\] \>\>\> print(parrot) \['dead', 'bereft of life', 'rests in peace'\] \>\>\> parrot == \['dead', 'bereft of life', 'rests in peace'\] True \>\>\> parrot == RList(\['a stiff'\]) False

Additionally, you can quickly (in `O(1)` time on average) look up the index of an item or check if an item is contained in the list:

> \>\>\> parrot.index(rests) \# this call is O(1) 2 \>\>\> rests in parrot \# and so is this True

This operation takes `O(n)` average time in normal lists.

The most important differences with respect to the semantics of traditional Python lists are:

> 1.  Slicing operations are not supported.
>
> 2.  The notion of "containment" is user-defined. By default, a value belongs to an `RList` if it has the same `key` as one of the list elements. The `key`, by default, is the value `id`. In other words, normal lists compare items with the `==` operator, while `RList` compares object IDs by default. Objects that compare equal (with the standard `==` operator) may be used interchangeably in a list, but not in a `RList`. For example, here is a simple class:
>
>     > \>\>\> class A: ... def \_\_init\_\_(self, x): ... self.x = x ... def \_\_eq\_\_(self, other): ... return self.x == other.x
>
>     and here is how it behaves in a normal list:
>
>     > \>\>\> a1 = A(42) \>\>\> a2 = A(42) \>\>\> a1 == a2 True \>\>\> a1 in \[a2\] True
>
>     The objects `a1` and `a2` compare equal, so to the eyes of the list `[a2]` they are "the same". `RList`, on the other hand, does not play along with this charade by default:
>
>     > \>\>\> a1 is a2 False \>\>\> id(a1) == id(a2) \# equivalent to the line above False \>\>\> a1 in RList(\[a2\]) False
>
>     Since `a1` and `a2` are distinct objects (they live in different memory locations), they are different in the eyes of `RList`. This may result in unexpected behaviour, especially with strings, ints or other small objects for which the Python interepreter may provide some kind of caching optimisation:
>
>     > \>\>\> lst = RList(\[1\]) \>\>\> 1 in lst True \>\>\> lst = RList(\[1234567\]) \>\>\> 1234567 in lst False \>\>\> \# wat? \>\>\> 1234567 in RList(\[1234567\]) True \>\>\> \# WAT?
>
>     This weird behaviour is actually a well-documented quirk of the CPython implementation.
>
>     If you want, you can define your own notion of `key` for your objects by passing a suitable function to the `key` argument of the `RList` constructor; the only constraint is that the value returned by `key` must be hashable. For example, if you have a list of strings, you can use the string itself as a key as follows:
>
>     > \>\>\> parrot_by_value = RList(\['Norwegian blue', 'plumage', 'pining'\], ... key=lambda x: x) \>\>\> 'plumage' in parrot_by_value True \>\>\> 'bereft of life' in parrot_by_value False
>
>     You can also use more sophisticated `key` functions:
>
>     > \>\>\> a_rlist = RList(\[A(0), A(1), A(2)\], key=lambda a: a.x) \>\>\> A(2) in a_rlist True \>\>\> A(5) in a_rlist False

### `class valjean.cosette.rlist.RList(args=None, *, key=id)  — bases: MutableSequence`

Create a reversible list from an iterable.

param args  
An iterable containing some elements.

#### `RList.insert(self, index, value)`

Insert an element at a given index.

#### `RList.index(self, value, start=0, stop=None)`

Return the index of the given value, if present.

param value  
The object to search for.

param int start  
The index to search from.

param int stop  
The index to search up to.

raises ValueError  
if the element is not present in the container.

returns  
The index of (the first occurrence of) `value` in the list. The returned value `i` always satisfies <span class="title-ref">start \<= i \< stop</span>.

#### `RList.indices(self, value)`

Return all the indices of the given value, if present.

param value  
The object to search for.

raises KeyError  
if the element is not present in the container.

returns  
All the list indices where `value` occurs.

#### `RList.get_index(self, value, default)`

Return the index of the given value, or a default if the value is missing.

param value  
The object to search for.

param default  
The value to be returned if `value` is not present in the container.

#### `RList.swap(self, i, j)`

Swap two elements of the list.

After this operation, the ith and jth elements will be swapped.

param int i  
The index of the first element.

param int j  
The index of the second element.

#### `RList.copy(self)`

Return a shallow copy of this object.
