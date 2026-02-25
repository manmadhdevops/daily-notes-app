def delete_notes():
    open("notes.txt", "w").close()
    print("All notes deleted!")