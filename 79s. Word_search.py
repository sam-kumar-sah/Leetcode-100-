//79. Word Search
'''
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent 
cell, where "adjacent" cells are those horizontally or vertically 
neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''

//code:
class solution(object):

    def exist(self,board,word):
        for y in range(len(board)):
            for x in range(len(board[0])):
                if(self.exit(board,word,x,y,0)):
                    return True
        return False

    #i=count
    def exit(self,board,word,x,y,i):
        if(len(word)==i):
            return True
        if( x<0 or x>=len(board[0]) or y<0 or y>=len(board)):
            return False
        if(board[y][x]!=word[i]):
            return False

        board[y][x]=board[y][x].swapcase()

        isexit=(self.exit(board,word,x+1,y,i+1) or
                self.exit(board,word,x,y+1,i+1) or
                self.exit(board,word,x-1,y,i+1) or
                self.exit(board,word,x,y-1,i+1)  )
        board[y][x]=board[y][x].swapcase()
        return isexit


board=[
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']  ]
word="FDA"
ss=solution()
print(ss.exist(board,word))
