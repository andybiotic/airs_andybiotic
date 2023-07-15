from industry import IndustryPrimaryPort, TileLocationChecks

industry = IndustryPrimaryPort(
    id="goods_yard",
    accept_cargo_types=["GOOD", "FOOD",],
    prod_cargo_types_with_multipliers=[
        ("FOOD", 6)
    ],
    prob_in_game="0",  # do not build during gameplay
    prob_map_gen="8",
    map_colour="143",
    name="string(STR_IND_GOODS_YARD)",
    nearby_station_name="string(STR_STATION_GOODS_YARD)",
    fund_cost_multiplier="8",
    special_flags=["IND_FLAG_ONLY_IN_TOWNS"],
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    
)

industry.enable_in_economy(
    "BLACK_GOLD_AND_FIRE",
)

industry.add_tile(
    id="goods_yard_tile_1",
    animation_length=71,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="concrete",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_large_warehouse = industry.add_spriteset(
    sprites=[(10, 10, 64, 64, -31, -32)],
)
spriteset_small_warehouse = industry.add_spriteset(
    sprites=[(80, 10, 64, 64, -31, -32)],
)
spriteset_small_hut = industry.add_spriteset(
    sprites=[(150, 10, 64, 64, -31, -32)],
)
spriteset_crane = industry.add_spriteset(
    sprites=[(220, 10, 64, 64, -31, -32)],
)
industry.add_spritelayout(
    id="goods_yard_spritelayout_large_warehouse",
    tile="goods_yard_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_large_warehouse],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="goods_yard_spritelayout_small_warehouse",
    tile="goods_yard_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_small_warehouse],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="goods_yard_spritelayout_small_hut",
    tile="goods_yard_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_small_hut],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="goods_yard_spritelayout_crane",
    tile="goods_yard_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_crane],
    add_to_object_num=4,
)

industry.add_industry_layout(
    id="goods_yard_industry_layout_1",
    layout=[
        (0, 0, "goods_yard_spritelayout_large_warehouse"),
        (0, 1, "goods_yard_spritelayout_small_warehouse"),
        (1, 0, "goods_yard_spritelayout_crane"),
        (1, 1, "goods_yard_spritelayout_small_hut"),
    ],
)
industry.add_industry_layout(
    id="goods_yard_industry_layout_2",
    layout=[
        (0, 0, "goods_yard_spritelayout_small_hut"),
        (0, 1, "goods_yard_spritelayout_small_warehouse"),
    ],
)
industry.add_industry_layout(
    id="goods_yard_industry_layout_3",
    layout=[
        (0, 0, "goods_yard_spritelayout_large_warehouse"),
        (1, 0, "goods_yard_spritelayout_crane"),
    ],
)
industry.add_industry_layout(
    id="goods_yard_industry_layout_4",
    layout=[
        (0, 0, "goods_yard_spritelayout_small_warehouse"),
        (1, 0, "goods_yard_spritelayout_crane"),
    ],
)
