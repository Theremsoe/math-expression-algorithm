def MathChallenge(strParam: str):
    size = len(strParam)
    j = 0
    p = -1
    k = 0

    exp = strParam

    if exp[0] == "-":
        exp = f"0{exp}"

    while j < size:
        if exp[j] == "(":
            if p == -1:
                p = j

            k += 1
        if exp[j] == ")":
            k -= 1

            if k == 0:
                result = MathChallenge(exp[p + 1 : j])
                return MathChallenge(f"{exp[:p]}{result}{exp[j + 1 :]}")

        j += 1

    """
    """
    if k != 0:
        raise ValueError("Invalid math expression")

    """
    Resolve divisions/multiplications
    """
    return resolution(resolution(exp, ["*", "/"]), ["+", "-"])


def resolution(exp: str, operands: list[str]) -> str:
    size = len(exp)
    k = 0
    l = 0
    r = 0
    op = -1

    while k < size:
        if (not exp[k].isdigit() and exp[k - 1].isdigit()) or k == size - 1:
            r = k if k == size - 1 else k - 1

            if l < op and op < r:
                if exp[op] in operands:
                    result = resolveOperation(exp[l:op], exp[op], exp[op + 1 : r + 1])

                    if k == size - 1:
                        return f"{exp[:l]}{result}"

                    return resolution(f"{exp[:l]}{result}{exp[r + 1:]}", operands)

                else:
                    l = op + 1
            op = k

        k += 1

    return exp


def resolveOperation(left: str, op: str, right: str) -> str:
    int_left = int(left)
    int_right = int(right)

    if op == "*":
        return str(int_left * int_right)

    if op == "/":
        return str(int_left // int_right)

    if op == "-":
        int_right *= -1

    return str(int_left + int_right)


assert MathChallenge("6-(1-2)") == "7"
assert MathChallenge("-9+3") == "-6"
assert MathChallenge("6*(4/2)+3*1") == "15"
assert MathChallenge("6/3-1") == "1"
