entity = ['goat', 'wolf', 'cabbage']
path = []


def eats(x, y):
    if x == 'goat' and y == 'cabbage':
        return True
    elif x == 'wolf' and y == 'goat':
        return True
    else:
        return False


def safe_pair(x, y):
    if eats(x, y) or eats(y, x):
        return False
    else:
        return True


def state_of(who, state):
    try:
        return state[who]
    except KeyError:
        state[who] = False
        return False


def safe_state(state):
    if state_of('man', state) == state_of('goat', state):
        return True
    elif state_of('goat', state) == state_of('wolf', state):
        return False
    elif state_of('goat', state) == state_of('cabbage', state):
        return False
    else:
        return True


def move(who, state):
    if state[who] == 'left':
        state[who] = 'right'
    else:
        state[who] = 'left'
    return state


def goal_reach(state):
    if not state:
        return False
    return (state_of('man', state) == 'right' and
            state_of('goat', state) == 'right' and
            state_of('wolf', state) == 'right' and
            state_of('cabbage', state) == 'right')


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


initial_state = {'man': 'left'}
for e in entity:
    initial_state[e] = 'left'

print("Searching for a solution from the initial state:")
print(search_sol(initial_state))

