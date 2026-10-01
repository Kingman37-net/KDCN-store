-- KDCN Store — Migration 001
-- Foundation: migration tracking
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS schema_migrations (
  version    TEXT PRIMARY KEY,
  applied_at TEXT NOT NULL DEFAULT (datetime('now')),
  checksum   TEXT,
  notes      TEXT
);

INSERT OR IGNORE INTO schema_migrations (version, notes)
VALUES ('001_initial', 'Migration tracking');
