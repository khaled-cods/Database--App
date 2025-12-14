import sqlite3
import shutil

conn = sqlite3.connect("skills.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    skillname TEXT,
    progress INTEGER,
    JopTitle TEXT,
    phonenumber INTEGER,
    Email TEXT
)
""")


conn.commit()


menu = """\n => Skill Menu <=
a => Add skill
s => Show skills (search by username)
d => Delete skill
u => Update skill
b => bacab_database
q => Quit
"""
def add_skill():
    username = input("Enter username: ").strip().lower()
    skill = input("Enter skill name: ").strip().lower()
    progress = int(input("Enter progress (1-500): "))
    JopTitle = input("Enter Job Title: ").strip() 
    phonenumber = int(input("please enter your phone number (1-12): "))
    Email = input ("Enter your Name   (The end by (@gmail.com): ").strip().lower()
    cursor.execute(
        "INSERT INTO skills (username, skillname, progress, JopTitle , phonenumber ,Email ) VALUES (?, ?, ?, ?, ? , ?)",
        (username, skill, progress, JopTitle , phonenumber,Email )
    )
    conn.commit()
    print("Skill added successfully!")


def show_skill():
    username = input("Enter username to search: ").strip().lower()

    cursor.execute(
        "SELECT id, skillname, progress, JopTitle, phonenumber,Email  FROM skills WHERE username = ?",
        (username,)
    )
    results = cursor.fetchall()

    if not results:
        print("No skills found for this user.")
        return

    print(f"\nSkills for user '{username}':")

    for skill in results:
        print(f"ID: {skill[0]} | Skill: {skill[1]} | Progress: {skill[2]} | JobTitle: {skill[3]} | phonenumber: {skill[4]}| Email: {skill[5]} ")


def delete_skill():
    show_skill()
    skill_id = int(input("Enter skill ID to delete: "))

    cursor.execute("DELETE FROM skills WHERE id = ?", (skill_id,))
    conn.commit()
    print("Skill deleted!")
def update_skill():
    show_skill()
    skill_id = int(input("Enter skill ID to update: "))
    new_progress = int(input("Enter new progress: "))

    cursor.execute(
        "UPDATE skills SET progress = ? WHERE id = ?",
        (new_progress, skill_id)
    )
    conn.commit()
    print("Skill updated!")
    
    
    
def backup_database():
    backup_name = "skills_backup.db"
    shutil.copy("skills.db", backup_name)
    print(f"\nBackup created successfully → {backup_name}")


def quit_program():
    print("Goodbye!really you goood user !")
    conn.close()
    exit()
while True:
    choice = input(menu + "\nChoose an option: ").strip().lower()

    if choice == "a":
        add_skill()
    elif choice == "s":
        show_skill()
    elif choice == "d":
        delete_skill()
    elif choice == "u":
        update_skill()
        
    elif choice == "b":
        backup_database()
    elif choice == "q":
        quit_program()
    else:
        print("Invalid option!")
