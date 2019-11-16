-- Table: dim_store

-- DROP TABLE dim_store;

CREATE TABLE dim_store
(
  dim_store_key bigserial NOT NULL,
  version integer,
  date_from timestamp without time zone,
  date_to timestamp without time zone,
  store_id text,
  store_name text,
  CONSTRAINT dim_store_pkey PRIMARY KEY (dim_store_key),
  CONSTRAINT dim_store_store_id_key UNIQUE (store_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE dim_store
  OWNER TO postgres;

-- Index: idx_dim_store_lookup

-- DROP INDEX idx_dim_store_lookup;

CREATE INDEX idx_dim_store_lookup
  ON dim_store
  USING btree
  (store_id COLLATE pg_catalog."default");

-- Index: idx_dim_store_tk

-- DROP INDEX idx_dim_store_tk;

CREATE INDEX idx_dim_store_tk
  ON dim_store
  USING btree
  (dim_store_key);

