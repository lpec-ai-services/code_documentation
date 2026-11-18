<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/main_concepts.html -->

# Main concepts

The high level API (Application Programming Interface) is meant to set
up and perform *simulations* of the evolution over a given time
range, discretized in *time steps*, of the thermodynamical
*state* of the *materials* of a *physical system* due
to imposed *loadings*.

This evolution is described using *models* describing one or
several physical phenomena. Most models are built on balance equation
(heat transfer, mechanics, diffusion, etc..) which requires to solve
partial differential equations, for which MANTA provides several
numerical methods, including the Finite Element Method (FEM), Finite
Volume Method (FVM), the Hybrid High Order method (HHO), etc. The models
relies on so-called *bricks* which describes the behavior of
materials, structural elements and boundary conditions. The high level
API provides some built-in bricks, but advanced users may create their
own and plug them, using the so-called low-level API.

The coupling between models is treated using a staggered approach
described by a *coupling scheme*. A coupling scheme may contain
models, embedded coupling schemes, accelerators, convergence
criteria, auxiliary tasks, etc.

Finally, a *simulation* allows to describe the evolution of the
physical system over a period of time, discretized by the user in
(temporal) *sequences*. Each sequences can be further discretized
in *steps* by the *simulation* to take into account
numerical constraints on the time step (notably in explicit
simulations), or to overcome convergence issues.

