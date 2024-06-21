
# Objects to serialise from JSON


class Modifier:
    def __init__(self) -> None:
        pass


class Player:
    def __init__(self, player: object) -> None:
        self.name:          str = player["name"];
        self.points:        int = player["points"];
        self.position:      str = player["position"];
        self.faction:       str = player["faction"];
        self.allocations:   list[object] = player["allocations"];



class Instance:
    def __init__(self, instance: object) -> None:
        self.name: str = instance["name"];

        self.players: list[Player] = [];
        for player in instance["players"]:
            self.players.append(Player(player));
