-- KDCN Store — Migration 002
-- Catalog: tiers, services, service_includes
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS tiers (
  id          TEXT PRIMARY KEY,
  name        TEXT NOT NULL,
  icon        TEXT NOT NULL,
  color       TEXT NOT NULL,
  tagline     TEXT NOT NULL,
  description TEXT NOT NULL,
  ideal_for   TEXT NOT NULL,
  price_range TEXT NOT NULL,
  position    INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS services (
  svc_id           TEXT PRIMARY KEY,
  code             TEXT NOT NULL UNIQUE,
  slug             TEXT NOT NULL UNIQUE,
  tier             TEXT NOT NULL REFERENCES tiers(id),
  name             TEXT NOT NULL,
  tagline          TEXT NOT NULL,
  pricing_type     TEXT NOT NULL CHECK (pricing_type IN ('FIXED','FROM','QUOTE')),
  currency         TEXT NOT NULL DEFAULT 'KES',
  price_min        INTEGER,
  price_max        INTEGER,
  price_display    TEXT NOT NULL,
  ideal_for        TEXT NOT NULL,
  objective        TEXT NOT NULL,
  whatsapp_message TEXT NOT NULL,
  image_path       TEXT NOT NULL,
  badge            TEXT,
  active           INTEGER NOT NULL DEFAULT 1 CHECK (active IN (0,1)),
  position         INTEGER NOT NULL DEFAULT 0,
  created_at       TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at       TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_services_tier   ON services(tier);
CREATE INDEX IF NOT EXISTS idx_services_active ON services(active);

CREATE TABLE IF NOT EXISTS service_includes (
  id             INTEGER PRIMARY KEY AUTOINCREMENT,
  service_svc_id TEXT NOT NULL REFERENCES services(svc_id) ON DELETE CASCADE,
  position       INTEGER NOT NULL,
  item           TEXT NOT NULL,
  UNIQUE (service_svc_id, position)
);

CREATE INDEX IF NOT EXISTS idx_service_includes_svc
  ON service_includes(service_svc_id, position);
