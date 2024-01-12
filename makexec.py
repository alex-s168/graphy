import sys


def makeexec(exprparsed, globals):
    parsedName = exprparsed[0]
    parsedArgs = exprparsed[1]
    parsedIsConstant = exprparsed[2]
    parsedCode = exprparsed[3]

    if parsedName in globals:
        print("Duplicate name", parsedName)
        sys.exit(1)

    if parsedIsConstant:
        val = eval(parsedCode, globals, {})
        return val, True, []
    else:
        def call(*args: object) -> object | None:
            argdict = {}
            if len(args) != len(parsedArgs):
                print("Incorrect number of arguments! Expected", len(parsedArgs), "received", len(args))
                sys.exit(1)
            for i, arg in enumerate(args):
                argK = parsedArgs[i]
                argdict[argK] = arg

            return eval(parsedCode, globals, argdict)

        return call, False, parsedArgs
