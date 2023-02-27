from industry import IndustrySecondary, TileLocationChecks

# !! Modern Goods Factory
# !! layout names will need set correctly
industry = IndustrySecondary(
    id="factory_2",
    accept_cargos_with_input_ratios=[
        ("VPTS", 2),
        ("STEL", 2),
        ("PLAS", 2),
    ],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[
        ("GOOD", 6),
    ],
    prob_in_game="7",
    prob_map_gen="8",
    map_colour="170",
    name="string(STR_IND_FACTORY_2)",
    nearby_station_name="string(STR_STATION_INDUSTRY_ESTATE_1)",
    fund_cost_multiplier="95",
)

industry.add_tile(
    id="factory_2_tile_1",
    animation_length=47,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

industry.enable_in_economy(
    "PLAINS_TRAINS_AND_STEEL",
    accept_cargos_with_input_ratios=[
        ("ALUM", 4),
        ("STSE", 6),
        ("RFPR", 2),
    ],
    prod_cargo_types_with_output_ratios=[
        ("GOOD", 8),
    ],
    fund_cost_multiplier="11",
    intro_year="1965",
)

industry.enable_in_economy(
    "BLACK_GOLD_AND_FIRE",
    accept_cargos_with_input_ratios=[
        ("STSE", 8),
        ("RFPR", 3),
    ],
    prod_cargo_types_with_output_ratios=[
        ("GOOD", 8),
    ],
    fund_cost_multiplier="11",
    intro_year="1965",
)

spriteset_ground = industry.add_spriteset(
    type="concrete",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 60, 64, 70, -31, -39)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 60, 64, 70, -31, -39)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 60, 64, 51, -31, -20)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 60, 64, 51, -31, -20)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 60, 64, 51, -31, -20)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 60, 64, 31, -31, 0)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 60, 64, 31, -31, 0)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(290, 121, 64, 51, -31, -20)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(10, 10, 64, 31, -31, 0)],
)

industry.add_spritelayout(
    id="factory_2_spritelayout_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_spritelayout(
    id="factory_2_spritelayout_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="factory_2_spritelayout_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se"],
)
industry.add_spritelayout(
    id="factory_2_spritelayout_4",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="factory_2_spritelayout_5",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se"],
)
industry.add_spritelayout(
    id="factory_2_spritelayout_6",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="factory_2_spritelayout_7",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="factory_2_spritelayout_8",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="factory_2_spritelayout_9",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
)

industry.add_industry_layout(
    id="factory_2_industry_layout_1",
    layout=[
        (0, 0, "factory_2_tile_1", "factory_2_spritelayout_5"),
        (0, 1, "factory_2_tile_1", "factory_2_spritelayout_5"),
        (0, 2, "factory_2_tile_1", "factory_2_spritelayout_3"),
        (0, 3, "factory_2_tile_1", "factory_2_spritelayout_1"),
        (1, 0, "factory_2_tile_1", "factory_2_spritelayout_5"),
        (1, 1, "factory_2_tile_1", "factory_2_spritelayout_5"),
        (1, 2, "factory_2_tile_1", "factory_2_spritelayout_6"),
        (1, 3, "factory_2_tile_1", "factory_2_spritelayout_9"),
        (2, 0, "factory_2_tile_1", "factory_2_spritelayout_2"),
        (2, 1, "factory_2_tile_1", "factory_2_spritelayout_6"),
        (2, 2, "factory_2_tile_1", "factory_2_spritelayout_8"),
        (2, 3, "factory_2_tile_1", "factory_2_spritelayout_4"),
    ],
)
industry.add_industry_layout(
    id="factory_2_industry_layout_2",
    layout=[
        (0, 2, "factory_2_tile_1", "factory_2_spritelayout_8"),
        (0, 3, "factory_2_tile_1", "factory_2_spritelayout_4"),
        (1, 0, "factory_2_tile_1", "factory_2_spritelayout_5"),
        (1, 1, "factory_2_tile_1", "factory_2_spritelayout_5"),
        (1, 2, "factory_2_tile_1", "factory_2_spritelayout_2"),
        (1, 3, "factory_2_tile_1", "factory_2_spritelayout_9"),
        (2, 0, "factory_2_tile_1", "factory_2_spritelayout_5"),
        (2, 1, "factory_2_tile_1", "factory_2_spritelayout_5"),
        (2, 2, "factory_2_tile_1", "factory_2_spritelayout_3"),
        (2, 3, "factory_2_tile_1", "factory_2_spritelayout_7"),
        (3, 0, "factory_2_tile_1", "factory_2_spritelayout_5"),
        (3, 1, "factory_2_tile_1", "factory_2_spritelayout_5"),
        (3, 2, "factory_2_tile_1", "factory_2_spritelayout_6"),
        (3, 3, "factory_2_tile_1", "factory_2_spritelayout_1"),
    ],
)
