def get():
    puzzleInput = []
    with open('inputs.txt', 'r') as f:
        lines = f.readlines()
        puzzleInput = [line.strip() for line in lines]
    return puzzleInput

