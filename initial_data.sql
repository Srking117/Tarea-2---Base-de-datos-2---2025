
INSERT INTO category (id, name, description) VALUES
(1, 'Ficción', 'Narrativas ficticias'),
(2, 'No Ficción', 'Libros basados en hechos reales'),
(3, 'Ciencia', 'Libros científicos y divulgativos'),
(4, 'Historia', 'Libros históricos'),
(5, 'Fantasía', 'Mundos y relatos fantásticos');


INSERT INTO book (id, title, author, isbn, stock, description, language, publisher) VALUES
(1, 'The Witcher', 'Andrzej Sapkowski', 'ISBN-BD2-2025-1120', 3, 'Fantasy RPG saga', 'en', 'Orbit'),
(2, 'Metro 2033', 'Dmitry Glukhovsky', 'ISBN-BD2-2025-1125', 2, 'Post-apocalyptic novel', 'en', 'Gollancz'),
(3, 'Dune', 'Frank Herbert', 'ISBN-BD2-2025-1130', 4, 'Sci-fi classic', 'en', 'Ace'),
(4, 'Halo: The Fall of Reach', 'Eric Nylund', 'ISBN-BD2-2025-1135', 1, 'Halo universe origin', 'en', 'Tor'),
(5, 'World War Z', 'Max Brooks', 'ISBN-BD2-2025-1140', 2, 'Zombie apocalypse chronicle', 'en', 'Broadway'),
(6, 'Foundation', 'Isaac Asimov', 'ISBN-BD2-2025-1145', 5, 'Galactic empire saga', 'en', 'Spectra'),
(7, 'The Art of War', 'Sun Tzu', 'ISBN-BD2-2025-1150', 3, 'Military strategy classic', 'en', 'Oxford'),
(8, 'Sapiens', 'Yuval Noah Harari', 'ISBN-BD2-2025-1155', 4, 'Human history analysis', 'en', 'Harper'),
(9, 'Dark Souls Design Works', 'FromSoftware', 'ISBN-BD2-2025-1160', 1, 'Game art and lore', 'en', 'UDON'),
(10, 'Skyrim Library', 'Bethesda', 'ISBN-BD2-2025-1165', 2, 'Elder Scrolls lore', 'en', 'Titan');


INSERT INTO book_categories (book_id, category_id) VALUES
(1, 5),
(2, 1),
(3, 3),
(4, 5),
(5, 1),
(6, 3),
(7, 4),
(8, 4),
(9, 5),
(10, 5);


INSERT INTO "user" (id, name, email, phone, address, password, is_active) VALUES
(1, 'Mario', 'mario@mail.com', '111111111', 'Chile', '$argon2id$v=19$m=65536,t=3,p=4$example$hash', TRUE),
(2, 'Luigi', 'luigi@mail.com', '222222222', 'Chile', '$argon2id$v=19$m=65536,t=3,p=4$example$hash', TRUE),
(3, 'Peach', 'peach@mail.com', '333333333', 'Chile', '$argon2id$v=19$m=65536,t=3,p=4$example$hash', TRUE),
(4, 'Link', 'link@mail.com', '444444444', 'Chile', '$argon2id$v=19$m=65536,t=3,p=4$example$hash', TRUE),
(5, 'Zelda', 'zelda@mail.com', '555555555', 'Chile', '$argon2id$v=19$m=65536,t=3,p=4$example$hash', TRUE);


INSERT INTO loan (id, user_id, book_id, loan_dt, due_date, return_dt, fine_amount, status) VALUES
(1, 1, 1, '2025-01-01', '2025-01-15', NULL, NULL, 'ACTIVE'),
(2, 2, 2, '2025-01-02', '2025-01-16', '2025-01-14', NULL, 'RETURNED'),
(3, 3, 3, '2025-01-03', '2025-01-17', NULL, 5000, 'OVERDUE'),
(4, 4, 4, '2025-01-04', '2025-01-18', '2025-01-18', NULL, 'RETURNED'),
(5, 5, 5, '2025-01-05', '2025-01-19', NULL, 10000, 'OVERDUE'),
(6, 1, 6, '2025-01-06', '2025-01-20', NULL, NULL, 'ACTIVE'),
(7, 2, 7, '2025-01-07', '2025-01-21', '2025-01-20', NULL, 'RETURNED'),
(8, 3, 8, '2025-01-08', '2025-01-22', NULL, NULL, 'ACTIVE');


INSERT INTO review (id, rating, comment, review_date, user_id, book_id) VALUES
(1, 5, 'Excelente libro', '2025-01-10', 1, 1),
(2, 4, 'Muy bueno', '2025-01-10', 2, 1),
(3, 3, 'Aceptable', '2025-01-10', 3, 1),
(4, 5, 'Obra maestra', '2025-01-11', 1, 2),
(5, 4, 'Entretenido', '2025-01-11', 2, 2),
(6, 5, 'Increíble', '2025-01-12', 3, 3),
(7, 4, 'Muy bueno', '2025-01-12', 4, 3),
(8, 5, 'Clásico', '2025-01-13', 5, 4),
(9, 3, 'Bueno', '2025-01-13', 1, 5),
(10, 4, 'Interesante', '2025-01-14', 2, 6),
(11, 5, 'Excelente', '2025-01-14', 3, 7),
(12, 4, 'Recomendado', '2025-01-15', 4, 8),
(13, 5, 'Arte puro', '2025-01-15', 5, 9),
(14, 4, 'Buen lore', '2025-01-16', 1, 10),
(15, 5, 'Fantástico', '2025-01-16', 2, 10);
