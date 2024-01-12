# Graphy
Simple Python library that uses `matplotlib` and `sympy` to visualize 1-D functions (2-D graphs)

## Usage
Execute `main.py` with the path of a `.graph` file as argument.

## ".graph" file format
A `.graph` file consists of two sections:
```
[code]
    # mathematical functions
[graphs]
    # graph configs
```

Comments are declared using `#`.

### "code" section
The code section consists of multiple lines of statements.

There are two different kinds of statements. Constants and functions.

You can declare constants like this: `name = expression`

and functions like this: `name(arguments) = expression`.

### "graphs" section
The graphs config section consists of csv-like data.

The first line is the header. This is used for indexing.
All lines after are all the graphs.

Data:

| header name | required | description                                | possible values |
|-------------|----------|--------------------------------------------|-----------------|
| function    | x        | the name of the function to display        | string          |
| width       | x        | the width of the graph                     | integer         |
| step        | x        | how many calculations to perform per point | float           |
| axis        | x        | on which axis to draw the grapj            | `x`, `y`        |
| color       | x        | the color of the graph                     | string          |
| alpha       |          | the alpha value of the graph               | float           |
| label       |          | the name of the graph                      | string          |

## Expressions
(There is way too much to document how they work exactly)

They are mostly like python expressions with the exception that instead of `x ** y`, you write `x^y`.

## Built-in functions and constants
### Constants
- `pi`
- `e`
- `tau`
### Functions
- `sin`
- `cos`
- `tan`
- `asin`
- `acos`
- `atan`
- `sqrt`
- `exp`
- `log`
- `log2`
- `sinh`
- `cosh`
- `tanh`
- `asinh`
- `atanh`