# Definition of numeric IDs for industries
industry_numeric_ids = dict(coal_mine = 0,
                            lime_kiln = 1,
                            metal_fabrication_plant = 2,
                            # unused = 3,
                            iron_ore_mine = 4,
                            # unused = 5,
                            smithy_forge = 6,
                            blast_furnace = 7,
                            aluminium_plant = 8,
                            metal_workshop = 9,
                            quarry = 10,
                            forest = 11,
                            sawmill = 12,
                            furniture_factory = 13,
                            paper_mill = 14,
                            oil_wells = 15,
                            oil_rig = 16,
                            oil_refinery = 17,
                            plastics_plant = 18,
                            sugar_refinery = 19,
                            dredging_site = 20,
                            iron_works = 21,
                            glass_works = 22,
                            recycling_plant = 23,
                            recycling_depot = 24,
                            junk_yard = 25,
                            arable_farm = 26,
                            sheep_farm = 27,
                            dairy_farm = 28,
                            mixed_farm = 29,
                            fruit_plantation = 30,
                            fishing_harbour = 31,
                            fishing_grounds = 32,
                            basic_farm = 33,
                            flour_mill = 34,
                            brewery = 35,
                            dairy = 36,
                            stockyard = 37,
                            machine_shop = 38,
                            port = 39,
                            fertiliser_plant = 40,
                            lumber_yard = 41,
                            textile_mill = 42,
                            cement_plant = 43,
                            clay_pit = 44,
                            brick_works = 45,
                            biorefinery = 46,
                            orchard_piggery = 47,
                            ranch = 48,
                            chemical_plant = 49,
                            coffee_estate = 50,
                            bulk_terminal = 51,
                            trading_post = 52,
                            rubber_plantation = 53,
                            # unused = 54,
                            diamond_mine = 55,
                            food_processor = 56,
                            hardware_store = 57,
                            hotel = 58,
                            food_market = 59,
                            petrol_pump = 60,
                            general_store = 61,
                            assembly_plant = 62,
                            builders_yard = 63,
                            copper_mine = 64,
                            nitrate_mine = 65,
                            power_plant = 66,
                            copper_refinery = 67,
                            vineyard = 68,
                            supply_yard = 69,
                            tyre_plant = 70,
                            pyrite_mine = 71,
                            pyrite_smelter = 72,
                            phosphate_mine = 73,
                            liquids_terminal = 74,
                            manganese_mine = 75,
                            potash_mine = 76,
                            basic_oxygen_furnace = 77,
                            coke_oven = 78,
                            electric_arc_furnace = 79,
                            slag_grinding_plant = 80,
                            foundry = 81,
                            # unused = 82,
                            # unused = 83,
                            # unused = 84,
                            hunting_camp = 85,
                            soda_ash_mine = 86)
#127 is last ID to be used (128 industry limit, zero-based)