This design is strongly inspired from the `licos` fuel performance
code. The reader may refer to [[HBM15](../references/references.md#id31)] for additional
details.

This description is quite formal and general. As we will see in the
following commented example, MANTA is very flexible and can be adapted
to most needs:

- if one needs to perform only one time step, one does not need to
  define a simulation,
- if only one model is considered, then there is no need to declared a
  coupling scheme,
- etc.

## Description of a standard computation

A standard computation using the high level API is decomposed in two
steps:

1. The initialization of the physical system. This initialization
   includes:

   1. the definition of the physical system,
   2. the definition of coupling scheme and models,
   3. the definition, for each models, of the bricks definining the
      material, the structural elements, the boundary conditions, etc.,
   4. the definition of the properties of materials and loadings
      imposed to the system,
   5. the definition of *post-processings*, called during the
      simulation at the end of each time steps, or at the end of each
      temporal sequences.
2. The set up of a *simulation* and its execution. A simulation may
   provide a sub-stepping strategy to handle difficult cases.

## A simple uniaxial test

To illustrate the previous concepts, let us consider the following
simple example of a uniaxial tensile test of an hyperelastic material in
implicit mechanics in Python, C++ and JSON:

PYTHON

```python
import manta

def runSimulation():
    ps = manta.PhysicalSystem(mesh = {'generator': 'Grid',
                                      'spaceDimension': 3})
    
    mm = manta.Model('ImplicitMechanics', ps)
    
    for b,c in {'left': 'UX', 'rear': 'UY', 'bottom': 'UZ'}.items():
        mm.add('ImposedDisplacement',
               boundary = b,
               component = c,
               strategy = 'elimination')
        
    mm.add('ImposedDisplacement',
           boundary = 'right',
           component = 'UX',
           value = 'ImposedDisplacementValue',
           strategy = 'elimination')
    
    mm.add('SolidMaterial',
           material = 'cube',
           library = './libHyperElasticityBehaviours-generic.so',
           behavior = 'SaintVenantKirchhoffElasticity')

    for n, v in {'YoungModulus': 150e9, 'PoissonRatio': 0.3}.items():
        ps.addProperty('Constant',
                       material =  'cube',
                       name = n,
                       value = v)

    ps.addLoading('ConstantUniformScalar',
	          material = 'cube',
                  name = 'Temperature',
                  value = 293.15)

    umax = 1e-2
    ps.addLoadingEvolution('ImposedDisplacementValue', lambda t: umax * t)
    # creating the coupling scheme
    ps.setModel(mm)
    #
    nIncr = 20
    dt = 1 / nIncr
    s = manta.Simulation(ps, times = [i * dt for i in range(0, 21)])
    s.run()

runSimulation()
```

C++

```c++
#include <cstdlib>
#include "manta/components-system/init.h"
#include "manta/frontend-manta/physical_system/physical_system.h"
#include "manta/frontend-manta/physical_system/simulation.h"
#include "manta/frontend-manta/model/abstract_model.h"
#include "manta/frontend-manta/model/model_factory.h"
#include "manta/components-executable_utilities/decl/fatal_error.h"
#include "manta/components-executable_utilities/config.h"

void runSimulation()
{
  using namespace manta;
  MANTA_FATAL_ERROR;
  constexpr auto dim = Int{3};
  //
  auto ctx = Context{};
  //
  auto ps = construct<PhysicalSystem>(ctx, R"({"mesh": {"generator": "Grid",
                                                        "spaceDimension": 3}})"_json);
  // mechanical model
  auto mm = ModelFactory::get().create(ctx, "ImplicitMechanics", *ps, {});
  // bricks
  for (const auto &[b, c] : OMap<std::string, std::string>{{"left", "UX"},    //
                                                           {"rear", "UY"},
                                                           {"bottom", "UZ"}}) {
    mm->add(ctx,
            "ImposedDisplacement",    //
            {{"boundary", std::string{b}}, {"component", c}, {"strategy", "elimination"}});
  }
  mm->add(ctx,
          "ImposedDisplacement",
          {{"boundary", "right"},    //
           {"component", "UX"},
           {"value", "ImposedDisplacementValue"},
           {"strategy", "elimination"}});
  mm->add(ctx,
          "SolidMaterial",
          Parameters{{"material", "cube"},
                     {"library", "./libHyperElasticityBehaviours-generic.so"},
                     {"behavior", "SaintVenantKirchhoffElasticity"}});
  // properties and loadings
  for (const auto &[n, v] : HMap<std::string, Real>{{"YoungModulus", 150e9},    //
                                                    {"PoissonRatio", 0.3}}) {
    ps->addProperty(ctx,
                    "Constant",    //
                    Parameters{{"material", "cube"}, {"name", n}, {"value", v}});
  }
  ps->addLoading(ctx,
                 "ConstantUniformScalar",    //
                 Parameters{{"material", "cube"}, {"name", "Temperature"}, {"value", 293.15}});
  //
  ps->addLoadingEvolution(ctx, "ImposedDisplacementValue", [](const Real t) noexcept {
    constexpr auto umax = Real{1e-3};
    return umax * t;
  });
  //
  ps->setModel(ctx, mm);
  ps->initialize(ctx);
  //
  auto s = construct<Simulation>(ctx, *ps, Simulation::TimesDescription{0, 1, 20});
  s->run(ctx);
}

int main(int argc, char **argv)
{
  manta::init(argc, argv);
  runSimulation();
  manta::finalize();
  return EXIT_SUCCESS;
}
```

JSON

```json
{
  "physicalSystem": {
    "mesh": {
      "generator": "Grid",
      "spaceDimension": 3
    },
    "geometricHypothesis": "Tridimensional",
    "model": {
      "ImplicitMechanics": {
        "bricks": [
          {
            "ImplicitMechanicsSolidMaterial": {
              "material": "cube",
              "library": "./libHyperElasticityBehaviours-generic.so",
              "behavior": "SaintVenantKirchhoffElasticity"
            }
          },
          {
            "ImposedDisplacement": {
              "boundary": "left",
              "component": "UX"
            }
          },
          {
            "ImposedDisplacement": {
              "boundary": "rear",
              "component": "UY"
            }
          },
          {
            "ImposedDisplacement": {
              "boundary": "bottom",
              "component": "UZ"
            }
          },
          {
            "ImposedDisplacement": {
              "boundary": "top",
              "component": "UZ",
              "value": "ImposedDisplacementValue"
            }
          }
        ]
      }
    },
    "properties": [
      {
        "Constant": {
          "name": "YoungModulus",
          "material": "cube",
          "value": 150000000000
        }
      },
      {
        "Constant": {
          "name": "PoissonRatio",
          "material": "cube",
          "value": 0.3
        }
      }
    ],
    "loadings": [
      {
        "ConstantUniformScalar": {
          "material": "cube",
          "name": "Temperature",
          "value": 293.15
        }
      }
    ],
    "loadingEvolutions": [
      {
        "Table": {
          "name": "ImposedDisplacementValue",
          "interpolationType": "linear",
          "abscissae": [
            0,
            1
          ],
          "ordinates": [
            0,
            0.01
          ]
        }
      }
    ]
  },
  "simulations": [
    {
      "times": [
        0,
        0.5,
        1
      ]
    }
  ]
}
```

The Python version targets most end-users and casual engineers, in
particular those accustomed to [Cast3M](https://www-cast3m.cea.fr/index.php)'s `Gibiane` scripting
language. It is meant to be readable and explicit.

The C++ API is **not** meant to be used directly by end-users. It
mostly targets domain specific applications or numerical platforms. The
C++ exemple is presented here to highlight its existence and show that
is an almost one to one equivalent to its Python counterpart.
Experienced C++ developers may have noticed in the example some
oddities that are mostly related to error handling. This remarks allows
highlighting another very important focus of Manta's design: the error
handling strategy used by the C++ API is meant to be consistent with
HPC programming models, such as MPI, while providing a robust user
experience and meaningful error messages. The code showed in the example
is simplified by the usage of `MANTA_FATAL_ERROR` macro. If this
macro was not used, one would have to check the returned value of each
function calls which would be extremly cumbersome. Those details
regarding error handling are totally hidden in the Python API which
reports errors using exceptions.

The JSON version of the example is here to showcase the fact that the
end-user API has been designed to be very declarative. This design is
meant to easily create domain specific applications with built-in
support for input files or even graphical interfaces.

### The physical system

The physical system is one of the main entry point for the user. In this
example, it is declared as follows:

PYTHON

```python
    ps = manta.PhysicalSystem(mesh = {'generator': 'Grid',
                                      'spaceDimension': 3})
```

C++

```c++
                                                        "spaceDimension": 3}})"_json);
  // mechanical model
```

JSON

```json
  "physicalSystem": {
    "mesh": {
      "generator": "Grid",
      "spaceDimension": 3
    },
    "geometricHypothesis": "Tridimensional",
    "model": {
      "ImplicitMechanics": {
        "bricks": [
          {
            "ImplicitMechanicsSolidMaterial": {
              "material": "cube",
              "library": "./libHyperElasticityBehaviours-generic.so",
              "behavior": "SaintVenantKirchhoffElasticity"
            }
          },
          {
            "ImposedDisplacement": {
              "boundary": "left",
              "component": "UX"
            }
          },
          {
            "ImposedDisplacement": {
              "boundary": "rear",
              "component": "UY"
            }
          },
          {
            "ImposedDisplacement": {
              "boundary": "bottom",
              "component": "UZ"
            }
          },
          {
            "ImposedDisplacement": {
              "boundary": "top",
              "component": "UZ",
              "value": "ImposedDisplacementValue"
            }
          }
        ]
      }
    },
    "properties": [
      {
        "Constant": {
          "name": "YoungModulus",
          "material": "cube",
          "value": 150000000000
        }
      },
      {
        "Constant": {
          "name": "PoissonRatio",
          "material": "cube",
          "value": 0.3
        }
      }
    ],
    "loadings": [
      {
        "ConstantUniformScalar": {
          "material": "cube",
          "name": "Temperature",
          "value": 293.15
        }
      }
    ],
    "loadingEvolutions": [
      {
        "Table": {
          "name": "ImposedDisplacementValue",
          "interpolationType": "linear",
          "abscissae": [
            0,
            1
          ],
          "ordinates": [
            0,
            0.01
          ]
        }
      }
    ]
  },
```

The declaration seems totally different in JSON compared to the
Python, C++ versions. In JSON, every aspects of the physical
system are declared (coupling scheme, model, boundary conditions) all at
once. In Python and C++, the physical system is completed
incrementally and intermediate objects are used. It is important to note
that the physical system could also have been created all at once in
Python and C++. This illustrates the "Matryoshka doll" aspect of the
design of MANTA. At various stages, the user can choose a coarse grain
approach, or choose to go deeper in the API to have finer grain control
for greater flexibility, depending on his/her needs. The rest of this
document will mostly focus on describing the Python and C++
versions.

In this example, the physical system uses a \(3D\) mesh generated by
the `Grid` generator. Aside from the `Grid` generator which is
mostly used for testing purposes, MANTA supports various file format
to define the mesh with a particular focus on the `MED` file
format provided by the [SALOME platform](https://www.salome-platform.org/?lang=en). The `MED` file
format has become the lingua franca between solvers in the french nuclear
industry and its supports allows to seamlessly interoperate with [Cast3M](https://www-cast3m.cea.fr/index.php) and [code_aster](https://code-aster.org/) for instance. Mesh files
generates by [Gmsh](https://gmsh.info/) are also supported.

By default, the `Grid` generator generates (in \(3D\)) a cube
of one element of unit lengths named `cube`, as well as the
boundaries `left`, `right`, `rear`, `front`,
`top`, and `bottom`. Lengths, number of elements, and names
can be changed using appropriate parameters.

The list of mesh sets read by the physical system can be retrieved using
the `info` function in Python:

PYTHON

```python
manta.info(ps)
```

By default, the information returned described every aspects of the
physical system. As we are only interested in information relative to
the mesh, the following syntax is more focused:

PYTHON

```python
manta.info(ps, False, mesh = True)
```

The first boolean states that we only want the specific information
given in the list of arguments.

Note

The list of valid arguments for physical
systems can be retrieved using `helpOptions` as follows:

PYTHON

```python
manta.info(ps, False, helpOptions = True)
```

Those first lines of code highlight a generic pattern in the end-user
int the signature of the Python and C++ methods and
functions:

- In Python, most arguments are passed using the `kwargs`
  parameter when possible or dictionaries otherwise.
- In C++, the first argument is almost ever a `Context` which has
  several role, in particular regarding error handling. The last
  argument is almost ever a `Parameters` which is more or less the
  equivalent of a dictionary in Python and is rich enough to store the
  data contained in a JSON file.

Such pattern is central to ensure the consistency of the Python, C++
and JSON API.

Note that objects are created using the `construct` function which
encaspulate the call to constructors, as constructors may use exceptions
to report errors.

The list of parameters (and their descriptions) of the `PhysicalSystem`
class is accessible in `python` through the `manta.info`
function or through the `manta-info` utility (see Section
[The manta-info utility](miscellaneous/tools.md#manta-info-utility)).

PYTHON

```python
manta.info('Main concepts', 'Physical system')
```

SH

```sh
manta-info "Main concepts:Physical system"
```

### Creation of the mechanical model

The mechanical model is created as follows:

PYTHON

```python
    mm = manta.Model('ImplicitMechanics', ps)
```

C++

```c++
  // bricks
```

JSON

```json
    "model": {
      "ImplicitMechanics": {
        "bricks": [
          {
            "ImplicitMechanicsSolidMaterial": {
              "material": "cube",
              "library": "./libHyperElasticityBehaviours-generic.so",
              "behavior": "SaintVenantKirchhoffElasticity"
            }
          },
          {
            "ImposedDisplacement": {
              "boundary": "left",
              "component": "UX"
            }
          },
          {
            "ImposedDisplacement": {
              "boundary": "rear",
              "component": "UY"
            }
          },
          {
            "ImposedDisplacement": {
              "boundary": "bottom",
              "component": "UZ"
            }
          },
          {
            "ImposedDisplacement": {
              "boundary": "top",
              "component": "UZ",
              "value": "ImposedDisplacementValue"
            }
          }
        ]
      }
    },
```

The name of the default model describing solid mechanics using an
implicit approach is *ImplicitMechanics*. This model is described
in Section [The ImplicitMechanics model](models/solid_mechanics/implicit_solid_mechanics.md#implicit-mechanics-model).

The list of available models is described in *Models* section of
the online help:

PYTHON

```python
manta.info('Models')
```

SH

```sh
manta-info "Models"
```

Here we create an empty model which must be populated using so-called
*bricks* which describes materials, structures and boundary
conditions, as shown the next section.

It is important to note that user-defined models can be registred in
`ModelFactory` class using plugins.

### Model bricks

Bricks plays a major role in MANTA as they allows to built the problem
solved by a model. In particular, bricks:

- declares the unknowns of determined by the model, the displacement
  field in our case,
- participate to the so-called dependency management algorithm which
  greatly simplify the description of a problem. This dependency
  management algorithm is illustrated more in depth below,
- instanciate, at the beginning of the simulation, so-called
  *formulations* which are the computational kernels.

The list of available bricks is accessible as follows:

PYTHON

```python
manta.info('Model bricks')
```

SH

```sh
manta-info "Model bricks"
```

User-defined bricks, defining new structural elements or new boundary
conditions, can be added as plugins.

Two different bricks are used in this example:

- the *ImposedDisplacement* brick to describe the boundary conditions,
- the *ImplicitMechanicsSolidMaterial* brick, to describe the
  behaviour of the material. The *ImplicitMechanics* model
  provides an alias for this brick named *SolidMaterial*. Most
  models provide a similar aliases.

Note

As stated in the introduction, MANTA supports several discretization
methods.

The discretization method can be selected, by order of priority
at the brick level (using the `discretizationMethod` parameter),
at the model level and at the physical level (using in those case the
`defaultDiscretizationMethod` parameter).

By default, the finite element method is used.

By default, models shall not allow to mix bricks using distinct
discretization methods. This can be changed using the parameter
`allowMixingDiscretizationMethods`, which must be set to
`true`.

#### The *ImposedDisplacement* brick

4 essential boundary conditions are applied:

- 3 faces of the cube (`left`, `rear` and `bottom`) are
  blocked in the direction or their normals.
- a face on which the displacement in direction or its normal is imposed
  to a given value.

Those bricks are declared as follows:

PYTHON

```python
    for b,c in {'left': 'UX', 'rear': 'UY', 'bottom': 'UZ'}.items():
        mm.add('ImposedDisplacement',
               boundary = b,
               component = c,
               strategy = 'elimination')
        
    mm.add('ImposedDisplacement',
           boundary = 'right',
           component = 'UX',
           value = 'ImposedDisplacementValue',
           strategy = 'elimination')
```

C++

```c++
                                                           {"rear", "UY"},
                                                           {"bottom", "UZ"}}) {
    mm->add(ctx,
            "ImposedDisplacement",    //
            {{"boundary", std::string{b}}, {"component", c}, {"strategy", "elimination"}});
  }
  mm->add(ctx,
          "ImposedDisplacement",
          {{"boundary", "right"},    //
           {"component", "UX"},
           {"value", "ImposedDisplacementValue"},
           {"strategy", "elimination"}});
  mm->add(ctx,
```

JSON

```json
          {
            "ImposedDisplacement": {
              "boundary": "left",
              "component": "UX"
            }
          },
          {
            "ImposedDisplacement": {
              "boundary": "rear",
              "component": "UY"
            }
          },
          {
            "ImposedDisplacement": {
              "boundary": "bottom",
              "component": "UZ"
            }
          },
          {
            "ImposedDisplacement": {
              "boundary": "top",
              "component": "UZ",
              "value": "ImposedDisplacementValue"
            }
          }
```

Those boundary conditions are treated by the *ImposedDisplacement*
brick.

The `component` parameter gives the name of the component of the
displacement field treated by the brick. This parameter can be replaced
by the `components` parameter to give a list of components.
Components can be given using integer (starting from \(0\)) and, for
certain fields declared in the so-called glossary, by a name. In
\(3D\), the names of the components of the displacement fields are
`UX`, `UY` and `UZ`. Those names are inherited from the
Cast3M's solver.

By default, if the `value` parameter is not specified, the unknown
field, here the displacement field, is set to zero.

The `value` parameter can be either a floating-point value or a
string. A string, like `ImposedDisplacementValue` as in the fourth
declaration, forces the *ImposedDisplacement* brick to declare a
nodal scalar dependency that must be defined on the boundary
`right`. This dependency, as all dependencies declared by the other
bricks, must be fulfilled by some provider for a simulation to be run.
In MANTA, a provider can be a loading, another model, an external
solver, etc.

For this example, the `strategy` parameter selects how the
constraint shall be handled. In this case, this declaration is
superfluous as the `identityLHS` strategy is the default one. It has
been explicitly specified to highlight the fact that MANTA exposes
several strategies and gives control to end-user to select the
appropriate one.

The parameters of a brick are accessible by the online help:

PYTHON

```python
manta.info('Model bricks', 'ImposedDisplacement')
```

SH

```sh
manta-info "Model bricks:ImposedDisplacement"
```

It is worth emphasizing the fact that those bricks are also providers of
the resultants of the forces required to apply their respective
constraints. The computations of those resultants are made on request,
i.e. if those quantities are not requested during the dependency management
algorithm, they are not computed.

The default name of the resultant for the last boundary condition is
`ResultantOfReactionForce[FX]` (or equivalently
`ResultantOfReactionForce[0]`). This name can be changed using the
`reaction` parameter.

In Python, the simpliest way to know the name of the reaction computed
by this brick is to modify the code as follows:

PYTHON

```python
b = mm.add('ImposedDisplacement',
        boundary = 'right',
        component = 'UX',
        value = 'ImposedDisplacement',
        strategy = 'elimination')
manta.info(b)
```

#### The *SolidMaterial* brick

The *SolidMaterial* brick describe a solid material using a small
strain or a finite strain behavior implemented using the [MFront](https://thelfer.github.io/tfel/web/index.html) code generator. This
brick is described in Section
[The ImplicitMechanicsSolidMaterial brick](bricks/solid_mechanics/implicit_mechanics_solid_material.md#implicit-mechanics-solid-material-brick) of the user guide.

PYTHON

```python
    mm.add('SolidMaterial',
           material = 'cube',
           library = './libHyperElasticityBehaviours-generic.so',
           behavior = 'SaintVenantKirchhoffElasticity')
```

C++

```c++
          "SolidMaterial",
          Parameters{{"material", "cube"},
                     {"library", "./libHyperElasticityBehaviours-generic.so"},
                     {"behavior", "SaintVenantKirchhoffElasticity"}});
  // properties and loadings
```

JSON

```json
          {
            "ImplicitMechanicsSolidMaterial": {
              "material": "cube",
              "library": "./libHyperElasticityBehaviours-generic.so",
              "behavior": "SaintVenantKirchhoffElasticity"
            }
          },
```

The main parameters of this brick are the:

- `material` (or equivalently `material`), which denotes on
  which part of the mesh the brick works,
- `library`, which indicates which shared library provides the
  behavior,
- `behavior`, which selects the behavior to use in this shared
  library.

Behaviors are complex:

- They may declare many dependencies, declared as *material properties*
  and *external state variables* in the MFront's wording.
- They can provide information on the state of the material through
  *internal state variables*.

When loading the behavior, the brick automatically retrieves:

- the type of behavior. Small and finite strain behaviors are currently
  supported.
- The names and types of the gradients, the thermodynamic forces, the
  material properties, external state variables and internal state
  variables.

In our example, we consider the classical Saint-Venant-Kirchhoff
hyperelastic behavior. The only gradient is the deformation gradient,
named `DeformationGradient`, and the associated thermodynamic force
the first Piola-Kirchhoff stress, named FirstPiolaKirchhoffStress.
This simple behavior does not declare any state variable. This behavior
requires:

- two material properties, the Young's modulus, named
  `YoungModulus`, and the Poisson's ratio, named
  `PoissonRatio`.
- an external state variable, the temperature, name `Temperature`.
  Note that this state variable is not used by the behavior. It is
  declared automatically by MFront for compatibility with most
  solvers.

Those information can be retrieved on the command line using the
`mfront-query` tool. In Python, it is much more convenient to
proceed as follows:

PYTHON

```python
b = mm.add('SolidMaterial',
           material = 'cube',
           library = './libHyperElasticityBehaviours-generic.so',
           behavior = 'SaintVenantKirchhoffElasticity')
manta.info(b)
```

The brick automatically uses those pieces of information during the dependency
management algorithm. If a requirement of the behavior is not fullfilled,
the simulation can't be run, as expected. But the brick, is also a
provider of the internal state variables that are available for other
models, post-processings, etc.

Section [Advices on the management of MFront material knowledge](miscellaneous/mfront_material_knowledge_management.md#mfront-material-knowledge-management) for details provides
some advices on management of material knowledge implemented using
MFront.

Note

As shown in the JSON version, the bricks could have been created by
passing appropriate arguments when generating the model. For example,
the following code is valid and replaces the lines defining the bricks:

PYTHON

```python
    mm = manta.Model('ImplicitMechanics', ps,
                     bricks = [{'ImplicitMechanicsSolidMaterial': {'material': 'cube',
                                                                   'library': './libHyperElasticityBehaviours-generic.so',
                                                                   'behavior': 'SaintVenantKirchhoffElasticity'}},
                               {'ImposedDisplacement': {'boundary': 'left', 'component': 'UX'}},
                               {'ImposedDisplacement': {'boundary': 'rear', 'component': 'UY'}},
                               {'ImposedDisplacement': {'boundary': 'bottom', 'component': 'UZ'}},
                               {'ImposedDisplacement': {'boundary': 'top', 'component': 'UZ',
                                                        'value': 'ImposedDisplacementValue'}}
                     ])
```

C++

```c++
  auto mm = ModelFactory::get().create(
      ctx,
      "ImplicitMechanics",
      *ps,
      Parameters{
          {"bricks",
           Vector<Parameters>{Parameters{{"ImplicitMechanicsSolidMaterial",
                                          Parameters{{"domain", "cube"},
                                                     {"library", "./libHyperElasticityBehaviours-generic.so"},
                                                     {"behavior", "SaintVenantKirchhoffElasticity"}}}},
                              Parameters{{"ImposedDisplacement", Parameters{{"boundary", "left"}, {"component", "UX"}}}},
                              Parameters{{"ImposedDisplacement", Parameters{{"boundary", "rear"}, {"component", "UY"}}}},
                              Parameters{{"ImposedDisplacement", Parameters{{"boundary", "bottom"}, {"component", "UZ"}}}},
                              Parameters{{"ImposedDisplacement",
                                          Parameters{{"boundary", "right"},
                                                     {"component", "UX"},
                                                     {"value", "ImposedDisplacementValue"},
                                                     {"strategy", "elimination"}}}}}}});
```

Of course, the C++ version is must more convoluted due to the limitations
of the language (no built-in supports for `list` and `dictionary`).

It is worth noting that all the parameters describing the model could
have been read from a JSON file, allowing a mixed approach between
pure scripts and an approach based on input files. Such mix could be
interesting to define the materials for instance.

It is also worth noting that one can define part of the bricks
in the constructor and complete their description later.

### Properties

The Young's modulus and the Poisson's ratio are defined using properties
(see Section [Properties](properties.md#properties)):

PYTHON

```python
    for n, v in {'YoungModulus': 150e9, 'PoissonRatio': 0.3}.items():
        ps.addProperty('Constant',
                       material =  'cube',
                       name = n,
                       value = v)
```

C++

```c++
                                                    {"PoissonRatio", 0.3}}) {
    ps->addProperty(ctx,
                    "Constant",    //
                    Parameters{{"material", "cube"}, {"name", n}, {"value", v}});
  }
  ps->addLoading(ctx,
```

JSON

```json
    "properties": [
      {
        "Constant": {
          "name": "YoungModulus",
          "material": "cube",
          "value": 150000000000
        }
      },
      {
        "Constant": {
          "name": "PoissonRatio",
          "material": "cube",
          "value": 0.3
        }
      }
    ],
```

Several properties are available, see the only documentation for a
complete list:

PYTHON

```python
manta.info('Properties')
```

SH

```sh
manta-info Properties
```

In particular, the `MFront` property allows to used material
properties generated by [MFront](https://thelfer.github.io/tfel/web/index.html). Those material
properties can have an arbitrary numbers of variables.

Properties can also be defined directly by functions of one or two
variables in Python or C++ although this strategy is discouraged in
favour of material properties. See Section
[Advices on the management of MFront material knowledge](miscellaneous/mfront_material_knowledge_management.md#mfront-material-knowledge-management) for details.

### Loadings

Two loadings are defined in this example, associated respectively to the
temperature and the imposed displacement:

PYTHON

```python
    ps.addLoading('ConstantUniformScalar',
	          material = 'cube',
                  name = 'Temperature',
                  value = 293.15)

    umax = 1e-2
    ps.addLoadingEvolution('ImposedDisplacementValue', lambda t: umax * t)
```

C++

```c++
                 "ConstantUniformScalar",    //
                 Parameters{{"material", "cube"}, {"name", "Temperature"}, {"value", 293.15}});
  //
  ps->addLoadingEvolution(ctx, "ImposedDisplacementValue", [](const Real t) noexcept {
    constexpr auto umax = Real{1e-3};
    return umax * t;
  });
  //
```

JSON

```json
    "loadings": [
      {
        "ConstantUniformScalar": {
          "material": "cube",
          "name": "Temperature",
          "value": 293.15
        }
      }
    ],
    "loadingEvolutions": [
      {
        "Table": {
          "name": "ImposedDisplacementValue",
          "interpolationType": "linear",
          "abscissae": [
            0,
            1
          ],
          "ordinates": [
            0,
            0.01
          ]
        }
      }
    ]
```

### Coupling scheme

The coupling scheme is a central concept in MANTA to describe
multi-physics problems using a staggered approach. This concept will be
described in depths in more advanced tutorials.

In this example, only one physical model is considered, so a suitable
coupling scheme boils down to calling this model once per time step. The
`setModel` method sets up such simple scheme:

PYTHON

```python
    ps.setModel(mm)
```

C++

```c++
  ps->initialize(ctx);
```

JSON

```JSON
    "model": {
      "ImplicitMechanics": {
        "bricks": [
          {
            "ImplicitMechanicsSolidMaterial": {
              "material": "cube",
              "library": "./libHyperElasticityBehaviours-generic.so",
              "behavior": "SaintVenantKirchhoffElasticity"
            }
          },
          {
            "ImposedDisplacement": {
              "boundary": "left",
              "component": "UX"
            }
          },
          {
            "ImposedDisplacement": {
              "boundary": "rear",
              "component": "UY"
            }
          },
          {
            "ImposedDisplacement": {
              "boundary": "bottom",
              "component": "UZ"
            }
          },
          {
            "ImposedDisplacement": {
              "boundary": "top",
              "component": "UZ",
              "value": "ImposedDisplacementValue"
            }
          }
        ]
      }
    },
```

Note

The setModel method is indeed equivalent to the following code:

```python
c = manta.CouplingScheme('LoopCouplingScheme', ps,
                         numberOfIterations = 1)
c.add(mm)
ps.setCouplingScheme(c)
```

### The simulation

The simulation is declared and run as follows:

PYTHON

```python
    nIncr = 20
    dt = 1 / nIncr
    s = manta.Simulation(ps, times = [i * dt for i in range(0, 21)])
    s.run()
```

C++

```c++
  auto s = construct<Simulation>(ctx, *ps, Simulation::TimesDescription{0, 1, 20});
  s->run(ctx);
```

JSON

```json
  "simulations": [
    {
      "times": [
        0,
        0.5,
        1
      ]
    }
  ]
```

In JSON, we declare several simulations in an array, each
simulations having its own sets of numerical parameters. Those
simulations will be run one after the other.

See also

The list of parameters (and their descriptions) of the `Simulation`
class is accessible in `python` through the `manta.info`
function or through the `manta-info` utility (see Section
[The manta-info utility](miscellaneous/tools.md#manta-info-utility)).

PYTHON

```python
manta.info('Main concepts', 'Simulation')
```

SH

```sh
manta-info "Main concepts:Simulation"
```

### Running the Simulation

Test case location

The test case can be found at:

[<MANTA REPO>/verification_tests/manta_frontend_integration_tests/frontend_doc_verification/](https://gitlab.com/manta-project/manta/-/tree/master/verification_tests/manta_frontend_integration_tests/frontend_doc_verification/)

The files required to run this simulation (with json, c++ and python) can be downloaded on the link cited above. The following instructions must be run
in the directory where those files are downloaded.

#### Compiling the MFront behavior

The MFront behavior can be compiled as follows:

```sh
mfront --obuild --interface=generic SaintVenantKirchhoffElasticity.mfront
ln -s src/libBehaviour.so libHyperElasticityBehaviours-generic.so
```

#### Running the Python version

```sh
python uniaxial_tensile_test.py
```

#### Running the JSON version

```sh
manta uniaxial_tensile_test.json
```

#### Compiling and running the C++ version

```sh
mkdir build
cd build
cmake ../ -DCMAKE_BUILD_TYPE=Release -DMANTA_INSTALL_DIR=....
make
./UniaxialTensileTest
```
