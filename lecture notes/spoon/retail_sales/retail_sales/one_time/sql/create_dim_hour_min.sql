-- Table: dim_hour_min

-- DROP TABLE dim_hour_min;

CREATE TABLE dim_hour_min
(
  dim_hour_min_key bigserial NOT NULL,
  version integer,
  date_from timestamp without time zone,
  date_to timestamp without time zone,
  hour_min text,
  hour_of_day text,
  CONSTRAINT dim_hour_min_pkey PRIMARY KEY (dim_hour_min_key),
  CONSTRAINT dim_hour_min_hour_min_key UNIQUE (hour_min)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE dim_hour_min
  OWNER TO postgres;

-- Index: idx_dim_hour_min_lookup

-- DROP INDEX idx_dim_hour_min_lookup;

CREATE INDEX idx_dim_hour_min_lookup
  ON dim_hour_min
  USING btree
  (hour_min COLLATE pg_catalog."default");

-- Index: idx_dim_hour_min_tk

-- DROP INDEX idx_dim_hour_min_tk;

CREATE INDEX idx_dim_hour_min_tk
  ON dim_hour_min
  USING btree
  (dim_hour_min_key);

