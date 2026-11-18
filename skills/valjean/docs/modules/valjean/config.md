<!-- source: modules/valjean/config.rst -->

# `config` — Configuration object

`Config` objects encapsulate a set of configuration options for a `valjean` run. Here is how you create one:

> \>\>\> from valjean.config import Config \>\>\> config = Config()

By default, `Config` objects come with a `'path'` configuration section, which may be used to set default values for any configuration option. A few options are set from the beginning:

> \>\>\> for opt, val in sorted(config\['path'\].items()): ... print(f'{opt} = {val}') log-root = /.../log output-root = /.../output report-root = /.../report

The `Config` class behaves like a simple dictionary:

> \>\>\> print(config.query('path', 'report-root')) /.../report

## Module API

### `class valjean.config.Config(dictionary=None)  — bases: MutableMapping`

The base configuration class for `valjean`.

#### `Config.from_file(cls, path)`

Construct a configuration object from a TOML file.

param path  
A path for the configuration file.

type path  
pathlib.Path or str

#### `Config.query(self, section, option)`

Return the value of `option` from `section`.

#### `Config.set(self, section, option, value)`

Set the value of `option` in `section` to be `value`.
