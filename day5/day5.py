import numpy as np

def read_input_file(file_name):
    try:
        with open(file_name, 'r') as f:
            lines = f.readlines()
            return [[int(elem) for elem in line.replace("->", ",").split(",")] for line in lines]
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
        return []

def create_board(lines):
    board = np.zeros((1000, 1000))
    for x1, y1, x2, y2 in lines:
        if y1 == y2:
            board[y1, min(x1,x2):max(x1,x2) + 1] += 1
        elif x1 == x2:
            board[min(y1,y2):max(y1,y2) + 1, x1] += 1   
        elif abs(y1 - y2) == abs(x1 - x2):
            start = min((x1,y1),(x2,y2), key=lambda x: x[0])
            end = max((x1,y1),(x2,y2), key=lambda x: x[0])
            for i in range(abs(x1-x2)+1):
                board[start[1]+(i*np.sign(end[1]-start[1])), start[0]+(i*np.sign(end[0]-start[0]))] += 1 
    return board

def count_overlap(board):
    max_overlap = int(np.amax(board))
    overlap_count = np.count_nonzero(board > 1)
    return max_overlap, overlap_count

def main():
    input_lines = read_input_file("inputs.txt")
    board = create_board(input_lines)
    max_overlap, overlap_count = count_overlap(board)
    print(f"Max overlap: {max_overlap}")
    print(f"Overlap count: {overlap_count}")

if __name__ == "__main__":
    main()
