from economy import Economy

economy = Economy(
    id="BLACK_GOLD_AND_FIRE",
    numeric_id=8,
    # as of May 2015 the following cargos must have fixed positions if used by an economy:
    # passengers: 0, mail: 2, goods 5, food 11
    # keep the rest of the cargos alphabetised
    # bump the min. compatible version if this list changes
    cargos=[
        "passengers",
        "building_materials",
        "mail", 
        "chemicals",
        "coal",
        "goods",
        "coke",
        "engineering_supplies",
        "iron_ore",
        "limestone",
        "logs",
        "food",
        "petrol",
        "pig_iron",
        "quicklime",
        "recyclables",
        "scrap_metal",
        "slag",
        "steel",
        "steel_sections",
        "steel_wire_rod",
        "stone",
        "timber",
        "vehicles",
        
    ],
    # as of March 2021 this cargoflow tuning is a temporary patch up, might need more work
    cargoflow_graph_tuning={
        "group_edges_subgraphs": [],
        "ranking_subgraphs": [
            ("sink", ["port", "T_town_industries"]),
        ],
        "clusters": [
            # {"nodes": [], "rank": "", "color": ""},
        ],
    },
)
