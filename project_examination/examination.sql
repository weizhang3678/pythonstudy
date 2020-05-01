
CREATE DATABASE examination;
use examination;
CREATE TABLE tb_emp1
    -> (
    -> id INT(11),
    -> name VARCHAR(25),
    -> deptId INT(11),
    -> salary FLOAT
    -> );

CREATE TABLE tbl_student
(
  STUDENT_ID INT(11),
  NAME VARCHAR(25),
  GENDER VARCHAR(25),
  CLASS VARCHAR(25),
  AGE INT(2),
  EMAIL VARCHAR(255),
  ADDRESS VARCHAR(255),
  PRIMARY KEY (STUDENT_ID)
);

CREATE TABLE tbl_course
(
  COURSE_ID INT(11),
  COURSE_NAME VARCHAR(255),
  PRIMARY KEY (COURSE_ID)
);

CREATE TABLE tbl_exam
(
  EXAM_ID INT(11),
  EXAM_TIME DATETIME,
  PRIMARY KEY (EXAM_ID)
);

CREATE TABLE tbl_score
(
  SCORE_ID INT(11),
  STUDENT_ID INT(11),
  EXAM_ID INT(11),
  COURSE_ID INT(11),
  MARKS decimal,
  PRIMARY KEY (SCORE_ID),
   foreign key(STUDENT_ID) references tbl_student(STUDENT_ID),
   foreign key(COURSE_ID) references tbl_course(COURSE_ID),
   foreign key(EXAM_ID) references tbl_exam(EXAM_ID)
);


