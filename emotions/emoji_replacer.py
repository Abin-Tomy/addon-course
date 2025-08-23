def Emoji_Replacer(message):
    emoji_dict = {
        "happy":"😊",
        "love": "❤️",
        "sad" : "🥲",
        "cool" : "😎",
        "angry" : "😡",
        "confused" : "😕",   
    }
    word = message.split()
    for word in word:
        if word.lower() in emoji_dict:
            message = message.replace(word, emoji_dict[word.lower()])
    return message
message = input("Enter your message: ")
print("Replaced emojis: ", Emoji_Replacer(message))