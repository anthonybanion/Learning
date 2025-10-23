class Player:
    def __init__(self, name, position):
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name
    
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        self._position = new_position

    def __str__(self):
        return f"{self.name} plays as {self.position}"


class SoccerTeam:
    def __init__(self, team_name):
        self._team_name = team_name
        self._players = []  # Aggregation relationship

    def add_player(self, player):
        if not isinstance(player, Player):
            raise ValueError("Only Player instances can be added to the team.")
        self._players.append(player)

    @property
    def team_name(self):
        return self._team_name

    @property
    def players(self):
        return self._players

    def __str__(self):
        if not self._players:
            return f"Team {self.team_name} has no players yet."
        player_names = ', '.join(player.name for player in self._players)
        return f"Team {self.team_name} has players: {player_names}"
    
# Example usage
if __name__ == "__main__":
    team = SoccerTeam("Dream Team")
    player1 = Player("Alice", "Forward")
    player2 = Player("Bob", "Midfielder")
    
    team.add_player(player1)
    team.add_player(player2)
    print(team)  # Output: Team Dream Team has players: Alice, Bob
    print(player1)

    