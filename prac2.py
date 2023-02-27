n = []
res = []
def generate_par(left:int, right:int, range_:int) -> None:

    if left == right == range_:
        n.append("".join(res))
        return
    if left < range_:
        res.append("(")
        generate_par(left+1,right,range_)
        res.pop()

    if left > right:
        res.append(")")
        generate_par(left,right+1,range_)
        res.pop()
        


range_ = int(input("Enter the the number of parenthesis : ").strip())
generate_par(0,0,range_)
print(n)
