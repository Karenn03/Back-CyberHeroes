CREATE TABLE IF NOT EXISTS Users (
  idUser SERIAL PRIMARY KEY NOT NULL,
  idCard INT NOT NULL UNIQUE,
  names VARCHAR(50) NOT NULL,
  surnames VARCHAR(50) NOT NULL,
  email VARCHAR(75) NOT NULL,
  password VARCHAR(255) NOT NULL,
  score INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Level (
  idLevel SERIAL PRIMARY KEY NOT NULL,
  difficulty VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS Game (
  idGame SERIAL PRIMARY KEY NOT NULL,
  idUser INT NOT NULL,
  startDate DATE NOT NULL,
  endDate DATE NOT NULL,
  finalScore INT NOT NULL,
  CONSTRAINT fk_Game_Level1
    FOREIGN KEY (idUser)
    REFERENCES Users (idUser)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS Monsters (
  idMonsters SERIAL PRIMARY KEY NOT NULL,
  idLevel INT NOT NULL,
  name VARCHAR(50) NOT NULL,
  description VARCHAR(100) NOT NULL,
  CONSTRAINT fk_Monsters_Level1
    FOREIGN KEY (idLevel)
    REFERENCES Level (idLevel)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS Categories (
  idCategory SERIAL PRIMARY KEY NOT NULL,
  idMonsters INT NOT NULL,
  category VARCHAR(65) NOT NULL,
  CONSTRAINT fk_Category_Monsters1
    FOREIGN KEY (idMonsters)
    REFERENCES Monsters (idMonsters)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS Questions (
  idQuestion SERIAL PRIMARY KEY NOT NULL,
  idCategory INT NOT NULL,
  content VARCHAR(200) NOT NULL,
  CONSTRAINT fk_Questions_Category1
    FOREIGN KEY (idCategory)
    REFERENCES Categories (idCategory)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS Answers (
  idAnswer SERIAL PRIMARY KEY NOT NULL,
  idQuestion INT NOT NULL,
  answer VARCHAR(170) NOT NULL,
  isCorrect BOOLEAN NOT NULL,
  CONSTRAINT fk_Answers_Questions
    FOREIGN KEY (idQuestion)
    REFERENCES Questions (idQuestion)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS Game_has_Monsters (
  idGameHasMonsters SERIAL PRIMARY KEY NOT NULL,
  idGame INT NOT NULL,
  idUser INT NOT NULL,
  idMonsters INT NOT NULL,
  idLevel INT NOT NULL,
  CONSTRAINT fk_Game_has_Monsters_Game1
    FOREIGN KEY (idGame, idUser)
    REFERENCES Game (idGame, idUser)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Game_has_Monsters_Monsters1
    FOREIGN KEY (idMonsters, idLevel)
    REFERENCES Monsters (idMonsters, idLevel)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS Game_has_Level (
  idGameHasLevel SERIAL PRIMARY KEY NOT NULL,
  idGame INT NOT NULL,
  idUser INT NOT NULL,
  idLevel INT NOT NULL,
  CONSTRAINT fk_Game_has_Level_Game1
    FOREIGN KEY (idGame, idUser)
    REFERENCES Game (idGame, idUser)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Game_has_Level_Level1
    FOREIGN KEY (idLevel)
    REFERENCES Level (idLevel)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);
