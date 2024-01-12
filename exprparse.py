from sympy.parsing.sympy_parser import (parse_expr,
                                        standard_transformations,
                                        convert_xor)

transformations = (standard_transformations + (convert_xor,))


def exprParse(exp: str):
    parts = exp.split('=', 1)
    args = []
    name = "expression"
    constant = False
    if len(parts) == 2:
        p1 = parts[0]
        p2 = p1.split("(")
        name = p2[0].strip()
        if len(p2) == 2:
            p3 = p2[1].split(")")[0]
            args = p3.replace(" ", "").split(",")
        else:
            constant = True
    expr = compile(str(parse_expr(parts[-1],
                                  transformations=transformations, evaluate=False)),
                   "<expression>", "eval")
    return [name, args, constant, expr]