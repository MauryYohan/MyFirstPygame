EXCLUSIFS = {
    1: "Exclusif Rouge Feu",
    2: "Exclusif Vert Feuille",
    9: "RFVF"
}

# Forme Lieux_RFVF:
# >>  Route 1 à 25                                          Index 0 à 24
# >>  Villes                                                Index 25 à 35
# >>  Lieux importants                                      Index 36 à 52
# >>  Lieux d'Iles Sevii                                    Index 53:0 à 53:4
#    > Ile 1                                                Index 54:0 à 54:1
#    > Ile 2                                                Index 55:0 à 55:4
#    > Ile 3                                                Index 56:0 à 56:1
#    > Ile 4                                                Index 57:0 à 57:6
#    > Ile 5                                                Index 58:0 à 58:7
#    > Ile 6                                                Index 59:0, 59:1:0
# cond spécs (Evol via echange, via le jeu ou autre)
LIEUX_RFVF = [
    "Route 1", "Route 2", "Route 3", "Route 4", "Route 5", "Route 6", "Route 7", "Route 8", "Route 9", "Route 10",
    "Route 11", "Route 12", "Route 13", "Route 14", "Route 15", "Route 16", "Route 17", "Route 18", "Chenal 19",
    "Chenal 20", "Chenal 21", "Route 22", "Route 23", "Route 24", "Route 25",
    "Argenta", "Azuria", "Bourg Palette", "Carmin-sur-Mer", "Céladopole", "Cramois'Île", "Jadielle", "Lavanville",
    "Parmanie", "Plateau Indigo", "Safrania",
    "Cave Taupiqueur", "Caverne Azurée", "Centrale", "Forêt de Jade", "Grotte", "Îles Écume", "Manoir Pokémon",
    "Mont Sélénite", "L'Océane", "Parc Safari", "Repaire Rocket", "Route Victoire", "Souterrain Est-Ouest",
    "Souterrain Nord-Sud", "Sylphe SARL", "Tour Pokémon", "Villa du Cap",
    [
        "Ile 1", "Mont Braise", "Plage Trésor", "Route Tison", "Source Braise", "Ville"
    ],
    [
        "Ile 2", "Cap Falaise", "Ville"
    ],
    [
        "Ile 3", "Bois Baies", "Chemin Île 3", "Pont du Lien", "Port Île 3", "Ville"
    ],
    [
        "Ile 4", "Grotte de Glace", "Ville"
    ],
    [
        "Ile 5", "Camp de Vacances", "Entrepôt (Rocket)", "Grotte Perdue", "Labyrinthe d'O", "Mémorial", "Pré de l'Île 5",
        "Ville"
    ],
    [
        "Ile 6", "Agualcanal", "Chemin Vert", "Forbuissons", "Grotte Métamo", "Île du Lointain", "Trou Percé", "Vallée Ruine",
        "Ville"
    ],
    [
        "Ile 7", "Canyon Sesor",
        [
            "Chambre Tanoby: Anémune",
            "Chambre Tanoby: Deulipe",
            "Chambre Tanoby: Prois",
            "Chambre Tanoby: Jonquatr",
            "Chambre Tanoby: Hibicinq",
            "Chambre Tanoby: Irix",
            "Chambre Tanoby: Poinsept"
        ], "Clé Tanoby", "Entrée Canyon", "Ruines Tanoby", "Tour Dresseurs", "Ville"
    ],
    [
        "Ile Aurore", "Roc Nombri"
    ]

]
LIEUX_RSE = []
SPECIFIC_EVOLUTION = [
    "Evolution par niveau",
    "Evolution par échange",
    "Evolution par pierre eau",
    "Evolution par pierre feu",
    "Evolution par pierre foudre",
    "Evolution par pierre plante",
    "Evolution par pierre lune"
]


poke_dex = dict()
# FORME Pokemon: #, Exclusivite, Lieux de rencontres
poke_dex["Bulbizarre"] = (EXCLUSIFS.get(9), 9,
                          LIEUX_RFVF[27])
poke_dex["Herbizarre"] = (2, 9, SPECIFIC_EVOLUTION[0])
poke_dex["Florizarre"] = (3, 9, SPECIFIC_EVOLUTION[0])
poke_dex["Salamèche"] = (4, 9,
                         LIEUX_RFVF[27])
poke_dex["Reptincel"] = (5, 9, SPECIFIC_EVOLUTION[0])
poke_dex["Dracaufeu"] = (6, 9, SPECIFIC_EVOLUTION[0])
poke_dex["Carapuce"] = (7, 9,
                        LIEUX_RFVF[27])
