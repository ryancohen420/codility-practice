"""
Explanation (in simple, question-style wording):

We need to count how many players succeed in moving onto an empty field.

To do that:
  1. Where does each player start?  
     – Player K stands at position (K, 0).
  2. How do we know which spots are taken?  
     – Keep a set called occupied with all starting positions.
  3. How does each player move?  
     – Loop through players in order: for K, arrow in enumerate(S).  
     – Look up (dx, dy) for that arrow.  
     – Compute target (tx, ty) = (K + dx, 0 + dy).  
     – If (tx, ty) is not in occupied, they move: update occupied and increment a counter.
  4. What do we return?  
     – The total count of successful moves.

Full Problem Statement:

There are N players standing in a row, one player on on the field. They are numbered from 0 to N-1 from left to right.

Players perfom moves one by one from left to right, that is, in ascending order of numbers. Each player presses an arrow key
in one of the four cardinal directions left ('<'), right ('>'), up ('^') or down ('V'). A key press in the given direction means that the player
attempts to move onto the cloest field in the direction specified. A move can be performed only if there is no other player already standing
on the target field.

Moves are represented as a string S of length N, where S[K] ( for K within the range 0..N-1) is the direction of the K-th player's move.
How many players will actually perform a move successfully?

Write a function: 

def function(S):

which, given a string S of length N representing arrow keys pressed by each of the players, returns the number of players that will perform a move
successfully.

Examples:

Given S = '><^v', your function should return 2. Player 0 (1st player from left) cannot move rightwards, because player 1 is standing on the target field
Player 1 cannot move leftwards because player 0 is standing on the target field. Players 2 and 3 can both perform their moves because there are no players
standing on their target fields.

So the return value is how many players can make a move

Assume that
- N is an integer within the range [1...50]
- String S is made only of the following characters ^, v, < and/or >
"""

def function(S):
    N = len(S) # number of players
    occupied = {(i, 0) for i in range(N)} # creates a loop andd set {(0,0), (1,0), (2,0)...(N-1)}
    
    # map each arrow key to a (dx, dy) tuple key value dict
    moves = {
        '<': (-1,0), 
        '>': (1, 0),
        '^': (0, 1),
        'v': (0, -1)
    }

    #initialise counter for sucessful moves
    sucess = 0

    #loop over each player index k and their arrow
    for K, arrow in enumerate(S):
        # look up arrow change position
        dx, dy = moves[arrow]

        #current position of player K is (k, 0)
        x, y = K, 0

        #target position after the move
        tx, ty = x + dx, y + dy

        #check if target is free
        if (tx, ty) not in occupied:
            occupied.remove((x, y)) # vacate spot
            occupied.add((tx, ty)) # occupy the new spot
            sucess += 1 # count this as a success

    return sucess


# --------------------------
# simple tests
if __name__ == '__main__':
    print(function('<>^vv^'))   
    print(function('><><><><><>'))