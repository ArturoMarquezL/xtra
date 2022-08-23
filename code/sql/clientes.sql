DROP TABLE IF EXISTS clientes;

CREATE TABLE clientes(
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre varchar(255) NOT NULL,
    email varchar(255) NOT NULL
);

INSERT INTO clientes(nombre, email) VALUES ('Dejah','dejajan@gmail.com');
INSERT INTO clientes(nombre, email) VALUES ('John','john@gmail.com');
INSERT INTO clientes(nombre, email) VALUES ('Carthoris','carthoris@gmail.com');

.headers ON

SELECT * FROM clientes;