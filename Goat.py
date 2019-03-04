entity = ['goat', 'wolf', 'cabbage']
path = []


# Defines who can eat whom
def eats(x, y):
    if x == 'goat' and y == 'cabbage':
        return True
    elif x == 'wolf' and y == 'goat':
        return True
    else:
        return False


# Defines if a pair of entities is safe to be left alone on one side
# of the river.
def safe_pair(x, y):
    if eats(x, y) or eats(y, x):
        return False
    else:
        return True


# Returns the state of the symbol who in the dictionary al. It
# returns its value and not a reference to it so it can be used for
# testing but not modified. If the symbol who is not part of the list
# it return nil.
def state_of(who, state):
    try:
        return state[who]
    except KeyError:
        state[who] = False
        return False


# Verifies if the state defined as an dictionary is safe. If the
# goat is on the same side as the man, then we're safe. Otherwise if
# the cabbage or the wolf is also on the other side, then we're not
# safe.
def safe_state(state):
    if state_of('man', state) == state_of('goat', state):
        return True
    elif state_of('goat', state) == state_of('wolf', state):
        return False
    elif state_of('goat', state) == state_of('cabbage', state):
        return False
    else:
        return True


# Moves the entity from one side to the other in the sate al. It is a
# list mutator. The positions of all the entities are defined by 0
# and 1 so the move replaces the current position with 1 - it. It
# returns the resulting list.
def move(who, state):
    if state[who] == 'left':
        state[who] = 'right'
    else:
        state[who] = 'left'
    return state


# Tests if the state has reached the goal. This is the case if all
# four entities are on the other side.
def goal_reach(state):
    if not state:
        return False
    return (state_of('man', state) == 'right' and
            state_of('goat', state) == 'right' and
            state_of('wolf', state) == 'right' and
            state_of('cabbage', state) == 'right')


# Searches for a solution from the initial state
def search_sol(state):
    next = state.copy()
    while next and not goal_reach(next):
        if safe_state(next):
            whos = list()
            input_size = input("how many to move max 2")

            for i in range(int(input_size)):
                wh = input("whom?")
                whos.append(str(wh))

            for who in whos:
                move(who, next)
        else:
            print("sorry u failed")
            break
    return next


# Initialization of the global variables
initial_state = {'man': 'left'}
for e in entity:
    initial_state[e] = 'left'

# Construct the full olution after evaluating the previous statements
print("Searching for a solution from the initial state:")
print(search_sol(initial_state))

# Evaluate the variable path to see the solution backwards.

