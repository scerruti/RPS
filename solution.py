# Examples below demonstrate possible solutions at each level

def extensive_evidence(human_move, computer_move):
    # First, if both players made the same move, it's a tie
    if human_move == computer_move:
        return 'tie'

    # if the human chose rock, check to see if the computer chose paper (human wins)
    # otherwise the human loses
    elif human_move == 'rock':
        if computer_move == 'paper':
            return 'lose'
        else:
            return 'win'

    # if the human chose paper, check to see if the computer chose scissors (human loses)
    # otherwise the human wins
    elif human_move == 'paper':
        if computer_move == 'scissors':
            return 'lose'
        else:
            return 'win'

    # The human must have chosen scissors, if the computer chose rock the human loses
    elif computer_move == 'rock':
        return 'lose'

    # Otherwise the human picked scissors and the computer picked paper so the human wins
    else:
        return 'win'


def significant_evidence(human_move, computer_move):
    # This code looks at the moves and decides who wins
    if human_move == 'rock':
        if computer_move == 'rock':
            return 'tie'
        if computer_move == 'paper':
            return 'lose'
        if computer_move == 'scissors':
            return 'win'
    if human_move == 'paper':
        if computer_move == 'rock':
            return 'win'
        if computer_move == 'paper':
            return 'win'
        if computer_move == 'scissors':
            return 'win'
    if human_move == 'scissors':
        if computer_move == 'rock':
            return 'lose'
        if computer_move == 'paper':
            return 'win'
        if computer_move == 'scissors':
            return 'tie'


def limited_evidence(human_move, computer_move):
    if human_move == 'rock' and computer_move == 'rock':
        return 'win'
    if human_move == 'rock' and computer_move == 'paper':
        return 'win'
    if human_move == 'rock' and computer_move == 'scissors':
        return 'win'
    if human_move == 'paper' and computer_move == 'rock':
        return 'win'
    if human_move == 'paper' and computer_move == 'paper':
        return 'win'
    if human_move == 'paper' and computer_move == 'scissors':
        return 'win'
