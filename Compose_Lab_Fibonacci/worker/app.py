import psycopg2
import time

a = 0
b = 1
position = 0


conn = psycopg2.connect(
	host="postgres",
	database="fibonacci",
	user="fibonacci",
	password="password"
)

cursor = conn.cursor()

while True:


	cursor.execute(
		"""INSERT INTO fibonacci_numbers(position, value)
		VALUES (%s, %s)
		""",
		(position, a)
	)

	conn.commit()

	print(f"Position {position}: {a}", flush=True)

	a, b = b, a + b
	position += 1

	time.sleep(5)
