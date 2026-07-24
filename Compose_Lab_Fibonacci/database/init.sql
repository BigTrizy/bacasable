CREATE TABLE fibonacci_numbers (
	id SERIAL PRIMARY KEY,
	position INTEGER,
	value BIGINT,
	created_at TIMESTAMP DEFAULT NOW()
);