poke_dex["Carabaffe"] = (8, 9, SPECIFIC_EVOLUTION[0])
poke_dex["Tortank"] = (9, 9, SPECIFIC_EVOLUTION[0])
poke_dex["Chenipan"] = (10, 9,
                        LIEUX_RFVF[39], LIEUX_RFVF[58][0], LIEUX_RFVF[1], LIEUX_RFVF[23], LIEUX_RFVF[24])
poke_dex["Chrysacier"] = (11, 9,
                          LIEUX_RFVF[39], LIEUX_RFVF[58][0], LIEUX_RFVF[23], LIEUX_RFVF[24])
poke_dex["Papilusion"] = (12, 9, SPECIFIC_EVOLUTION[0])
poke_dex["Aspicot"] = (13, 9,
                       LIEUX_RFVF[39], LIEUX_RFVF[58][0], LIEUX_RFVF[1], LIEUX_RFVF[23], LIEUX_RFVF[24])
poke_dex["Coconfort"] = (14, 9,
                         LIEUX_RFVF[39], LIEUX_RFVF[58][0], LIEUX_RFVF[23], LIEUX_RFVF[24])
poke_dex["Dardargnan"] = (15, 9, SPECIFIC_EVOLUTION[0])
poke_dex["Roucool"] = (16, 9,
                       LIEUX_RFVF[55][0], LIEUX_RFVF[0], LIEUX_RFVF[1], LIEUX_RFVF[2], LIEUX_RFVF[4], LIEUX_RFVF[5],
                       LIEUX_RFVF[6], LIEUX_RFVF[7], LIEUX_RFVF[11], LIEUX_RFVF[12], LIEUX_RFVF[13], LIEUX_RFVF[14],
                       LIEUX_RFVF[23], LIEUX_RFVF[24])
poke_dex["Roucoups"] = (17, 9,
                        LIEUX_RFVF[55][0], LIEUX_RFVF[12], LIEUX_RFVF[13], LIEUX_RFVF[14])
poke_dex["Roucarnage"] = (18, 9,
                          SPECIFIC_EVOLUTION[0])
poke_dex["Rattata"] = (19, 9,
                       LIEUX_RFVF[42], LIEUX_RFVF[0], LIEUX_RFVF[1], LIEUX_RFVF[3], LIEUX_RFVF[8], LIEUX_RFVF[15],
                       LIEUX_RFVF[16], LIEUX_RFVF[17], LIEUX_RFVF[21])
poke_dex["Rattatac"] = (20, 9,
                        LIEUX_RFVF[42], LIEUX_RFVF[15], LIEUX_RFVF[16], LIEUX_RFVF[17], LIEUX_RFVF[21])
poke_dex["Piafabec"] = (21, 9,
                        LIEUX_RFVF[53][0], LIEUX_RFVF[54][0], LIEUX_RFVF[58][0], LIEUX_RFVF[59][0], LIEUX_RFVF[53][1],
                        LIEUX_RFVF[2], LIEUX_RFVF[3], LIEUX_RFVF[8], LIEUX_RFVF[9], LIEUX_RFVF[10], LIEUX_RFVF[15],
                        LIEUX_RFVF[16], LIEUX_RFVF[17], LIEUX_RFVF[21], LIEUX_RFVF[22])
poke_dex["Rapasdepic"] = (22, 9,
                          LIEUX_RFVF[53][0], LIEUX_RFVF[54][0], LIEUX_RFVF[58][0], LIEUX_RFVF[59][0], LIEUX_RFVF[53][1],
                          LIEUX_RFVF[16], LIEUX_RFVF[17], LIEUX_RFVF[22])
poke_dex["Abo"] = (23, 1,
                   LIEUX_RFVF[3], LIEUX_RFVF[7], LIEUX_RFVF[8], LIEUX_RFVF[9], LIEUX_RFVF[10], LIEUX_RFVF[22])
poke_dex["Arbok"] = (24, 1,
                     LIEUX_RFVF[22], LIEUX_RFVF[47])
poke_dex["Pikachu"] = (25, 9,
                       LIEUX_RFVF[38], LIEUX_RFVF[39])
poke_dex["Raichu"] = (26, 9,
                      SPECIFIC_EVOLUTION[4])
poke_dex["Sabelette"] = (27, 2,
                         LIEUX_RFVF[3], LIEUX_RFVF[7], LIEUX_RFVF[8], LIEUX_RFVF[9], LIEUX_RFVF[10], LIEUX_RFVF[22])
