import axelrod as axl

players = [s() for s in axl.strategies if "length"
           not in s.classifier["makes_use_of"]]
parameterized_players = [axl.Random(0.1), axl.Random(0.3), axl.Random(0.7),
                         axl.Random(0.9), axl.GTFT(0.1), axl.GTFT(0.3),
                         axl.GTFT(0.7), axl.GTFT(0.9)]

players += parameterized_players
players.sort(key=lambda p:p.__repr__())
