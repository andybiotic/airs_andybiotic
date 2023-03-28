from industry import IndustryTertiary, TileLocationChecks

industry = IndustryTertiary(
    id="coal_stage",
    accept_cargo_types=["COAL"],
    prob_in_game="2",
    prob_map_gen="6",
    map_colour="61",
    special_flags=["IND_FLAG_BUILT_ON_WATER"],
    location_checks=dict(same_type_distance=16),
    prospect_chance="0.75",
    name="string(STR_IND_COAL_STAGE)",
    nearby_station_name="string(STR_STATION_INDUSTRY_HARBOUR_3)",
    fund_cost_multiplier="152",
    override_default_construction_states=True,    
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
)

industry.enable_in_economy(
    "BLACK_GOLD_AND_FIRE",
    fund_cost_multiplier="18",
)

industry.add_tile(
    id="coal_stage_tile_1",
    land_shape_flags="bitmask(LSF_ONLY_ON_FLAT_LAND)",
    location_checks=TileLocationChecks(always_allow_founder=False),
)
industry.add_tile(
    id="coal_stage_tile_2",
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    location_checks=TileLocationChecks(always_allow_founder=False, require_coast=True),
)

# empty tile
# covered store
# small_hut
# coal_jetty_a
# coal_jetty_b
# warehouse
# loader (4 angles)
# boat 1
# boat 2

