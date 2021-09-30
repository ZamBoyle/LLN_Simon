/* On utilise l'encodage UTF8 */
charset utf8;

DROP DATABASE IF EXISTS eqlaflix;
CREATE DATABASE eqlaflix;

/* On Change de base de données */
use eqlaflix;

SET FOREIGN_KEY_CHECKS=0;




/* Creation de la Table Genre pour les films. */


DROP TABLE IF EXITS 'films'; 

CREATE TABLE Films(
    IdFilm int UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY ,
    Titre varchar(255),
    Genre smallint UNSIGNED,
    Realisateur varchar(255) not null,
    DateSortie date NOT NULL,
    BoxOffice int UNSIGNED NOT NULL,
    pays varchar(150),
    -- pays int(11),
    Deleted boolean default FALSE,
    -- FOREIGN KEY(pays) REFERENCES Pays(Id_Pays),
    FOREIGN KEY(Genre) REFERENCES GenreFilm(IdGenre)
);


INSERT INTO Films(Titre , Genre, Realisateur, DateSortie, BoxOffice, pays )
VALUES('Titanic' , 14, 'James Cameron', '1997-01-01' , 20634793, 'americain' ), 
("Bienvenue chez les Ch'tis" , 14, 'Dany Boon', '2008-02-20' , 20489303, "francais" ),
("Intouchables" , null, "E. Toledano et O. Nakache",'2011-01-01' , 19490688, 'francais' ), 
("Tarzan" , 2, "Kevin Lima", '1999-01-01', 7859791, ''); 


system cls; 
-- select * from .......;