# Definition of industry tile numeric IDs
# tiles 0-153 currently vacant
tile_numeric_ids = dict(soda_ash_mine_tile_1 = 142,
                        paper_mill_tile_1 = 143,
                        hunting_camp_tile_1 = 144,
                        foundry_tile_1 = 145,
                        # unused = 146,
                        # unused = 147,
                        # unused = 148,
                        # unused = 149,
                        # unused = 150,
                        slag_grinding_plant_tile_1 = 151,
                        electric_arc_furnace_tile_1 = 152,
                        coke_oven_tile_1 = 153,
                        basic_oxygen_furnace_tile_1 = 154,
                        manganese_mine_tile_1 = 155,
                        manganese_mine_tile_2 = 156,
                        manganese_mine_tile_3 = 157,
                        blast_furnace_tile_1 = 158,
                        blast_furnace_tile_2 = 159,
                        arable_farm_tile_1 = 160,
                        brewery_tile_1 = 161,
                        brewery_tile_2 = 162,
                        fertiliser_plant_tile_1 = 163,
                        builders_yard_tile_1 = 164,
                        brick_works_tile_1 = 165,
                        biorefinery_tile_1 = 166,
                        basic_farm_tile_1 = 167,
                        # unused = 168,
                        port_tile_1 = 169,
                        port_tile_2 = 170,
                        orchard_piggery_tile_1 = 171,
                        orchard_piggery_tile_2 = 172,
                        ranch_tile_1 = 173,
                        copper_mine_tile_1 = 174,
                        dairy_tile_1 = 175,
                        dairy_tile_2 = 176,
                        copper_refinery_tile_1 = 177,
                        glass_works_tile_1 = 178,
                        stockyard_tile_1 = 179,
                        dairy_farm_tile_1 = 180,
                        plastics_plant_tile_1 = 181,
                        flour_mill_tile_1 = 182,
                        textile_mill_tile_1 = 183,
                        furniture_factory_tile_1 = 184,
                        aluminium_plant_tile_1 = 185,
                        machine_shop_tile_1 = 186,
                        lumber_yard_tile_1 = 187,
                        lumber_yard_tile_2 = 188,
                        power_plant_tile_1 = 189,
                        mixed_farm_tile_1 = 190,
                        lime_kiln_tile_1 = 191,
                        sheep_farm_tile_1 = 192,
                        junk_yard_tile_1 = 193,
                        food_market_tile_1 = 194,
                        fishing_harbour_tile_1 = 195,
                        fishing_harbour_tile_2 = 196,
                        # unused = 197,
                        dredging_site_tile_1 = 198,
                        metal_workshop_tile_1 = 199,
                        metal_fabrication_plant_tile_1 = 200,
                        recycling_plant_tile_1 = 201,
                        recycling_depot_tile_1 = 202,
                        petrol_pump_tile_1 = 203,
                        fishing_grounds_tile_1 = 204,
                        TILE_FOREST_1 = 205,
                        TILE_FOREST_2 = 206,
                        fruit_plantation_tile_1 = 207,
                        fruit_plantation_tile_2 = 208,
                        smithy_forge_tile_1 = 209,
                        iron_works_tile_1 = 210,
                        iron_works_tile_2 = 211,
                        iron_works_tile_3 = 212,
                        # unused = 213,
                        sugar_refinery_tile_1 = 214,
                        oil_wells_tile_1 = 215,
                        oil_wells_tile_2 = 216,
                        hotel_tile_1 = 217,
                        hardware_store_tile_1 = 218,
                        general_store_tile_1 = 219,
                        coffee_plantation_tile_1 = 220,
                        coffee_plantation_tile_2 = 221,
                        bulk_terminal_tile_1 = 222,
                        bulk_terminal_tile_2 = 223,
                        #unused = 224,
                        trading_post_tile_1 = 225,
                        trading_post_tile_2 = 226,
                        rubber_plantation_tile_1 = 227,
                        rubber_plantation_tile_2 = 228,
                        food_processor_tile_1 = 229,
                        nitrate_mine_tile_1 = 230,
                        chemical_plant_tile_1 = 231,
                        assembly_plant_tile_1 = 232,
                        cement_plant_tile_1 = 233,
                        sawmill_tile_1 = 234,
                        oil_refinery_tile_1 = 235,
                        rubber_plantation_tile_3 = 236,
                        fruit_plantation_tile_3 = 237,
                        coffee_plantation_tile_3 = 238,
                        clay_pit_tile_1 = 239,
                        clay_pit_tile_2 = 240,
                        quarry_tile_1 = 241,
                        quarry_tile_2 = 242,
                        TILE_VINEYARD_1 = 243,
                        TILE_VINEYARD_2 = 244,
                        TILE_VINEYARD_3 = 245,
                        supply_yard_tile_1 = 246,
                        tyre_plant_tile_1 = 247,
                        pyrite_mine_tile_1 = 248,
                        pyrite_smelter_tile_1 = 249,
                        liquids_terminal_tile_1 = 250,
                        liquids_terminal_tile_2 = 251,
                        fishing_village_tile_1 = 252,
                        fishing_village_tile_2 = 253,
                        chemical_plant_tile_2 = 254)

chameleon_cache_dir =  '.chameleon_cache'

# specify location for intermediate files generated during build (nml, graphics, lang etc)
generated_files_dir =  'generated'

# this is for nml or grfcodec, don't need to use python path module here
graphics_path =  'generated/graphics/'

# OpenTTD's max date
max_game_date = 5000000

# amount of cargo required to trigger 'enhanced' production at primary industries
FARM_MINE_SUPPLY_REQUIREMENT = 16

# time window (days) for delivery of combinatory cargos to secondary industries
secondary_production_span = 90
