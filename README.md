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

## How its done

The program takes in a set of parameters through the command line, each with a
key and a value. Each key will affect the output of the program, for example:

`i:40 v:12 eff:1 rpm:6000`

Here, we have specified the following:

- `i`: The applied current
- `v`: The applied voltage
- `eff`: The efficiency of the motor
- `rpm`: The RPM of the motor

These will be run through a set of equations and formulae according to the target.
If the target cannot be calculated due to a lack of data, the program will not generate any meaningful output. \

The output will be resolved in one of two ways:

- A pretty-printed data table (Default behavior)
- A terse output ordered per specified target (`--terse / -t`)

Examples using the above command: \
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
python m_out_main.py TGT:PO#1 EFRV:5600rpm G1:12/1 G2:3/4 EFF:80% IV:11.6V IC:10A PF:0.75 # and so-on...
```

You may pipe file contents.

```sh
# Example
cat motor_config.txt | python m_out_main.py -
```

To understand how to format the input, please refer to the documentation which
can be accessed through invoking the program with the `--help`/`-h` flag, or by
reading the GitHub Wiki (Not available yet).

## License

See LICENSE file.

