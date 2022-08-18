CREATE DATABASE irrigador_api
	WITH
		ENCODING = UTF8
		LC_COLLATE = 'pt_BR.UTF-8'
		LC_CTYPE = 'pt_BR.UTF-8'
		TEMPLATE = template0;

\c irrigador_api

CREATE SCHEMA IF NOT EXISTS "public";

CREATE TABLE "public"."sensors" (
	id INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY(start 1),
	temp_ai FLOAT NOT NULL,
	temp_soil FLOAT NOT NULL,
	humidity_air FLOAT NOT NULL,
	humidity_soil FLOAT NOT NULL,
	recorded_on TIMESTAMP NOT NULL,
	CONSTRAINT "PK_sensors" PRIMARY KEY ( "id" )
);

CREATE TYPE "public"."report_enum" AS ENUM(
	'INIT_CYCLE',
	'END_CYCLE',
	'LOW_BATTERY'
);

CREATE TABLE "public"."reports" (
	id INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY(start 1),
	battery_level FLOAT NOT NULL,
	remaining_points JSON NOT NULL,
	recorded_on TIMESTAMP NOT NULL,
	status_report report_enum NOT NULL,
	CONSTRAINT "PK_reports" PRIMARY KEY ( "id" )
);

CREATE TABLE "public"."field" (
	id INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY(start 1),
	field_width FLOAT NOT NULL,
	filed_length FLOAT NOT NULL, 

	CONSTRAINT "PK_field" PRIMARY KEY ( "id" )
);

CREATE TABLE "public"."route" (
	id INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY(start 1),
	base_pos POINT NOT NULL,
	irrigation_route JSON NOT NULL,
	field_id INT NOT NULL,

	CONSTRAINT "PK_route" PRIMARY KEY ( "id" ),
	CONSTRAINT "FK_field" FOREIGN KEY ("field_id") REFERENCES "public"."field" ("id")
);