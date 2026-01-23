import alg

def game():
    inp = input("Please enter a move: ")
    inp = list(inp)
    x,y = inp[0].lower(), int(inp[1])
    if 'a' <= x <= 'h':
        x = (ord(x) - ord('a') + 1)

    if alg.getLegalMoves((x,y))
    print(move)