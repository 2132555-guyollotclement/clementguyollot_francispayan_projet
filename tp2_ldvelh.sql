/*
 * Création de la BD ldvelh
 * TP2 - BD2
 *
 * Fichier : 	tp2_ldvelh.sql
 * Auteurs :	Francis Payan / Clément Guyollot
 * Langage : 	SQL (MySQL)
 * Date : 		Novembre 2022
 */

# Création de la BD
DROP DATABASE IF EXISTS ldvelh;
CREATE DATABASE ldvelh;
USE ldvelh;

# Création de l'utilisateur avec droits restreints
CREATE USER IF NOT EXISTS 'math'@'localhost' IDENTIFIED BY '';


/* Octroyer à l'usager math le droit de faire des requêtes select et insert sur toutes 
les tables de la base de données ldvelh
 */
GRANT SELECT, INSERT
ON ldvelh.*
TO math@localhost;


# Création de la table livre
CREATE TABLE livre (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    titre VARCHAR(100)
);

# Insertion des données du livre
INSERT INTO livre (titre) 
	VALUES ('Les Maîtres des Ténèbres');


# Création de la table prologue
CREATE TABLE prologue (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    titre VARCHAR(100),
    texte TEXT,
    livre_id INTEGER,
    FOREIGN KEY (livre_id) REFERENCES livre (id)
);

# Insertion des données du prologue
INSERT INTO prologue (titre, texte, livre_id) 
	VALUES ('Avertir le roi', 'Au nord du royaume du Sommerlund, il est de tradition depuis des siècles d\'envoyer les fils des Seigneurs de la Guerre au monastère Kaï. C\'est là qu\'on leur enseigne l\'art et la science de leurs nobles ancêtres. Les Moines Kaï sont de grands maîtres dans l\'art qu\'ils enseignent. Pour transmettre leurs connaissances, ils doivent faire subir à leurs disciples de rudes épreuves au cours de leur apprentissage, mais ces derniers ne s\'en plaignent jamais. Ils leur témoignent au contraire amour et respect, sachant très bien qu\'ils quitteront un jour le monastère en possédant tous les secrets de la tradition Kaï: ils pourront alors rentrer chez eux, l\'esprit et le corps formés aux techniques de la guerre. Profondément attachés à leur patrie, ils seront ainsi prêts à la défendre contre le danger constant qui la menace : la soif de conquête des Maîtres des Ténèbres venus de l\'ouest. Au temps jadis, à l\'époque de la Lune Noire, les Maîtres des Ténèbres menèrent une guerre sans merci contre le royaume du Sommerlund. Ce fut une longue et douloureuse épreuve de force à l\'issue de laquelle les guerriers du Sommerlund remportèrent la victoire lors de la grande bataille de Maaken. Le roi Ulnar et ses alliés de Durenor anéantirent l\'armée des Maîtres des Ténèbres dans le défilé de Moytura et précipitèrent l\'ennemi au fond de la gorge de Maaken. Vashna, le plus puissant parmi les Maîtres des Ténèbres, périt d\'un coup mortel que le roi Ulnar lui porta de sa puissante épée, l\'Epée du Soleil, que l\'on désigne généralement sous le nom de «Glaive de Sommer». Depuis ce temps, les Maîtres des Ténèbres ont juré de prendre leur revanche sur le royaume du Sommerlund et la Maison d\'Ulnar. Lorsque l\'aube se lève sur le premier jour de votre aventure, tous les Seigneurs Kaï sont présents au monastère : on doit, en effet, célébrer aujourd\'hui même la grande fête de Fehmarn et l\'on se prépare tôt le matin aux réjouissances. Mais soudain, un immense nuage noir s\'élève au ciel d\'occident: d\'énormes   créatures aux ailes sombres emplissent les nues en si grand nombre que le soleil semble s\'éteindre. Cette invasion porte la marque des Maîtres des Ténèbres. Les ennemis jurés du Royaume du Sommerlund passent une nouvelle fois à l\'attaque : la guerre a recommencé. En ce matin fatal, Loup Silencieux (c\'est le nom qui vous a été donné par les Moines Kaï) est allé chercher du bois dans la forêt : c\'est la corvée qu\'on vous a assignée pour vous punir de votre inattention en classe. Or, sur le chemin du retour, vous apercevez tout à coup ce gigantesque nuage de créatures noires qui fond sur le monastère et semble l\'engloutir aussitôt. Vous laissez tomber votre bois à terre et vous vous précipitez sur le lieu de la bataille. Mais les monstres noirs ont obscurci le soleil et il fait à présent si sombre que vous trébuchez contre une racine en tombant tête la première. Dans votre chute, vous heurtez violemment du front une branche basse qui vous assomme. Une fraction de seconde avant de perdre connaissance, vous avez cependant le temps de saisir du regard un terrifiant spectacle: les murs du monastère Kaï sont en train de s\'écrouler sur eux-mêmes dans un fracas de tonnerre. Vous ne reprenez conscience qu\'au bout de plusieurs heures et, les larmes aux yeux, vous contemplez avec horreur le tas de ruines que l\'ennemi a laissé derrière lui. Les Guerriers Kaï ont été ensevelis sous les décombres et il ne reste plus aucun survivant parmi vos compagnons. Avec une infinie douleur, vous levez alors votre visage vers le ciel, à nouveau clair, et vous faites le serment de venger la mort des Moines et des Seigneurs Kaï. Vous ferez payer leur crime aux Maîtres des Ténèbres ! Votre tâche d\'ailleurs commence à l\'instant même : il vous faut, en effet, gagner la capitale du royaume pour prévenir le Roi en personne de l\'effroyable péril qui menace le pays ; car maintenant, l\'ennemi est en marche, et si vous n\'agissez pas à temps, votre patrie tombera sous son joug. Vous êtes le dernier des Seigneurs Kaï et le sort de votre peuple repose désormais entre vos seules mains: le Loup Silencieux est devenu Loup Solitaire et les envahisseurs feront tout pour vous empêcher d\'atteindre le Palais du Roi...', 1);


