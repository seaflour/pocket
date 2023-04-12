import sqlite3

conn = sqlite3.connect('database.db')

with open('schema.sql') as f:
    conn.executescript(f.read())

cursor = conn.cursor()

# types
cursor.execute("INSERT INTO monType (typeName, id) VALUES(?, ?)",
               ('BIRD', 0)
               )
cursor.execute("INSERT INTO monType (typeName, id) VALUES(?, ?)",
               ('NORMAL', 1)
               )
cursor.execute("INSERT INTO monType (typeName, id) VALUES(?, ?)",
               ('FIRE', 2)
               )
cursor.execute("INSERT INTO monType (typeName, id) VALUES(?, ?)",
               ('WATER', 3)
               )
cursor.execute("INSERT INTO monType (typeName, id) VALUES(?, ?)",
               ('GRASS', 4)
               )
cursor.execute("INSERT INTO monType (typeName, id) VALUES(?, ?)",
               ('ELECTRIC', 5)
               )
cursor.execute("INSERT INTO monType (typeName, id) VALUES(?, ?)",
               ('ICE', 6)
               )
cursor.execute("INSERT INTO monType (typeName, id) VALUES(?, ?)",
               ('FIGHTING', 7)
               )
cursor.execute("INSERT INTO monType (typeName, id) VALUES(?, ?)",
               ('POISON', 8)
               )
cursor.execute("INSERT INTO monType (typeName, id) VALUES(?, ?)",
               ('GROUND', 9)
               )
cursor.execute("INSERT INTO monType (typeName, id) VALUES(?, ?)",
               ('FLYING', 10)
               )
cursor.execute("INSERT INTO monType (typeName, id) VALUES(?, ?)",
               ('PSYCHIC', 11)
               )
cursor.execute("INSERT INTO monType (typeName, id) VALUES(?, ?)",
               ('BUG', 12)
               )
cursor.execute("INSERT INTO monType (typeName, id) VALUES(?, ?)",
               ('ROCK', 13)
               )
cursor.execute("INSERT INTO monType (typeName, id) VALUES(?, ?)",
               ('GHOST', 14)
               )
cursor.execute("INSERT INTO monType (typeName, id) VALUES(?, ?)",
               ('DRAGON', 15)
               )

# mons
# TODO evolutions ... 
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (0,'MissingNo.', 0, 1, None)
               )

cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (1, 'Bulbasaur', 4, 8, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (2, 'Ivysaur', 4, 8, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (3, 'Venusaur', 4, 8, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (4, 'Charmander', 2, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (5, 'Charmeleon', 2, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (6, 'Charizard', 2, 10, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (7, 'Squirtle', 3, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (8, 'Wartortle', 3, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (9, 'Blastoise', 3, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (10, 'Caterpie', 12, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (11, 'Metapod', 12, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (12, 'Butterfree', 12, 10, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (13, 'Weedle', 12, 8, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (14, 'Kakuna', 12, 8, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (15, 'Beedrill', 12, 8, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (16, 'Pidgey', 1, 10, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (17, 'Pidgeotto', 1, 10, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (18, 'Pidgeot', 1, 10, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (19, 'Rattata', 1, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (20, 'Raticate', 1, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (21, 'Spearow', 1, 10, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (22, 'Fearow', 1, 10, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (23, 'Ekans', 8, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (24, 'Arbok', 8, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (25, 'Pikachu', 5, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (26, 'Raichu', 5, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (27, 'Sandshrew', 9, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (28, 'Sandslash', 9, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (29, 'Nidoran Female', 8, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (30, 'Nidorina', 8, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (31, 'Nidoqueen', 8, 9, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (32, 'Nidoran Male', 8, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (33, 'Nidorino', 8, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (34, 'Nidoking', 8, 9, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (35, 'Clefairy', 1, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (36, 'Clefable', 1, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (37, 'Vulpix', 2, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (38, 'Ninetales', 2, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (39, 'Jigglypuff', 1, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (40, 'Wigglytuff', 1, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (41, 'Zubat', 8, 10, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (42, 'Golbat', 8, 10, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (43, 'Oddish', 4, 8, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (44, 'Gloom', 4, 8, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (45, 'Vileplume', 4, 8, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (46, 'Paras', 12, 4, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (47, 'Parasect', 12, 4, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (48, 'Venonat', 12, 8, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (49, 'Venomoth', 12, 8, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (50, 'Diglett', 9, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (51, 'Dugtrio', 9, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (52, 'Meowth', 1, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (53, 'Persian', 1, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (54, 'Psyduck', 3, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (55, 'Golduck', 3, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (56, 'Mankey', 7, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (57, 'Primeape', 7, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (58, 'Growlithe', 2, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (59, 'Arcanine', 2, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (60, 'Poliwag', 3, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (61, 'Poliwhirl', 3, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (62, 'Poliwrath', 3, 7, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (63, 'Abra', 11, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (64, 'Kadabra', 11, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (65, 'Alakazam', 11, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (66, 'Machop', 7, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (67, 'Machoke', 7, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (68, 'Machamp', 7, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (69, 'Bellsprout', 4, 8, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (70, 'Weepinbell', 4, 8, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (71, 'Victreebel', 4, 8, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (72, 'Tentacool', 3, 8, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (73, 'Tentacruel', 3, 8, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (74, 'Geodude', 13, 9, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (75, 'Graveler', 13, 9, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (76, 'Golem', 13, 9, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (77, 'Ponyta', 2, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (78, 'Rapidash', 2, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (79, 'Slowpoke', 3, 11, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (80, 'Slowbro', 3, 11, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (81, 'Magnemite', 5, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (82, 'Magneton', 5, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (83, "FarFetch'd", 1, 10, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (84, 'Doduo', 1, 10, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (85, 'Dodrio', 1, 10, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (86, 'Seel', 3, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (87, 'Dewgong', 3, 6, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (88, 'Grimer', 8, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (89, 'Muk', 8, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (90, 'Shellder', 3, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (91, 'Cloyster', 3, 6, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (92, 'Gastly', 14, 8, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (93, 'Haunter', 14, 8, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (94, 'Gengar', 14, 8, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (95, 'Onix', 13, 9, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (96, 'Drowzee', 11, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (97, 'Hypno', 11, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (98, 'Krabby', 3, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (99, 'Kingler', 3, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (10, 'Voltorb', 5, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (11, 'Electrode', 5, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (12, 'Exeggcute', 4, 11, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (13, 'Exeggutor', 4, 11, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (14, 'Cubone', 9, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (15, 'Marowak', 9, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (16, 'Hitmonlee', 7, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (17, 'Hitmonchan', 7, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (18, 'Lickitung', 1, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (19, 'Koffing', 8, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (110, 'Weezing', 8, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (111, 'Rhyhorn', 9, 13, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (112, 'Rhydon', 9, 13, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (113, 'Chansey', 1, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (114, 'Tangela', 4, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (115, 'Kangaskhan', 1, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (116, 'Horsea', 3, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (117, 'Seadra', 3, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (118, 'Goldeen', 3, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (119, 'Seaking', 3, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (120, 'Staryu', 3, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (121, 'Starmie', 3, 11, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (122, 'Mr. Mime', 11, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (123, 'Scyther', 12, 10, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (124, 'Jynx', 6, 11, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (125, 'Electabuzz', 5, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (126, 'Magmar', 2, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (127, 'Pinsir', 12, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (128, 'Tauros', 1, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (129, 'Magikarp', 3, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (130, 'Gyarados', 3, 10, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (131, 'Lapras', 3, 6, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (132, 'Ditto', 1, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (133, 'Eevee', 1, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (134, 'Vaporeon', 3, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (135, 'Jolteon', 5, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (136, 'Flareon', 2, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (137, 'Porygon', 1, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (138, 'Omanyte', 13, 3, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (139, 'Omastar', 13, 3, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (140, 'Kabuto', 13, 3, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (141, 'Kabutops', 13, 3, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (142, 'Aerodactyl', 13, 10, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (143, 'Snorlax', 1, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (144, 'Articuno', 6, 10, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (145, 'Zapdos', 5, 10, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (146, 'Moltres', 2, 10, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (147, 'Dratini', 15, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (148, 'Dragonair', 15, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (149, 'Dragonite', 15, 10, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (150, 'Mewtwo', 11, None, None)
               )
cursor.execute("INSERT INTO mon (dex, monName, prime, second, evolves) VALUES(?, ?, ?, ?, ?)",
               (151, 'Mew', 11, None, None)
               )
conn.commit()
conn.close()