poke_dex["Sablaireau"] = (28, 2,
                          LIEUX_RFVF[22], LIEUX_RFVF[47])
poke_dex["Nidoran F"] = (29, 9,
                         LIEUX_RFVF[2])
poke_dex["Nidorina"] = (30, 9,
                        LIEUX_RFVF[45])
poke_dex["Nidoqueen"] = (31, 9,
                         SPECIFIC_EVOLUTION[6])
poke_dex["Nidoran M"] = (32, 9,
                         LIEUX_RFVF[2])
poke_dex["Nidorino"] = (33, 9,
                        LIEUX_RFVF[45])
poke_dex["Nidoking"] = (34, 9,
                        SPECIFIC_EVOLUTION[6])
poke_dex["Melofee"] = (35, 9,
                       LIEUX_RFVF[43])
poke_dex["Melodelfe"] = (36, 9,
                         SPECIFIC_EVOLUTION[6])

poke_dex["Goupix"] = (37, 2,
                      LIEUX_RFVF[42], LIEUX_RFVF[6], LIEUX_RFVF[7], "Mont Mémoria RSE")
poke_dex["Feunard"] = (32,
                       SPECIFIC_EVOLUTION[2])

poke_dex["Rondoudou"] = (33, 9,
                         LIEUX_RFVF[2])
poke_dex["Grodoudou"] = (34, 9,
                         SPECIFIC_EVOLUTION[6])

poke_dex["Nosferapti"] = (35, 9, LIEUX_RFVF[40], LIEUX_RFVF[56][0], LIEUX_RFVF[57][0], LIEUX_RFVF[58][0], LIEUX_RFVF[41], LIEUX_RFVF[43]
    )
poke_dex["Nosferalto"] = \
    (
        9,
        LIEUX_RFVF[37],
        LIEUX_RFVF[56][0],
        LIEUX_RFVF[57][0],
        LIEUX_RFVF[41]
    )

poke_dex["Mystherbe"] = \
    (
        9,
        LIEUX_RFVF[54][0],
        LIEUX_RFVF[55][0],
        LIEUX_RFVF[58][0],
        LIEUX_RFVF[4],
        LIEUX_RFVF[5],
        LIEUX_RFVF[6],
        LIEUX_RFVF[11],
        LIEUX_RFVF[12],
        LIEUX_RFVF[13],
        LIEUX_RFVF[14],
        LIEUX_RFVF[23],
        LIEUX_RFVF[24]
    )

poke_dex["Ortide"] = \
    (
        9,
        LIEUX_RFVF[54][0],
        LIEUX_RFVF[55][0],
        LIEUX_RFVF[58][0],
        LIEUX_RFVF[11],
        LIEUX_RFVF[12],
        LIEUX_RFVF[13],
        LIEUX_RFVF[14]
    )
poke_dex["Rafflesia"] = (9, SPECIFIC_EVOLUTION[5])

poke_dex["Paras"] = (9, LIEUX_RFVF[43], LIEUX_RFVF[45])
poke_dex["Parasect"] = (9, LIEUX_RFVF[37], LIEUX_RFVF[45])

poke_dex["Mimitoss"] = \
    (
        9,
        LIEUX_RFVF[55][0],
        LIEUX_RFVF[45],
        LIEUX_RFVF[11],
        LIEUX_RFVF[12],
        LIEUX_RFVF[13],
        LIEUX_RFVF[14]
    )
poke_dex["Aeromite"] = (9, LIEUX_RFVF[55][0], LIEUX_RFVF[45])

poke_dex["Taupiqueur"] = (9, LIEUX_RFVF[36])
poke_dex["Triopikeur"] = (9, LIEUX_RFVF[36])

poke_dex["Miaouss"] = \
    (
        9,
        LIEUX_RFVF[53][0],
        LIEUX_RFVF[54][0],
        LIEUX_RFVF[55][0],
        LIEUX_RFVF[58][0],
        LIEUX_RFVF[59][0],
        LIEUX_RFVF[4],
        LIEUX_RFVF[5],
        LIEUX_RFVF[6],
        LIEUX_RFVF[7]
     )
poke_dex["Persian"] = (9, LIEUX_RFVF[53][0], LIEUX_RFVF[54][0], LIEUX_RFVF[55][0], LIEUX_RFVF[58][0], LIEUX_RFVF[59][0])

