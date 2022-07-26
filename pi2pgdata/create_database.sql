CREATE DATABASE irrigador_api
	WITH
		ENCODING = UTF8
		LC_COLLATE = 'pt_BR.UTF-8'
		LC_CTYPE = 'pt_BR.UTF-8'
		TEMPLATE = template0;

\c irrigador_api

CREATE SCHEMA IF NOT EXISTS "public";

CREATE TABLE "public"."sensores" (
	id INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY(start 1),

	CONSTRAINT "PK_sensores" PRIMARY KEY ( "id" )
);

CREATE TABLE "public"."trajectory" (
	id INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY(start 1),
	height FLOAT NOT NULL,
	lenght FLOAT NOT NULL, 

	CONSTRAINT "PK_trajectory" PRIMARY KEY ( "id" )
);