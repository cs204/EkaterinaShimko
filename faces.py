def convert(emoji):
    emoji1 = emoji.replace(":)", "🙂")
    emoji2 = emoji1.replace(":(", "🙁")
    return emoji2
def main():
    s = input()
    s1 = convert(s)
    print(s1)
main()
