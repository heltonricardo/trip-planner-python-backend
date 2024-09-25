CREATE TABLE IF NOT EXISTS 'trips' (
    id TEXT PRIMARY KEY,
    destination TEXT NOT NULL,
    start_date DATETIME,
    end_date DATETIME,
    owner_name TEXT NOT NULL,
    owner_email TEXT NOT NULL,
    is_confirmed INTEGER
);

CREATE TABLE IF NOT EXISTS 'links' (
    id TEXT PRIMARY KEY,
    trip_id TEXT,
    url TEXT NOT NULL,
    title TEXT NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES trips(id)
);

CREATE TABLE IF NOT EXISTS 'participants' (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    trip_id TEXT NOT NULL,
    is_confirmed INTEGER,
    FOREIGN KEY (trip_id) REFERENCES trips(id)
);

CREATE TABLE IF NOT EXISTS 'activities'(
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    occurs_at DATETIME,
    trip_id TEXT NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES trips(id)
);
