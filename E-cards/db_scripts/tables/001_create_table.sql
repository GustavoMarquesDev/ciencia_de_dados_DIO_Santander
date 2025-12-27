CREATE TABLE tbl_collections (
    id SERIAL PRIMARY KEY,
    collectionSetName VARCHAR(100) NOT NULL,
    releaseDate DATE NOT NULL,
    totalCardsInCollection INT NOT NULL
);

CREATE TABLE tbl_types (
    id SERIAL PRIMARY KEY,
    typeName VARCHAR(100) NOT NULL
);

CREATE TABLE tbl_stages (
    id SERIAL PRIMARY KEY,
    stageName VARCHAR(100) NOT NULL
);

CREATE TABLE tbl_cards (
    id SERIAL PRIMARY KEY,
    hp INT,
    name VARCHAR(100) NOT NULL,
    info TEXT,
    attack VARCHAR(100),
    damage VARCHAR(50),
    weak VARCHAR(100),
    ressis VARCHAR(100),
    retreat VARCHAR(100),
    cardNumberInCollection INT NOT NULL,
    collection_id INT NOT NULL,
    type_id INT,
    stage_id INT,
    CONSTRAINT fk_collection FOREIGN KEY (collection_id) REFERENCES tbl_collection (id) ON DELETE CASCADE,
    CONSTRAINT fk_type FOREIGN KEY (type_id) REFERENCES tbl_type (id),
    CONSTRAINT fk_stage FOREIGN KEY (stage_id) REFERENCES tbl_stage (id)
);
