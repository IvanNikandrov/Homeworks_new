from dataclasses import dataclass

"""
create dataclass `Engine`
"""


@dataclass
class Engine:
    volume = 100
    pistons = 4

    def __init__(self, volume=volume, pistons=pistons):
        self.volume = volume
        self.pistons = pistons
