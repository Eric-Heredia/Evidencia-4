CREATE DATABASE ObjetoMaquinaFototerapia;

USE ObjetoMaquinaFototerapia;

CREATE TABLE Maquinas (
    id INT PRIMARY KEY,
    potenciaMaxima INT
);
CREATE TABLE Sesiones (
    id INT PRIMARY KEY AUTO_INCREMENT,
    idMaquina INT,
    fechaHoraInicio DATETIME,
    duracion INT,
    FOREIGN KEY (idMaquina) REFERENCES Maquinas(id)
);
CREATE TABLE Ajustes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    idSesion INT,
    nuevaIntensidad INT,
    fechaHoraAjuste DATETIME,
    FOREIGN KEY (idSesion) REFERENCES Sesiones(id)
);

INSERT INTO Maquinas (id, potenciaMaxima)
VALUES
    (1, 100),
    (2, 150),
    (3, 125);

INSERT INTO Sesiones (idMaquina, fechaHoraInicio, duracion)
VALUES
    (1, '2024-04-01 10:00:00', 30),
    (2, '2024-04-02 15:30:00', 45),
    (3, '2024-04-03 09:15:00', 60);

INSERT INTO Ajustes (idSesion, nuevaIntensidad, fechaHoraAjuste)
VALUES
    (1, 80, '2024-04-01 10:15:00'),
    (2, 120, '2024-04-02 16:00:00'),
    (3, 100, '2024-04-03 09:30:00'),
    (1, 90, '2024-04-01 10:30:00'),
    (2, 110, '2024-04-02 16:15:00'),
    (3, 115, '2024-04-03 09:45:00'),
    (1, 100, '2024-04-01 10:45:00'),
    (2, 150, '2024-04-02 16:30:00'),
    (3, 125, '2024-04-03 10:00:00'),
    (1, 85, '2024-04-01 10:55:00');
    
    SELECT * FROM Maquinas;
    SELECT * FROM Sesiones WHERE idMaquina = 1;
    SELECT * FROM Ajustes WHERE idSesion = 1;
    SELECT SUM(duracion) AS duracionTotal FROM Sesiones;
    SELECT * FROM Maquinas ORDER BY potenciaMaxima DESC LIMIT 1;