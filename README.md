# Motor Output Calculator

When dealing with motors, one usually pays special attention to concepts
such as output free-running/stall torque and possible velocity. These factors
are determined by input factors such as voltage and current. Applied
output modifiers such as gearing may also affect the resultant motor output
values.

This program models a motor's theoretical behavior based on the given parameters
in such a way that it allows for quick testing and easy calculation of target
values.

For now, **I do not promote the use of this program for real engineering work.**

If you're curious and wish to acquire more information on the topic,
I invite the reader to check out the following Wikipedia
articles: [Torque](https://en.wikipedia.org/wiki/Torque),
[Motor Constants](https://en.wikipedia.org/wiki/Motor_constants)

## How it's done

The program takes in a set of parameters through the command line, each with a
key and a value. These are the motor's properties. Each key will affect the output of the program, for example:

`i:40 v:12 eff:1 rpm:6000`

Here, we have specified the following:

- `i`: The applied current
- `v`: The applied voltage
- `eff`: The efficiency of the motor
- `rpm`: The RPM of the motor

These will be run through a set of equations and formulae which model the behavior of a motor and it's properties.
If any properties cannot be calculated due to a lack of data, the program will simply not calculate them.

The output will be resolved in one of two ways:

- A pretty-printed data table (Default behavior)
- A terse output separated by an equals sign and padding spaces.
  This format may facilitate shell parsing or other kinds of parsing (`--terse / -t`)

Examples using the above command: \
\
**Pretty print**

```
┌──────────────────────────────────┬──────────┐
│ Input Current (A)                │ 40.0     │
├──────────────────────────────────┼──────────┤
│ Input Voltage (V)                │ 12.0     │
├──────────────────────────────────┼──────────┤
│ Efficiency (0-1)                 │ 1.0      │
├──────────────────────────────────┼──────────┤
│ Revolutions per Minute (rev/min) │ 6000.0   │
├──────────────────────────────────┼──────────┤
│ Mechanical Power Input (W)       │ 480.0    │
├──────────────────────────────────┼──────────┤
│ Angular Velocity (rad/s)         │ 628.3185 │
├──────────────────────────────────┼──────────┤
│ Input Resistance (R)             │ 0.3      │
├──────────────────────────────────┼──────────┤
│ Mechanical Power Output (W)      │ 480.0    │
├──────────────────────────────────┼──────────┤
│ Output Torque (Nm)               │ 0.7639   │
└──────────────────────────────────┴──────────┘
```

**Terse print**

```
Input Current (A)                = 40.0    
Input Voltage (V)                = 12.0    
Efficiency (0-1)                 = 1.0     
Revolutions per Minute (rev/min) = 6000.0  
Mechanical Power Input (W)       = 480.0   
Angular Velocity (rad/s)         = 628.3185
Input Resistance (R)             = 0.3     
Mechanical Power Output (W)      = 480.0   
Output Torque (Nm)               = 0.7639  
```

## Usage

### Running the program

Invoke the script through the use of a python interpreter. Pass the desired
parameters and configurations through the command line.

```sh
# Example
python main.py i:40 v:12 eff:1 rpm:6000
```

To query available keys, please refer to the property registry which
can be accessed through invoking the program with the `--show-props` flag.

```sh
# Query properties
python main.py --show-props
```

## Requisite: Module Reference

The following python modules were used in the creation of this program:

- [logging](https://docs.python.org/3/library/logging.html): used to create diagnostic messages on wrong inputs
- [argparse](https://docs.python.org/3/library/argparse.html): used to parse command line parameters
- [inspect](https://docs.python.org/3/library/inspect.html): used to extract the signature of generic lambdas used to
  perform per-requisite calculations
- [re](https://docs.python.org/3/library/re.html): used to correctly identity floating point numbers instead of using
  `isnumeric`

## License

See LICENSE file.

