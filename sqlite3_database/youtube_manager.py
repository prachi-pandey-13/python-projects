import sqlite3
conn = sqlite3.connect('youtube_manager.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Videos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               Name TEXT NOT NULL,
               Time TEXT NOT NULL
               )
 ''')

def list_videos():
    cursor.execute("SELECT * FROM Videos")
    videos = cursor.fetchall()

    if not videos:
        print("No videos found")
        return

    for row in videos:
        print(row)
        
def add_video(name, time):
    cursor.execute("Insert INTO Videos (Name, Time) VALUES (?, ?)", (name, time))
    conn.commit()
def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE Videos SET Name = ?, Time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()
def delete_video(video_id):
    cursor.execute("DELETE FROM Videos WHERE id = ?", (video_id,))
    conn.commit()
def main():
    while True:
        print("\n Youtube Manager APP With Database")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit App")
        choice = input("Enter your choice: ")
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name : ")
            time = input("Enter the video time : ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video ID to Update : ")
            name = input("Enter the video name : ")
            time = input("Enter the video time : ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video ID to delete : ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice ")
    conn.close()
if __name__ == '__main__':
    main()