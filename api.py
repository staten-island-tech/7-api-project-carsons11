# import requests

# def getPoke(poke):
#     response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
#     if response.status_code != 200:
#         print("Error fetching data!")
#         return None
    
#     data = response.json()
#     return {
#         "name": data["name"],
#         "height": data["height"],
#         "weight": data["weight"],
#         "types": [t["type"]["name"] for t in data["types"]]
#     }

# pokemon = getPoke("Bulbasaur")
# print(pokemon)
# for key, value in pokemon.items():
#     print(key, "→", value)
# types = []
# for t in data["types"]:
#     types.append(t["type"]["name"])
# pokemon = getPoke("Bulbasaur")

# for key, value in pokemon.items():
#     print(f"{key.title()}: {value}")

import tkinter as tk # bring in tkinter and call it tk
# Create the main window (like your app's frame)
window = tk.Tk()
window.title("Message Reverser") # title at the top of the window
window.geometry("400x250") # set the size (width x height)
window.resizable(False, False) # keep it from being resized
# --- Widgets (the things that go inside the window) ---
# Label: tells user what to do
prompt = tk.Label(window, text="Type your message below:",
font=("Arial", 14))
prompt.pack(pady=10) # pack() places the widget; pady adds space above and below