sprite_ground = industry.add_sprite(sprite_number="GROUNDSPRITE_WATER")
spriteset_ground_empty = industry.add_spriteset(type="empty")
spriteset_concrete = industry.add_spriteset(
    sprites=[(10, 10, 64, 39, -31, -8)],
    always_draw=1,
)
spriteset_conveyor_nw_se = industry.add_spriteset(
    sprites=[(80, 10, 64, 39, -31, -8)],
)
spriteset_conveyor_ne_sw = industry.add_spriteset(
    sprites=[(150, 10, 64, 39, -31, -8)],
)
spriteset_coal_pile_a = industry.add_spriteset(
    sprites=[(220, 10, 64, 39, -31, -8)],
)
spriteset_coal_pile_b = industry.add_spriteset(
    sprites=[(290, 10, 64, 39, -31, -8)],
)
spriteset_coal_pile_c = industry.add_spriteset(
    sprites=[(360, 10, 64, 39, -31, -8)],
)
spriteset_jetty_se_nw = industry.add_spriteset(
    sprites=[(10, 60, 64, 39, -31, -7)],
)
spriteset_jetty_ne_sw = industry.add_spriteset(
    sprites=[(80, 60, 64, 39, -31, -7)], always_draw=1
)
spriteset_jetty_slope_nw_se = industry.add_spriteset(
    sprites=[(150, 60, 64, 39, -31, -7)],
)
spriteset_jetty_slope_ne_sw = industry.add_spriteset(
    sprites=[(220, 60, 64, 39, -31, -7)],
)
spriteset_jetty_slope_se_nw = industry.add_spriteset(
    sprites=[(290, 60, 64, 39, -31, -7)],
)
spriteset_jetty_slope_sw_ne = industry.add_spriteset(
    sprites=[(360, 60, 64, 39, -31, -7)],
)
spriteset_small_hut = industry.add_spriteset(
    sprites=[(440, 10, 64, 84, -31, -43)], zoffset=18
)
spriteset_coal_jetty_a = industry.add_spriteset(
    sprites=[(510, 10, 64, 84, -35, -61)],
)
spriteset_coal_jetty_b = industry.add_spriteset(
    sprites=[(580, 10, 64, 84, -31, -61)],
)
spriteset_warehouse = industry.add_spriteset(
    sprites=[(650, 10, 64, 84, -31, -61)],
)
spriteset_coast_loader_se_nw = industry.add_spriteset(
    sprites=[(720, 10, 64, 84, -31, -61)],
)
spriteset_coast_loader_ne_sw = industry.add_spriteset(
    sprites=[(790, 10, 64, 84, -31, -61)],
)
spriteset_large_loader_ne_sw = industry.add_spriteset(
    sprites=[(440, 110, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_large_loader_nw_se = industry.add_spriteset(
    sprites=[(510, 110, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_large_loader_se_nw = industry.add_spriteset(
    sprites=[(580, 110, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_large_loader_sw_ne = industry.add_spriteset(
    sprites=[(650, 110, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_coast_loader_nw_se = industry.add_spriteset(
    sprites=[(720, 110, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_coast_loader_sw_ne = industry.add_spriteset(
    sprites=[(790, 110, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_boat_1 = industry.add_spriteset(
    sprites=[(10, 110, 64, 39, -35, -15)],
)
spriteset_boat_2 = industry.add_spriteset(
    sprites=[(80, 110, 64, 39, -40, -12)],
)
spriteset_boat_3 = industry.add_spriteset(
    sprites=[(150, 110, 64, 39, -13, -19)],
)
spriteset_boat_4 = industry.add_spriteset(
    sprites=[(220, 110, 64, 39, -27, -12)],
)
spriteset_boat_5 = industry.add_spriteset(
    sprites=[(290, 110, 64, 39, -15, -11)],
)
spriteset_boat_6 = industry.add_spriteset(
    sprites=[(360, 110, 64, 39, -25, -20)],
)
spriteset_boat_7 = industry.add_spriteset(
    sprites=[(360, 110, 64, 39, -29, -5)],
)
spriteset_boat_8 = industry.add_spriteset(
    sprites=[(290, 110, 64, 39, -32, -21)],
)
industry.add_spritelayout(
    id="coal_stage_spritelayout_conveyor_nw_se",
    tile="coal_stage_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_conveyor_nw_se,
    ],
)
industry.add_spritelayout(
    id="coal_stage_spritelayout_conveyor_ne_sw",
    tile="coal_stage_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_conveyor_ne_sw,
    ],
)
industry.add_spritelayout(
    id="coal_stage_spritelayout_coal_jetty_a",
    tile="coal_stage_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
        building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_coal_jetty_a,
    ],
)
industry.add_spritelayout(
    id="coal_stage_spritelayout_water_barge_sw_ne",
    tile="coal_stage_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_boat_1],
)
industry.add_spritelayout(
    id="coal_stage_spritelayout_water_barge_ne_sw",
    tile="coal_stage_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_boat_2],
)
industry.add_spritelayout(
    id="coal_stage_spritelayout_water_barge_se_nw",
    tile="coal_stage_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_boat_3],
)
industry.add_spritelayout(
    id="coal_stage_spritelayout_water_barge_nw_se",
    tile="coal_stage_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_boat_4],
)
industry.add_spritelayout(
    id="coal_stage_spritelayout_water_empty",
    tile="coal_stage_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[],
)
industry.add_spritelayout(
    id="coal_stage_spritelayout_water_coaster_ne_sw",
    tile="coal_stage_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_boat_5],
)
industry.add_spritelayout(
    id="coal_stage_spritelayout_water_coaster_nw_se",
    tile="coal_stage_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_boat_6],
)
industry.add_spritelayout(
    id="coal_stage_spritelayout_water_coaster_se_nw",
    tile="coal_stage_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_boat_7],
)
industry.add_spritelayout(
    id="coal_stage_spritelayout_water_coaster_sw_ne",
    tile="coal_stage_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_boat_8],
)
industry.add_spritelayout(
    id="coal_stage_spritelayout_coal_jetty_b",
    tile="coal_stage_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_coal_jetty_b,
    ],
)
industry.add_spritelayout(
    id="coal_stage_spritelayout_loader_nw_se",
    tile="coal_stage_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_large_loader_nw_se,
    ],
)
industry.add_spritelayout(
    id="coal_stage_spritelayout_loader_sw_ne",
    tile="coal_stage_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_large_loader_sw_ne,
    ],
)
industry.add_spritelayout(
    id="coal_stage_spritelayout_loader_ne_sw",
    tile="coal_stage_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_large_loader_ne_sw,
    ],
)
industry.add_spritelayout(
    id="coal_stage_spritelayout_loader_se_nw",
    tile="coal_stage_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_large_loader_se_nw,
    ],
)
industry.add_spritelayout(
    id="coal_stage_spritelayout_jetty_empty",
    tile="coal_stage_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete],
)
industry.add_magic_spritelayout(
    type="harbour_coast_foundations",
    base_id="coal_stage_spritelayout_coast_small_hut",
    tile="coal_stage_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_small_hut],
        "foundation_sprites": {
            "ne_sw": spriteset_jetty_ne_sw,
            "se_nw": spriteset_jetty_se_nw,
            "slope_nw_se": spriteset_jetty_slope_nw_se,
            "slope_ne_sw": spriteset_jetty_slope_ne_sw,
            "slope_se_nw": spriteset_jetty_slope_se_nw,
            "slope_sw_ne": spriteset_jetty_slope_sw_ne,
        },
    },
)
industry.add_magic_spritelayout(
    type="harbour_coast_foundations",
    base_id="coal_stage_spritelayout_coast_warehouse",
    tile="coal_stage_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_warehouse],
        "foundation_sprites": {
            "ne_sw": spriteset_jetty_ne_sw,
            "se_nw": spriteset_jetty_se_nw,
            "slope_nw_se": spriteset_jetty_slope_nw_se,
            "slope_ne_sw": spriteset_jetty_slope_ne_sw,
            "slope_se_nw": spriteset_jetty_slope_se_nw,
            "slope_sw_ne": spriteset_jetty_slope_sw_ne,
        },
    },
)
industry.add_magic_spritelayout(
    type="harbour_coast_foundations",
    base_id="coal_stage_spritelayout_coast_coal_pile_a",
    tile="coal_stage_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_coal_pile_a],
        "foundation_sprites": {
            "ne_sw": spriteset_jetty_ne_sw,
            "se_nw": spriteset_jetty_se_nw,
            "slope_nw_se": spriteset_jetty_slope_nw_se,
            "slope_ne_sw": spriteset_jetty_slope_ne_sw,
            "slope_se_nw": spriteset_jetty_slope_se_nw,
            "slope_sw_ne": spriteset_jetty_slope_sw_ne,
        },
    },
)
industry.add_magic_spritelayout(
    type="harbour_coast_foundations",
    base_id="coal_stage_spritelayout_coast_coal_pile_b",
    tile="coal_stage_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_coal_pile_b],
        "foundation_sprites": {
            "ne_sw": spriteset_jetty_ne_sw,
            "se_nw": spriteset_jetty_se_nw,
            "slope_nw_se": spriteset_jetty_slope_nw_se,
            "slope_ne_sw": spriteset_jetty_slope_ne_sw,
            "slope_se_nw": spriteset_jetty_slope_se_nw,
            "slope_sw_ne": spriteset_jetty_slope_sw_ne,
        },
    },
)
industry.add_magic_spritelayout(
    type="harbour_coast_foundations",
    base_id="coal_stage_spritelayout_coast_coal_pile_c",
    tile="coal_stage_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_coal_pile_c],
        "foundation_sprites": {
            "ne_sw": spriteset_jetty_ne_sw,
            "se_nw": spriteset_jetty_se_nw,
            "slope_nw_se": spriteset_jetty_slope_nw_se,
            "slope_ne_sw": spriteset_jetty_slope_ne_sw,
            "slope_se_nw": spriteset_jetty_slope_se_nw,
            "slope_sw_ne": spriteset_jetty_slope_sw_ne,
        },
    },
)
industry.add_magic_spritelayout(
    type="harbour_coast_foundations",
    base_id="coal_stage_spritelayout_coast_loader_nw_se",
    tile="coal_stage_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_coast_loader_nw_se],
        "foundation_sprites": {
            "ne_sw": spriteset_jetty_ne_sw,
            "se_nw": spriteset_jetty_se_nw,
            "slope_nw_se": spriteset_jetty_slope_nw_se,
            "slope_ne_sw": spriteset_jetty_slope_ne_sw,
            "slope_se_nw": spriteset_jetty_slope_se_nw,
            "slope_sw_ne": spriteset_jetty_slope_sw_ne,
        },
    },
)
industry.add_magic_spritelayout(
    type="harbour_coast_foundations",
    base_id="coal_stage_spritelayout_coast_loader_sw_ne",
    tile="coal_stage_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_coast_loader_sw_ne],
        "foundation_sprites": {
            "ne_sw": spriteset_jetty_ne_sw,
            "se_nw": spriteset_jetty_se_nw,
            "slope_nw_se": spriteset_jetty_slope_nw_se,
            "slope_ne_sw": spriteset_jetty_slope_ne_sw,
            "slope_se_nw": spriteset_jetty_slope_se_nw,
            "slope_sw_ne": spriteset_jetty_slope_sw_ne,
        },
    },
)
industry.add_magic_spritelayout(
    type="harbour_coast_foundations",
    base_id="coal_stage_spritelayout_coast_loader_ne_sw",
    tile="coal_stage_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_coast_loader_ne_sw],
        "foundation_sprites": {
            "ne_sw": spriteset_jetty_ne_sw,
            "se_nw": spriteset_jetty_se_nw,
            "slope_nw_se": spriteset_jetty_slope_nw_se,
            "slope_ne_sw": spriteset_jetty_slope_ne_sw,
            "slope_se_nw": spriteset_jetty_slope_se_nw,
            "slope_sw_ne": spriteset_jetty_slope_sw_ne,
        },
    },
)
industry.add_magic_spritelayout(
    type="harbour_coast_foundations",
    base_id="coal_stage_spritelayout_coast_loader_se_nw",
    tile="coal_stage_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_coast_loader_se_nw],
        "foundation_sprites": {
            "ne_sw": spriteset_jetty_ne_sw,
            "se_nw": spriteset_jetty_se_nw,
            "slope_nw_se": spriteset_jetty_slope_nw_se,
            "slope_ne_sw": spriteset_jetty_slope_ne_sw,
            "slope_se_nw": spriteset_jetty_slope_se_nw,
            "slope_sw_ne": spriteset_jetty_slope_sw_ne,
        },
    },
)
industry.add_industry_layout(
    id="coal_stage_industry_layout_1",
    layout=[
        (0, 1, "spritelayout_null_water"),
        (0, 2, "spritelayout_null_water"),
        (1, 1, "coal_stage_spritelayout_loader_se_nw"),
        (1, 2, "coal_stage_spritelayout_conveyor_nw_se"),
        (1, 3, "coal_stage_spritelayout_coast_loader_nw_se"),
        (2, 1, "coal_stage_spritelayout_water_coaster_nw_se"),
        (2, 2, "coal_stage_spritelayout_coal_jetty_a"),
        (2, 3, "coal_stage_spritelayout_coast_warehouse"),
        (3, 1, "spritelayout_null_water"),
        (3, 2, "coal_stage_spritelayout_jetty_empty"),
        (3, 3, "coal_stage_spritelayout_coast_small_hut"),
        (4, 1, "coal_stage_spritelayout_loader_se_nw"),
        (4, 2, "coal_stage_spritelayout_conveyor_nw_se"),
        (4, 3, "coal_stage_spritelayout_coast_loader_nw_se"),
        (5, 1, "spritelayout_null_water"),
        (5, 2, "spritelayout_null_water"),
    ],
)
industry.add_industry_layout(
    id="coal_stage_industry_layout_2",
    layout=[
        (0, 0, "spritelayout_null_water"),
        (0, 1, "coal_stage_spritelayout_loader_ne_sw"),
        (0, 2, "spritelayout_null_water"),
        (0, 3, "coal_stage_spritelayout_water_coaster_ne_sw"),
        (0, 4, "coal_stage_spritelayout_loader_ne_sw"),
        (0, 5, "spritelayout_null_water"),
        (1, 0, "spritelayout_null_water"),
        (1, 1, "coal_stage_spritelayout_conveyor_ne_sw"),
        (1, 2, "coal_stage_spritelayout_jetty_empty"),
        (1, 3, "coal_stage_spritelayout_jetty_empty"),
        (1, 4, "coal_stage_spritelayout_conveyor_ne_sw"),
        (1, 5, "spritelayout_null_water"),
        (2, 1, "coal_stage_spritelayout_coast_loader_sw_ne"),
        (2, 2, "coal_stage_spritelayout_coast_coal_pile_a"),
        (2, 3, "coal_stage_spritelayout_coast_small_hut"),
        (2, 4, "coal_stage_spritelayout_coast_loader_sw_ne"),
    ],
)
industry.add_industry_layout(
    id="coal_stage_industry_layout_3",
    layout=[
        (0, 1, "coal_stage_spritelayout_coast_loader_ne_sw"),
        (0, 2, "coal_stage_spritelayout_coast_coal_pile_b"),
        (0, 3, "coal_stage_spritelayout_coast_loader_ne_sw"),
        (0, 4, "coal_stage_spritelayout_coast_small_hut"),
        (0, 5, "coal_stage_spritelayout_coast_loader_ne_sw"),
        (1, 0, "spritelayout_null_water"),
        (1, 1, "coal_stage_spritelayout_loader_sw_ne"),
        (1, 2, "coal_stage_spritelayout_water_coaster_sw_ne"),
        (1, 3, "coal_stage_spritelayout_loader_sw_ne"),
        (1, 4, "spritelayout_null_water"),
        (1, 5, "coal_stage_spritelayout_loader_sw_ne"),
        (1, 6, "spritelayout_null_water"),
    ],
)
industry.add_industry_layout(
    id="coal_stage_industry_layout_4",
    layout=[
        (0, 1, "spritelayout_null_water"),
        (0, 2, "spritelayout_null_water"),
        (0, 3, "spritelayout_null_water"),
        (1, 0, "coal_stage_spritelayout_coast_loader_se_nw"),
        (1, 1, "coal_stage_spritelayout_conveyor_nw_se"),
        (1, 2, "coal_stage_spritelayout_loader_nw_se"),
        (1, 3, "spritelayout_null_water"),
        (2, 0, "coal_stage_spritelayout_coast_coal_pile_c"),
        (2, 1, "coal_stage_spritelayout_water_coaster_se_nw"),
        (2, 2, "spritelayout_null_water"),
        (2, 3, "spritelayout_null_water"),
        (3, 0, "coal_stage_spritelayout_coast_warehouse"),
        (3, 1, "coal_stage_spritelayout_jetty_empty"),
        (3, 2, "coal_stage_spritelayout_coal_jetty_a"),
        (3, 3, "spritelayout_null_water"),
        (4, 0, "coal_stage_spritelayout_coast_loader_se_nw"),
        (4, 1, "coal_stage_spritelayout_conveyor_nw_se"),
        (4, 2, "coal_stage_spritelayout_loader_nw_se"),
        (4, 5, "spritelayout_null_water"),
        (5, 1, "spritelayout_null_water"),
        (5, 2, "spritelayout_null_water"),
        (5, 3, "spritelayout_null_water"),
        (5, 4, "spritelayout_null_water"),
    ],
)
