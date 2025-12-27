-- Seed para tbl_collection
INSERT INTO tbl_collections (collectionSetName, releaseDate, totalCardsInCollection)
VALUES 
('Base Set', '1999-01-09', 102),
('Jungle', '1999-06-16', 64),
('Fossil', '1999-10-10', 62);

-- Seed para tbl_type
INSERT INTO tbl_types (typeName)
VALUES 
('Grass'),
('Fire'),
('Water'),
('Electric'),
('Psychic'),
('Fighting');

-- Seed para tbl_stage
INSERT INTO tbl_stages (stageName)
VALUES 
('Basic'),
('Stage 1'),
('Stage 2');

-- Seed para tbl_cards
INSERT INTO tbl_cards 
(hp, name, info, attack, damage, weak, ressis, retreat, cardNumberInCollection, collection_id, type_id, stage_id)
VALUES
(60, 'Bulbasaur', 'Seed Pokémon', 'Vine Whip', '20', 'Fire', 'Water', '1', 44, 1, 1, 1),
(50, 'Charmander', 'Lizard Pokémon', 'Ember', '30', 'Water', 'Grass', '1', 46, 1, 2, 1),
(50, 'Squirtle', 'Tiny Turtle Pokémon', 'Bubble', '20', 'Electric', 'Fire', '1', 7, 1, 3, 1),
(40, 'Pikachu', 'Mouse Pokémon', 'Thunder Jolt', '30', 'Fighting', 'Steel', '1', 58, 1, 4, 1),
(60, 'Jigglypuff', 'Balloon Pokémon', 'Pound', '20', 'Fighting', 'Psychic', '1', 54, 2, 5, 1),
(90, 'Hitmonlee', 'Kicking Pokémon', 'Stretch Kick', '50', 'Psychic', 'None', '2', 7, 3, 6, 1);
