<!-- source: c3po/exchangeMethods/ExchangeMethod.py -->

# `c3po.exchangeMethods.ExchangeMethod`

Contain the class `ExchangeMethod`.

### `class c3po.exchangeMethods.ExchangeMethod.ExchangeMethod  — bases: object`

`ExchangeMethod` is a class interface (to be implemented) which standardizes exchange methods to be used with `LocalExchanger`.

See `c3po.LocalExchanger.LocalExchanger.__init__`.

#### `ExchangeMethod.getPatterns(self)`

Return a list of patterns.

A pattern is a tuple of 4 integers. They are related respectively to the number of fields to get, fields to set, values to get and values to set with the `__call__` method.

Patterns indicate dependencies of the exchange method and is used to check for proper use of the object, and for optimizations.

For example, for an `ExchangeMethod` with the patterns: `[(1,1,0,0), (0,0,1,1)]`, a call with 3 fields to set, 3 fields to get, 2 values to get (that would provide 2 values to set) could be replace by 5 calls: 3 with 1 field to get and 1 field to set, plus 2 with 1 value to get (that would provide 1 value to set). On the other hand, this `ExchangeMethod` could not be called with 0 field to get, 1 field to set and 1 value to get.

The order of the pattern list is used as a priority order.

A negative value can be used to mean that the number of required elements is not known. All elements of this kind are required for this pattern, but they will not be available for the following ones.

#### `ExchangeMethod.clean(self)`

Clean up internal variables used to speed up data exchange under the assumption that meshes do not vary.

<div class="note">

<div class="title">

Note

</div>

The method is usually called by the `c3po.Exchanger` object that holds `self`.

</div>
