import math
import sys
import matplotlib.pyplot as plt

from exprparse import exprParse
from makexec import makeexec
from section_ffm import parse as parse_section_ffm
from data_ffm import parse as parse_data_ffm

graphFile = ""
if len(sys.argv) > 1:
    with open(sys.argv[1], "r") as f:
        graphFile = f.read()
else:
    print("No graph file path was provided as an argument. Graph data (content):")
    graphFile = sys.stdin.read()

graphFile = graphFile.splitlines()
graphFileSections = parse_section_ffm(graphFile)

if "graphs" not in graphFileSections:
    print("No graph configs are in the graph file!", flush=False)
    print("Add the [graph] section to the graph file and provide graph data!")
    sys.exit(1)

if "code" not in graphFileSections:
    print("There are no functions to draw!", flush=False)
    print("Add the [code] section to the graph file and provide graph data!")
    sys.exit(1)

# dict<name, <constantValue / functionObject, isConstant, functionArguments?>>
decl = {}
declPass = {
    # constants
    "pi": math.pi,
    "tau": math.tau,
    "e": math.e,

    # functions
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "sqrt": math.sqrt,
    "exp": math.exp,
    "log": math.log,
    "log2": math.log2,
    "sinh": math.sinh,
    "cosh": math.cosh,
    "tanh": math.tanh,
    "asinh": math.asinh,
    "atanh": math.atanh,
}

for line in graphFileSections["code"].splitlines():
    if len(line.strip()) == 0:
        continue

    parsed = exprParse(line)
    parsedName = parsed[0]

    v = makeexec(parsed, declPass)

    decl[parsedName] = v
    declPass[parsedName] = v[0]

graphs = parse_data_ffm(graphFileSections["graphs"].splitlines())

plt.rcParams["figure.autolayout"] = True

print(f"Plotting {len(graphs)} graph(s)...")

for graph in graphs:
    fn = graph["function"]
    if fn not in decl:
        print(f"Function {fn} not defined!")
        sys.exit(1)

    f = decl[fn]
    if f[1]:
        print(f"Provided {fn} is not a function (is a constant)!)")
        sys.exit(1)

    if len(f[2]) != 1:
        print(f"Provided {fn} needs to have exactly one argument!")
        sys.exit(1)

    fptr = f[0]

    width = int(graph["width"])
    step = float(graph["step"])
    color = graph["color"]
    axis = graph["axis"]
    alpha = float(graph["alpha"]) if "alpha" in graph else 1.0
    label = graph["label"] if "label" in graph else None

    dx: list[float]
    dy: list[float]

    if axis == "x":
        dx = [fptr(i / step) for i in range(int(width * step))]
        dy = [i / step for i in range(int(width * step))]
    elif axis == "y":
        dx = [i / step for i in range(int(width * step))]
        dy = [fptr(i / step) for i in range(int(width * step))]
    else:
        print("Invalid axis!")
        sys.exit(1)

    plt.plot(dx, dy, color=color, alpha=alpha, label=label)

plt.legend()
plt.show()

print("Done!")