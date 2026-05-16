# Portfolio 6: Lists
# Course: BES10a
# Student: Ethan Seth S. Gratuito
# Project: Terminal Anime Watchlist Manager

print("--- Personal Anime Watchlist Manager ---")

# 1. Initializing a list with starting data
watched_anime = ["Dr. STONE", "Jojo's Bizarre Adventure", "Summer Time Rendering"]

print("\nCurrent Watchlist:")
for anime in watched_anime:
    print(f"- {anime}")

print("\n--- Update Watchlist ---")

# 2. Using an indefinite loop to append new items to the list
while True:
    new_entry = input("Enter an anime you just finished (or type 'done' to finish): ")
    
    if new_entry.lower() == 'done':
        break
        
    # Adding the new string to the end of the list
    watched_anime.append(new_entry)

# 3. Logical operator to check if a specific item is in the list
if "Gantz" in watched_anime:
    print("\nSystem Note: 'Gantz' is in your completion log. The Black Sphere approves.")

# 4. Modifying the list by sorting it alphabetically
watched_anime.sort()

# 5. Using built-in functions to get the total count
total_watched = len(watched_anime)

print(f"\n--- Final Sorted Watchlist (Total: {total_watched}) ---")
for anime in watched_anime:
    print(f"> {anime}")
