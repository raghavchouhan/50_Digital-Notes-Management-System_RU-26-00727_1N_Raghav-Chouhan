# Digital Notes Management System 📝

A simple Python-based, console application to manage notes without any complicated setup. You can add, view, search, edit and delete notes, all from a simple menu.

This is my Python project, built as a way to practise the basics of programming and get more comfortable with file handling.

## ✨ Features

- **Add Notes:** Create a new note by entering a title and its content.
- **View Notes:** See all your saved notes in one place.
- **Search Notes:** Find notes using keywords from their title or content.
- **Edit Notes:** Update the content of an existing note using its ID.
- **Delete Notes:** Remove a note using its ID.
- **Unique IDs:** Every note gets its own ID (N1, N2, N3, etc.).
- **Save Notes:** Notes are stored in a text file, so they are still available when you run the program again.

## 🛠️ Built With

- Python 3
- Lists and Dictionaries
- Functions
- Loops and Conditional Statements
- String Operations
- File Handling

## 📁 Project Structure

```text
Digital_Notes_Management/
│
├── main.py       # Main Python program
├── notes.txt     # Stores all the notes
└── README.md     # Project information
```

## 🚀 Getting Started

You don't need any extra libraries to run this project. Just make sure Python 3 is installed.

### 1. Get the project

Download or clone the project and open its folder in VS Code.

### 2. Check the files

Make sure `main.py` and `notes.txt` are in the same folder.

**Note:** `notes.txt` should exist before running the program. It can be an empty file when you start.

### 3. Run the program

Open the terminal in the project folder and enter:

```bash
python main.py
```

That's it! The application menu should appear in your terminal.

## 💻 How to Use

Once the program starts, you'll see six options:

| Option | Action |
|---|---|
| 1 | Add a Note |
| 2 | View All Notes |
| 3 | Search Notes |
| 4 | Edit a Note |
| 5 | Delete a Note |
| 6 | Exit |

Just enter the number of the operation you want to perform and follow the instructions on the screen.

## 📄 How Notes Are Stored

All notes are saved in `notes.txt` using a simple format:

```text
N1|Python|Learn Python basics
N2|Mathematics|Revise algebra
N3|AI|Explore machine learning
```

Each line represents one note, with three parts separated by the `|` symbol:

- Note ID
- Note Title
- Note Content

The program reads this file when it starts and updates it whenever a note is added, edited or deleted.

**Small limitation:** The `|` character cannot be used in note titles or content because it is used to separate the information in the text file.

## 📚 What I Learned

While working on this project, I got to practise:

- Creating and using Python functions.
- Working with lists and dictionaries.
- Using loops and conditional statements.
- Taking input from users.
- Performing basic search operations.
- Reading from and writing to text files.
- Understanding CRUD operations (Create, Read, Update and Delete).

## 👤 Author

**Raghav Chouhan**

B.Tech CSE Undergraduate

---

*Built with Python, a lot of practice, and a few debugging moments along the way. :)*
