# This file will hold data specific to Super Metroid which both the patcher and the interface use.
# This file only holds constants - any data specific to a given patch or version is not present.


class SuperMetroidConstants:
    # Dictionary of locations by their in-game bitflag index
    bitflagIndexToLocationNameDict = {
        0: "Crateria Landing Site Power Bombs",
        1: "Crateria Ocean Underwater Missiles",
        2: "Crateria Ocean Cliff Missiles",
        3: "Crateria Ocean Morph Maze Missiles",
        4: "Crateria Moat Missiles",
        5: "Crateria Gauntlet Energy Tank",
        6: "Crateria Mother Brain Missiles",
        7: "Crateria Morph Ball Bombs",
        8: "Crateria Terminator Energy Tank",
        9: "Crateria Gauntlet Right Missiles",
        10: "Crateria Gauntlet Left Missiles",
        11: "Crateria Shinespark Shaft Super Missiles",
        12: "Crateria Final Missiles",
        13: "Green Brinstar Etecoons Power Bombs",
        14: "Pink Brinstar Spore Spawn Super Missiles",
        15: "Green Brinstar Early Supers Crumble Bridge Missiles",
        16: "Green Brinstar Early Supers Super Missiles",
        17: "Green Brinstar Reserve Tank",
        18: "Green Brinstar Reserve Tank Missiles 2",
        19: "Green Brinstar Reserve Tank Missiles",
        21: "Pink Brinstar Big Pink Grapple Missiles",
        22: "Pink Brinstar Big Pink Bottom Missiles",
        23: "Pink Brinstar Charge Beam",
        24: "Pink Brinstar Big Pink Grapple Power Bombs",
        25: "Green Brinstar Green Hill Zone Missiles",
        26: "Blue Brinstar Morph Ball",
        27: "Blue Brinstar Power Bombs",
        28: "Blue Brinstar Energy Tank Room Missiles",
        29: "Blue Brinstar Energy Tank",
        30: "Green Brinstar Etecoons Energy Tank",
        31: "Green Brinstar Etecoons Super Missiles",
        33: "Pink Brinstar Waterway Energy Tank",
        34: "Blue Brinstar First Missiles",
        35: "Pink Brinstar Wavegate Energy Tank",
        36: "Blue Brinstar Billy Mayes Missiles",
        37: "Blue Brinstar Billy Mayes' Double Offer Missiles",
        38: "Red Brinstar X-Ray Scope",
        39: "Red Brinstar Samus Eater Power Bombs",
        40: "Red Brinstar Alpha Power Bombs",
        41: "Red Brinstar Behind Alpha Power Bombs Missiles",
        42: "Red Brinstar Spazer",
        43: "Warehouse Brinstar Energy Tank",
        44: "Warehouse Brinstar Missiles",
        48: "Warehouse Brinstar Varia Suit",
        49: "Norfair Cathedral Missiles",
        50: "Norfair Ice Beam",
        51: "Norfair Crumble Shaft Missiles",
        52: "Norfair Crocomire Energy Tank",
        53: "Norfair Hi-Jump Boots",
        54: "Norfair Crocomire Escape Missiles",
        55: "Norfair Hi-Jump Missiles",
        56: "Norfair Hi-Jump Energy Tank",
        57: "Norfair Crocomire Power Bombs",
        58: "Norfair Crocomire Cosine Missiles",
        59: "Norfair Grapple Missiles",
        60: "Norfair Grapple Beam",
        61: "Norfair Bubble Mountain Reserve Tank",
        62: "Norfair Bubble Mountain Reserve Missiles",
        63: "Norfair Bubble Mountain Grapple Missiles",
        64: "Norfair Bubble Mountain Missiles",
        65: "Norfair Speedboost Missiles",
        66: "Norfair Speed Booster",
        67: "Norfair Wave Beam Missiles",
        68: "Norfair Wave Beam",
        70: "Norfair Golden Torizo Missiles",
        71: "Norfair Golden Torizo Super Missiles",
        73: "Norfair Mickey Mouse Missiles",
        74: "Norfair Springball Maze Missiles",
        75: "Norfair Lower Escape Power Bombs",
        76: "Norfair Power Bombs of Shame",
        77: "Norfair FrankerZ Missiles",
        78: "Norfair Ridley Energy Tank",
        79: "Norfair Screw Attack",
        80: "Norfair Dark Room Energy Tank",
        128: "Wrecked Ship Spooky Missiles",
        129: "Wrecked Ship Reserve Tank",
        130: "Wrecked Ship Bowling Missiles",
        131: "Wrecked Ship Robot Missiles",
        132: "Wrecked Ship Energy Tank",
        133: "Wrecked Ship West Super Missiles",
        134: "Wrecked Ship East Super Missiles",
        135: "Wrecked Ship Gravity Suit",
        136: "Maridia Main Street Missiles",
        137: "Maridia Main Street Super Missiles",
        138: "Maridia Turtle Energy Tank",
        139: "Maridia Turtle Missiles",
        140: "Maridia Watering Hole Super Missiles",
        141: "Maridia Watering Hole Missiles",
        142: "Maridia Pseudo-Spark Missiles",
        143: "Maridia Plasma Beam",
        144: "Maridia West Sandtrap Missiles",
        145: "Maridia Reserve Tank",
        146: "Maridia East Sandtrap Missiles",
        147: "Maridia East Sandtrap Power Bombs",
        148: "Maridia Aqueduct Missiles",
        149: "Maridia Aqeuduct Super Misiles",
        150: "Maridia Springball",
        151: "Maridia Precious Missiles",
        152: "Maridia Botwoon Energy Tank",
        154: "Maridia Space Jump",
    }

    # List of ammo items, ordered by ascending Message ID
    ammoItemList = [
        "Energy Tank",
        "Missile Expansion",
        "Super Missile Expansion",
        "Power Bomb Expansion",
        "Reserve Tank",
    ]

    # List of toggle items, ordered by ascending Message ID
    toggleItemList = [
        "Grapple Beam",
        "X-Ray Scope",
        "Varia Suit",
        "Spring Ball",
        "Morph Ball",
        "Screw Attack",
        "Hi-Jump Boots",
        "Space Jump",
        "Speed Booster",
        "Charge Beam",
        "Ice Beam",
        "Wave Beam",
        "Spazer Beam",
        "Plasma Beam",
        "Morph Ball Bombs",
        "Gravity Suit",
    ]

    beamBitflagsDict = {
        "Charge Beam": 0x1000,
        "Ice Beam": 0x0002,
        "Wave Beam": 0x0001,
        "Spazer Beam": 0x0004,
        "Plasma Beam": 0x0008,
    }

    equipmentBitflagsDict = {
        "Varia Suit": 0x0001,
        "Spring Ball": 0x0002,
        "Morph Ball": 0x0004,
        "Screw Attack": 0x0008,
        "Hi-Jump Boots": 0x0100,
        "Space Jump": 0x0200,
        "Speed Booster": 0x2000,
        "Morph Ball Bombs": 0x1000,
        "Gravity Suit": 0x0020,
    }

    # Combined list, in order of ascending Message ID
    itemList = ammoItemList[0:4] + toggleItemList[0:15] + [ammoItemList[4]] + [toggleItemList[15]]

    # Dictionary of nonstandard message box sizes
    # TODO: Replace this with something more elegant? Possibly.
    itemMessageNonstandardSizes = {
        "Missile Expansion": 0x0100,
        "Super Missile Expansion": 0x0100,
        "Power Bomb Expansion": 0x0100,
        "Morph Ball Bombs": 0x0100,
        "Speed Booster": 0x0100,
        "Grapple Beam": 0x0100,
        "X-Ray Scope": 0x0100,
    }

    # Dictionary of item message locations
    itemMessageAddresses = {
        "Energy Tank": 0x877F,
        "Missile Expansion": 0x87BF,
        "Super Missile Expansion": 0x88BF,
        "Power Bomb Expansion": 0x89BF,
        "Grapple Beam": 0x8ABF,
        "X-Ray Scope": 0x8BBF,
        "Varia Suit": 0x8CBF,
        "Spring Ball": 0x8CFF,
        "Morph Ball": 0x8D3F,
        "Screw Attack": 0x8D7F,
        "Hi-Jump Boots": 0x8DBF,
        "Space Jump": 0x8DFF,
        "Speed Booster": 0x8E3F,
        "Charge Beam": 0x8F3F,
        "Ice Beam": 0x8F7F,
        "Wave Beam": 0x8FBF,
        "Spazer Beam": 0x8FFF,
        "Plasma Beam": 0x903F,
        "Morph Ball Bombs": 0x907F,
        "Reserve Tank": 0x94FF,
        "Gravity Suit": 0x953F,
    }

    itemMessageIDs = {
        "Energy Tank": 0x0001,
        "Missile Expansion": 0x0002,
        "Super Missile Expansion": 0x0003,
        "Power Bomb Expansion": 0x0004,
        "Grapple Beam": 0x0005,
        "X-Ray Scope": 0x0006,
        "Varia Suit": 0x0007,
        "Spring Ball": 0x0008,
        "Morph Ball": 0x0009,
        "Screw Attack": 0x000A,
        "Hi-Jump Boots": 0x000B,
        "Space Jump": 0x000C,
        "Speed Booster": 0x000D,
        "Charge Beam": 0x000E,
        "Ice Beam": 0x000F,
        "Wave Beam": 0x0010,
        "Spazer Beam": 0x0011,
        "Plasma Beam": 0x0012,
        "Morph Ball Bombs": 0x0013,
        "Reserve Tank": 0x0019,
        "Gravity Suit": 0x001A,
    }

    # Widths for all messages, either "Small" or "Large".
    # Small boxes have a width of 19 tiles,
    # Large boxes have a width of 26 tiles.
    # This dictates how messages are generated.
    # If a message type is not in this dict,
    # It is "Small".
    # All non-item messages, such as save station menus, recharge stations, etc. are also always small.
    # This includes unused messages.
    # Note that messageboxes may have varying heights.
    itemMessageWidths = {
        "Energy Tank": "Small",
        "Missile Expansion": "Large",
        "Super Missile Expansion": "Large",
        "Power Bomb Expansion": "Large",
        "Grapple Beam": "Large",
        "X-Ray Scope": "Large",
        "Varia Suit": "Small",
        "Spring Ball": "Small",
        "Morph Ball": "Small",
        "Screw Attack": "Small",
        "Hi-Jump Boots": "Small",
        "Space Jump": "Small",
        "Speed Booster": "Large",
        "Charge Beam": "Small",
        "Ice Beam": "Small",
        "Wave Beam": "Small",
        "Spazer Beam": "Small",
        "Plasma Beam": "Small",
        "Morph Ball Bombs": "Large",
        "Reserve Tank": "Small",
        "Gravity Suit": "Small",
    }

    # Locations of item sprites
    # Stored little-endian
    nativeItemSpriteLocations = {
        "Energy Tank": 0x0091,
        "Missile Expansion": 0x0092,
        "Super Missile Expansion": 0x0093,
        "Power Bomb Expansion": 0x0094,
        "Morph Ball Bombs": 0x0080,
        "Charge Beam": 0x008B,
        "Ice Beam": 0x008C,
        "Hi-Jump Boots": 0x0084,
        "Speed Booster": 0x008A,
        "Wave Beam": 0x008D,
        "Spazer Beam": 0x008F,
        "Spring Ball": 0x0082,
        "Varia Suit": 0x0083,
        "Gravity Suit": 0x0081,
        "X-Ray Scope": 0x0089,
        "Plasma Beam": 0x008E,
        "Grapple Beam": 0x0088,
        "Space Jump": 0x0086,
        "Screw Attack": 0x0085,
        "Morph Ball": 0x0087,
        "Reserve Tank": 0x0090,
    }

    # None indicates default palette
    # Item Palettes for native sprites
    # None is eqv. to all 0's.
    nativeItemPalettes = {
        "Energy Tank": None,
        "Missile Expansion": None,
        "Super Missile Expansion": None,
        "Power Bomb Expansion": None,
        "Morph Ball Bombs": None,
        "Charge Beam": None,
        "Ice Beam": bytearray([0x00, 0x03, 0x00, 0x00, 0x00, 0x03, 0x00, 0x00]),
        "Hi-Jump Boots": None,
        "Speed Booster": None,
        "Wave Beam": bytearray([0x00, 0x02, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00]),
        "Spazer Beam": None,
        "Spring Ball": None,
        "Varia Suit": None,
        "Gravity Suit": None,
        "X-Ray Scope": bytearray([0x01, 0x01, 0x00, 0x00, 0x03, 0x03, 0x00, 0x00]),
        "Plasma Beam": bytearray([0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00]),
        "Grapple Beam": None,
        "Space Jump": None,
        "Screw Attack": None,
        "Morph Ball": None,
        "Reserve Tank": None,
    }

    # List of all possible item locations as they are ordered in memory.
    itemLocationList = [
        0x00,
        0x01,
        0x02,
        0x03,
        0x04,
        0x05,
        0x06,
        0x07,
        0x08,
        0x09,
        0x0A,
        0x0B,
        0x0C,
        0x0D,
        0x0E,
        0x0F,
        0x10,
        0x11,
        0x12,
        0x13,
        0x15,
        0x16,
        0x17,
        0x18,
        0x19,
        0x1A,
        0x1B,
        0x1C,
        0x1D,
        0x1E,
        0x1F,
        0x21,
        0x22,
        0x23,
        0x24,
        0x25,
        0x26,
        0x27,
        0x28,
        0x29,
        0x2A,
        0x2B,
        0x2C,
        0x30,
        0x31,
        0x32,
        0x33,
        0x34,
        0x35,
        0x36,
        0x37,
        0x38,
        0x39,
        0x3A,
        0x3B,
        0x3C,
        0x3D,
        0x3E,
        0x3F,
        0x40,
        0x41,
        0x42,
        0x43,
        0x44,
        0x46,
        0x47,
        0x49,
        0x4A,
        0x4B,
        0x4C,
        0x4D,
        0x4E,
        0x4F,
        0x50,
        0x80,
        0x81,
        0x82,
        0x83,
        0x84,
        0x85,
        0x86,
        0x87,
        0x88,
        0x89,
        0x8A,
        0x8B,
        0x8C,
        0x8D,
        0x8E,
        0x8F,
        0x90,
        0x91,
        0x92,
        0x93,
        0x94,
        0x95,
        0x96,
        0x97,
        0x98,
        0x9A,
    ]

    # List of item PLM type offsets.
    # Used to set items as shot block or chozo orbs when necessary,
    # Depending upon which location an item is placed into.
    itemPLMBlockTypeList = [
        0,
        0,
        2,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        1,
        1,
        0,
        0,
        1,
        2,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        2,
        0,
        0,
        0,
        1,
        0,
        0,
        2,
        1,
        0,
        1,
        0,
        1,
        2,
        2,
        1,
        2,
        1,
        2,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        1,
        2,
        0,
        0,
        2,
        1,
        0,
        1,
        0,
        2,
        0,
        0,
        0,
        0,
        0,
        2,
        1,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        2,
        0,
        0,
        0,
        1,
        0,
        1,
        0,
        0,
        0,
        0,
        1,
        2,
        0,
        1,
    ]

    # Item index list
    # A list of all valid item indices, in order
    itemIndexList = sorted(bitflagIndexToLocationNameDict)
    # List of item PLM Locations in ROM.
    # This is where we place each item's entity so that it will show up in the room.
    # Doing so overwrites the item that would have been there previously (i.e. in an unpatched ROM).
    itemPLMLocationList = [
        0x781CC,
        0x781E8,
        0x781EE,
        0x781F4,
        0x78248,
        0x78264,
        0x783EE,
        0x78404,
        0x78432,
        0x78464,
        0x7846A,
        0x78478,
        0x78486,
        0x784AC,
        0x784E4,
        0x78518,
        0x7851E,
        0x7852C,
        0x78532,
        0x78538,
        0x78608,
        0x7860E,
        0x78614,
        0x7865C,
        0x78676,
        0x786DE,
        0x7874C,
        0x78798,
        0x7879E,
        0x787C2,
        0x787D0,
        0x787FA,
        0x78802,
        0x78824,
        0x78836,
        0x7883C,
        0x78876,
        0x788CA,
        0x7890E,
        0x78914,
        0x7896E,
        0x7899C,
        0x789EC,
        0x78ACA,
        0x78AE4,
        0x78B24,
        0x78B46,
        0x78BA4,
        0x78BAC,
        0x78BC0,
        0x78BE6,
        0x78BEC,
        0x78C04,
        0x78C14,
        0x78C2A,
        0x78C36,
        0x78C3E,
        0x78C44,
        0x78C52,
        0x78C66,
        0x78C74,
        0x78C82,
        0x78CBC,
        0x78CCA,
        0x78E6E,
        0x78E74,
        0x78F30,
        0x78FCA,
        0x78FD2,
        0x790C0,
        0x79100,
        0x79108,
        0x79110,
        0x79184,
        0x7C265,
        0x7C2E9,
        0x7C2EF,
        0x7C319,
        0x7C337,
        0x7C357,
        0x7C365,
        0x7C36D,
        0x7C437,
        0x7C43D,
        0x7C47D,
        0x7C483,
        0x7C4AF,
        0x7C4B5,
        0x7C533,
        0x7C559,
        0x7C5DD,
        0x7C5E3,
        0x7C5EB,
        0x7C5F1,
        0x7C603,
        0x7C609,
        0x7C6E5,
        0x7C74D,
        0x7C755,
        0x7C7A7,
    ]

    locationNamesList = [
        "Crateria Landing Site Power Bombs",
        "Crateria Ocean Underwater Missiles",
        "Crateria Ocean Cliff Missiles",
        "Crateria Ocean Morph Maze Missiles",
        "Crateria Moat Missiles",
        "Crateria Gauntlet Energy Tank",
        "Crateria Mother Brain Missiles",
        "Crateria Morph Ball Bombs",
        "Crateria Terminator Energy Tank",
        "Crateria Gauntlet Right Missiles",
        "Crateria Gauntlet Left Missiles",
        "Crateria Shinespark Shaft Super Missiles",
        "Crateria Final Missiles",
        "Green Brinstar Etecoons Power Bombs",
        "Pink Brinstar Spore Spawn Super Missiles",
        "Green Brinstar Early Supers Crumble Bridge Missiles",
        "Green Brinstar Early Supers Super Missiles",
        "Green Brinstar Reserve Tank",
        "Green Brinstar Reserve Tank Missiles 2",
        "Green Brinstar Reserve Tank Missiles",
        "Pink Brinstar Big Pink Grapple Missiles",
        "Pink Brinstar Big Pink Bottom Missiles",
        "Pink Brinstar Charge Beam",
        "Pink Brinstar Big Pink Grapple Power Bombs",
        "Green Brinstar Green Hill Zone Missiles",
        "Blue Brinstar Morph Ball",
        "Blue Brinstar Power Bombs",
        "Blue Brinstar Energy Tank Room Missiles",
        "Blue Brinstar Energy Tank",
        "Green Brinstar Etecoons Energy Tank",
        "Green Brinstar Etecoons Super Missiles",
        "Pink Brinstar Waterway Energy Tank",
        "Blue Brinstar First Missiles",
        "Pink Brinstar Wavegate Energy Tank",
        "Blue Brinstar Billy Mayes Missiles",
        "Blue Brinstar Billy Mayes' Double Offer Missiles",
        "Red Brinstar X-Ray Scope",
        "Red Brinstar Samus Eater Power Bombs",
        "Red Brinstar Alpha Power Bombs",
        "Red Brinstar Behind Alpha Power Bombs Missiles",
        "Red Brinstar Spazer",
        "Warehouse Brinstar Energy Tank",
        "Warehouse Brinstar Missiles",
        "Warehouse Brinstar Varia Suit",
        "Norfair Cathedral Missiles",
        "Norfair Ice Beam",
        "Norfair Crumble Shaft Missiles",
        "Norfair Crocomire Energy Tank",
        "Norfair Hi-Jump Boots",
        "Norfair Crocomire Escape Missiles",
        "Norfair Hi-Jump Missiles",
        "Norfair Hi-Jump Energy Tank",
        "Norfair Crocomire Power Bombs",
        "Norfair Crocomire Cosine Missiles",
        "Norfair Grapple Missiles",
        "Norfair Grapple Beam",
        "Norfair Bubble Mountain Reserve Tank",
        "Norfair Bubble Mountain Reserve Missiles",
        "Norfair Bubble Mountain Grapple Missiles",
        "Norfair Bubble Mountain Missiles",
        "Norfair Speedboost Missiles",
        "Norfair Speed Booster",
        "Norfair Wave Beam Missiles",
        "Norfair Wave Beam",
        "Norfair Golden Torizo Missiles",
        "Norfair Golden Torizo Super Missiles",
        "Norfair Mickey Mouse Missiles",
        "Norfair Springball Maze Missiles",
        "Norfair Lower Escape Power Bombs",
        "Norfair Power Bombs of Shame",
        "Norfair FrankerZ Missiles",
        "Norfair Ridley Energy Tank",
        "Norfair Screw Attack",
        "Norfair Dark Room Energy Tank",
        "Wrecked Ship Spooky Missiles",
        "Wrecked Ship Reserve Tank",
        "Wrecked Ship Bowling Missiles",
        "Wrecked Ship Robot Missiles",
        "Wrecked Ship Energy Tank",
        "Wrecked Ship West Super Missiles",
        "Wrecked Ship East Super Missiles",
        "Wrecked Ship Gravity Suit",
        "Maridia Main Street Missiles",
        "Maridia Main Street Super Missiles",
        "Maridia Turtle Energy Tank",
        "Maridia Turtle Missiles",
        "Maridia Watering Hole Super Missiles",
        "Maridia Watering Hole Missiles",
        "Maridia Pseudo-Spark Missiles",
        "Maridia Plasma Beam",
        "Maridia West Sandtrap Missiles",
        "Maridia Reserve Tank",
        "Maridia East Sandtrap Missiles",
        "Maridia East Sandtrap Power Bombs",
        "Maridia Aqueduct Missiles",
        "Maridia Aqeuduct Super Misiles",
        "Maridia Springball",
        "Maridia Precious Missiles",
        "Maridia Botwoon Energy Tank",
        "Maridia Space Jump",
    ]

    regionToHexDict = {
        "Crateria": "0000",
        "Brinstar": "0100",
        "Norfair": "0200",
        "Wrecked Ship": "0300",
        "Maridia": "0400",
        "Tourian": "0500",
        "Ceres Station": "0600",
    }

    itemNameToQuantityName = {
        "Energy Tank": "Energy",
        "Missile Expansion": "Missiles",
        "Super Missile Expansion": "Super Missiles",
        "Power Bomb Expansion": "Power Bombs",
        "Reserve Tank": "Reserve Energy",
    }

    defaultAmmoItemToQuantity = {
        "Energy Tank": 100,
        "Missile Expansion": 5,
        "Super Missile Expansion": 5,
        "Power Bomb Expansion": 5,
        "Reserve Tank": 100,
    }

    # Address to current quantity of indicated type.
    # Max quantity is stored 2 bytes after current quantity in all cases.
    ammoItemAddresses = {
        "Energy Tank": "F509C2",
        "Missile Expansion": "F509C6",
        "Super Missile Expansion": "F509CA",
        "Power Bomb Expansion": "F509CE",
        "Reserve Tank": "F509D4",
    }

    # What address we should look at to find equipment (from SNI's perspective, it's complicated)
    toggleItemBaseAddress = "F509A2"

    # Formatted offsets for where to read/write toggleable items.
    # Stored as a tuple.
    # First  value: Byte offset.
    # Second value: Bit offset.
    # NOTE: Equipped and collected items are stored adjacently in memory.
    # The item collected flag is always exactly two bytes after the corresponding item equipped flag.
    # Bit offset is the offset from lsb.
    # Ex. the 1 in 00000001 has offset 0.
    toggleItemBitflagOffsets = {
        "Grapple Beam": (1, 6),
        "X-Ray Scope": (1, 7),
        "Varia Suit": (0, 0),
        "Spring Ball": (0, 1),
        "Morph Ball": (0, 2),
        "Screw Attack": (0, 3),
        "Hi-Jump Boots": (1, 0),
        "Space Jump": (1, 1),
        "Speed Booster": (1, 5),
        "Charge Beam": (5, 4),
        "Ice Beam": (4, 1),
        "Wave Beam": (4, 0),
        "Spazer Beam": (4, 2),
        "Plasma Beam": (4, 3),
        "Morph Ball Bombs": (1, 4),
        "Gravity Suit": (0, 5),
    }

    vanillaPickupList = [
        "Power Bomb Expansion",
        "Missile Expansion",
        "Missile Expansion",
        "Missile Expansion",
        "Missile Expansion",
        "Energy Tank",
        "Missile Expansion",
        "Morph Ball Bombs",
        "Energy Tank",
        "Missile Expansion",
        "Missile Expansion",
        "Super Missile Expansion",
        "Missile Expansion",
        "Power Bomb Expansion",
        "Super Missile Expansion",
        "Missile Expansion",
        "Super Missile Expansion",
        "Reserve Tank",
        "Missile Expansion",
        "Missile Expansion",
        "Missile Expansion",
        "Missile Expansion",
        "Charge Beam",
        "Power Bomb Expansion",
        "Missile Expansion",
        "Morph Ball",
        "Power Bomb Expansion",
        "Missile Expansion",
        "Energy Tank",
        "Energy Tank",
        "Super Missile Expansion",
        "Energy Tank",
        "Missile Expansion",
        "Energy Tank",
        "Missile Expansion",
        "Missile Expansion",
        "X-Ray Scope",
        "Power Bomb Expansion",
        "Power Bomb Expansion",
        "Missile Expansion",
        "Spazer Beam",
        "Energy Tank",
        "Missile Expansion",
        "Varia Suit",
        "Missile Expansion",
        "Ice Beam",
        "Missile Expansion",
        "Energy Tank",
        "Hi-Jump Boots",
        "Missile Expansion",
        "Missile Expansion",
        "Energy Tank",
        "Power Bomb Expansion",
        "Missile Expansion",
        "Missile Expansion",
        "Grapple Beam",
        "Reserve Tank",
        "Missile Expansion",
        "Missile Expansion",
        "Missile Expansion",
        "Missile Expansion",
        "Speed Booster",
        "Missile Expansion",
        "Wave Beam",
        "Missile Expansion",
        "Super Missile Expansion",
        "Missile Expansion",
        "Missile Expansion",
        "Power Bomb Expansion",
        "Power Bomb Expansion",
        "Missile Expansion",
        "Energy Tank",
        "Screw Attack",
        "Energy Tank",
        "Missile Expansion",
        "Reserve Tank",
        "Missile Expansion",
        "Missile Expansion",
        "Energy Tank",
        "Super Missile Expansion",
        "Super Missile Expansion",
        "Gravity Suit",
        "Missile Expansion",
        "Super Missile Expansion",
        "Energy Tank",
        "Missile Expansion",
        "Super Missile Expansion",
        "Missile Expansion",
        "Missile Expansion",
        "Plasma Beam",
        "Missile Expansion",
        "Reserve Tank",
        "Missile Expansion",
        "Power Bomb Expansion",
        "Missile Expansion",
        "Super Missile Expansion",
        "Spring Ball",
        "Missile Expansion",
        "Energy Tank",
        "Space Jump",
    ]
