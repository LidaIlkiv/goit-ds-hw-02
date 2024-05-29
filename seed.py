import faker
from random import randint
import sqlite3

NUMBER_USERS = 5
NUMBER_TASKS = 10
def generate_fake_data(number_users, number_tasks) -> tuple:
    fake_fullnames = []
    fake_emails = []
    fake_tasks_title = []
    fake_tasks_description = []   
    
    fake_data = faker.Faker()


    for _ in range(number_users):
        fake_fullnames.append(fake_data.name())    
        fake_emails.append(fake_data.unique.email())
    
    for _ in range(number_tasks):
        fake_tasks_title.append(fake_data.catch_phrase())
        fake_tasks_description.append(fake_data.text())


    return fake_fullnames, fake_emails, fake_tasks_title, fake_tasks_description


def prepare_data(users, emails, tasks_title, tasks_description) :
    for_users = []
    for_status = [('new',), ('in progress',), ('completed',)]
    for_tasks = []

    for user, email in zip(users, emails):
        for_users.append((user, email ))

    for task_title, task_description in zip(tasks_title, tasks_description):
        for_tasks.append((task_title, task_description, randint(1, len(for_status)), randint(1, NUMBER_USERS)))

    return for_users, for_status, for_tasks

def insert_data_to_db(users, status, tasks) -> None:
    with sqlite3.connect('students_tasks.db') as con:
        cur = con.cursor()

        sql_to_users = """INSERT INTO users(fullname, email) VALUES (?, ?)"""
        cur.executemany(sql_to_users, users)

        sql_to_status = """INSERT INTO status(name) VALUES (?)"""
        cur.executemany(sql_to_status, status)

        sql_to_tasks = """INSERT INTO tasks(title, description, status_id, user_id) VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_tasks, tasks)

        con.commit()

if __name__ == "__main__":
    users , status, tasks = prepare_data(*generate_fake_data(NUMBER_USERS, NUMBER_TASKS))
    insert_data_to_db(users, status, tasks)


    