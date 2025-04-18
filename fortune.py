# fortune.py

import random

# Personal Info
name = "Tarun Shrivastava"
admission_number = "20JE1022"
first_name = name.split()[0]

# Welcome Message
print(f"🔮 Welcome to {name}'s Fortune Teller ({admission_number}) 🔮")

# Prompt for mood
mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

# Fortune Messages
fortunes = {
    "happy": [
        f"✨ Your fortune: Great things await you, {first_name}! Keep smiling. ✨",
        "🌈 A happy day brings unexpected surprises. Enjoy every moment!"
    ],
    "sad": [
        "💧 Things may feel heavy now, but brighter days are coming.",
        "🌦️ Every storm runs out of rain. Stay strong."
    ],
    "neutral": [
        "☁️ A calm day is a perfect time to plan your next big move.",
        "🌀 Still waters run deep. Something exciting is on the horizon!"
    ]
}

# Get and display the fortune
if mood in fortunes:
    print(random.choice(fortunes[mood]))
else:
    print("❓ Sorry, I couldn't understand your mood. Try again with: happy/sad/neutral/stressed.")
