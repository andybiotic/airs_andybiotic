from industry import IndustrySecondary, TileLocationChecks

# !! Basic Goods Factory
# !! layout names will need set correctly
industry = IndustrySecondary(
    id="factory_1",
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
    prob_map_gen="6",
    map_colour="166",
    name="string(STR_IND_FACTORY_1)",
    nearby_station_name="string(STR_STATION_FACTORY_1)",
    fund_cost_multiplier="95",
)

industry.enable_in_economy(
    "PLAINS_TRAINS_AND_STEEL",
    accept_cargos_with_input_ratios=[
        ("STSE", 4),
        ("COAL", 1),
    ],
    prod_cargo_types_with_output_ratios=[
        ("GOOD", 4),
    ],
    fund_cost_multiplier="11",
)

industry.add_tile(
    id="factory_1_tile_1",
    animation_length=47,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="cobble",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 60, 64, 70, -31, -39)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 60, 64, 70, -31, -39)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 60, 64, 70, -31, -39)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 60, 64, 51, -31, -20)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 60, 64, 70, -31, -39)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 60, 64, 31, -31, 0)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 60, 64, 31, -31, 0)],
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="dark_smoke_small",
    xoffset=0,
    yoffset=8,
    zoffset=53,
)

industry.add_spritelayout(
    id="factory_1_spritelayout_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    smoke_sprites=[sprite_smoke],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="factory_1_spritelayout_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="factory_1_spritelayout_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se"],
)
industry.add_spritelayout(
    id="factory_1_spritelayout_4",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se"],
)
industry.add_spritelayout(
    id="factory_1_spritelayout_5",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se"],
)
industry.add_spritelayout(
    id="factory_1_spritelayout_6",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="factory_1_spritelayout_7",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="factory_1_industry_layout_1",
    layout=[
        (0, 0, "factory_1_tile_1", "factory_1_spritelayout_3"),
        (0, 1, "factory_1_tile_1", "factory_1_spritelayout_3"),
        (0, 2, "factory_1_tile_1", "factory_1_spritelayout_5"),
        (0, 3, "factory_1_tile_1", "factory_1_spritelayout_4"),
        (0, 4, "factory_1_tile_1", "factory_1_spritelayout_5"),
        (1, 0, "factory_1_tile_1", "factory_1_spritelayout_3"),
        (1, 1, "factory_1_tile_1", "factory_1_spritelayout_3"),
        (1, 2, "factory_1_tile_1", "factory_1_spritelayout_7"),
        (1, 3, "factory_1_tile_1", "factory_1_spritelayout_4"),
        (1, 4, "factory_1_tile_1", "factory_1_spritelayout_6"),
        (2, 0, "factory_1_tile_1", "factory_1_spritelayout_3"),
        (2, 1, "factory_1_tile_1", "factory_1_spritelayout_1"),
        (2, 2, "factory_1_tile_1", "factory_1_spritelayout_2"),
        (2, 3, "factory_1_tile_1", "factory_1_spritelayout_7"),
        (2, 4, "factory_1_tile_1", "factory_1_spritelayout_7"),
    ],
)
industry.add_industry_layout(
    id="factory_1_industry_layout_2",
    layout=[
        (0, 2, "factory_1_tile_1", "factory_1_spritelayout_3"),
        (0, 3, "factory_1_tile_1", "factory_1_spritelayout_3"),
        (1, 0, "factory_1_tile_1", "factory_1_spritelayout_1"),
        (1, 1, "factory_1_tile_1", "factory_1_spritelayout_2"),
        (1, 2, "factory_1_tile_1", "factory_1_spritelayout_3"),
        (1, 3, "factory_1_tile_1", "factory_1_spritelayout_3"),
        (2, 0, "factory_1_tile_1", "factory_1_spritelayout_4"),
        (2, 1, "factory_1_tile_1", "factory_1_spritelayout_7"),
        (2, 2, "factory_1_tile_1", "factory_1_spritelayout_6"),
        (2, 3, "factory_1_tile_1", "factory_1_spritelayout_6"),
        (3, 0, "factory_1_tile_1", "factory_1_spritelayout_4"),
        (3, 1, "factory_1_tile_1", "factory_1_spritelayout_5"),
        (3, 2, "factory_1_tile_1", "factory_1_spritelayout_4"),
        (3, 3, "factory_1_tile_1", "factory_1_spritelayout_7"),
    ],
)
