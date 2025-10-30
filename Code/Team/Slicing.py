song_name = input("Your favourate song: ")
length = len(song_name)

print("This song has ", length, " characters.")

start = int(input("Start number is: "))
end = int(input("End number is: "))
part = song_name[start:end]
print(part)
