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

For more information on the topic, I invite you to see the following Wikipedia
articles: [Torque](https://en.wikipedia.org/wiki/Torque),
[Motor Constants](https://en.wikipedia.org/wiki/Motor_constants)

## Usage

### Running the program
Invoke the script through the use of a python interpreter. Pass the desired
parameters and configurations through the command line.

```sh
# Calculate the power output of a motor whose shaft has a gearing of 9:1.
# Its nominal voltage is 12.0V but only receives 11.6V.
# Usual power output of this motor is 380 Watts at 40 Amperes
# And more...
python m-out.py TGT:PO EFRV:5600rpm G1:12/1 G2:3/4 NV:12.0V IV:11.6V PO1:380W@40A # and so-on...
```

To understand how to format the input, please refer to the documentation which
can be accessed through invoking the program with the `--help`/`-h` flag, or by
reading the GitHub Wiki (Not available yet).

## License
See LICENSE file.

