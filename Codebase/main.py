# DIGITAL NOTES MANAGEMENT SYSTEM



# function to load notes from file

def load_notes():
    notes = []

    file = open("notes.txt", "r")

    for line in file:
        line = line.strip()

        if line != "":
            data = line.split("|", 2)

            note = {
                "id": data[0],
                "title": data[1],
                "content": data[2]
            }

            notes.append(note)

    file.close()

    return notes



# save notes in file

def save_notes(notes):
    file = open("notes.txt", "w")

    for note in notes:
        file.write(note["id"] + "|" + note["title"] + "|" + note["content"] + "\n")

    file.close()


#add a note

def add_note(notes):
    title = input("Enter title: ").strip()

    if title == "":
        print("Title cannot be empty. Note not saved.")
        return

    if "|" in title:
        print("Title cannot contain |. Note not saved.")
        return

    content = input("Enter content: ")

    if "|" in content:
        print("Content cannot contain |. Note not saved.")
        return

    # Generate note ID
    number = 1

    for note in notes:
        old_number = int(note["id"][1:])

        if old_number >= number:
            number = old_number + 1

    note_id = "N" + str(number)

    # creating a new note
    note = {
        "id": note_id,
        "title": title,
        "content": content
    }

    notes.append(note)

    save_notes(notes)

    print("Note saved. ID:", note_id, "|", title)


# view all notes

def view_notes(notes):
    if len(notes) == 0:
        print("No notes found.")

    else:
        for note in notes:
            print(note["id"], "|", note["title"], "|", note["content"])


# search notes

def search_notes(notes):
    keyword = input("Enter keyword: ").strip().lower()

    if keyword == "":
        print("Please enter a keyword.")
        return

    found = False

    for note in notes:
        if keyword in note["title"].lower() or keyword in note["content"].lower():
            print(note["id"], "|", note["title"], "|", note["content"])
            found = True

    if not found:
        print("No matching notes found.")


# edit a note

def edit_note(notes):
    note_id = input("Enter note ID: ").strip().upper()

    for note in notes:
        if note["id"] == note_id:
            new_content = input("Enter new content: ")

            if "|" in new_content:
                print("Content cannot contain |.")
                return

            note["content"] = new_content

            save_notes(notes)

            print("Note", note_id, "updated.")
            return

    print("Note ID does not exist.")


# delete a note

def delete_note(notes):
    note_id = input("Enter note ID: ").strip().upper()

    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)

            save_notes(notes)

            print("Note", note_id, "deleted. Notes left:", len(notes))
            return

    print("Note ID does not exist.")


# Main function
def main():
    notes = load_notes()

    while True:
        print("\n⋆ ————— DIGITAL NOTES MANAGEMENT SYSTEM ————— ⋆")
        print("               1. Add Note")
        print("            2. View All Notes")
        print("              3. Search Notes")
        print("               4. Edit Note")
        print("              5. Delete Note")
        print("                 6. Exit")
        print("↼··············································⇀")

        choice = input("      Enter your choice: ")

        if choice == "1":
            add_note(notes)

        elif choice == "2":
            view_notes(notes)

        elif choice == "3":
            search_notes(notes)

        elif choice == "4":
            edit_note(notes)

        elif choice == "5":
            delete_note(notes)

        elif choice == "6":
            print("  Thank you for using the application! (°◡°) ")
            print("↼∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙⇀")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
main()
