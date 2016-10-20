# 내장 모듈 pickle 은 파이썬 객체를 바이트 스트림으로 작렬화하거나 바이트를 객체로 역질렬화하는데 사용한다.
# pickle로 만든 바이트 스트림을 신회할 수 없는 부분과 통신할 때 사용하면 안된다.
# pickle의 목적은 바이너리 채널을 통해 프로그램 간에 파이썬 객체를 넘겨주는 것이다.

import pickle


class GameState(object):
    def __init__(self):
        self.level = 0
        self.lives = 4


state = GameState()
state.level += 1  # 플레이어가 레벨을 통과함
state.lives -= 1  # 플레이어가 재도전해야 함

state_path = 'tmp/game_state.bin'
with open(state_path, 'wb') as f:
    pickle.dump(state, f)

with open(state_path, 'rb') as f:
    state_after = pickle.load(f)
print(state_after.__dict__)


class GameState(object):
    def __init__(self):
        self.level = 0
        self.lives = 4
        self.points = 0


state = GameState()
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)

with open(state_path, 'rb') as f:
    state_after = pickle.load(f)
print(state_after.__dict__)

assert isinstance(state_after, GameState)


# 기본 속성값
# 가장 간단한 방법은 기본 인수가 있는 생성자를 사용하는 것이다.
class GameState(object):
    def __init__(self, level=0, lives=4, points=0):
        self.level = level
        self.lives = lives
        self.points = points


def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    return unpickle_game_state, (kwargs,)


def unpickle_game_state(kwargs):
    return GameState(**kwargs)


import copyreg

copyreg.pickle(GameState, pickle_game_state)

state = GameState()
state.points += 1000
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)


class GameState(object):
    def __init__(self, level=0, lives=4, points=0, magic=5):
        self.level = level
        self.lives = lives
        self.points = points
        self.magic = magic


# try:
#     pickle.loads(serialized)
# except:
#     pass
# else:
#     assert False

def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    kwargs['version'] = 2
    return unpickle_game_state, (kwargs,)


def unpickle_game_state(kwargs):
    version = kwargs.pop('version', 1)
    if version == 1:
        kwargs.pop('lives')

    return GameState(**kwargs)


copyreg.pickle(GameState, pickle_game_state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)


class BetterGameState(object):
    def __init__(self, level=0, lives=4, points=0, magic=5):
        self.level = level
        self.lives = lives
        self.points = points
        self.magic = magic


pickle.loads(serialized)
