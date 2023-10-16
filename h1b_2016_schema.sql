-- Table: public.twentysixteen2016

-- DROP TABLE IF EXISTS public.twentysixteen2016;

CREATE TABLE IF NOT EXISTS public.twentysixteen2016
(
    case_number character varying(255) COLLATE pg_catalog."default",
    case_status character varying(255) COLLATE pg_catalog."default",
    case_submitted character varying(255) COLLATE pg_catalog."default",
    decision_date character varying(255) COLLATE pg_catalog."default",
    visa_class character varying(255) COLLATE pg_catalog."default",
    employment_start_date character varying(255) COLLATE pg_catalog."default",
    employment_end_date character varying(255) COLLATE pg_catalog."default",
    employer_name character varying(255) COLLATE pg_catalog."default",
    employer_address character varying(255) COLLATE pg_catalog."default",
    employer_city character varying(255) COLLATE pg_catalog."default",
    employer_state character varying(255) COLLATE pg_catalog."default",
    employer_postal_code character varying(255) COLLATE pg_catalog."default",
    employer_country character varying(255) COLLATE pg_catalog."default",
    employer_province character varying(255) COLLATE pg_catalog."default",
    employer_phone character varying(255) COLLATE pg_catalog."default",
    employer_phone_ext character varying(255) COLLATE pg_catalog."default",
    agent_attorney_name character varying(255) COLLATE pg_catalog."default",
    agent_attorney_city character varying(255) COLLATE pg_catalog."default",
    agent_attorney_state character varying(255) COLLATE pg_catalog."default",
    job_title character varying(255) COLLATE pg_catalog."default",
    soc_code character varying(255) COLLATE pg_catalog."default",
    soc_name character varying(255) COLLATE pg_catalog."default",
    naics_code character varying(255) COLLATE pg_catalog."default",
    total_workers character varying(255) COLLATE pg_catalog."default",
    full_time_position character(1) COLLATE pg_catalog."default",
    prevailing_wage character varying(255) COLLATE pg_catalog."default",
    pw_unit_of_pay character varying(255) COLLATE pg_catalog."default",
    pw_source character varying(255) COLLATE pg_catalog."default",
    pw_source_year character varying(255) COLLATE pg_catalog."default",
    pw_source_other character varying(255) COLLATE pg_catalog."default",
    wage_rate_of_pay_from character varying(255) COLLATE pg_catalog."default",
    wage_rate_of_pay_to character varying(255) COLLATE pg_catalog."default",
    wage_unit_of_pay character varying(255) COLLATE pg_catalog."default",
    h1b_dependent character(1) COLLATE pg_catalog."default",
    willful_violator character(1) COLLATE pg_catalog."default",
    worksite_city character varying(255) COLLATE pg_catalog."default",
    worksite_county character varying(255) COLLATE pg_catalog."default",
    worksite_state character varying(255) COLLATE pg_catalog."default",
    worksite_postal_code character varying(255) COLLATE pg_catalog."default",
    original_cert_date character varying(255) COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.twentysixteen2016
    OWNER to postgres;