# Création de la table chapitre
CREATE TABLE chapitre (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    livre_id INTEGER,
    no_chapitre INTEGER,
    texte TEXT,
    FOREIGN KEY (livre_id) REFERENCES livre (id)
);


# Création de la table lien_chapitre
CREATE TABLE lien_chapitre  (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    no_chapitre_origine INTEGER,
    no_chapitre_destination INTEGER,
    FOREIGN KEY (no_chapitre_origine) REFERENCES chapitre (id),
    FOREIGN KEY (no_chapitre_destination) REFERENCES chapitre (id)
);


# Création de la table personnage
CREATE TABLE personnage (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100),
    livre_id INTEGER,
    FOREIGN KEY (livre_id) REFERENCES livre (id)
);


# Création de la table discipline
CREATE TABLE discipline (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100)
);

# Insertion des disciplines
INSERT INTO discipline (nom) VALUES
	 ('Camouflage'),
	 ('Chasse'),
	 ('Sixième sens'),
	 ('Orientation'),
	 ('Guérison'),
	 ('Maitrise des armes'),
	 ('Bouclier physique'),
	 ('Puissance psychique'),
	 ('Communication animale'),
	 ('Maitrise psychique de la matière');


# Création de la table personnage_discipline
CREATE TABLE personnage_discipline (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    personnage_id INTEGER,
    discipline_id INTEGER,
    FOREIGN KEY (personnage_id) REFERENCES personnage (id),
    FOREIGN KEY (discipline_id) REFERENCES discipline (id)
);


# Création de la table arme
CREATE TABLE arme (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100)
);

# Insertion des noms d'armes
INSERT INTO arme (nom) VALUES
	 ('Le poignard'),
	 ('La lance'),
	 ('La masse'),
	 ('La sabre'),
	 ('Le marteau de guerre'),
	 ('L''épée'),
	 ('La hâche'),
	 ('Le baton'),
	 ('Le glaive');


# Création de la table personnage_arme
CREATE TABLE personnage_arme (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    personnage_id INTEGER,
    arme_id INTEGER,
    FOREIGN KEY (personnage_id) REFERENCES personnage (id),
    FOREIGN KEY (arme_id) REFERENCES arme (id)
);

# Création de la table sauvegarde
CREATE TABLE sauvegarde (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    titre VARCHAR(200),
    livre_id INTEGER,
    chapitre_id INTEGER,
    personnage_id INTEGER,
    FOREIGN KEY (livre_id) REFERENCES livre (id),
    FOREIGN KEY (personnage_id) REFERENCES personnage (id),
    FOREIGN KEY (chapitre_id) REFERENCES chapitre (id)
);


/*
 * Quand on ajoute un héro, validez AVANT l'ajout que le nom n'existe pas déjà dans la table personnage.
 * Si le nom existe, empêche la requête INSERT et retourne un message d'erreurs
 */

DROP TRIGGER IF EXISTS hero_before_insert;

DELIMITER $$

CREATE TRIGGER hero_before_insert
    BEFORE INSERT 
    ON personnage FOR EACH ROW 

    BEGIN 
    DECLARE _nb_hero_similaire INTEGER;
        SET _nb_hero_similaire = (
			SELECT count(*)
				FROM Partie personnage
                WHERE nom = NEW.nom
		);

        IF _nb_hero_similaire > 0 THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Ce héro est déjà parti à l\'aventure !';
        END IF;

    END$$

DELIMITER ;


/* 
 * Affiche un message d'erreur si aucune sauvegarde n'a été sélectionnée AVANT la suppression
 */

DROP TRIGGER IF EXISTS sauvegarde_before_delete;

DELIMITER $$
CREATE TRIGGER sauvegarde_before_delete
    BEFORE DELETE 
    ON sauvegarde FOR EACH ROW 

    BEGIN 
    DECLARE _nb_sauvegarde_selectionne INTEGER;
        SET _nb_sauvegarde_selectionne = (
			SELECT OLD.id
				FROM sauvegarde
                WHERE id = OLD.supprime_par
		);
        IF NOT EXISTS (SELECT * FROM sauvegarde WHERE id = OLD.supprime_par) THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Aucune sauvegarde n\a été sélectionnée';
        END IF;

    END$$

DELIMITER ;




