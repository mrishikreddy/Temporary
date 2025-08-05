res = []
def dfs(board, word, i, j, visited):
    if 0<=i<len(board) and 0<=j<len(board[0]) and not visited[i][j]:
        word += board[i][j]
        if word in words:
            res.append(word)

        visited[i][j] = True
        dfs(board, word, i+1, j, visited)
        dfs(board, word, i-1, j, visited)
        dfs(board, word, i, j+1, visited)
        dfs(board, word, i, j-1, visited)
        visited[i][j] = False


board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
words = set(words)

visited = [ [False]*len(board[0]) for _ in range(len(board))]
for i in range(len(board)):
    for j in range(len(board[0])):
        dfs(board, "", i, j, visited)
        
print(res)
