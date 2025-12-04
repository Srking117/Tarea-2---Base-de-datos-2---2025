
-- 1. Categorias
INSERT INTO category (name, description)
VALUES
('Ficcion', 'Universos narrativos imaginarios'),
('No Ficcion', 'Registros y documentacion'),
('Ciencia', 'Tecnologia y analisis de mundos'),
('Historia', 'Cronologias y lore'),
('Fantasia', 'Mundos epicos y criaturas');

-- 2. Libros 
INSERT INTO book (title, author, isbn, stock, description, language, publisher)
VALUES
('League of Legends Lore Definitivo', 'Riot Forge', 'ISBN-BD2-2025-1120', 5, 'Compendio del universo de Runaterra', 'es', 'Riot Publishing'),
('Halo Cronicas del Jefe Maestro', '343 Industries', 'ISBN-BD2-2025-1125', 3, 'Historia del Jefe Maestro y la UNSC', 'en', 'UNSC Books'),
('God of War Saga Nordica', 'Santa Monica Studio', 'ISBN-BD2-2025-1130', 4, 'Viaje de Kratos y Atreus en tierras nordicas', 'es', 'Midgard Press'),
('Red Dead Redemption 2 Guia del Forajido', 'Rockstar Team', 'ISBN-BD2-2025-1135', 6, 'Cronicas de Arthur Morgan y la banda Van der Linde', 'en', 'Rockstar Books'),
('Assassins Creed Hermandad y Secretos', 'Ubisoft Lore Team', 'ISBN-BD2-2025-1140', 2, 'Relatos sobre la Hermandad de los Asesinos', 'es', 'Abstergo Press'),
('Super Mario Historia del Reino Champinon', 'Nintendo Archives', 'ISBN-BD2-2025-1145', 7, 'Evolucion del universo Mario', 'es', 'Nintendo Publishing'),
('Pokemon Atlas de Regiones', 'Game Freak', 'ISBN-BD2-2025-1150', 5, 'Mapa completo desde Kanto hasta Paldea', 'en', 'PokePress'),
('Hollow Knight Cartografia del Vacio', 'Team Cherry', 'ISBN-BD2-2025-1155', 4, 'Exploracion de Hallownest', 'es', 'Deepnest Books'),
('Elden Ring Mitos de las Tierras Intermedias', 'FromSoftware', 'ISBN-BD2-2025-1160', 3, 'Lore de las Tierras Intermedias', 'en', 'Erdtree Press'),
('Zelda Cronicas de Hyrule', 'Nintendo Legends', 'ISBN-BD2-2025-1165', 6, 'Leyendas de la saga Zelda', 'es', 'Hyrule Publishing');

-- 3. Relacion many-to-many 
INSERT INTO book_categories (book_id, category_id)
VALUES
(1, 5), (2, 4), (3, 5), (4, 4), (5, 1),
(6, 5), (7, 3), (8, 5), (9, 3), (10, 5);

-- 4. Usuarios "5 usuarios"
INSERT INTO "user" (username, password, email, phone, address, is_active)
VALUES
('kratos_user', '$argon2id$v=19$m=65536,t=3,p=4$kmT0YBpCjwBvJH35$LMQvL2WeM5KQ5PA3', 'kratos@example.com', '56911111111', 'Midgard 123', TRUE),
('cortana_ai', '$argon2id$v=19$m=65536,t=3,p=4$aSYj02nYqJz3dUw8$JH3A7pdJ9kS7P2Xc', 'cortana@example.com', '56922222222', 'UNSC Base', TRUE),
('link_hero', '$argon2id$v=19$m=65536,t=3,p=4$zFf92fT6YB4mLtQ9$1VqU0w7K5yxz6HYa', 'link@example.com', '56933333333', 'Kokiri Forest', TRUE),
('arthur_cowboy', '$argon2id$v=19$m=65536,t=3,p=4$NWYw8eB9KVbr2tS3$8D8PAzjx4iaqvvOe', 'arthur@example.com', '56944444444', 'Valentine Town', TRUE),
('mario_plumber', '$argon2id$v=19$m=65536,t=3,p=4$dSDRwlA8Jwtmz28y$6OEakUFQFSoYkZcC', 'mario@example.com', '56955555555', 'Mushroom Kingdom', TRUE);

-- 5. Prestamos "8 registros"
INSERT INTO loan (user_id, book_id, loan_dt, return_dt, due_date, status, fine_amount)
VALUES
(1, 1, NOW() - INTERVAL '20 days', NULL, NOW() - INTERVAL '6 days', 'OVERDUE', NULL),
(2, 2, NOW() - INTERVAL '10 days', NULL, NOW() + INTERVAL '4 days', 'ACTIVE', NULL),
(3, 3, NOW() - INTERVAL '5 days',  NULL, NOW() + INTERVAL '9 days', 'ACTIVE', NULL),
(4, 4, NOW() - INTERVAL '30 days', NULL, NOW() - INTERVAL '16 days', 'OVERDUE', NULL),
(5, 5, NOW() - INTERVAL '3 days',  NULL, NOW() + INTERVAL '11 days', 'ACTIVE', NULL),
(1, 6, NOW() - INTERVAL '14 days', NULL, NOW() + INTERVAL '0 days', 'ACTIVE', NULL),
(2, 7, NOW() - INTERVAL '1 days',  NULL, NOW() + INTERVAL '13 days', 'ACTIVE', NULL),
(3, 8, NOW() - INTERVAL '40 days', NULL, NOW() - INTERVAL '26 days', 'OVERDUE', NULL);

-- 6. Reviews "15 en total"
INSERT INTO review (rating, comment, user_id, book_id)
VALUES
(5, 'Excelente libro del universo de LOL', 1, 1),
(4, 'Muy bueno, gran narrativa', 2, 2),
(5, 'Kratos siempre epico', 3, 3),
(3, 'Buen contenido pero algo largo', 4, 4),
(5, 'Para fanaticos de la saga AC', 5, 5),
(4, 'Mario siempre es divertido', 1, 6),
(5, 'Pokemon con gran detalle de regiones', 2, 7),
(5, 'Hollow Knight obra maestra', 3, 8),
(4, 'Lore profundo de Elden Ring', 4, 9),
(5, 'Zelda increible como siempre', 5, 10),
(4, 'Runaterra fascinante', 1, 1),
(3, 'Halo interesante pero tecnico', 2, 2),
(5, 'Saga Nordica increible', 3, 3),
(4, 'Forajidos bien narrados', 4, 4),
(5, 'Atlas con gran detalle', 5, 7);
