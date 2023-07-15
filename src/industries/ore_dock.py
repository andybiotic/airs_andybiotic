from industry import IndustryPrimaryNoSupplies, TileLocationChecks

industry = IndustryPrimaryNoSupplies(
    id="ore_dock",
    accept_cargo_types=[],
    prod_cargo_types_with_multipliers=[],
    prob_in_game="0",  # do not build during gameplay
    prob_map_gen="8",
    map_colour="45",
    special_flags=["IND_FLAG_BUILT_ON_WATER"],
    location_checks=dict(same_type_distance=16),
    prospect_chance="0.75",
    name="string(STR_IND_ORE_DOCK)",
    nearby_station_name="string(STR_STATION_INDUSTRY_HARBOUR_4)",
    fund_cost_multiplier="152",
    override_default_construction_states=True,
)

industry.enable_in_economy(
    "BLACK_GOLD_AND_FIRE",
    prod_cargo_types_with_multipliers=[
        ("IORE", 22)
    ],
    intro_year=1895,
    fund_cost_multiplier="12",
)

industry.add_tile(
    id="ore_dock_tile_1",
    land_shape_flags="bitmask(LSF_ONLY_ON_FLAT_LAND)",
    location_checks=TileLocationChecks(always_allow_founder=False),
)
industry.add_tile(
    id="ore_dock_tile_2",
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    location_checks=TileLocationChecks(always_allow_founder=False, require_coast=True),
)
sprite_ground = industry.add_sprite(sprite_number="GROUNDSPRITE_WATER")
spriteset_ground_empty = industry.add_spriteset(type="empty")
spriteset_concrete = industry.add_spriteset(
    sprites=[(10, 10, 64, 39, -31, -8)],
    always_draw=1,
)
spriteset_jetty_se_nw = industry.add_spriteset(
    sprites=[(10, 60, 64, 39, -31, -7)],
    always_draw=1,
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
spriteset_office = industry.add_spriteset(
    sprites=[(440, 10, 64, 74, -31, -34)], 
    zoffset=18
)
spriteset_coast_mineral_pile = industry.add_spriteset(
    sprites=[(510, 10, 64, 74, -31, -34)], 
    zoffset=16
)
spriteset_coast_unloader_sw = industry.add_spriteset(
    sprites=[(440, 110, 64, 74, -31, -34)], 
    zoffset=16
)
spriteset_coast_unloader_se = industry.add_spriteset(
    sprites=[(510, 110, 64, 74, -31, -34)], 
    zoffset=16
)
spriteset_coast_unloader_nw = industry.add_spriteset(
    sprites=[(580, 110, 64, 74, -31, -34)], 
    zoffset=16
)
spriteset_coast_unloader_ne = industry.add_spriteset(
    sprites=[(650, 110, 64, 74, -31, -34)], 
    zoffset=16
)
spriteset_warehouse = industry.add_spriteset(
    sprites=[(720, 110, 64, 74, -31, -34)], 
    zoffset=16
)
spriteset_loader_sw = industry.add_spriteset(
    sprites=[(10, 160, 64, 122, -31, -34)], zoffset=40
)
spriteset_loader_se = industry.add_spriteset(
    sprites=[(80, 160, 64, 122, -31, -34)], zoffset=40
)
spriteset_loader_nw = industry.add_spriteset(
    sprites=[(150, 160, 64, 122, -31, -34)], zoffset=40
)
spriteset_loader_ne = industry.add_spriteset(
    sprites=[(220, 160, 64, 122, -31, -34)], zoffset=40
)
spriteset_gantry_ne_sw = industry.add_spriteset(
    sprites=[(290, 160, 64, 122, -31, -34)], zoffset=40
)
spriteset_gantry_nw_se = industry.add_spriteset(
    sprites=[(360, 160, 64, 122, -31, -34)], zoffset=40
)
spriteset_mineral_pile_1 = industry.add_spriteset(
    sprites=[(150, 10, 64, 39, -31, 0)],
    zoffset=16,
)
spriteset_mineral_pile_2 = industry.add_spriteset(
    sprites=[(220, 10, 64, 39, -31, 0)],
    zoffset=16,
)
spriteset_checkpoint = industry.add_spriteset(
    sprites=[(290, 10, 64, 39, -31, 0)],
    zoffset=18,
)
spriteset_small_hut = industry.add_spriteset(
    sprites=[(360, 10, 64, 39, -31, 0)],
    zoffset=18,
)
spriteset_small_boat_ne_sw_east = industry.add_spriteset(
    sprites=[(10, 110, 64, 39, -35, -15)],
)
spriteset_small_boat_ne_sw_west = industry.add_spriteset(
    sprites=[(80, 110, 64, 39, -31, -14)],
)
spriteset_small_boat_nw_se_west = industry.add_spriteset(
    sprites=[(150, 110, 64, 39, -31, -8)],
)
spriteset_small_boat_nw_se_east = industry.add_spriteset(
    sprites=[(220, 110, 64, 39, -27, -12)],
)
spriteset_large_boat_ne_sw = industry.add_spriteset(
    sprites=[(290, 110, 64, 39, -15, -11)],
)
spriteset_large_boat_nw_se = industry.add_spriteset(
    sprites=[(360, 110, 64, 39, -45, -15)],
)
industry.add_spritelayout(
    id="ore_dock_spritelayout_water_empty",
    tile="ore_dock_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[],
)
industry.add_spritelayout(
    id="ore_dock_spriteset_small_hut",
    tile="ore_dock_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_small_hut,
    ],
)
industry.add_spritelayout(
    id="ore_dock_spritelayout_checkpoint",
    tile="ore_dock_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_checkpoint,
    ],
)
industry.add_spritelayout(
    id="ore_dock_spritelayout_containers_jetty_1",
    tile="ore_dock_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_concrete, spriteset_mineral_pile_1],
)
industry.add_spritelayout(
    id="ore_dock_spritelayout_containers_jetty_2",
    tile="ore_dock_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_ne_sw, spriteset_concrete, spriteset_coast_unloader_sw],
)
industry.add_spritelayout(
    id="ore_dock_spritelayout_office",
    tile="ore_dock_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_office,
    ],
)
industry.add_spritelayout(
    id="ore_dock_spritelayout_small_boat_ne_sw_east",
    tile="ore_dock_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_small_boat_ne_sw_east],
)
industry.add_spritelayout(
    id="ore_dock_spritelayout_small_boat_ne_sw_west",
    tile="ore_dock_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_small_boat_ne_sw_west],
)
industry.add_spritelayout(
    id="ore_dock_spritelayout_small_boat_nw_se_west",
    tile="ore_dock_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_small_boat_nw_se_west],
)
industry.add_spritelayout(
    id="ore_dock_spritelayout_small_boat_nw_se_east",
    tile="ore_dock_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_small_boat_nw_se_east],
)
industry.add_spritelayout(
    id="ore_dock_spritelayout_large_boat_ne_sw",
    tile="ore_dock_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_large_boat_ne_sw],
)
industry.add_spritelayout(
    id="ore_dock_spritelayout_large_boat_nw_se",
    tile="ore_dock_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_large_boat_nw_se],
)
industry.add_spritelayout(
    id="ore_dock_spritelayout_loader_sw",
    tile="ore_dock_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_loader_sw,
    ],
)
industry.add_spritelayout(
    id="ore_dock_spritelayout_loader_se",
    tile="ore_dock_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_loader_se,
    ],
)
industry.add_spritelayout(
    id="ore_dock_spritelayout_loader_nw",
    tile="ore_dock_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_loader_nw,
    ],
)
industry.add_spritelayout(
    id="ore_dock_spritelayout_loader_ne",
    tile="ore_dock_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_loader_ne,
    ],
)

