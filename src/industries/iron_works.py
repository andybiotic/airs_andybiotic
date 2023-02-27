from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="iron_works",
    accept_cargos_with_input_ratios=[
        ("IORE", 3),
        ("COAL", 3),
    ],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[
        ("STEL", 8),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="196",
    name="string(STR_IND_IRON_WORKS)",
    nearby_station_name="string(STR_STATION_FURNACE)",
    fund_cost_multiplier="69",
    expiry_year=1905,
    provides_snow=True,
)

industry.enable_in_economy(
    "BLACK_GOLD_AND_FIRE",
    prod_cargo_types_with_output_ratios=[
        ("IRON", 6),
    ],
    fund_cost_multiplier="18",
)

# not animated tiles
industry.add_tile(
    id="iron_works_tile_1",
    location_checks=TileLocationChecks(disallow_industry_adjacent=True),
)
# animated tiles
industry.add_tile(
    id="iron_works_tile_2",
    animation_length=180,
    animation_looping=True,
    animation_speed=2,
    custom_animation_control={
        "macro": "random_first_frame",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)",
    },
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)
industry.add_tile(
    id="iron_works_tile_3",
    animation_length=3,
    animation_looping=True,
    animation_speed=8,
    custom_animation_control={
        "macro": "random_first_frame",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)",
    },
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)


spriteset_ground = industry.add_spriteset(
    type="cobble",
)
spriteset_ground_overlay = industry.add_spriteset(
    type="empty",
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 70, -31, -40)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 70, -31, -39)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 70, -31, -39)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(430, 10, 64, 70, -31, -39)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(500, 10, 64, 70, -31, -39)],
)
spriteset_iron_pigs_anim = industry.add_spriteset(
    sprites=[
        (220, 10, 64, 70, -31, -39),
        (290, 10, 64, 70, -31, -39),
        (360, 10, 64, 70, -31, -39),
    ],
    animation_rate=1,
)
spriteset_ground_pigs = industry.add_spriteset(
    type="cobble",
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_iron_pigs_anim.sprites),
)
spriteset_ground_overlay_pigs = industry.add_spriteset(
    type="empty",
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_iron_pigs_anim.sprites),
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="dark_smoke_small",
    xoffset=0,
    yoffset=4,
    zoffset=23,
)

industry.add_spritelayout(
    id="iron_works_spritelayout_furnace_anim",
    tile="iron_works_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    smoke_sprites=[sprite_smoke],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="iron_works_spritelayout_large_shed",
    tile="iron_works_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=[],
)
industry.add_spritelayout(
    id="iron_works_spritelayout_large_shed_clerestory_roof",
    tile="iron_works_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=[],
)
industry.add_spritelayout(
    id="iron_works_spritelayout_iron_pigs_anim",
    tile="iron_works_tile_2",
    ground_sprite=spriteset_ground_pigs,
    ground_overlay=spriteset_ground_overlay_pigs,
    building_sprites=[spriteset_iron_pigs_anim],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="iron_works_spritelayout_staithes",
    tile="iron_works_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne"],
)
industry.add_spritelayout(
    id="iron_works_spritelayout_logs",
    tile="iron_works_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se"],
)
industry.add_spritelayout(
    id="iron_works_spritelayout_empty",
    tile="iron_works_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se"],
)
industry.add_industry_layout(
    id="iron_works_industry_layout_1",
    layout=[
        (0, 0, "iron_works_spritelayout_large_shed_clerestory_roof"),
        (0, 1, "iron_works_spritelayout_empty"),
        (0, 2, "iron_works_spritelayout_empty"),
        (1, 0, "iron_works_spritelayout_large_shed_clerestory_roof"),
        (1, 1, "iron_works_spritelayout_empty"),
        (1, 2, "iron_works_spritelayout_empty"),
        (2, 0, "iron_works_spritelayout_large_shed"),
        (2, 1, "iron_works_spritelayout_staithes"),
        (2, 2, "iron_works_spritelayout_logs"),
    ],
)
