import sqlite3
import datetime

try:
    sqliteConnection = sqlite3.connect('db.sqlite3')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    # CHOOSE COMMENT ID AND PLACE ID FOR YOUR NEW COMMENT AND START THE SCRIPT
    comment_id = 6
    place_id = 10
    my_current_time = datetime.datetime.now()

    count = cursor.execute("INSERT INTO MainApp_review (id, reviewers_disability_type, reviewers_attitude,\
                        reviewers_comment, place_id_id,  review_date) VALUES \
                          (?,?,?,?,?,?)", \
                        (comment_id, 'Wheelchair', 'Impossible', 'LoREM IPSUM', place_id, my_current_time))

    sqliteConnection.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")


