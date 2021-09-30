/* On utilise l'encodage UTF8 */
charset utf8;

/*
CREATION DE LA DB ON LA SUPPRIME SI ELLE EXISTE DEJA
Ca permettra de vite relancer le script de création et vous permettre de corriger ici.
Le plus simple est donc de supprimer la base de données pour vous faire gagner du temps.
*/
DROP DATABASE IF EXISTS eqlaflix;
CREATE DATABASE eqlaflix;

/* On Change de base de données */
use eqlaflix;




SET FOREIGN_KEY_CHECKS=0;




/* Creation de la Table Genre pour les films. */



/*
DROP TABLE IF EXITS 'films'; 
CREATION DE LA TABLE flims
IdFilm: entier 
Titre :
Genre: 
Realisateur :  
DateSortie :
BoxOffice :  
*/
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
("La Grande Vadrouille" , null, "Gérard Oury", '1966-01-01', 17273065, 'franco-britanique'), 
("Il était une fois dans l'Ouest" , 43, "Sergio Leone", '1968-01-01', 14862764, 'italo-americain' ), 
("Avatar" , 37, "James Cameron", '2009-01-01', 14677888, "americain" ), 
("Autant en emporte le vent" , null, "Victor Fleming", '1950-01-01', 14677888, "americain" ), 
("Astérix et Obélix : Mission Cléopâtre" , null, "Alain Chabat", '2002-01-01', 14559509, "franco-allemand" ), 
("Les Dix Commandements" , null, "Cecil B. DeMille", '1956-01-01', 14229745, "americain" ), 
("Ben-Hur" , null, "William Wyler", '1960-01-01', 13826124, "americain" ), 
("Les Visiteurs" , null, "Jean-Marie Poiré", '1993-01-01', 13782991, "francais" ), 
("Le Pont de la rivière Kwaï" , null, "David Lean", '1957-01-01', 13481750, "britanico-americain"  ), 
("Le Petit Monde de don Camillo" , null, "Julien Duvivier", '1952-01-01', 12791168, "franco-italien" ), 
("La Grande Illusion" , null, "Jean Renoir", '1937-01-01', 12500000, "francais" ), 
("Qu'est-ce qu'on a fait au Bon Dieu ?" , 6, "Philippe de Chauveron", '2014-01-01', 12366033, "francais" ), 
("Le Jour le plus long" , null, "Ken Annakin", '1962-01-01', 11933629, "americain" ), 
("Cendrillon" , 2, "Wilfred Jackson", '1950-01-01', 11873677, "" ),
("Le Corniaud" , 6, "Gérard Oury", '1965-01-01', 11739783, "franco-italo-espagnol" ),
("Star Wars, épisode VII : Le Réveil de la Force" , 37, "J. J. Abrams", '2015-01-01', 10507561, "americain" ),
("Les Bronzés 3 : Amis pour la vie" , null, "Patrice Leconte", '2006-01-01', 10355930, "francais" ),
("Taxi 2" , null, "Gérard Krawczyk", '2006-01-01', 10345901, "francais" ),
("Trois hommes et un couffin" , null, "Coline Serreau", '1985-01-01', 10251465, "francais" ),
("Les Canons de Navarone" , null, "J. Lee Thompson", '1961-01-01', 10197729, "anglo-americain" ),
("Le Roi lion (1994)" , 2, "Roger Allers", '1994-01-01', 10135871, "" ),
("Le Roi lion (2019)" , null, "Jon Favreau", '2019-01-01', 10017995, "americain" ),
("Les Misérables" , null, "Jean-Paul Le Chanois", '1957-01-01', 9940533,"franco-italo-allemand" ),
("La Guerre des boutons" , 6, "Yves Robert", '1962-01-01', 9936391, "francais" ),
("Le Docteur Jivago" , null, "David Lean", '1966-01-01', 9816054, "americain" ),
("Vingt Milles Lieues sous les mers" , null, "Richard Fleisher", '1954-01-01', 9619259, "americain" ),
("Sous le plus grand chapiteau du monde" , null, "Cecil B. DeMille", '1952-01-01', 9488114, "americain" ),
("Harry Potter à l'école des sorciers" , 20, "Chris Columbus", '2001-01-01', 9470490, "britanico-americain" ),
("Le Monde de Nemo" , 2, "Andrew Stanton", '2003-01-01', 9311689, "" ),
("Le Dîner de cons" , null, "Francis Veber", '1998-01-01', 9247001, 'francais' ),
("Harry Potter et la Chambre des secrets" , 20, "Chris Columbus", '2002-01-01', 9144701, "britano-americain " ),
("L'Ours" , null, "Jean-Jacques Annaud", '1988-01-01', 9136266, "francais" ),
("Le Grand Bleu" , null, "Luc Besson", '1988-01-01', 9074317, "franco-italo-americain" ),
("Astérix et Obélix contre César" , null, "Claude Zidi", '1999-01-01', 8948624, "franco-italo-allemand" ),
("Emmanuelle" , 17, "Just Jaeckin", '1974-01-01', 8893996, "francais" ),
("La Vache et le Prisonnier" , null, "Henri Verneuil", '1959-01-01', 8844199, "franco-italien" ),
("La Grande Évasion" , null, "John Sturges", '1963-01-01', 8756631, "americain" ),
("West Side Story" , 8, "Robert Wise", '1962-01-01', 8719610, "americain" ),
("Le Bataillon du ciel" , null, "Alexander Esway", '1947-01-01', 8649691, "francais" ),
("Le Fabuleux Destin d'Amélie Poulain" , 35, "Jean-Pierre Jeunet", '2001-01-01', 8636041, "franco-allemand"  ),
("Les Choristes" , 7, "Christophe Barratier", '2004-01-01', 8636016, "franco-allemand"),
("Pour qui sonne le glas" , null, "Sam Wood", '1947-01-01', 8274596, "americain"),
("Rien à déclarer" , null, "Dany Boon", '2011-01-01', 8150825, "franco-belge"),
("Violettes Imépriales" , 41, "Richard Pottier", '1952-01-01', 8125766, "franco-espagnol" ),
("Les Couloirs du temps : Les Visiteurs 2" , null, "Jean-Marie Poiré", '1998-01-01', 8043129, "francais"),
("Le Dictateur" , 36, "Charlie Chaplin", '1945-01-01', 8030641, "americain"),
("E.T. l'extra-terrestre" , 37, "Steven Spielberg", '1982-01-01', 7881332, "americain"),
("Un Indien dans la ville" , null, "Hervé Palud", '1994-01-01',  	7870802, "francais"),
("Tarzan" , 2, "Kevin Lima", '1999-01-01', 7859791, ''); 


system cls; 
-- select * from .......;

