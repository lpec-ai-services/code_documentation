<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/post_processings/generalities.html -->

# Generalities on post-processings

Post-processings are executed at the beginning of the simulation and at
the end of every time steps.

See also

Further help about available post-processings can be found in the
`Post-Processings` section of the online help which is accessible in
`python` through the `manta.info` function or through the
`manta-info` utility (see Section [The manta-info utility](../miscellaneous/tools.md#manta-info-utility)).

PYTHON

```python
manta.info('Post-Processings')
```

SH

```sh
manta-info Post-Processings
```

There are mostly three ways to add a new post-processing to a physical
system:

1. Post-processings can be added to a physical system using the a first
   version of the `addPostProcessing` method. This version takes the name
   of the post-processing and the parameters passed to the initialize the
   post-processing. This method is mostly a shortcut for the second
   option.
2. Post-processing can be generated using `create` method of the
   `PostProcessingFactory` class (see Section [The PostProcessingFactory class](#post-processing-class)).
   The resulting post-processing can then
   be added to the physical system using the `addPostProcessing` method.
   Direct usage of the `PostProcessingFactory` class is discouraged.
3. New post-processings can be defined by the user by inheriting from
   the `AbstractPostProcessing` class.

Note

In `python`, the `PostProcessing` function is also available to create a
new post-processing as follows:

```python
p = PostProcessing('Curves', ps,
                   file = 'curves/local-temperatures.txt',
                   curves = [{'NodalValue': {'field': 'Temperature',
                                             'nodes': ['p1', 'p2', 'p3']}}
ps.addPostProcessing(p)
```

This function just hides `PostProcessingFactory` class.

## The `PostProcessingFactory` class

The `PostProcessingFactory` class is the standard way to create a
new post-processings. For more details, see Section
[Factory functions and abstract factories](../../developer_guide/dev_guidelines/patterns.md#abstract-factories). Its direct usage is generally discouraged, as
discussed in the introduction of this section.

The `PostProcessingFactory` class however allows to retrieve the
list of available post-processings and their descriptions.

Following the singleton pattern, only one instance of this class exists.
It can be accessed through the `static` method get, as follows:

PYTHON

```python
f = PostProcessingFactory.get()
```

C++

```c++
auto& f = PostProcessingFactory::get()
```