poke_dex["Psykokwak"] = \
    (
        1,
        LIEUX_RFVF[26],
        LIEUX_RFVF[27],
        LIEUX_RFVF[37],
        LIEUX_RFVF[29],
        LIEUX_RFVF[53][0],
        LIEUX_RFVF[54][0],
        LIEUX_RFVF[55][0],
        LIEUX_RFVF[56][0],
        LIEUX_RFVF[57][0],
        LIEUX_RFVF[58][0],
        LIEUX_RFVF[59][0],
        LIEUX_RFVF[41],
        LIEUX_RFVF[31],
        LIEUX_RFVF[32],
        LIEUX_RFVF[44],
        LIEUX_RFVF[45],
        LIEUX_RFVF[33],
        LIEUX_RFVF[3],
        LIEUX_RFVF[5],
        LIEUX_RFVF[9],
        LIEUX_RFVF[10],
        LIEUX_RFVF[11],
        LIEUX_RFVF[12],
        LIEUX_RFVF[18],
        LIEUX_RFVF[19],
        LIEUX_RFVF[20],
        LIEUX_RFVF[21],
        LIEUX_RFVF[22],
        LIEUX_RFVF[23],
        LIEUX_RFVF[24]
    )
poke_dex["Akwakwak"] = (1, LIEUX_RFVF[37], LIEUX_RFVF[54][0], LIEUX_RFVF[55][0], LIEUX_RFVF[41])

poke_dex["Ferosinge"] = \
    (
        9,
        LIEUX_RFVF[40],
        LIEUX_RFVF[2],
        LIEUX_RFVF[3],
        LIEUX_RFVF[21],
        LIEUX_RFVF[22]
    )
poke_dex["Colossinge"] = (9, LIEUX_RFVF[37], LIEUX_RFVF[22], LIEUX_RFVF[47])

poke_dex["Caninos"] = (1, LIEUX_RFVF[42], LIEUX_RFVF[6], LIEUX_RFVF[7])
poke_dex["Arcanin"] = (1, SPECIFIC_EVOLUTION[2])

poke_dex["Ptitard"] = \
    (
        9,
        LIEUX_RFVF[37],
        LIEUX_RFVF[54][0],
        LIEUX_RFVF[55][0],
        LIEUX_RFVF[56][0],
        LIEUX_RFVF[58][0],
        LIEUX_RFVF[31],
        LIEUX_RFVF[45],
        LIEUX_RFVF[33],
        LIEUX_RFVF[5],
        LIEUX_RFVF[21],
        LIEUX_RFVF[22],
        LIEUX_RFVF[24]
    )
poke_dex["Tetarte"] = \
    (
        9,
        LIEUX_RFVF[37],
        LIEUX_RFVF[54][0],
        LIEUX_RFVF[56][0],
        LIEUX_RFVF[58][0],
        LIEUX_RFVF[31],
        LIEUX_RFVF[5],
        LIEUX_RFVF[21],
        LIEUX_RFVF[22],
        LIEUX_RFVF[24]
    )
poke_dex["Tartard"] = (9, SPECIFIC_EVOLUTION[2])

poke_dex["Abra"] = (9, LIEUX_RFVF[23], LIEUX_RFVF[24])
poke_dex["Kadabra"] = (9, LIEUX_RFVF[37])
poke_dex["Alakazam"] = (9, SPECIFIC_EVOLUTION[1])

poke_dex["Machoc"] = \
    (
        9,
        LIEUX_RFVF[40],
        LIEUX_RFVF[53][1],
        LIEUX_RFVF[47]
    )
poke_dex["Machopeur"] = (9, LIEUX_RFVF[37], LIEUX_RFVF[53][1], LIEUX_RFVF[47])
poke_dex["Mackogneur"] = (9, SPECIFIC_EVOLUTION[1])

poke_dex["Chetiflor"] = (2, LIEUX_RFVF[54][0], LIEUX_RFVF[55][0], LIEUX_RFVF[58][0], LIEUX_RFVF[4], LIEUX_RFVF[5], LIEUX_RFVF[6], LIEUX_RFVF[11], LIEUX_RFVF[12],
                         LIEUX_RFVF[13], LIEUX_RFVF[14], LIEUX_RFVF[23], LIEUX_RFVF[24])
poke_dex["Boustiflor"] = (2, LIEUX_RFVF[54][0], LIEUX_RFVF[55][0], LIEUX_RFVF[58][0], LIEUX_RFVF[11], LIEUX_RFVF[12], LIEUX_RFVF[13], LIEUX_RFVF[14])
poke_dex["Empiflor"] = (2, SPECIFIC_EVOLUTION[5])

