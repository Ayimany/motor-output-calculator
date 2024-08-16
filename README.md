# Motor Output Calculator
When dealing with motors, one usually pays special attention to concepts
such as output free-running/stall torque and possible velocity. These factors
are often affected by input factors such as voltage and current. Applied
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

## How its done

The program takes in a set of parameters through the command line, each with a
key and a value. Each key will affect the output of the program, for example:

`TGT:PO#3 IC:25A EFF:90% PF:0.9 IV:11.6`

Here, we have specified the following:
- `TGT`: The target value which we want to calculate (3 Phase Power Output)
- `EFF`: The motor's efficiency
- `PF`: The power factor
- `IC`: The input current
- `IV`: The input voltage

These will be run through a set of equations and formulae accoring to the target.
If the target cannot be calculated due to a lack of data, the program will not generate any output. \

The output will be resolved in one of two ways:
- A pretty-printed data table (Default behavior)
- A terse output ordered per specified target (`--terse / -t`)

Examples using the above command: \
**Pretty print**
```
┌────────────────────────┬──────────┐
│ Target                 │ Value    │
├────────────────────────┼──────────┤
│ Power Output (3 Phase) │ 0.421 kW │
└────────────────────────┴──────────┘
```

**Terse print**
```
0.421 kW
```

## Usage

### Running the program
Invoke the script through the use of a python interpreter. Pass the desired
parameters and configurations through the command line.

```sh
# Example
python m-out.py TGT:PO#1 EFRV:5600rpm G1:12/1 G2:3/4 EFF:80% IV:11.6V IC:10A PF:0.75 # and so-on...
```

You may pipe file contents.

```sh
# Example
cat motor_config.txt | python m-out.py -
```

To understand how to format the input, please refer to the documentation which
can be accessed through invoking the program with the `--help`/`-h` flag, or by
reading the GitHub Wiki (Not available yet).

## License
See LICENSE file.

