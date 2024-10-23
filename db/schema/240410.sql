--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2 (Debian 16.2-1.pgdg120+2)
-- Dumped by pg_dump version 16.2 (Debian 16.2-1.pgdg120+2)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

ALTER TABLE ONLY public.golem DROP CONSTRAINT golem_un;
ALTER TABLE ONLY public.golem DROP CONSTRAINT golem_pk;
DROP TABLE public.golem;
DROP SEQUENCE public.seq_golem;
--
-- Name: seq_golem; Type: SEQUENCE; Schema: public; Owner: mago
--

CREATE SEQUENCE public.seq_golem
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.seq_golem OWNER TO mago;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: golem; Type: TABLE; Schema: public; Owner: mago
--

CREATE TABLE public.golem (
    gol_seq integer DEFAULT nextval('public.seq_golem'::regclass) NOT NULL,
    email character varying NOT NULL,
    pwd character varying NOT NULL,
    nickname character varying NOT NULL,
    profile_img character varying,
    token character varying,
    join_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    last_at timestamp with time zone
);


ALTER TABLE public.golem OWNER TO mago;

--
-- Name: COLUMN golem.email; Type: COMMENT; Schema: public; Owner: mago
--

COMMENT ON COLUMN public.golem.email IS '로그인용';


--
-- Name: COLUMN golem.nickname; Type: COMMENT; Schema: public; Owner: mago
--

COMMENT ON COLUMN public.golem.nickname IS '서비스내 유저 식별용';


--
-- Name: COLUMN golem.join_at; Type: COMMENT; Schema: public; Owner: mago
--

COMMENT ON COLUMN public.golem.join_at IS '가입일';


--
-- Name: COLUMN golem.last_at; Type: COMMENT; Schema: public; Owner: mago
--

COMMENT ON COLUMN public.golem.last_at IS '마지막 접속일';


--
-- Name: golem golem_pk; Type: CONSTRAINT; Schema: public; Owner: mago
--

ALTER TABLE ONLY public.golem
    ADD CONSTRAINT golem_pk PRIMARY KEY (gol_seq);


--
-- Name: golem golem_un; Type: CONSTRAINT; Schema: public; Owner: mago
--

ALTER TABLE ONLY public.golem
    ADD CONSTRAINT golem_un UNIQUE (nickname);


--
-- PostgreSQL database dump complete
--

