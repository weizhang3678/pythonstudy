CREATE DATABASE examination;


CREATE TABLE public.tbl_student
(
  "STUDENT_ID" character varying(255) NOT NULL DEFAULT NULL::character varying,
  "NAME" character varying(255),
  "GENDER" character varying(255),
  "CLASS" character varying(255),
  "AGE" integer,
  "EMAIL" character varying(255),
  "ADDRESS" character varying(255),
  PRIMARY KEY ("STUDENT_ID")
);

CREATE TABLE public.tbl_course
(
  "COURSE_ID" character varying(255) NOT NULL DEFAULT NULL::character varying,
  "COURSE_NAME" character varying(255),
  PRIMARY KEY ("COURSE_ID")
);

CREATE TABLE public.tbl_exam
(
  "EXAM_ID" character varying(255) NOT NULL DEFAULT NULL::character varying,
  "EXAM_TIME" timestamp(6) with time zone,
  PRIMARY KEY ("EXAM_ID")
);

CREATE TABLE public.tbl_score
(
  "SCORE_ID" character varying(255) NOT NULL DEFAULT NULL::character varying,
  "STUDENT_ID" character varying(255),
  "EXAM_ID" character varying(255),
  "COURSE_ID" character varying(255),
  "MARKS" decimal,
   PRIMARY KEY ("SCORE_ID"),
   foreign key("STUDENT_ID") references "tbl_student"("STUDENT_ID"),
   foreign key("COURSE_ID") references "tbl_course"("COURSE_ID"),
   foreign key("EXAM_ID") references "tbl_exam"("EXAM_ID")
);
