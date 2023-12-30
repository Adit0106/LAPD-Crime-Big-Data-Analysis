import psycopg2

hostname = 'localhost'
database = 'cs777'
username = 'postgres'
pwd = 'IronMan@0132'
port_id = 5432
conn = None
cur = None

try:
    conn = psycopg2.connect(
                host=hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id)

    cur=conn.cursor()

    create_script=''' 
        CREATE TABLE IF NOT EXISTS victim_demographics (
            VictAge INT,
            VictSex VARCHAR(10),
            VictDescent VARCHAR(50),
            CrimeType INT,
            CHECK (CrimeType IN (1, 2))
        );
    '''

    cur.execute(create_script)
    conn.commit()
    
    cur.close()
    conn.close()

except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()