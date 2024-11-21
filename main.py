import mysql.connector as mc

conn = mc.connect(
    host = 'localhost',
    user = 'root',
    password = '.yearup1298B',
)
c = conn.cursor()
c.execute('USE menagerie')

def step_9():
    c.execute("SHOW DATABASES")
    return c.fetchall()

def step_11():
    c.execute('DESC pet')
    for item in c.fetchall():
        print(item)

def step_14():
    c.execute('SELECT * FROM pet')
    for item in c.fetchall():
        print(item)

def step_17():
    c.execute("SELECT * FROM pet WHERE sex = 'f' AND species = 'dog'")
    for item in c.fetchall():
        print(item)

def step_20():
    c.execute('SELECT name, birth FROM pet')
    for item in c.fetchall():
        print(item)

def step_23():
    c.execute("SELECT owner, count(owner) from pet group by owner")
    for item in c.fetchall():
        print(item)

def step_26():
    c.execute("SELECT name, birth, MONTH(birth) from pet")
    for item in c.fetchall():
        print(item)
step_26()