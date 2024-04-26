import json
import os
import datetime

class Note:
    def __init__(self, note_id, title, body, timestamp):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.timestamp = timestamp

class NoteManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                for note_data in data:
                    note = Note(**note_data)
                    self.notes.append(note)

    def save_notes(self):
        with open(self.file_path, 'w') as file:
            data = [vars(note) for note in self.notes]
            json.dump(data, file, default=str, indent=4)

    def list_notes(self):
        for note in self.notes:
            print(f"ID: {note.note_id}, Title: {note.title}, Timestamp: {note.timestamp}")

    def add_note(self, title, body):
        note_id = len(self.notes) + 1
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note = Note(note_id, title, body, timestamp)
        self.notes.append(note)
        self.save_notes()

    def edit_note(self, note_id, new_title, new_body):
        for note in self.notes:
            if note.note_id == note_id:
                note.title = new_title
                note.body = new_body
                note.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                return
        print("Note not found.")

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.note_id != note_id]
        self.save_notes()

def main():
    file_path = "notes.json"
    note_manager = NoteManager(file_path)

    while True:
        print("\nOptions:")
        print("1. List notes")
        print("2. Add note")
        print("3. Edit note")
        print("4. Delete note")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            note_manager.list_notes()
        elif choice == "2":
            title = input("Enter note title: ")
            body = input("Enter note body: ")
            note_manager.add_note(title, body)
        elif choice == "3":
            note_id = int(input("Enter note ID to edit: "))
            new_title = input("Enter new title: ")
            new_body = input("Enter new body: ")
            note_manager.edit_note(note_id, new_title, new_body)
        elif choice == "4":
            note_id = int(input("Enter note ID to delete: "))
            note_manager.delete_note(note_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()