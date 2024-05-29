import sqlite3
import faker

# Отримати всі завдання певного користувача.Використайте SELECT для отримання завдань конкретного користувача за його user_id.
def select_task_by_user(user_id) -> list:
    with sqlite3.connect('students_tasks.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM tasks WHERE user_id=?", (user_id,))
        return cur.fetchall()
# print(select_task_by_user(1))

# Вибрати завдання за певним статусом.Використайте підзапит для вибору завдань з конкретним статусом, наприклад, 'new'.
def select_task_by_status(name) -> list:
    with sqlite3.connect('students_tasks.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM tasks WHERE status_id IN (SELECT id FROM status WHERE name LIKE ?)", (name,))
        return cur.fetchall()    
# print(select_task_by_status('new'))

# Оновити статус конкретного завдання. Змініть статус конкретного завдання на 'in progress' або інший статус.
def update_status(name, id) -> list:
    with sqlite3.connect('students_tasks.db') as con:
        cur = con.cursor()        
        cur.execute("UPDATE tasks SET status_id = (SELECT id FROM status WHERE name LIKE ?)  WHERE id = ?", (name, id))
        return cur.fetchall()
# print(update_status('in progress', 2))

# Отримати список користувачів, які не мають жодного завдання. Використайте комбінацію SELECT, WHERE NOT IN і підзапит.
def select_users_without_tasks() -> list:
    with sqlite3.connect('students_tasks.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks)")
        return cur.fetchall()
# print(select_users_without_tasks())

# Додати нове завдання для конкретного користувача. Використайте INSERT для додавання нового завдання.
def insert_task_for_user(id) -> list:
    fake_data = faker.Faker()
    with sqlite3.connect('students_tasks.db') as con:
        cur = con.cursor()        
        cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)", (fake_data.catch_phrase(),fake_data.text(),1 ,id ))
        return cur.fetchall()
# insert_task_for_user(5)

#Отримати всі завдання, які ще не завершено. Виберіть завдання, чий статус не є 'завершено'.
def select_task_not_completed() -> list:
    with sqlite3.connect('students_tasks.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM tasks WHERE status_id <> 3")
        return cur.fetchall()    
# print(select_task_not_completed())

#Видалити конкретне завдання. Використайте DELETE для видалення завдання за його id.
def delete_task(id) -> list:
    with sqlite3.connect('students_tasks.db') as con:
        cur = con.cursor()        
        cur.execute("DELETE FROM tasks WHERE id = ?", (id,))
        return cur.fetchall()
# delete_task(11)

#Знайти користувачів з певною електронною поштою. Використайте SELECT із умовою LIKE для фільтрації за електронною поштою.
def select_user_by_email(email) -> list:
    with sqlite3.connect('students_tasks.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE email LIKE ?", (email,))
        return cur.fetchall()    
# print(select_user_by_email('bensonsamuel@example.net'))

#Оновити ім'я користувача. Змініть ім'я користувача за допомогою UPDATE.
def update_user(fullname,newname ) -> list:
    with sqlite3.connect('students_tasks.db') as con:
        cur = con.cursor()        
        cur.execute("UPDATE users SET fullname = ? WHERE fullname = ?", (newname, fullname))
        return cur.fetchall()
# update_user('Jose Howard', 'Josef Howard')

#Отримати кількість завдань для кожного статусу. Використайте SELECT, COUNT, GROUP BY для групування завдань за статусами.
def get_count_tasks_by_status() -> list:
    with sqlite3.connect('students_tasks.db') as con:
        cur = con.cursor()        
        cur.execute("SELECT COUNT(status_id) as total_tasks, status_id FROM tasks GROUP BY status_id")
        return cur.fetchall()
# print(get_count_tasks_by_status())

#Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти.
def get_tasks_by_domen(domen) -> list:
    with sqlite3.connect('students_tasks.db') as con:
        cur = con.cursor()
        cur.execute("""SELECT t.id, t.title, t.description, u.email AS email 
                    FROM tasks AS t
                    INNER JOIN users AS u ON u.id = t.user_id 
                    WHERE email LIKE ?""", (domen,))
        return cur.fetchall()    
# print(get_tasks_by_domen('%@example.net'))

#Отримати список завдань, що не мають опису. Виберіть завдання, у яких відсутній опис.
def get_tasks_without_description() -> list:
    with sqlite3.connect('students_tasks.db') as con:
        cur = con.cursor()        
        cur.execute("SELECT id, title, description FROM tasks WHERE description = NULL")
        return cur.fetchall()
# print(get_tasks_without_description())

#Вибрати користувачів та їхні завдання, які є у статусі 'in progress'.
def get_users_tasks_in_progress() -> list:
    with sqlite3.connect('students_tasks.db') as con:
        cur = con.cursor()
        cur.execute("""SELECT u.id, u.fullname, t.title AS task, t.description 
                    FROM users AS u
                    INNER JOIN tasks AS t ON u.id = t.user_id 
                    WHERE status_id = 2 
                    ORDER BY fullname""")
        return cur.fetchall()    
# print(get_users_tasks_in_progress())

#Отримати користувачів та кількість їхніх завдань. 
def get_count_tasks_by_users() -> list:
    with sqlite3.connect('students_tasks.db') as con:
        cur = con.cursor()        
        cur.execute("""SELECT u.id, u.fullname, COUNT(t.user_id) AS total_tasks 
                    FROM users AS u 
                    LEFT JOIN tasks AS t ON u.id = t.user_id
                    GROUP BY user_id
                    ORDER BY u.id""")
        return cur.fetchall()
# print(get_count_tasks_by_users())







