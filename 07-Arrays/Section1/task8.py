computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]
computer_games.sort()

index = 0
while index < len(computer_games):
    print(index + 1, ":", computer_games[index])
    index += 1