poke_dex["Tentacool"] = (9, LIEUX_RFVF[26], LIEUX_RFVF[27], LIEUX_RFVF[53][0], LIEUX_RFVF[55][0], LIEUX_RFVF[56][0], LIEUX_RFVF[57][0], LIEUX_RFVF[58][0], LIEUX_RFVF[59][0], LIEUX_RFVF[32],
                         LIEUX_RFVF[44], LIEUX_RFVF[3], LIEUX_RFVF[9], LIEUX_RFVF[10], LIEUX_RFVF[11], LIEUX_RFVF[12], LIEUX_RFVF[18],
                         LIEUX_RFVF[19], LIEUX_RFVF[20], LIEUX_RFVF[23])
poke_dex["Tentacruel"] = (9, LIEUX_RFVF[53][0], LIEUX_RFVF[55][0], LIEUX_RFVF[56][0], LIEUX_RFVF[57][0], LIEUX_RFVF[58][0], LIEUX_RFVF[59][0])

poke_dex["Racaillou"] = (9, LIEUX_RFVF[37], LIEUX_RFVF[40], LIEUX_RFVF[53][0], LIEUX_RFVF[59][0], LIEUX_RFVF[53][1], LIEUX_RFVF[43])
poke_dex["Gravalanch"] = (9, LIEUX_RFVF[37], LIEUX_RFVF[40], LIEUX_RFVF[53][0], LIEUX_RFVF[59][0], LIEUX_RFVF[53][1])
poke_dex["Grolem"] = (9, SPECIFIC_EVOLUTION[1])

poke_dex["Ponyta"] = (9, LIEUX_RFVF[53][0], LIEUX_RFVF[53][1])
poke_dex["Galopa"] = (9, LIEUX_RFVF[53][0], LIEUX_RFVF[53][1])

poke_dex["Ramoloss"] = (2, LIEUX_RFVF[26], LIEUX_RFVF[27], LIEUX_RFVF[37], LIEUX_RFVF[29], LIEUX_RFVF[53][0], LIEUX_RFVF[54][0], LIEUX_RFVF[55][0],
                        LIEUX_RFVF[56][0], LIEUX_RFVF[57][0], LIEUX_RFVF[58][0], LIEUX_RFVF[59][0], LIEUX_RFVF[41], LIEUX_RFVF[31], LIEUX_RFVF[32], LIEUX_RFVF[44],
                        LIEUX_RFVF[45], LIEUX_RFVF[33], LIEUX_RFVF[3], LIEUX_RFVF[5], LIEUX_RFVF[9], LIEUX_RFVF[10], LIEUX_RFVF[11],
                        LIEUX_RFVF[12], LIEUX_RFVF[18], LIEUX_RFVF[19], LIEUX_RFVF[20], LIEUX_RFVF[21], LIEUX_RFVF[22],
                        LIEUX_RFVF[23], LIEUX_RFVF[24])
poke_dex["Flagadoss"] = (2, LIEUX_RFVF[37], LIEUX_RFVF[54][0], LIEUX_RFVF[55][0], LIEUX_RFVF[41])

poke_dex["Magneti"] = (9, LIEUX_RFVF[38])
poke_dex["Magneton"] = (9, LIEUX_RFVF[37], LIEUX_RFVF[38])

poke_dex["Canarticho"] = (9, LIEUX_RFVF[28])

poke_dex["Doduo"] = (9, LIEUX_RFVF[45], LIEUX_RFVF[15], LIEUX_RFVF[16], LIEUX_RFVF[17])
poke_dex["Dodrio"] = (9, SPECIFIC_EVOLUTION[0])

poke_dex["Otaria"] = (9, LIEUX_RFVF[56][0], LIEUX_RFVF[41])
poke_dex["Lamantine"] = (9, LIEUX_RFVF[56][0], LIEUX_RFVF[41])

poke_dex["Tadmorv"] = (9, LIEUX_RFVF[29], LIEUX_RFVF[42])
poke_dex["Grotadmorv"] = (2, LIEUX_RFVF[42])

poke_dex["Kokiyas"] = (1, LIEUX_RFVF[27], LIEUX_RFVF[53][0], LIEUX_RFVF[56][0], LIEUX_RFVF[32], LIEUX_RFVF[44], LIEUX_RFVF[24])
poke_dex["Crustabri"] = (91, 1, SPECIFIC_EVOLUTION[2])

print(LIEUX_RFVF[59][2][0])
