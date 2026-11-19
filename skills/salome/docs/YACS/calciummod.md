<!-- source: https://docs.salome-platform.org/latest/gui/YACS/calciummod.html -->

# [`calcium`](#module-calcium) – python interface

calcium python module provides all is needed to connect to YACS and exchange data between coupled components.

Presentation is done in the following order:

- constants
- array types
- functions to connect and disconnect
- functions to export data
- functions to import data
- functions to erase data
- example

## Constants

The constants defined in this module are:

calcium.CP_TEMPS
:   This constant is used in cp_e* and cp_l* calls to indicate that data are associated to a time step.

calcium.CP_ITERATION
:   This constant is used in cp_e* and cp_l* calls to indicate that data are associated to an iteration number.

calcium.CP_SEQUENTIEL
:   This constant is used in cp_l* calls to indicate that the call requests the next data that has been produced.

calcium.CP_CONT
:   This constant can be used in cp_fin to indicate that variables produced by the component are defined
    beyond the last time or iteration number and their value is equal to the last value produced.

calcium.CP_ARRET
:   This constant can be used in cp_fin to indicate that variables produced by the component are not defined
    beyond the last time or iteration number.

and all the error codes as listed in [Error codes](calciumapi.md#errcodes).

## Array types

numpy arrays can be used to export or import data but if the numpy module is not installed
calcium provides simple array types to replace them.

*class* calcium.intArray(*nelem*)
:   The constructor takes a single argument which is the number of elements of the array

*class* calcium.longArray(*nelem*)
:   The constructor takes a single argument which is the number of elements of the array

*class* calcium.floatArray(*nelem*)
:   The constructor takes a single argument which is the number of elements of the array

*class* calcium.doubleArray(*nelem*)
:   The constructor takes a single argument which is the number of elements of the array

*class* calcium.stringArray(*nelem*, *eltsize*)
:   The constructor takes two arguments: the number of elements of the array and the size
    of the elements (strings)

## Functions to connect and disconnect

calcium.cp_cd(*compo*) → info, name
:   Initialize the connection with YACS.

    Parameters:
    :   - **compo** (*SALOME component object*) – component reference
        - **info** (*int*) – error code
        - **name** (*string*) – instance name given by YACS

calcium.cp_fin(*compo*, *directive*) → info
:   Close the connection with YACS.

    Parameters:
    :   - **compo** (*SALOME component object*) – component reference
        - **directive** (*int*) – indicate how variables will be handled after disconnection. If directive = CP_CONT,
          variables produced by this component are defined constant beyond the last time or iteration number. If
          directive = CP_ARRET, variables are not defined beyond the last step.
        - **info** (*int*) – error code

## Functions to export data

calcium.cp_ere(*compo*, *dep*, *t*, *i*, *nm_var*, *n*, *var_real*) → info

calcium.cp_edb(*compo*, *dep*, *t*, *i*, *nm_var*, *n*, *var_double*) → info

calcium.cp_ecp(*compo*, *dep*, *t*, *i*, *nm_var*, *n*, *var_complex*) → info

calcium.cp_een(*compo*, *dep*, *t*, *i*, *nm_var*, *n*, *var_integer*) → info

calcium.cp_elg(*compo*, *dep*, *t*, *i*, *nm_var*, *n*, *var_long*) → info

calcium.cp_eln(*compo*, *dep*, *t*, *i*, *nm_var*, *n*, *var_long*) → info

calcium.cp_elo(*compo*, *dep*, *t*, *i*, *nm_var*, *n*, *var_boolean*) → info

calcium.cp_ech(*compo*, *dep*, *t*, *i*, *nm_var*, *n*, *var_string*) → info
:   Parameters:
    :   - **compo** (*SALOME component object*) – component reference
        - **dep** (*int*) – dependency mode (calcium.CP_TEMPS, calcium.CP_ITERATION)
        - **t** (*float*) – export time if mode=calcium.CP_TEMPS
        - **i** (*int*) – export iteration number if mode=calcium.CP_ITERATION
        - **nm_var** (*string*) – port name
        - **n** (*int*) – number of values to export
        - **var_real** (float numpy array or [`calcium.floatArray`](#calcium.calcium.floatArray)) – array containing float values to export
        - **var_double** (double numpy array or [`calcium.doubleArray`](#calcium.calcium.doubleArray)) – array containing double values to export
        - **var_complex** (complex numpy array or [`calcium.floatArray`](#calcium.calcium.floatArray) (double size)) – array containing complex values to export
        - **var_integer** (integer numpy array or [`calcium.intArray`](#calcium.calcium.intArray)) – array containing integer values to export
        - **var_long** (long numpy array or [`calcium.longArray`](#calcium.calcium.longArray)) – array containing long values to export
        - **var_boolean** (integer numpy array or [`calcium.intArray`](#calcium.calcium.intArray)) – array containing boolean values to export
        - **var_string** (string numpy array or [`calcium.stringArray`](#calcium.calcium.stringArray)) – array containing string values to export
        - **info** (*int*) – error code

With numpy, the data types to use when creating the array, are the following:

| Request | numpy data type |
| --- | --- |
| cp_lre | ‘f’ |
| cp_ldb | ‘d’ |
| cp_lcp | ‘F’ |
| cp_len | ‘i’ |
| cp_llg | ‘l’ |
| cp_lln | ‘l’ |
| cp_llo | ‘i’ |
| cp_lch | ‘Sxx’ |

Note

For cp_lch xx is the size of the element string

## Functions to import data

calcium.cp_lre(*compo*, *dep*, *ti*, *tf*, *i*, *nm_var*, *len*, *var_real*) → info, t, ii, n

calcium.cp_ldb(*compo*, *dep*, *ti*, *tf*, *i*, *nm_var*, *len*, *var_double*) → info, t, ii, n

calcium.cp_lcp(*compo*, *dep*, *ti*, *tf*, *i*, *nm_var*, *len*, *var_complex*) → info, t, ii, n

calcium.cp_len(*compo*, *dep*, *ti*, *tf*, *i*, *nm_var*, *len*, *var_integer*) → info, t, ii, n

calcium.cp_llg(*compo*, *dep*, *ti*, *tf*, *i*, *nm_var*, *len*, *var_long*) → info, t, ii, n

calcium.cp_lln(*compo*, *dep*, *ti*, *tf*, *i*, *nm_var*, *len*, *var_long*) → info, t, ii, n

calcium.cp_llo(*compo*, *dep*, *ti*, *tf*, *i*, *nm_var*, *len*, *var_boolean*) → info, t, ii, n

calcium.cp_lch(*compo*, *dep*, *ti*, *tf*, *i*, *nm_var*, *len*, *var_string*) → info, t, ii, n
:   Parameters:
    :   - **compo** (*SALOME component object*) – component reference
        - **dep** (*int*) – dependency mode (calcium.CP_TEMPS, calcium.CP_ITERATION or calcium.CP_SEQUENTIEL)
        - **ti** (*float*) – interval start time
        - **tf** (*float*) – interval end time
        - **i** (*int*) – iteration number
        - **nm_var** (*string*) – port name
        - **len** (*int*) – number of values to import
        - **var_real** (float numpy array or [`calcium.floatArray`](#calcium.calcium.floatArray)) – array to store imported float values (must be large enough to contain imported values)
        - **var_double** (double numpy array or [`calcium.doubleArray`](#calcium.calcium.doubleArray)) – array to store imported double values
        - **var_complex** (complex numpy array or [`calcium.floatArray`](#calcium.calcium.floatArray) (double size)) – array to store imported complex values
        - **var_integer** (integer numpy array or [`calcium.intArray`](#calcium.calcium.intArray)) – array to store imported integer values
        - **var_long** (long numpy array or [`calcium.longArray`](#calcium.calcium.longArray)) – array to store imported long values
        - **var_boolean** (integer numpy array or [`calcium.intArray`](#calcium.calcium.intArray)) – array to store imported boolean values
        - **var_string** (string numpy array or [`calcium.stringArray`](#calcium.calcium.stringArray)) – array to store imported string values
        - **info** (*int*) – error code
        - **t** (*float*) – effective time if mode=calcium.CP_TEMPS or associated time if mode=calcium.CP_SEQUENTIEL
        - **ii** (*int*) – associated iteration number if mode=calcium.CP_SEQUENTIEL
        - **n** (*int*) – effective number of imported values (<= len)

## Functions to erase data

The functions cp_fini and cp_fint are used to request that all values of the specified
variable defined for iteration number or time before a given one be erased.

The functions cp_effi and cp_efft are used to request that all values of the specified
variable defined for iteration number or time after a given one be erased.

calcium.cp_fini(*compo*, *nm_var*, *i*) → info
:   Erase all values of port nm_var before iteration i

    Parameters:
    :   - **compo** (*SALOME component object*) – component reference
        - **nm_var** (*string*) – port name
        - **i** (*int*) – iteration number
        - **info** (*int**,* *return*) – error code

calcium.cp_fint(*compo*, *nm_var*, *t*) → info
:   Erase all values of port nm_var before time t

    Parameters:
    :   - **compo** (*SALOME component object*) – component reference
        - **nm_var** (*string*) – port name
        - **t** (*float*) – time
        - **info** (*int**,* *return*) – error code

calcium.cp_effi(*compo*, *nm_var*, *i*) → info
:   Erase all values of port nm_var after iteration i

    Parameters:
    :   - **compo** (*SALOME component object*) – component reference
        - **nm_var** (*string*) – port name
        - **i** (*int*) – iteration number
        - **info** (*int**,* *return*) – error code

calcium.cp_efft(*compo*, *nm_var*, *t*) → info
:   Erase all values of port nm_var after time t

    Parameters:
    :   - **compo** (*SALOME component object*) – component reference
        - **nm_var** (*string*) – port name
        - **t** (*float*) – time
        - **info** (*int**,* *return*) – error code

## Example

If you want to export a double precision real array and import an integer array in time mode,
you could write a function as follows. Connection and disconnection must be done only once.

```numpy
import calcium
import numpy

def coupling(compo):
  # connect to YACS
  info, name = calcium.cp_cd(compo)
  # export 10 double values at time 0. on port outa
  af=numpy.zeros(10,'d')
  af[0]=4.3
  info = calcium.cp_edb(compo,calcium.CP_TEMPS,0.,0,"outa",10,af);
  tf=1.;
  # import 10 integer values at interval time (0.,1.) on port ina
  # (by default it is imported at the start time 0.)
  ai=numpy.zeros(10,'i')
  info,t,i,n = calcium.cp_len(compo,calcium.CP_TEMPS,0., 1.,0,"ina",10,ai);
  # disconnect
  info = calcium.cp_fin(compo,calcium.CP_CONT);
```
