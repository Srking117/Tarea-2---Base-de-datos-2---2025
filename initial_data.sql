INSERT INTO categories (name, description) VALUES
('Accion', 'Libros inspirados en mundos de accion y combate'),
('Aventura', 'Historias epicas ambientadas en universos fantasticos'),
('Ciencia Ficcion', 'Tecnologia avanzada, viajes espaciales y futuro distante'),
('Fantasia Oscura', 'Reinos llenos de criaturas miticas y peligros mortales'),
('Exploracion', 'Narrativas centradas en viajes, descubrimientos y misterios');

INSERT INTO books (title, author, isbn, pages, published_year, stock, description, language, publisher)
VALUES
('Runas del Vacio', 'KaiSa', 'ISBN001', 320, 2019, 5, 'Una historia sobre el viaje de una cazadora contra criaturas del vacio', 'en', 'Shurima Press'),
('Ecos de Zaun', 'Ekko', 'ISBN002', 210, 2018, 4, 'Un joven capaz de manipular el tiempo enfrenta su destino', 'en', 'Zaunite Books'),
('Hijos del Anillo', 'Master Chief', 'ISBN003', 450, 2001, 6, 'La guerra contra el Covenant narrada desde el punto de vista humano', 'en', 'UNSC Publishing'),
('Furia Espartana', 'Kratos', 'ISBN004', 380, 2017, 3, 'Relato de un guerrero marcado por la venganza y los dioses', 'en', 'Olympus House'),
('Sombras de Hallownest', 'El Caballero', 'ISBN005', 290, 2017, 5, 'Aventuras en un reino olvidado lleno de insectos y secretos', 'en', 'Hallownest Press'),
('Colmillos Carmesi', 'Arthur Morgan', 'ISBN006', 520, 2018, 7, 'Un forajido lucha contra el ocaso de su era', 'en', 'Western Frontier'),
('Saltos en el Reino Champinon', 'Mario', 'ISBN007', 180, 1996, 8, 'Cronicas de aventuras contra criaturas y castillos', 'en', 'Mushroom Library'),
('Sombras de Kanto', 'Red', 'ISBN008', 240, 1998, 5, 'Historias de entrenadores, criaturas y batallas legendarias', 'en', 'Kanto Editions'),
('Llamas del Erdtree', 'Tarnished', 'ISBN009', 610, 2022, 2, 'Viajes por tierras fracturadas buscando gloria y poder', 'en', 'Lands Between Press'),
('La Leyenda del Heroe Verde', 'Link', 'ISBN010', 330, 2006, 4, 'Un heroe destinado a proteger el reino del caos', 'en', 'Hyrule Publishing');

INSERT INTO book_categories (book_id, category_id) VALUES
(1, 1), (1, 2),
(2, 3),
(3, 3),
(4, 1),
(5, 4),
(6, 1),
(7, 2),
(8, 2),
(9, 4),
(10, 2);

INSERT INTO users (email, full_name, password, is_active) VALUES
('usuario1@example.com', 'Jugador Uno', '$argon2id$v=19$m=65536,t=3,p=4$testhash123', true),
('usuario2@example.com', 'Explorador Legendario', '$argon2id$v=19$m=65536,t=3,p=4$testhash456', true),
('usuario3@example.com', 'Cazador de Reinos', '$argon2id$v=19$m=65536,t=3,p=4$testhash789', true),
('usuario4@example.com', 'Forajido Sin Nombre', '$argon2id$v=19$m=65536,t=3,p=4$testhashabc', true),
('usuario5@example.com', 'Heroe Verde', '$argon2id$v=19$m=65536,t=3,p=4$testhashxyz', true);

INSERT INTO loans (loan_dt, due_date, return_dt, status, fine_amount, user_id, book_id)
VALUES
(NOW() - INTERVAL '20 days', NOW() - INTERVAL '6 days', NULL, 'overdue', 0, 1, 1),
(NOW() - INTERVAL '2 days',  NOW() + INTERVAL '12 days', NULL, 'borrowed', 0, 2, 3),
(NOW() - INTERVAL '14 days', NOW() - INTERVAL '1 days', NOW(), 'returned', 0, 3, 5),
(NOW() - INTERVAL '7 days',  NOW() + INTERVAL '7 days', NULL, 'borrowed', 0, 4, 6),
(NOW() - INTERVAL '30 days', NOW() - INTERVAL '16 days', NULL, 'overdue', 0, 1, 4),
(NOW() - INTERVAL '10 days', NOW() + INTERVAL '4 days', NULL, 'borrowed', 0, 5, 2),
(NOW() - INTERVAL '1 days',  NOW() + INTERVAL '13 days', NULL, 'borrowed', 0, 3, 7),
(NOW() - INTERVAL '3 days',  NOW() + INTERVAL '11 days', NULL, 'borrowed', 0, 4, 8);

INSERT INTO reviews (rating, comment, review_date, user_id, book_id) VALUES
(5, 'Una obra increible', NOW(), 1, 1),
(4, 'Muy bueno', NOW(), 2, 1),
(3, 'Entretenido', NOW(), 3, 1),
(5, 'Ecos interesantes', NOW(), 2, 2),
(4, 'Gran historia', NOW(), 1, 2),
(5, 'Obra maestra del anillo', NOW(), 3, 3),
(4, 'Excelente narrativa', NOW(), 4, 3),
(5, 'Kratos supremo', NOW(), 5, 4),
(3, 'Bueno pero corto', NOW(), 2, 4),
(4, 'Atmosfera unica', NOW(), 1, 5),
(5, 'Magnifico', NOW(), 3, 5),
(5, 'Historia poderosa', NOW(), 1, 6),
(4, 'Buen ritmo', NOW(), 4, 7),
(5, 'Kanto legendario', NOW(), 5, 8),
(5, 'Heroe verde epico', NOW(), 3, 10);
