import psutil
import time
import psycopg2

con = psycopg2.connect(
    host="dummy",
    database="system-monitor-db",
    user="postgres",
    password="dummy", 
    port="5432"
)

cursor = con.cursor()

while True:

    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory()[2]

    cpu_interrupts = psutil.cpu_stats()[1]
    cpu_calls = psutil.cpu_stats()[3]

    memory_used = psutil.virtual_memory()[3]
    memory_free = psutil.virtual_memory()[4]

    bytes_sent = psutil.net_io_counters()[0]
    bytes_received = psutil.net_io_counters()[1]

    disk_usage = psutil.disk_usage('/')[3]

    cursor.execute(
        """INSERT INTO performance VALUES
        (NOW(),%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
        (
            cpu_usage,
            memory_usage,
            cpu_interrupts,
            cpu_calls,
            memory_used,
            memory_free,
            bytes_sent,
            bytes_received,
            disk_usage
        )
    )

    con.commit()
    time.sleep(1)
