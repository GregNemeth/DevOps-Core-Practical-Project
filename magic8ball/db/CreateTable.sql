CREATE TABLE IF NOT EXISTS nexus
             (
                          id         INTEGER NOT NULL AUTO_INCREMENT,
                          omen       VARCHAR(200) NOT NULL,
                          PRIMARY KEY (id),
                          UNIQUE (omen)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS history
             (
                          id         INTEGER NOT NULL AUTO_INCREMENT,
                          a          INTEGER NOT NULL,
                          b          INTEGER NOT NULL,
                          x          INTEGER NOT NULL,
                          PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



INSERT INTO `nexus` VALUES (1,'It is certain'),(2,'Very doubtful'),(3,'It is decidedly so'),
                           (4,'My reply is no'),(5, 'Concentrate and ask again'),(6,'Yes definitely'),
                           (7, 'Reply hazy try again'),(8,'The gods are with you on this one'),(9,'Ask again later');
