-- Table: dim_date

-- DROP TABLE dim_date;

CREATE TABLE dim_date
(
  dim_date_key bigserial NOT NULL,
  version integer,
  date_from timestamp without time zone,
  date_to timestamp without time zone,
  date_str text,
  cal_year smallint,
  cal_month smallint,
  cal_day_of_year smallint,
  cal_day_of_month smallint,
  cal_day_of_week smallint,
  cal_week_of_year smallint,
  d_o_w_str text,
  d_o_w_str3 text,
  d_o_w_str1 text,
  weakday_indicator text,
  CONSTRAINT dim_date_pkey PRIMARY KEY (dim_date_key),
  CONSTRAINT dim_date_date_str_key UNIQUE (date_str)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE dim_date
  OWNER TO postgres;

-- Index: idx_dim_date_lookup

-- DROP INDEX idx_dim_date_lookup;

CREATE INDEX idx_dim_date_lookup
  ON dim_date
  USING btree
  (date_str COLLATE pg_catalog."default");

-- Index: idx_dim_date_tk

-- DROP INDEX idx_dim_date_tk;

CREATE INDEX idx_dim_date_tk
  ON dim_date
  USING btree
  (dim_date_key);

