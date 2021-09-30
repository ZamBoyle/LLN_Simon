
DROP DATABASE IF EXISTS supersimon;
CREATE DATABASE supersimon;

/* On Change de base de données */
use supersimon;

SET FOREIGN_KEY_CHECKS=0;




/* Creation de la Table Genre pour les score. */


DROP TABLE IF EXISTS score; 

CREATE TABLE score(
    IdScore int UNSIGNED AUTO_INCREMENT PRIMARY KEY ,
    pseudo varchar(255) not null,
    score int not null,
	datescore datetime
	);

/*
INSERT INTO score(pseudo,  score, datescore)
VALUES('simondad', 20, '2021/12/12'),
('simonmom', 15, '2021/12/12'), 
('simonson', 10, '2021/12/12'), 
('simonsister', 5, '2021/12/12'), 
('simonbaby', 1, '2021/12/12');
*/

select * from score;