industry.add_spritelayout(
    id="ore_dock_spritelayout_gantry_ne_sw",
    tile="ore_dock_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_gantry_ne_sw,
    ],
)
industry.add_spritelayout(
    id="ore_dock_spritelayout_gantry_nw_se",
    tile="ore_dock_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_gantry_nw_se,
    ],
)
industry.add_spritelayout(
    id="ore_dock_spritelayout_mineral_pile_1",
    tile="ore_dock_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_mineral_pile_1,
    ],
)
industry.add_spritelayout(
    id="ore_dock_spritelayout_mineral_pile_2",
    tile="ore_dock_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_mineral_pile_2,
    ],
)
industry.add_magic_spritelayout(
    type="harbour_coast_foundations",
    base_id="ore_dock_spritelayout_coast_checkpoint",
    tile="ore_dock_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_checkpoint],
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
    base_id="ore_dock_spritelayout_coast_office",
    tile="ore_dock_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_office],
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
    base_id="ore_dock_spritelayout_coast_warehouse",
    tile="ore_dock_tile_2",
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
    base_id="ore_dock_spritelayout_coast_mineral_pile_3",
    tile="ore_dock_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_coast_mineral_pile],
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
    base_id="ore_dock_spritelayout_coast_unloader_sw",
    tile="ore_dock_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_coast_unloader_sw],
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
    base_id="ore_dock_spritelayout_coast_unloader_se",
    tile="ore_dock_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_coast_unloader_se],
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
    base_id="ore_dock_spritelayout_coast_unloader_nw",
    tile="ore_dock_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_coast_unloader_nw],
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
    base_id="ore_dock_spritelayout_coast_unloader_ne",
    tile="ore_dock_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_coast_unloader_ne],
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
    base_id="ore_dock_spritelayout_coast_truck",
    tile="ore_dock_tile_2",
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
industry.add_industry_layout(
    id="ore_dock_industry_layout_1",
    layout=[
        (0, 0, "ore_dock_spritelayout_water_empty"),
        (0, 1, "ore_dock_spritelayout_small_boat_nw_se_west"),
        (0, 2, "ore_dock_spritelayout_mineral_pile_1"),
        (0, 3, "ore_dock_spritelayout_coast_mineral_pile_3"),
        (1, 0, "ore_dock_spritelayout_loader_se"),
        (1, 1, "ore_dock_spritelayout_gantry_nw_se"),
        (1, 2, "ore_dock_spritelayout_gantry_nw_se"),
        (1, 3, "ore_dock_spritelayout_coast_unloader_nw"),
        (2, 0, "ore_dock_spritelayout_small_boat_nw_se_east"),
        (2, 1, "ore_dock_spritelayout_water_empty"),
        (2, 2, "ore_dock_spriteset_small_hut"),
        (2, 3, "ore_dock_spritelayout_coast_office"),
        (3, 0, "ore_dock_spritelayout_water_empty"),
        (3, 1, "ore_dock_spritelayout_water_empty"),
        (3, 2, "ore_dock_spritelayout_mineral_pile_1"),
        (3, 3, "ore_dock_spritelayout_coast_mineral_pile_3"),
    ],
)
industry.add_industry_layout(
    id="ore_dock_industry_layout_2",
    layout=[
        (0, 0, "ore_dock_spritelayout_coast_mineral_pile_3"),
        (0, 1, "ore_dock_spritelayout_coast_office"),
        (0, 2, "ore_dock_spritelayout_coast_unloader_sw"),
        (0, 3, "ore_dock_spritelayout_coast_warehouse"),
        (1, 0, "ore_dock_spritelayout_small_boat_nw_se_east"),
        (1, 1, "ore_dock_spritelayout_water_empty"),
        (1, 2, "ore_dock_spritelayout_gantry_ne_sw"),
        (1, 3, "ore_dock_spritelayout_water_empty"),
        (2, 1, "ore_dock_spritelayout_water_empty"),
        (2, 2, "ore_dock_spritelayout_gantry_ne_sw"),
        (2, 3, "ore_dock_spritelayout_small_boat_ne_sw_west"),
        (3, 1, "ore_dock_spritelayout_large_boat_ne_sw"),
        (3, 2, "ore_dock_spritelayout_loader_ne"),
        (3, 3, "ore_dock_spritelayout_water_empty"),
    ],
)
industry.add_industry_layout(
    id="ore_dock_industry_layout_3",
    layout=[
        (0, 0, "ore_dock_spritelayout_coast_unloader_se"),
        (0, 1, "ore_dock_spritelayout_gantry_nw_se"),
        (0, 2, "ore_dock_spritelayout_gantry_nw_se"),
        (0, 3, "ore_dock_spritelayout_loader_nw"),
        (0, 4, "ore_dock_spritelayout_mineral_pile_1"),
        (0, 5, "spritelayout_null_water"),
        (1, 0, "ore_dock_spritelayout_coast_mineral_pile_3"),
        (1, 1, "ore_dock_spriteset_small_hut"),
        (1, 2, "ore_dock_spritelayout_small_boat_nw_se_east"),
        (1, 3, "ore_dock_spritelayout_water_empty"),
        (1, 4, "ore_dock_spritelayout_water_empty"),
        (1, 5, "spritelayout_null_water"),
        (2, 0, "ore_dock_spritelayout_coast_office"),
        (2, 1, "ore_dock_spritelayout_mineral_pile_1"),
        (2, 2, "spritelayout_null_water"),
        (3, 1, "spritelayout_null_water"),
        (3, 2, "spritelayout_null_water"),
    ],
)
industry.add_industry_layout(
    id="ore_dock_industry_layout_4",
    layout=[
        (0, 1, "spritelayout_null_water"),
        (1, 0, "ore_dock_spritelayout_water_empty"),
        (1, 1, "ore_dock_spritelayout_loader_sw"),
        (1, 2, "ore_dock_spritelayout_mineral_pile_1"),
        (1, 3, "ore_dock_spritelayout_water_empty"),
        (2, 0, "ore_dock_spritelayout_large_boat_ne_sw"),
        (2, 1, "ore_dock_spritelayout_gantry_ne_sw"),
        (2, 2, "ore_dock_spriteset_small_hut"),
        (2, 3, "ore_dock_spritelayout_water_empty"),
        (3, 0, "ore_dock_spritelayout_water_empty"),
        (3, 1, "ore_dock_spritelayout_gantry_ne_sw"),
        (3, 2, "ore_dock_spriteset_small_hut"),
        (3, 3, "ore_dock_spritelayout_checkpoint"),
        (4, 0, "ore_dock_spritelayout_coast_warehouse"),
        (4, 1, "ore_dock_spritelayout_coast_unloader_ne"),
        (4, 2, "ore_dock_spritelayout_coast_office"),
        (4, 3, "ore_dock_spritelayout_coast_mineral_pile_3"),
    ],
)
