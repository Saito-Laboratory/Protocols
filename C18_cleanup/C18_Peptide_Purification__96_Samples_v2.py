import json
from opentrons import protocol_api, types

metadata = {
    "protocolName": "C18 Peptide Purification - 96 Samples",
    "author": "Saito Lab",
    "description": "This Protocol Designer protocol automates the purification of 96 peptide samples from salts and organic impurities using Pierce C18 tips on the OT-2 with multichannel pipettes.",
    "created": "2025-12-10T19:47:54.714Z",
    "internalAppBuildDate": "Wed, 04 Mar 2026 17:13:57 GMT",
    "lastModified": "2026-03-16T14:56:47.348Z",
    "protocolDesigner": "8.9.0",
    "source": "Protocol Designer",
}

requirements = {"robotType": "OT-2", "apiLevel": "2.27"}

def run(protocol: protocol_api.ProtocolContext) -> None:
    # Load Labware:
    reservoir_1 = protocol.load_labware(
        "nest_12_reservoir_15ml",
        location="7",
        label="NEST 12 Well Reservoir 15 mL - 50% ACN",
        namespace="opentrons",
        version=3,
    )
    reservoir_2 = protocol.load_labware(
        "nest_12_reservoir_15ml",
        location="4",
        label="NEST 12 Well Reservoir 15 mL - 0.1% TFA",
        namespace="opentrons",
        version=3,
    )
    reservoir_3 = protocol.load_labware(
        "nest_12_reservoir_15ml",
        location="8",
        label="NEST 12 Well Reservoir 15 mL - ACN Waste",
        namespace="opentrons",
        version=3,
    )
    reservoir_4 = protocol.load_labware(
        "nest_12_reservoir_15ml",
        location="5",
        label="NEST 12 Well Reservoir 15 mL - TFA Waste",
        namespace="opentrons",
        version=3,
    )
    tip_rack_1 = protocol.load_labware(
        "opentrons_96_tiprack_300ul",
        location="10",
        namespace="opentrons",
        version=1,
    )
    well_plate_1 = protocol.load_labware_from_definition(
        CUSTOM_LABWARE["custom_beta/thermo_kingfisher_96_deepwell_2ml/1"],
        location="3",
    )
    well_plate_2 = protocol.load_labware_from_definition(
        CUSTOM_LABWARE["custom_beta/thermo_kingfisher_96_deepwell_2ml/1"],
        location="11",
    )
    well_plate_3 = protocol.load_labware_from_definition(
        CUSTOM_LABWARE["custom_beta/thermo_kingfisher_96_deepwell_2ml/1"],
        location="1",
    )
    well_plate_4 = protocol.load_labware_from_definition(
        CUSTOM_LABWARE["custom_beta/thermo_kingfisher_96_deepwell_2ml/1"],
        location="2",
    )

    # Load Pipettes:
    pipette_right = protocol.load_instrument("p300_multi", "right")

    # Define Liquids:
    liquid_1 = protocol.define_liquid(
        "50% ACN",
        description="Conditioning solution",
        display_color="#ff6e6e",
    )
    liquid_2 = protocol.define_liquid(
        "0.1% TFA",
        description="Equilibration solution",
        display_color="#6e8eff",
    )
    liquid_3 = protocol.define_liquid(
        "0.1% TFA/5% ACN",
        description="Rinse solution",
        display_color="#9dffd4",
    )
    liquid_4 = protocol.define_liquid(
        "0.1% Formic Acid/70% ACN",
        description="Elution solution",
        display_color="#ffd752",
    )
    liquid_5 = protocol.define_liquid(
        "Sample",
        description="Acidified peptide samples",
        display_color="#50d5ff",
    )

    # Load Liquids:
    reservoir_1.load_liquid(
        wells=[
            "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8",
            "A9", "A10", "A11", "A12"
        ],
        liquid=liquid_1,
        volume=2000,
    )
    reservoir_2.load_liquid(
        wells=[
            "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8",
            "A9", "A10", "A11", "A12"
        ],
        liquid=liquid_2,
        volume=2000,
    )
    well_plate_1.load_liquid(
        wells=[
            "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1",
            "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2",
            "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3",
            "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4",
            "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5",
            "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6",
            "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7",
            "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8",
            "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9",
            "A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10",
            "A11", "B11", "C11", "D11", "E11", "F11", "G11", "H11",
            "A12", "B12", "C12", "D12", "E12", "F12", "G12", "H12"
        ],
        liquid=liquid_4,
        volume=50,
    )
    well_plate_3.load_liquid(
        wells=[
            "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1",
            "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2",
            "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3",
            "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4",
            "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5",
            "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6",
            "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7",
            "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8",
            "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9",
            "A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10",
            "A11", "B11", "C11", "D11", "E11", "F11", "G11", "H11",
            "A12", "B12", "C12", "D12", "E12", "F12", "G12", "H12"
        ],
        liquid=liquid_5,
        volume=100,
    )
    well_plate_4.load_liquid(
        wells=[
            "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1",
            "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2",
            "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3",
            "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4",
            "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5",
            "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6",
            "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7",
            "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8",
            "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9",
            "A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10",
            "A11", "B11", "C11", "D11", "E11", "F11", "G11", "H11",
            "A12", "B12", "C12", "D12", "E12", "F12", "G12", "H12"
        ],
        liquid=liquid_3,
        volume=200,
    )

    # PROTOCOL STEPS

    # Step 1: Col 1: Conditioning 1st
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A1"]],
        dest=[reservoir_3["A1"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_1",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 2: Col 1: Conditioning 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A1"]],
        dest=[reservoir_3["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_2",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 3: Col 1: Equilibrate 1st
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_2["A1"]],
        dest=[reservoir_4["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_3",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 3},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 4: Col 1: Equilibrate 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_2["A1"]],
        dest=[reservoir_4["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_4",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 5: Col 1: Load sample
    pipette_right.mix(
        repetitions=5,
        volume=100,
        location=well_plate_3["A1"].bottom(z=1),
        aspirate_flow_rate=5,
        dispense_flow_rate=5,
        final_push_out=0,
    )

    # Step 6: Col 1: Rinse 1st
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_4["A1"]],
        dest=[well_plate_2["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_6",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 7: Col 1: Rinse 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_4["A1"]],
        dest=[well_plate_2["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_7",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 8: Col 1: ELUTE Sample
    pipette_right.mix(
        repetitions=5,
        volume=50,
        location=well_plate_1["A1"].bottom(z=1),
        aspirate_flow_rate=5,
        dispense_flow_rate=5,
        final_push_out=20,
    )
    pipette_right.flow_rate.blow_out = 94
    pipette_right.blow_out(well_plate_1["A1"].top())
    pipette_right.drop_tip()

    # Step 9: Col 2: Conditioning 1st
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A2"]],
        dest=[reservoir_3["A2"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_9",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 10: Col 2: Conditioning 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A2"]],
        dest=[reservoir_3["A2"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_10",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 11: Col 2: Equilibrate 1st
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_2["A2"]],
        dest=[reservoir_4["A2"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_11",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 3},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 12: Col 2: Equilibrate 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_2["A2"]],
        dest=[reservoir_4["A2"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_12",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 13: Col 2: Load sample
    pipette_right.mix(
        repetitions=5,
        volume=100,
        location=well_plate_3["A2"].bottom(z=1),
        aspirate_flow_rate=5,
        dispense_flow_rate=5,
        final_push_out=0,
    )

    # Step 14: Col 2: Rinse 1st
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_4["A2"]],
        dest=[well_plate_2["A2"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_14",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 15: Col 2: Rinse 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_4["A2"]],
        dest=[well_plate_2["A2"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_15",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 16: Col 2: ELUTE Sample
    pipette_right.mix(
        repetitions=5,
        volume=50,
        location=well_plate_1["A2"].bottom(z=1),
        aspirate_flow_rate=5,
        dispense_flow_rate=5,
        final_push_out=20,
    )
    pipette_right.flow_rate.blow_out = 94
    pipette_right.blow_out(well_plate_1["A2"].top())
    pipette_right.drop_tip()

    # Step 17: Col 3: Conditioning 1st
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A3"]],
        dest=[reservoir_3["A3"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_17",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 18: Col 3: Conditioning 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A3"]],
        dest=[reservoir_3["A3"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_18",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 19: Col 3: Equilibrate 1st
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_2["A3"]],
        dest=[reservoir_4["A3"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_19",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 3},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 20: Col 3: Equilibrate 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_2["A3"]],
        dest=[reservoir_4["A3"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_20",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 21: Col 3: Load sample
    pipette_right.mix(
        repetitions=5,
        volume=100,
        location=well_plate_3["A3"].bottom(z=1),
        aspirate_flow_rate=5,
        dispense_flow_rate=5,
        final_push_out=0,
    )

    # Step 22: Col 3: Rinse 1st
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_4["A3"]],
        dest=[well_plate_2["A3"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_22",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 23: Col 3: Rinse 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_4["A3"]],
        dest=[well_plate_2["A3"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_23",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 24: Col 3: ELUTE Sample
    pipette_right.mix(
        repetitions=5,
        volume=50,
        location=well_plate_1["A3"].bottom(z=1),
        aspirate_flow_rate=5,
        dispense_flow_rate=5,
        final_push_out=20,
    )
    pipette_right.flow_rate.blow_out = 94
    pipette_right.blow_out(well_plate_1["A3"].top())
    pipette_right.drop_tip()

    # Step 25: Col 4: Conditioning 1st
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A4"]],
        dest=[reservoir_3["A4"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_25",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 26: Col 4: Conditioning 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A4"]],
        dest=[reservoir_3["A4"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_26",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 27: Col 4: Equilibrate 1st
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_2["A4"]],
        dest=[reservoir_4["A4"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_27",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 3},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 28: Col 4: Equilibrate 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_2["A4"]],
        dest=[reservoir_4["A4"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_28",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 29: Col 4: Load sample
    pipette_right.mix(
        repetitions=5,
        volume=100,
        location=well_plate_3["A4"].bottom(z=1),
        aspirate_flow_rate=5,
        dispense_flow_rate=5,
        final_push_out=0,
    )

    # Step 30: Col 4: Rinse 1st
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_4["A4"]],
        dest=[well_plate_2["A4"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_30",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 31: Col 4: Rinse 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_4["A4"]],
        dest=[well_plate_2["A4"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_31",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 32: Col 4: ELUTE Sample
    pipette_right.mix(
        repetitions=5,
        volume=50,
        location=well_plate_1["A4"].bottom(z=1),
        aspirate_flow_rate=5,
        dispense_flow_rate=5,
        final_push_out=20,
    )
    pipette_right.flow_rate.blow_out = 94
    pipette_right.blow_out(well_plate_1["A4"].top())
    pipette_right.drop_tip()

    # Step 33: Col 5: Conditioning 1st
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A5"]],
        dest=[reservoir_3["A5"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_33",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 34: Col 5: Conditioning 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A5"]],
        dest=[reservoir_3["A5"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_34",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 35: Col 5: Equilibrate 1st
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_2["A5"]],
        dest=[reservoir_4["A5"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_35",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 3},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 36: Col 5: Equilibrate 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_2["A5"]],
        dest=[reservoir_4["A5"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_36",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 37: Col 5: Load sample
    pipette_right.mix(
        repetitions=5,
        volume=100,
        location=well_plate_3["A5"].bottom(z=1),
        aspirate_flow_rate=5,
        dispense_flow_rate=5,
        final_push_out=0,
    )

    # Step 38: Col 5: Rinse 1st
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_4["A5"]],
        dest=[well_plate_2["A5"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_38",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 39: Col 5: Rinse 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_4["A5"]],
        dest=[well_plate_2["A5"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_39",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 40: Col 5: ELUTE Sample
    pipette_right.mix(
        repetitions=5,
        volume=50,
        location=well_plate_1["A5"].bottom(z=1),
        aspirate_flow_rate=5,
        dispense_flow_rate=5,
        final_push_out=20,
    )
    pipette_right.flow_rate.blow_out = 94
    pipette_right.blow_out(well_plate_1["A5"].top())
    pipette_right.drop_tip()

    # Step 41: Col 6: Conditioning 1st
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A6"]],
        dest=[reservoir_3["A6"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_41",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 42: Col 6: Conditioning 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A6"]],
        dest=[reservoir_3["A6"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_42",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 43: Col 6: Equilibrate 1st
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_2["A6"]],
        dest=[reservoir_4["A6"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_43",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 3},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 44: Col 6: Equilibrate 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_2["A6"]],
        dest=[reservoir_4["A6"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_44",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 45: Col 6: Load sample
    pipette_right.mix(
        repetitions=5,
        volume=100,
        location=well_plate_3["A6"].bottom(z=1),
        aspirate_flow_rate=5,
        dispense_flow_rate=5,
        final_push_out=0,
    )

    # Step 46: Col 6: Rinse 1st
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_4["A6"]],
        dest=[well_plate_2["A6"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_46",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 47: Col 6: Rinse 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_4["A6"]],
        dest=[well_plate_2["A6"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_47",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 48: Col 6: ELUTE Sample
    pipette_right.mix(
        repetitions=5,
        volume=50,
        location=well_plate_1["A6"].bottom(z=1),
        aspirate_flow_rate=5,
        dispense_flow_rate=5,
        final_push_out=20,
    )
    pipette_right.flow_rate.blow_out = 94
    pipette_right.blow_out(well_plate_1["A6"].top())
    pipette_right.drop_tip()

    # Step 49: Col 7: Conditioning 1st
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A7"]],
        dest=[reservoir_3["A7"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_49",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 50: Col 7: Conditioning 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A7"]],
        dest=[reservoir_3["A7"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_50",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 51: Col 7: Equilibrate 1st
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_2["A7"]],
        dest=[reservoir_4["A7"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_51",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 3},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 52: Col 7: Equilibrate 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_2["A7"]],
        dest=[reservoir_4["A7"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_52",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 53: Col 7: Load sample
    pipette_right.mix(
        repetitions=5,
        volume=100,
        location=well_plate_3["A7"].bottom(z=1),
        aspirate_flow_rate=5,
        dispense_flow_rate=5,
        final_push_out=0,
    )

    # Step 54: Col 7: Rinse 1st
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_4["A7"]],
        dest=[well_plate_2["A7"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_54",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 55: Col 7: Rinse 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_4["A7"]],
        dest=[well_plate_2["A7"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_55",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 56: Col 7: ELUTE Sample
    pipette_right.mix(
        repetitions=5,
        volume=50,
        location=well_plate_1["A7"].bottom(z=1),
        aspirate_flow_rate=5,
        dispense_flow_rate=5,
        final_push_out=20,
    )
    pipette_right.flow_rate.blow_out = 94
    pipette_right.blow_out(well_plate_1["A7"].top())
    pipette_right.drop_tip()

    # Step 57: Col 8: Conditioning 1st
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A8"]],
        dest=[reservoir_3["A8"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_57",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 58: Col 8: Conditioning 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A8"]],
        dest=[reservoir_3["A8"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_58",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 59: Col 8: Equilibrate 1st
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_2["A8"]],
        dest=[reservoir_4["A8"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_59",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 3},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 60: Col 8: Equilibrate 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_2["A8"]],
        dest=[reservoir_4["A8"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_60",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 61: Col 8: Load sample
    pipette_right.mix(
        repetitions=5,
        volume=100,
        location=well_plate_3["A8"].bottom(z=1),
        aspirate_flow_rate=5,
        dispense_flow_rate=5,
        final_push_out=0,
    )

    # Step 62: Col 8: Rinse 1st
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_4["A8"]],
        dest=[well_plate_2["A8"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_62",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 63: Col 8: Rinse 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_4["A8"]],
        dest=[well_plate_2["A8"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_63",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 64: Col 8: ELUTE Sample
    pipette_right.mix(
        repetitions=5,
        volume=50,
        location=well_plate_1["A8"].bottom(z=1),
        aspirate_flow_rate=5,
        dispense_flow_rate=5,
        final_push_out=20,
    )
    pipette_right.flow_rate.blow_out = 94
    pipette_right.blow_out(well_plate_1["A8"].top())
    pipette_right.drop_tip()

    # Step 65: Col 9: Conditioning 1st
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A9"]],
        dest=[reservoir_3["A9"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_65",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 66: Col 9: Conditioning 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A9"]],
        dest=[reservoir_3["A9"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_66",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 67: Col 9: Equilibrate 1st
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_2["A9"]],
        dest=[reservoir_4["A9"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_67",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 3},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 68: Col 9: Equilibrate 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_2["A9"]],
        dest=[reservoir_4["A9"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_68",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 69: Col 9: Load sample
    pipette_right.mix(
        repetitions=5,
        volume=100,
        location=well_plate_3["A9"].bottom(z=1),
        aspirate_flow_rate=5,
        dispense_flow_rate=5,
        final_push_out=0,
    )

    # Step 70: Col 9: Rinse 1st
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_4["A9"]],
        dest=[well_plate_2["A9"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_70",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 71: Col 9: Rinse 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_4["A9"]],
        dest=[well_plate_2["A9"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_71",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 72: Col 9: ELUTE Sample
    pipette_right.mix(
        repetitions=5,
        volume=50,
        location=well_plate_1["A9"].bottom(z=1),
        aspirate_flow_rate=5,
        dispense_flow_rate=5,
        final_push_out=20,
    )
    pipette_right.flow_rate.blow_out = 94
    pipette_right.blow_out(well_plate_1["A9"].top())
    pipette_right.drop_tip()

    # Step 73: Col 10: Conditioning 1st
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A10"]],
        dest=[reservoir_3["A10"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_73",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 74: Col 10: Conditioning 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A10"]],
        dest=[reservoir_3["A10"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_74",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 75: Col 10: Equilibrate 1st
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_2["A10"]],
        dest=[reservoir_4["A10"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_75",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 3},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 76: Col 10: Equilibrate 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_2["A10"]],
        dest=[reservoir_4["A10"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_76",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 77: Col 10: Load sample
    pipette_right.mix(
        repetitions=5,
        volume=100,
        location=well_plate_3["A10"].bottom(z=1),
        aspirate_flow_rate=5,
        dispense_flow_rate=5,
        final_push_out=0,
    )

    # Step 78: Col 10: Rinse 1st
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_4["A10"]],
        dest=[well_plate_2["A10"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_78",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 79: Col 10: Rinse 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_4["A10"]],
        dest=[well_plate_2["A10"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_79",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 80: Col 10: ELUTE Sample
    pipette_right.mix(
        repetitions=5,
        volume=50,
        location=well_plate_1["A10"].bottom(z=1),
        aspirate_flow_rate=5,
        dispense_flow_rate=5,
        final_push_out=20,
    )
    pipette_right.flow_rate.blow_out = 94
    pipette_right.blow_out(well_plate_1["A10"].top())
    pipette_right.drop_tip()

    # Step 81: Col 11: Conditioning 1st
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A11"]],
        dest=[reservoir_3["A11"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_81",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 82: Col 11: Conditioning 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A11"]],
        dest=[reservoir_3["A11"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_82",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 83: Col 11: Equilibrate 1st
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_2["A11"]],
        dest=[reservoir_4["A11"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_83",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 3},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 84: Col 11: Equilibrate 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_2["A11"]],
        dest=[reservoir_4["A11"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_84",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 85: Col 11: Load sample
    pipette_right.mix(
        repetitions=5,
        volume=100,
        location=well_plate_3["A11"].bottom(z=1),
        aspirate_flow_rate=5,
        dispense_flow_rate=5,
        final_push_out=0,
    )

    # Step 86: Col 11: Rinse 1st
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_4["A11"]],
        dest=[well_plate_2["A11"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_86",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 87: Col 11: Rinse 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_4["A11"]],
        dest=[well_plate_2["A11"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_87",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 88: Col 11: ELUTE Sample
    pipette_right.mix(
        repetitions=5,
        volume=50,
        location=well_plate_1["A11"].bottom(z=1),
        aspirate_flow_rate=5,
        dispense_flow_rate=5,
        final_push_out=20,
    )
    pipette_right.flow_rate.blow_out = 94
    pipette_right.blow_out(well_plate_1["A11"].top())
    pipette_right.drop_tip()

    # Step 89: Col 12: Conditioning 1st
    pipette_right.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A12"]],
        dest=[reservoir_3["A12"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_89",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 90: Col 12: Conditioning 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_1["A12"]],
        dest=[reservoir_3["A12"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_90",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 91: Col 12: Equilibrate 1st
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_2["A12"]],
        dest=[reservoir_4["A12"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_91",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 3},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 92: Col 12: Equilibrate 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[reservoir_2["A12"]],
        dest=[reservoir_4["A12"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_92",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 30)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 5,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-bottom",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 0.5},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 93: Col 12: Load sample
    pipette_right.mix(
        repetitions=5,
        volume=100,
        location=well_plate_3["A12"].bottom(z=1),
        aspirate_flow_rate=5,
        dispense_flow_rate=5,
        final_push_out=0,
    )

    # Step 94: Col 12: Rinse 1st
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_4["A12"]],
        dest=[well_plate_2["A12"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_94",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 95: Col 12: Rinse 2nd
    pipette_right.transfer_with_liquid_class(
        volume=100,
        source=[well_plate_4["A12"]],
        dest=[well_plate_2["A12"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_95",
            properties={"p300_multi": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 5)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 96: Col 12: ELUTE Sample
    pipette_right.mix(
        repetitions=5,
        volume=50,
        location=well_plate_1["A12"].bottom(z=1),
        aspirate_flow_rate=5,
        dispense_flow_rate=5,
        final_push_out=20,
    )
    pipette_right.flow_rate.blow_out = 94
    pipette_right.blow_out(well_plate_1["A12"].top())
    pipette_right.drop_tip()

CUSTOM_LABWARE = json.loads("""{"custom_beta/thermo_kingfisher_96_deepwell_2ml/1":{"ordering":[["A1","B1","C1","D1","E1","F1","G1","H1"],["A2","B2","C2","D2","E2","F2","G2","H2"],["A3","B3","C3","D3","E3","F3","G3","H3"],["A4","B4","C4","D4","E4","F4","G4","H4"],["A5","B5","C5","D5","E5","F5","G5","H5"],["A6","B6","C6","D6","E6","F6","G6","H6"],["A7","B7","C7","D7","E7","F7","G7","H7"],["A8","B8","C8","D8","E8","F8","G8","H8"],["A9","B9","C9","D9","E9","F9","G9","H9"],["A10","B10","C10","D10","E10","F10","G10","H10"],["A11","B11","C11","D11","E11","F11","G11","H11"],["A12","B12","C12","D12","E12","F12","G12","H12"]],"brand":{"brand":"Thermo fisher","brandId":[]},"metadata":{"displayName":"thermo_kingfisher_96_deepwell_2ml","displayCategory":"wellPlate","displayVolumeUnits":"µL","tags":[]},"dimensions":{"xDimension":127.76,"yDimension":85.47,"zDimension":44},"wells":{"A1":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":14,"y":74.47,"z":3},"B1":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":14,"y":65.47,"z":3},"C1":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":14,"y":56.47,"z":3},"D1":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":14,"y":47.47,"z":3},"E1":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":14,"y":38.47,"z":3},"F1":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":14,"y":29.47,"z":3},"G1":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":14,"y":20.47,"z":3},"H1":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":14,"y":11.47,"z":3},"A2":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":23,"y":74.47,"z":3},"B2":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":23,"y":65.47,"z":3},"C2":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":23,"y":56.47,"z":3},"D2":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":23,"y":47.47,"z":3},"E2":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":23,"y":38.47,"z":3},"F2":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":23,"y":29.47,"z":3},"G2":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":23,"y":20.47,"z":3},"H2":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":23,"y":11.47,"z":3},"A3":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":32,"y":74.47,"z":3},"B3":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":32,"y":65.47,"z":3},"C3":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":32,"y":56.47,"z":3},"D3":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":32,"y":47.47,"z":3},"E3":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":32,"y":38.47,"z":3},"F3":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":32,"y":29.47,"z":3},"G3":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":32,"y":20.47,"z":3},"H3":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":32,"y":11.47,"z":3},"A4":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":41,"y":74.47,"z":3},"B4":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":41,"y":65.47,"z":3},"C4":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":41,"y":56.47,"z":3},"D4":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":41,"y":47.47,"z":3},"E4":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":41,"y":38.47,"z":3},"F4":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":41,"y":29.47,"z":3},"G4":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":41,"y":20.47,"z":3},"H4":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":41,"y":11.47,"z":3},"A5":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":50,"y":74.47,"z":3},"B5":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":50,"y":65.47,"z":3},"C5":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":50,"y":56.47,"z":3},"D5":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":50,"y":47.47,"z":3},"E5":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":50,"y":38.47,"z":3},"F5":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":50,"y":29.47,"z":3},"G5":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":50,"y":20.47,"z":3},"H5":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":50,"y":11.47,"z":3},"A6":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":59,"y":74.47,"z":3},"B6":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":59,"y":65.47,"z":3},"C6":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":59,"y":56.47,"z":3},"D6":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":59,"y":47.47,"z":3},"E6":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":59,"y":38.47,"z":3},"F6":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":59,"y":29.47,"z":3},"G6":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":59,"y":20.47,"z":3},"H6":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":59,"y":11.47,"z":3},"A7":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":68,"y":74.47,"z":3},"B7":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":68,"y":65.47,"z":3},"C7":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":68,"y":56.47,"z":3},"D7":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":68,"y":47.47,"z":3},"E7":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":68,"y":38.47,"z":3},"F7":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":68,"y":29.47,"z":3},"G7":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":68,"y":20.47,"z":3},"H7":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":68,"y":11.47,"z":3},"A8":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":77,"y":74.47,"z":3},"B8":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":77,"y":65.47,"z":3},"C8":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":77,"y":56.47,"z":3},"D8":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":77,"y":47.47,"z":3},"E8":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":77,"y":38.47,"z":3},"F8":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":77,"y":29.47,"z":3},"G8":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":77,"y":20.47,"z":3},"H8":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":77,"y":11.47,"z":3},"A9":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":86,"y":74.47,"z":3},"B9":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":86,"y":65.47,"z":3},"C9":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":86,"y":56.47,"z":3},"D9":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":86,"y":47.47,"z":3},"E9":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":86,"y":38.47,"z":3},"F9":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":86,"y":29.47,"z":3},"G9":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":86,"y":20.47,"z":3},"H9":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":86,"y":11.47,"z":3},"A10":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":95,"y":74.47,"z":3},"B10":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":95,"y":65.47,"z":3},"C10":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":95,"y":56.47,"z":3},"D10":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":95,"y":47.47,"z":3},"E10":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":95,"y":38.47,"z":3},"F10":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":95,"y":29.47,"z":3},"G10":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":95,"y":20.47,"z":3},"H10":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":95,"y":11.47,"z":3},"A11":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":104,"y":74.47,"z":3},"B11":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":104,"y":65.47,"z":3},"C11":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":104,"y":56.47,"z":3},"D11":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":104,"y":47.47,"z":3},"E11":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":104,"y":38.47,"z":3},"F11":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":104,"y":29.47,"z":3},"G11":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":104,"y":20.47,"z":3},"H11":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":104,"y":11.47,"z":3},"A12":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":113,"y":74.47,"z":3},"B12":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":113,"y":65.47,"z":3},"C12":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":113,"y":56.47,"z":3},"D12":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":113,"y":47.47,"z":3},"E12":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":113,"y":38.47,"z":3},"F12":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":113,"y":29.47,"z":3},"G12":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":113,"y":20.47,"z":3},"H12":{"depth":41,"totalLiquidVolume":2000,"shape":"rectangular","xDimension":8,"yDimension":8,"x":113,"y":11.47,"z":3}},"groups":[{"metadata":{"wellBottomShape":"v"},"wells":["A1","B1","C1","D1","E1","F1","G1","H1","A2","B2","C2","D2","E2","F2","G2","H2","A3","B3","C3","D3","E3","F3","G3","H3","A4","B4","C4","D4","E4","F4","G4","H4","A5","B5","C5","D5","E5","F5","G5","H5","A6","B6","C6","D6","E6","F6","G6","H6","A7","B7","C7","D7","E7","F7","G7","H7","A8","B8","C8","D8","E8","F8","G8","H8","A9","B9","C9","D9","E9","F9","G9","H9","A10","B10","C10","D10","E10","F10","G10","H10","A11","B11","C11","D11","E11","F11","G11","H11","A12","B12","C12","D12","E12","F12","G12","H12"]}],"parameters":{"format":"irregular","quirks":[],"isTiprack":false,"isMagneticModuleCompatible":false,"loadName":"thermo_kingfisher_96_deepwell_2ml"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}}}""")

DESIGNER_APPLICATION = """{"robot":{"model":"OT-2 Standard"},"designerApplication":{"name":"opentrons/protocol-designer","version":"8.8.0","data":{"pipetteTiprackAssignments":{"c1b2ebcc-dca9-4616-90f6-418886696aab":["opentrons/opentrons_96_tiprack_300ul/1"]},"dismissedWarnings":{"form":[],"timeline":[]},"ingredients":{"0":{"displayName":"50% ACN","description":"Conditioning solution","displayColor":"#ff6e6e","liquidGroupId":"0"},"1":{"displayName":"0.1% TFA","description":"Equilibration solution","displayColor":"#6e8eff","liquidGroupId":"1","liquidClass":null},"2":{"displayName":"0.1% TFA/5% ACN","description":"Rinse solution","displayColor":"#9dffd4","liquidGroupId":"2","liquidClass":null},"3":{"displayName":"0.1% Formic Acid/70% ACN","description":"Elution solution","displayColor":"#ffd752","liquidGroupId":"3","liquidClass":null},"4":{"displayName":"Sample","description":"Acidified peptide samples","displayColor":"#50d5ff","liquidGroupId":"4","liquidClass":null}},"ingredLocations":{"labware-1:opentrons/nest_12_reservoir_15ml/3":{"A1":{"0":{"volume":2000}},"A2":{"0":{"volume":2000}},"A3":{"0":{"volume":2000}},"A4":{"0":{"volume":2000}},"A5":{"0":{"volume":2000}},"A6":{"0":{"volume":2000}},"A7":{"0":{"volume":2000}},"A8":{"0":{"volume":2000}},"A9":{"0":{"volume":2000}},"A10":{"0":{"volume":2000}},"A11":{"0":{"volume":2000}},"A12":{"0":{"volume":2000}}},"labware-2:opentrons/nest_12_reservoir_15ml/3":{"A1":{"1":{"volume":2000}},"A2":{"1":{"volume":2000}},"A3":{"1":{"volume":2000}},"A4":{"1":{"volume":2000}},"A5":{"1":{"volume":2000}},"A6":{"1":{"volume":2000}},"A7":{"1":{"volume":2000}},"A8":{"1":{"volume":2000}},"A9":{"1":{"volume":2000}},"A10":{"1":{"volume":2000}},"A11":{"1":{"volume":2000}},"A12":{"1":{"volume":2000}}},"493d4361-5dad-4912-b8f2-c676cfbbb5da:custom_beta/thermo_kingfisher_96_deepwell_2ml/1":{"A1":{"3":{"volume":50}},"B1":{"3":{"volume":50}},"C1":{"3":{"volume":50}},"D1":{"3":{"volume":50}},"E1":{"3":{"volume":50}},"F1":{"3":{"volume":50}},"G1":{"3":{"volume":50}},"H1":{"3":{"volume":50}},"A2":{"3":{"volume":50}},"B2":{"3":{"volume":50}},"C2":{"3":{"volume":50}},"D2":{"3":{"volume":50}},"E2":{"3":{"volume":50}},"F2":{"3":{"volume":50}},"G2":{"3":{"volume":50}},"H2":{"3":{"volume":50}},"A3":{"3":{"volume":50}},"B3":{"3":{"volume":50}},"C3":{"3":{"volume":50}},"D3":{"3":{"volume":50}},"E3":{"3":{"volume":50}},"F3":{"3":{"volume":50}},"G3":{"3":{"volume":50}},"H3":{"3":{"volume":50}},"A4":{"3":{"volume":50}},"B4":{"3":{"volume":50}},"C4":{"3":{"volume":50}},"D4":{"3":{"volume":50}},"E4":{"3":{"volume":50}},"F4":{"3":{"volume":50}},"G4":{"3":{"volume":50}},"H4":{"3":{"volume":50}},"A5":{"3":{"volume":50}},"B5":{"3":{"volume":50}},"C5":{"3":{"volume":50}},"D5":{"3":{"volume":50}},"E5":{"3":{"volume":50}},"F5":{"3":{"volume":50}},"G5":{"3":{"volume":50}},"H5":{"3":{"volume":50}},"A6":{"3":{"volume":50}},"B6":{"3":{"volume":50}},"C6":{"3":{"volume":50}},"D6":{"3":{"volume":50}},"E6":{"3":{"volume":50}},"F6":{"3":{"volume":50}},"G6":{"3":{"volume":50}},"H6":{"3":{"volume":50}},"A7":{"3":{"volume":50}},"B7":{"3":{"volume":50}},"C7":{"3":{"volume":50}},"D7":{"3":{"volume":50}},"E7":{"3":{"volume":50}},"F7":{"3":{"volume":50}},"G7":{"3":{"volume":50}},"H7":{"3":{"volume":50}},"A8":{"3":{"volume":50}},"B8":{"3":{"volume":50}},"C8":{"3":{"volume":50}},"D8":{"3":{"volume":50}},"E8":{"3":{"volume":50}},"F8":{"3":{"volume":50}},"G8":{"3":{"volume":50}},"H8":{"3":{"volume":50}},"A9":{"3":{"volume":50}},"B9":{"3":{"volume":50}},"C9":{"3":{"volume":50}},"D9":{"3":{"volume":50}},"E9":{"3":{"volume":50}},"F9":{"3":{"volume":50}},"G9":{"3":{"volume":50}},"H9":{"3":{"volume":50}},"A10":{"3":{"volume":50}},"B10":{"3":{"volume":50}},"C10":{"3":{"volume":50}},"D10":{"3":{"volume":50}},"E10":{"3":{"volume":50}},"F10":{"3":{"volume":50}},"G10":{"3":{"volume":50}},"H10":{"3":{"volume":50}},"A11":{"3":{"volume":50}},"B11":{"3":{"volume":50}},"C11":{"3":{"volume":50}},"D11":{"3":{"volume":50}},"E11":{"3":{"volume":50}},"F11":{"3":{"volume":50}},"G11":{"3":{"volume":50}},"H11":{"3":{"volume":50}},"A12":{"3":{"volume":50}},"B12":{"3":{"volume":50}},"C12":{"3":{"volume":50}},"D12":{"3":{"volume":50}},"E12":{"3":{"volume":50}},"F12":{"3":{"volume":50}},"G12":{"3":{"volume":50}},"H12":{"3":{"volume":50}}},"4a5d3464-21f9-4fb5-8a3f-552680c3c2bc:custom_beta/thermo_kingfisher_96_deepwell_2ml/1":{"A1":{"4":{"volume":100}},"B1":{"4":{"volume":100}},"C1":{"4":{"volume":100}},"D1":{"4":{"volume":100}},"E1":{"4":{"volume":100}},"F1":{"4":{"volume":100}},"G1":{"4":{"volume":100}},"H1":{"4":{"volume":100}},"A2":{"4":{"volume":100}},"B2":{"4":{"volume":100}},"C2":{"4":{"volume":100}},"D2":{"4":{"volume":100}},"E2":{"4":{"volume":100}},"F2":{"4":{"volume":100}},"G2":{"4":{"volume":100}},"H2":{"4":{"volume":100}},"A3":{"4":{"volume":100}},"B3":{"4":{"volume":100}},"C3":{"4":{"volume":100}},"D3":{"4":{"volume":100}},"E3":{"4":{"volume":100}},"F3":{"4":{"volume":100}},"G3":{"4":{"volume":100}},"H3":{"4":{"volume":100}},"A4":{"4":{"volume":100}},"B4":{"4":{"volume":100}},"C4":{"4":{"volume":100}},"D4":{"4":{"volume":100}},"E4":{"4":{"volume":100}},"F4":{"4":{"volume":100}},"G4":{"4":{"volume":100}},"H4":{"4":{"volume":100}},"A5":{"4":{"volume":100}},"B5":{"4":{"volume":100}},"C5":{"4":{"volume":100}},"D5":{"4":{"volume":100}},"E5":{"4":{"volume":100}},"F5":{"4":{"volume":100}},"G5":{"4":{"volume":100}},"H5":{"4":{"volume":100}},"A6":{"4":{"volume":100}},"B6":{"4":{"volume":100}},"C6":{"4":{"volume":100}},"D6":{"4":{"volume":100}},"E6":{"4":{"volume":100}},"F6":{"4":{"volume":100}},"G6":{"4":{"volume":100}},"H6":{"4":{"volume":100}},"A7":{"4":{"volume":100}},"B7":{"4":{"volume":100}},"C7":{"4":{"volume":100}},"D7":{"4":{"volume":100}},"E7":{"4":{"volume":100}},"F7":{"4":{"volume":100}},"G7":{"4":{"volume":100}},"H7":{"4":{"volume":100}},"A8":{"4":{"volume":100}},"B8":{"4":{"volume":100}},"C8":{"4":{"volume":100}},"D8":{"4":{"volume":100}},"E8":{"4":{"volume":100}},"F8":{"4":{"volume":100}},"G8":{"4":{"volume":100}},"H8":{"4":{"volume":100}},"A9":{"4":{"volume":100}},"B9":{"4":{"volume":100}},"C9":{"4":{"volume":100}},"D9":{"4":{"volume":100}},"E9":{"4":{"volume":100}},"F9":{"4":{"volume":100}},"G9":{"4":{"volume":100}},"H9":{"4":{"volume":100}},"A10":{"4":{"volume":100}},"B10":{"4":{"volume":100}},"C10":{"4":{"volume":100}},"D10":{"4":{"volume":100}},"E10":{"4":{"volume":100}},"F10":{"4":{"volume":100}},"G10":{"4":{"volume":100}},"H10":{"4":{"volume":100}},"A11":{"4":{"volume":100}},"B11":{"4":{"volume":100}},"C11":{"4":{"volume":100}},"D11":{"4":{"volume":100}},"E11":{"4":{"volume":100}},"F11":{"4":{"volume":100}},"G11":{"4":{"volume":100}},"H11":{"4":{"volume":100}},"A12":{"4":{"volume":100}},"B12":{"4":{"volume":100}},"C12":{"4":{"volume":100}},"D12":{"4":{"volume":100}},"E12":{"4":{"volume":100}},"F12":{"4":{"volume":100}},"G12":{"4":{"volume":100}},"H12":{"4":{"volume":100}}},"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1":{"A1":{"2":{"volume":200}},"B1":{"2":{"volume":200}},"C1":{"2":{"volume":200}},"D1":{"2":{"volume":200}},"E1":{"2":{"volume":200}},"F1":{"2":{"volume":200}},"G1":{"2":{"volume":200}},"H1":{"2":{"volume":200}},"A2":{"2":{"volume":200}},"B2":{"2":{"volume":200}},"C2":{"2":{"volume":200}},"D2":{"2":{"volume":200}},"E2":{"2":{"volume":200}},"F2":{"2":{"volume":200}},"G2":{"2":{"volume":200}},"H2":{"2":{"volume":200}},"A3":{"2":{"volume":200}},"B3":{"2":{"volume":200}},"C3":{"2":{"volume":200}},"D3":{"2":{"volume":200}},"E3":{"2":{"volume":200}},"F3":{"2":{"volume":200}},"G3":{"2":{"volume":200}},"H3":{"2":{"volume":200}},"A4":{"2":{"volume":200}},"B4":{"2":{"volume":200}},"C4":{"2":{"volume":200}},"D4":{"2":{"volume":200}},"E4":{"2":{"volume":200}},"F4":{"2":{"volume":200}},"G4":{"2":{"volume":200}},"H4":{"2":{"volume":200}},"A5":{"2":{"volume":200}},"B5":{"2":{"volume":200}},"C5":{"2":{"volume":200}},"D5":{"2":{"volume":200}},"E5":{"2":{"volume":200}},"F5":{"2":{"volume":200}},"G5":{"2":{"volume":200}},"H5":{"2":{"volume":200}},"A6":{"2":{"volume":200}},"B6":{"2":{"volume":200}},"C6":{"2":{"volume":200}},"D6":{"2":{"volume":200}},"E6":{"2":{"volume":200}},"F6":{"2":{"volume":200}},"G6":{"2":{"volume":200}},"H6":{"2":{"volume":200}},"A7":{"2":{"volume":200}},"B7":{"2":{"volume":200}},"C7":{"2":{"volume":200}},"D7":{"2":{"volume":200}},"E7":{"2":{"volume":200}},"F7":{"2":{"volume":200}},"G7":{"2":{"volume":200}},"H7":{"2":{"volume":200}},"A8":{"2":{"volume":200}},"B8":{"2":{"volume":200}},"C8":{"2":{"volume":200}},"D8":{"2":{"volume":200}},"E8":{"2":{"volume":200}},"F8":{"2":{"volume":200}},"G8":{"2":{"volume":200}},"H8":{"2":{"volume":200}},"A9":{"2":{"volume":200}},"B9":{"2":{"volume":200}},"C9":{"2":{"volume":200}},"D9":{"2":{"volume":200}},"E9":{"2":{"volume":200}},"F9":{"2":{"volume":200}},"G9":{"2":{"volume":200}},"H9":{"2":{"volume":200}},"A10":{"2":{"volume":200}},"B10":{"2":{"volume":200}},"C10":{"2":{"volume":200}},"D10":{"2":{"volume":200}},"E10":{"2":{"volume":200}},"F10":{"2":{"volume":200}},"G10":{"2":{"volume":200}},"H10":{"2":{"volume":200}},"A11":{"2":{"volume":200}},"B11":{"2":{"volume":200}},"C11":{"2":{"volume":200}},"D11":{"2":{"volume":200}},"E11":{"2":{"volume":200}},"F11":{"2":{"volume":200}},"G11":{"2":{"volume":200}},"H11":{"2":{"volume":200}},"A12":{"2":{"volume":200}},"B12":{"2":{"volume":200}},"C12":{"2":{"volume":200}},"D12":{"2":{"volume":200}},"E12":{"2":{"volume":200}},"F12":{"2":{"volume":200}},"G12":{"2":{"volume":200}},"H12":{"2":{"volume":200}}}},"savedStepForms":{"__INITIAL_DECK_SETUP_STEP__":{"stepType":"manualIntervention","id":"__INITIAL_DECK_SETUP_STEP__","labwareLocationUpdate":{"labware-1:opentrons/nest_12_reservoir_15ml/3":"7","labware-2:opentrons/nest_12_reservoir_15ml/3":"4","labware-3:opentrons/nest_12_reservoir_15ml/3":"8","labware-4:opentrons/nest_12_reservoir_15ml/3":"5","labware-9:opentrons/opentrons_96_tiprack_300ul/1":"10","493d4361-5dad-4912-b8f2-c676cfbbb5da:custom_beta/thermo_kingfisher_96_deepwell_2ml/1":"3","f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1":"11","4a5d3464-21f9-4fb5-8a3f-552680c3c2bc:custom_beta/thermo_kingfisher_96_deepwell_2ml/1":"1","b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1":"2"},"pipetteLocationUpdate":{"c1b2ebcc-dca9-4616-90f6-418886696aab":"right"},"moduleLocationUpdate":{},"trashBinLocationUpdate":{"trashbin-1":"cutout12"},"wasteChuteLocationUpdate":{},"stagingAreaLocationUpdate":{},"gripperLocationUpdate":{},"moduleStateUpdate":{}},"step-1":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-1:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-3","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-3:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":true,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 1: Conditioning 1st","stepDetails":"","id":"step-1","dispense_touchTip_mmfromTop":null},"step-2":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-1:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-3","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-3:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 1: Conditioning 2nd","stepDetails":"","id":"step-2","dispense_touchTip_mmfromTop":null},"step-3":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"3","aspirate_flowRate":"30","aspirate_labware":"labware-2:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"dest_well","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-4:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 1: Equilibrate 1st","stepDetails":"","id":"step-3","dispense_touchTip_mmfromTop":null},"step-4":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-2:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"dest_well","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-4:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 1: Equilibrate 2nd","stepDetails":"","id":"step-4","dispense_touchTip_mmfromTop":null},"step-5":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dropTip_location":"trashbin-1","labware":"4a5d3464-21f9-4fb5-8a3f-552680c3c2bc:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","pushOut_checkbox":false,"pushOut_volume":0,"times":"5","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","wells":["A1"],"stepType":"mix","stepName":"Col 1: Load sample","stepDetails":"","id":"step-5"},"step-6":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-4","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 1: Rinse 1st","stepDetails":"","id":"step-6","dispense_touchTip_mmfromTop":null},"step-7":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-4","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 1: Rinse 2nd","stepDetails":"","id":"step-7","dispense_touchTip_mmfromTop":null},"17438349-9ef5-4b0a-86d1-c8c2035315b9":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","blowout_checkbox":true,"blowout_flowRate":94,"blowout_location":"dest_well","blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dropTip_location":"trashbin-1","labware":"493d4361-5dad-4912-b8f2-c676cfbbb5da:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","pushOut_checkbox":true,"pushOut_volume":"20","times":"5","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"50","wells":["A1"],"stepType":"mix","stepName":"Col 1: ELUTE Sample","stepDetails":"","id":"17438349-9ef5-4b0a-86d1-c8c2035315b9"},"e2019c30-6b40-4bec-a4ca-0bceae952f3c":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-1:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-3","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-3:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":true,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 2: Conditioning 1st","stepDetails":"","id":"e2019c30-6b40-4bec-a4ca-0bceae952f3c","dispense_touchTip_mmfromTop":null},"cad42a6d-a644-485b-b8b4-8a5b2d5ba8c1":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-1:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-3","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-3:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 2: Conditioning 2nd","stepDetails":"","id":"cad42a6d-a644-485b-b8b4-8a5b2d5ba8c1","dispense_touchTip_mmfromTop":null},"e6781b49-8830-481f-be3a-7863d6990994":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"3","aspirate_flowRate":"30","aspirate_labware":"labware-2:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"dest_well","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-4:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 2: Equilibrate 1st","stepDetails":"","id":"e6781b49-8830-481f-be3a-7863d6990994","dispense_touchTip_mmfromTop":null},"eafcf019-cce8-4d2a-b3c0-6d51c4bcbea8":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-2:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"dest_well","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-4:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 2: Equilibrate 2nd","stepDetails":"","id":"eafcf019-cce8-4d2a-b3c0-6d51c4bcbea8","dispense_touchTip_mmfromTop":null},"b71c1767-e3f4-4608-af4c-6f0efea4cbd4":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dropTip_location":"trashbin-1","labware":"4a5d3464-21f9-4fb5-8a3f-552680c3c2bc:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","pushOut_checkbox":false,"pushOut_volume":0,"times":"5","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","wells":["A2"],"stepType":"mix","stepName":"Col 2: Load sample","stepDetails":"","id":"b71c1767-e3f4-4608-af4c-6f0efea4cbd4"},"a383761a-d67e-4998-a06f-4380fe58de15":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-4","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 2: Rinse 1st","stepDetails":"","id":"a383761a-d67e-4998-a06f-4380fe58de15","dispense_touchTip_mmfromTop":null},"65c401ea-d280-4291-a07a-55756b3020a7":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-4","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 2: Rinse 2nd","stepDetails":"","id":"65c401ea-d280-4291-a07a-55756b3020a7","dispense_touchTip_mmfromTop":null},"7d988df8-d34e-4964-bf38-99f34bc54b9c":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","blowout_checkbox":true,"blowout_flowRate":94,"blowout_location":"dest_well","blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dropTip_location":"trashbin-1","labware":"493d4361-5dad-4912-b8f2-c676cfbbb5da:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","pushOut_checkbox":true,"pushOut_volume":"20","times":"5","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"50","wells":["A2"],"stepType":"mix","stepName":"Col 2: ELUTE Sample","stepDetails":"","id":"7d988df8-d34e-4964-bf38-99f34bc54b9c"},"37cd4644-cd6b-4a78-8c65-a49c85e54536":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-1:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-3","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-3:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":true,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 3: Conditioning 1st","stepDetails":"","id":"37cd4644-cd6b-4a78-8c65-a49c85e54536","dispense_touchTip_mmfromTop":null},"f8a43d4d-22f8-4508-a873-319c5b24c933":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-1:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-3","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-3:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 3: Conditioning 2nd","stepDetails":"","id":"f8a43d4d-22f8-4508-a873-319c5b24c933","dispense_touchTip_mmfromTop":null},"cfe5d147-7578-4d44-a9a9-36a7e67288d6":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"3","aspirate_flowRate":"30","aspirate_labware":"labware-2:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"dest_well","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-4:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 3: Equilibrate 1st","stepDetails":"","id":"cfe5d147-7578-4d44-a9a9-36a7e67288d6","dispense_touchTip_mmfromTop":null},"04d69dee-4c9d-42d2-914d-cb4cd1641ae2":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-2:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"dest_well","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-4:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 3: Equilibrate 2nd","stepDetails":"","id":"04d69dee-4c9d-42d2-914d-cb4cd1641ae2","dispense_touchTip_mmfromTop":null},"4048742f-9b04-427d-bc3c-5e8352518f8f":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dropTip_location":"trashbin-1","labware":"4a5d3464-21f9-4fb5-8a3f-552680c3c2bc:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","pushOut_checkbox":false,"pushOut_volume":0,"times":"5","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","wells":["A3"],"stepType":"mix","stepName":"Col 3: Load sample","stepDetails":"","id":"4048742f-9b04-427d-bc3c-5e8352518f8f"},"d2cd7488-319c-4080-9d1f-cd1335b28ecf":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-4","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 3: Rinse 1st","stepDetails":"","id":"d2cd7488-319c-4080-9d1f-cd1335b28ecf","dispense_touchTip_mmfromTop":null},"8b107c8b-5c52-40e0-b404-acce6b2b7be7":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-4","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 3: Rinse 2nd","stepDetails":"","id":"8b107c8b-5c52-40e0-b404-acce6b2b7be7","dispense_touchTip_mmfromTop":null},"62e8e9bc-3b45-4abc-8657-668d01e5d3a6":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","blowout_checkbox":true,"blowout_flowRate":94,"blowout_location":"dest_well","blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dropTip_location":"trashbin-1","labware":"493d4361-5dad-4912-b8f2-c676cfbbb5da:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","pushOut_checkbox":true,"pushOut_volume":"20","times":"5","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"50","wells":["A3"],"stepType":"mix","stepName":"Col 3: ELUTE Sample","stepDetails":"","id":"62e8e9bc-3b45-4abc-8657-668d01e5d3a6"},"84316cf6-6e6e-4930-b8c4-d1d2f3752645":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-1:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-3","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-3:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":true,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 4: Conditioning 1st","stepDetails":"","id":"84316cf6-6e6e-4930-b8c4-d1d2f3752645","dispense_touchTip_mmfromTop":null},"46166675-caf5-4acc-a4b7-6cd3534f42b2":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-1:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-3","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-3:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 4: Conditioning 2nd","stepDetails":"","id":"46166675-caf5-4acc-a4b7-6cd3534f42b2","dispense_touchTip_mmfromTop":null},"27a33688-3613-4f1a-8dd4-d16537223d79":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"3","aspirate_flowRate":"30","aspirate_labware":"labware-2:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"dest_well","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-4:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 4: Equilibrate 1st","stepDetails":"","id":"27a33688-3613-4f1a-8dd4-d16537223d79","dispense_touchTip_mmfromTop":null},"d6c14ede-3853-4612-9595-c45c6cdf3ca0":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-2:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"dest_well","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-4:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 4: Equilibrate 2nd","stepDetails":"","id":"d6c14ede-3853-4612-9595-c45c6cdf3ca0","dispense_touchTip_mmfromTop":null},"ea488171-e216-4d1d-96e5-081ea68c57a2":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dropTip_location":"trashbin-1","labware":"4a5d3464-21f9-4fb5-8a3f-552680c3c2bc:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","pushOut_checkbox":false,"pushOut_volume":0,"times":"5","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","wells":["A4"],"stepType":"mix","stepName":"Col 4: Load sample","stepDetails":"","id":"ea488171-e216-4d1d-96e5-081ea68c57a2"},"34f1e51a-8bfe-4c02-a37f-6015f53fe8d8":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-4","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 4: Rinse 1st","stepDetails":"","id":"34f1e51a-8bfe-4c02-a37f-6015f53fe8d8","dispense_touchTip_mmfromTop":null},"5266fa19-5e18-4d2f-a0b2-956ece4b3a61":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-4","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 4: Rinse 2nd","stepDetails":"","id":"5266fa19-5e18-4d2f-a0b2-956ece4b3a61","dispense_touchTip_mmfromTop":null},"8e52efcb-fe63-4982-85c7-682da86e4594":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","blowout_checkbox":true,"blowout_flowRate":94,"blowout_location":"dest_well","blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dropTip_location":"trashbin-1","labware":"493d4361-5dad-4912-b8f2-c676cfbbb5da:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","pushOut_checkbox":true,"pushOut_volume":"20","times":"5","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"50","wells":["A4"],"stepType":"mix","stepName":"Col 4: ELUTE Sample","stepDetails":"","id":"8e52efcb-fe63-4982-85c7-682da86e4594"},"d66059e3-0a14-48b8-9206-9b361f436efa":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-1:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A5"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-3","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-3:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A5"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":true,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 5: Conditioning 1st","stepDetails":"","id":"d66059e3-0a14-48b8-9206-9b361f436efa","dispense_touchTip_mmfromTop":null},"1f33b65a-819d-47e9-b8ed-d7ab8bff4f26":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-1:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A5"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-3","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-3:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A5"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 5: Conditioning 2nd","stepDetails":"","id":"1f33b65a-819d-47e9-b8ed-d7ab8bff4f26","dispense_touchTip_mmfromTop":null},"0a380ebd-17d1-4477-bcf6-eb3fdbc70830":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"3","aspirate_flowRate":"30","aspirate_labware":"labware-2:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A5"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"dest_well","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-4:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A5"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 5: Equilibrate 1st","stepDetails":"","id":"0a380ebd-17d1-4477-bcf6-eb3fdbc70830","dispense_touchTip_mmfromTop":null},"9786a59c-fcab-4bcc-9dbc-ca52cfcb98ea":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-2:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A5"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"dest_well","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-4:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A5"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 5: Equilibrate 2nd","stepDetails":"","id":"9786a59c-fcab-4bcc-9dbc-ca52cfcb98ea","dispense_touchTip_mmfromTop":null},"08fb7dfd-592d-42cd-a443-85b4c2490aa2":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dropTip_location":"trashbin-1","labware":"4a5d3464-21f9-4fb5-8a3f-552680c3c2bc:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","pushOut_checkbox":false,"pushOut_volume":0,"times":"5","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","wells":["A5"],"stepType":"mix","stepName":"Col 5: Load sample","stepDetails":"","id":"08fb7dfd-592d-42cd-a443-85b4c2490aa2"},"283e211d-6029-4c97-a7c8-0cd6a0566cb2":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A5"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-4","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A5"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 5: Rinse 1st","stepDetails":"","id":"283e211d-6029-4c97-a7c8-0cd6a0566cb2","dispense_touchTip_mmfromTop":null},"8f1b269b-1d47-4c03-9fc7-ddf317c2d574":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A5"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-4","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A5"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 5: Rinse 2nd","stepDetails":"","id":"8f1b269b-1d47-4c03-9fc7-ddf317c2d574","dispense_touchTip_mmfromTop":null},"d74e8c9f-1731-48ce-b2de-fb04e7d1df6e":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","blowout_checkbox":true,"blowout_flowRate":94,"blowout_location":"dest_well","blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dropTip_location":"trashbin-1","labware":"493d4361-5dad-4912-b8f2-c676cfbbb5da:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","pushOut_checkbox":true,"pushOut_volume":"20","times":"5","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"50","wells":["A5"],"stepType":"mix","stepName":"Col 5: ELUTE Sample","stepDetails":"","id":"d74e8c9f-1731-48ce-b2de-fb04e7d1df6e"},"55b9c967-d3f6-47aa-8b90-4768be3de442":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-1:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-3","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-3:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":true,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 6: Conditioning 1st","stepDetails":"","id":"55b9c967-d3f6-47aa-8b90-4768be3de442","dispense_touchTip_mmfromTop":null},"ffc40d81-aa4d-4eb9-8134-ccb2fcf9adce":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-1:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-3","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-3:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 6: Conditioning 2nd","stepDetails":"","id":"ffc40d81-aa4d-4eb9-8134-ccb2fcf9adce","dispense_touchTip_mmfromTop":null},"f83b0adf-e818-4f55-88fd-a46b7c00ff56":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"3","aspirate_flowRate":"30","aspirate_labware":"labware-2:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"dest_well","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-4:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 6: Equilibrate 1st","stepDetails":"","id":"f83b0adf-e818-4f55-88fd-a46b7c00ff56","dispense_touchTip_mmfromTop":null},"196d0421-7782-46fd-870d-9526d0b95215":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-2:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"dest_well","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-4:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 6: Equilibrate 2nd","stepDetails":"","id":"196d0421-7782-46fd-870d-9526d0b95215","dispense_touchTip_mmfromTop":null},"1575c014-f310-4226-b6d7-add708bc0528":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dropTip_location":"trashbin-1","labware":"4a5d3464-21f9-4fb5-8a3f-552680c3c2bc:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","pushOut_checkbox":false,"pushOut_volume":0,"times":"5","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","wells":["A6"],"stepType":"mix","stepName":"Col 6: Load sample","stepDetails":"","id":"1575c014-f310-4226-b6d7-add708bc0528"},"46e68c97-1efe-4bcc-89cd-ffb620f85a42":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-4","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 6: Rinse 1st","stepDetails":"","id":"46e68c97-1efe-4bcc-89cd-ffb620f85a42","dispense_touchTip_mmfromTop":null},"8ae8e0c9-e3a3-49ea-b1c4-d8635c4db916":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-4","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 6: Rinse 2nd","stepDetails":"","id":"8ae8e0c9-e3a3-49ea-b1c4-d8635c4db916","dispense_touchTip_mmfromTop":null},"1a6a1e4d-1ecd-4307-b1f1-ca6e49d88077":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","blowout_checkbox":true,"blowout_flowRate":94,"blowout_location":"dest_well","blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dropTip_location":"trashbin-1","labware":"493d4361-5dad-4912-b8f2-c676cfbbb5da:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","pushOut_checkbox":true,"pushOut_volume":"20","times":"5","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"50","wells":["A6"],"stepType":"mix","stepName":"Col 6: ELUTE Sample","stepDetails":"","id":"1a6a1e4d-1ecd-4307-b1f1-ca6e49d88077"},"01a4e84a-8b7f-4465-bba9-75a0f2c3adde":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-1:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A7"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-3","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-3:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A7"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":true,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 7: Conditioning 1st","stepDetails":"","id":"01a4e84a-8b7f-4465-bba9-75a0f2c3adde","dispense_touchTip_mmfromTop":null},"be272985-9dc4-4f3c-8f27-d437dfa7add7":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-1:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A7"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-3","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-3:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A7"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 7: Conditioning 2nd","stepDetails":"","id":"be272985-9dc4-4f3c-8f27-d437dfa7add7","dispense_touchTip_mmfromTop":null},"31f2cc35-58a9-47a1-a0aa-e9282eda85b7":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"3","aspirate_flowRate":"30","aspirate_labware":"labware-2:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A7"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"dest_well","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-4:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A7"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 7: Equilibrate 1st","stepDetails":"","id":"31f2cc35-58a9-47a1-a0aa-e9282eda85b7","dispense_touchTip_mmfromTop":null},"b77d48d5-c784-4c76-a29b-ba8cb046fe3a":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-2:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A7"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"dest_well","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-4:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A7"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 7: Equilibrate 2nd","stepDetails":"","id":"b77d48d5-c784-4c76-a29b-ba8cb046fe3a","dispense_touchTip_mmfromTop":null},"d40b28e9-1b18-453c-8dc8-a0d5da06b93a":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dropTip_location":"trashbin-1","labware":"4a5d3464-21f9-4fb5-8a3f-552680c3c2bc:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","pushOut_checkbox":false,"pushOut_volume":0,"times":"5","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","wells":["A7"],"stepType":"mix","stepName":"Col 7: Load sample","stepDetails":"","id":"d40b28e9-1b18-453c-8dc8-a0d5da06b93a"},"0188566c-fe07-498d-82c0-82f236fe5f5f":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A7"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-4","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A7"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 7: Rinse 1st","stepDetails":"","id":"0188566c-fe07-498d-82c0-82f236fe5f5f","dispense_touchTip_mmfromTop":null},"e0de49ae-cb28-4acd-a5d1-f284c74617e6":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A7"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-4","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A7"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 7: Rinse 2nd","stepDetails":"","id":"e0de49ae-cb28-4acd-a5d1-f284c74617e6","dispense_touchTip_mmfromTop":null},"0eecdbeb-87ee-4fc2-b888-cb26bc3826e1":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","blowout_checkbox":true,"blowout_flowRate":94,"blowout_location":"dest_well","blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dropTip_location":"trashbin-1","labware":"493d4361-5dad-4912-b8f2-c676cfbbb5da:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","pushOut_checkbox":true,"pushOut_volume":"20","times":"5","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"50","wells":["A7"],"stepType":"mix","stepName":"Col 7: ELUTE Sample","stepDetails":"","id":"0eecdbeb-87ee-4fc2-b888-cb26bc3826e1"},"469c0be5-4522-4570-b23a-eb452211f908":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-1:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A8"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-3","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-3:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A8"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":true,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 8: Conditioning 1st","stepDetails":"","id":"469c0be5-4522-4570-b23a-eb452211f908","dispense_touchTip_mmfromTop":null},"21ffb8bd-fd30-4d9b-91d8-cb9329ae8fa3":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-1:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A8"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-3","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-3:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A8"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 8: Conditioning 2nd","stepDetails":"","id":"21ffb8bd-fd30-4d9b-91d8-cb9329ae8fa3","dispense_touchTip_mmfromTop":null},"f6de6060-641a-4693-9cb9-4331de7b6848":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"3","aspirate_flowRate":"30","aspirate_labware":"labware-2:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A8"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"dest_well","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-4:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A8"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 8: Equilibrate 1st","stepDetails":"","id":"f6de6060-641a-4693-9cb9-4331de7b6848","dispense_touchTip_mmfromTop":null},"a9df697f-423e-4d44-b58d-d7ec6984a33b":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-2:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A8"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"dest_well","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-4:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A8"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 8: Equilibrate 2nd","stepDetails":"","id":"a9df697f-423e-4d44-b58d-d7ec6984a33b","dispense_touchTip_mmfromTop":null},"2e02cb47-c933-483a-babc-5cfc3c0dc859":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dropTip_location":"trashbin-1","labware":"4a5d3464-21f9-4fb5-8a3f-552680c3c2bc:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","pushOut_checkbox":false,"pushOut_volume":0,"times":"5","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","wells":["A8"],"stepType":"mix","stepName":"Col 8: Load sample","stepDetails":"","id":"2e02cb47-c933-483a-babc-5cfc3c0dc859"},"153dfdc1-d2e4-4020-933f-11631095a1f5":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A8"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-4","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A8"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 8: Rinse 1st","stepDetails":"","id":"153dfdc1-d2e4-4020-933f-11631095a1f5","dispense_touchTip_mmfromTop":null},"ec6d63a6-5842-4dea-bcef-fe0432947cab":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A8"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-4","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A8"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 8: Rinse 2nd","stepDetails":"","id":"ec6d63a6-5842-4dea-bcef-fe0432947cab","dispense_touchTip_mmfromTop":null},"482eb4e9-4e66-4b37-ac5f-eb2edec579a3":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","blowout_checkbox":true,"blowout_flowRate":94,"blowout_location":"dest_well","blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dropTip_location":"trashbin-1","labware":"493d4361-5dad-4912-b8f2-c676cfbbb5da:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","pushOut_checkbox":true,"pushOut_volume":"20","times":"5","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"50","wells":["A8"],"stepType":"mix","stepName":"Col 8: ELUTE Sample","stepDetails":"","id":"482eb4e9-4e66-4b37-ac5f-eb2edec579a3"},"45d00abd-14bc-43ad-812c-2251d7dde4a9":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-1:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A9"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-3","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-3:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A9"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":true,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 9: Conditioning 1st","stepDetails":"","id":"45d00abd-14bc-43ad-812c-2251d7dde4a9","dispense_touchTip_mmfromTop":null},"93668514-bae4-4e8d-8070-cacb13c2800f":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-1:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A9"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-3","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-3:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A9"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 9: Conditioning 2nd","stepDetails":"","id":"93668514-bae4-4e8d-8070-cacb13c2800f","dispense_touchTip_mmfromTop":null},"c553f2d1-1af7-4772-88ca-0e097b966e16":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"3","aspirate_flowRate":"30","aspirate_labware":"labware-2:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A9"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"dest_well","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-4:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A9"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 9: Equilibrate 1st","stepDetails":"","id":"c553f2d1-1af7-4772-88ca-0e097b966e16","dispense_touchTip_mmfromTop":null},"91ef7c07-a998-4bb2-9e23-025bd0e7d035":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-2:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A9"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"dest_well","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-4:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A9"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 9: Equilibrate 2nd","stepDetails":"","id":"91ef7c07-a998-4bb2-9e23-025bd0e7d035","dispense_touchTip_mmfromTop":null},"4cca2d6c-116e-4005-bae6-a32a16eb73fb":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dropTip_location":"trashbin-1","labware":"4a5d3464-21f9-4fb5-8a3f-552680c3c2bc:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","pushOut_checkbox":false,"pushOut_volume":0,"times":"5","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","wells":["A9"],"stepType":"mix","stepName":"Col 9: Load sample","stepDetails":"","id":"4cca2d6c-116e-4005-bae6-a32a16eb73fb"},"cce27324-4b9a-46a2-9acd-ab81abc6bf29":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A9"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-4","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A9"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 9: Rinse 1st","stepDetails":"","id":"cce27324-4b9a-46a2-9acd-ab81abc6bf29","dispense_touchTip_mmfromTop":null},"9087859c-8d3f-41ef-b2ea-e66a77b88956":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A9"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-4","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A9"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 9: Rinse 2nd","stepDetails":"","id":"9087859c-8d3f-41ef-b2ea-e66a77b88956","dispense_touchTip_mmfromTop":null},"e49c5df8-bbb8-415f-be8b-85d57127de61":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","blowout_checkbox":true,"blowout_flowRate":94,"blowout_location":"dest_well","blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dropTip_location":"trashbin-1","labware":"493d4361-5dad-4912-b8f2-c676cfbbb5da:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","pushOut_checkbox":true,"pushOut_volume":"20","times":"5","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"50","wells":["A9"],"stepType":"mix","stepName":"Col 9: ELUTE Sample","stepDetails":"","id":"e49c5df8-bbb8-415f-be8b-85d57127de61"},"29e047cf-60d8-4183-98af-816067b0bb77":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-1:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A10"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-3","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-3:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A10"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":true,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 10: Conditioning 1st","stepDetails":"","id":"29e047cf-60d8-4183-98af-816067b0bb77","dispense_touchTip_mmfromTop":null},"842f3ace-0a5c-4dac-9b6b-0569548d2778":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-1:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A10"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-3","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-3:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A10"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 10: Conditioning 2nd","stepDetails":"","id":"842f3ace-0a5c-4dac-9b6b-0569548d2778","dispense_touchTip_mmfromTop":null},"f86ec4dc-fcfc-4f68-a82f-13936544c5d4":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"3","aspirate_flowRate":"30","aspirate_labware":"labware-2:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A10"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"dest_well","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-4:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A10"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 10: Equilibrate 1st","stepDetails":"","id":"f86ec4dc-fcfc-4f68-a82f-13936544c5d4","dispense_touchTip_mmfromTop":null},"cd876d26-e323-4225-8577-875195aaf950":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-2:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A10"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"dest_well","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-4:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A10"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 10: Equilibrate 2nd","stepDetails":"","id":"cd876d26-e323-4225-8577-875195aaf950","dispense_touchTip_mmfromTop":null},"7a913aea-6940-4dbc-b822-5a7fe3f48f25":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dropTip_location":"trashbin-1","labware":"4a5d3464-21f9-4fb5-8a3f-552680c3c2bc:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","pushOut_checkbox":false,"pushOut_volume":0,"times":"5","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","wells":["A10"],"stepType":"mix","stepName":"Col 10: Load sample","stepDetails":"","id":"7a913aea-6940-4dbc-b822-5a7fe3f48f25"},"8c62ea9c-d1e0-4d58-afd6-f7b4282b56f0":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A10"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-4","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A10"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 10: Rinse 1st","stepDetails":"","id":"8c62ea9c-d1e0-4d58-afd6-f7b4282b56f0","dispense_touchTip_mmfromTop":null},"f54c7d9f-b442-44e1-9780-7549959fc684":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A10"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-4","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A10"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 10: Rinse 2nd","stepDetails":"","id":"f54c7d9f-b442-44e1-9780-7549959fc684","dispense_touchTip_mmfromTop":null},"cb54ba87-1174-4529-bc70-5a930d3893b0":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","blowout_checkbox":true,"blowout_flowRate":94,"blowout_location":"dest_well","blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dropTip_location":"trashbin-1","labware":"493d4361-5dad-4912-b8f2-c676cfbbb5da:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","pushOut_checkbox":true,"pushOut_volume":"20","times":"5","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"50","wells":["A10"],"stepType":"mix","stepName":"Col 10: ELUTE Sample","stepDetails":"","id":"cb54ba87-1174-4529-bc70-5a930d3893b0"},"97b45d40-94b6-4a98-9cf9-dc3fe8a307e1":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-1:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A11"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-3","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-3:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A11"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":true,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 11: Conditioning 1st","stepDetails":"","id":"97b45d40-94b6-4a98-9cf9-dc3fe8a307e1","dispense_touchTip_mmfromTop":null},"6135a255-6613-4e5e-9bae-9e698c763b02":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-1:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A11"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-3","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-3:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A11"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 11: Conditioning 2nd","stepDetails":"","id":"6135a255-6613-4e5e-9bae-9e698c763b02","dispense_touchTip_mmfromTop":null},"756bd338-0903-4d11-8fdb-e1537350e1df":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"3","aspirate_flowRate":"30","aspirate_labware":"labware-2:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A11"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"dest_well","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-4:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A11"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 11: Equilibrate 1st","stepDetails":"","id":"756bd338-0903-4d11-8fdb-e1537350e1df","dispense_touchTip_mmfromTop":null},"022584de-ea25-46f6-afdc-73a371a5760a":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-2:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A11"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"dest_well","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-4:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A11"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 11: Equilibrate 2nd","stepDetails":"","id":"022584de-ea25-46f6-afdc-73a371a5760a","dispense_touchTip_mmfromTop":null},"818dac47-ac7f-441c-a078-833927f2ca3c":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dropTip_location":"trashbin-1","labware":"4a5d3464-21f9-4fb5-8a3f-552680c3c2bc:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","pushOut_checkbox":false,"pushOut_volume":0,"times":"5","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","wells":["A11"],"stepType":"mix","stepName":"Col 11: Load sample","stepDetails":"","id":"818dac47-ac7f-441c-a078-833927f2ca3c"},"94f0de9c-68b9-4655-b943-f1ad2e325320":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A11"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-4","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A11"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 11: Rinse 1st","stepDetails":"","id":"94f0de9c-68b9-4655-b943-f1ad2e325320","dispense_touchTip_mmfromTop":null},"47be1698-e021-4c67-916c-52283a60990f":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A11"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-4","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A11"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 11: Rinse 2nd","stepDetails":"","id":"47be1698-e021-4c67-916c-52283a60990f","dispense_touchTip_mmfromTop":null},"7be3b7db-a489-4457-a391-8eaa36abb1bb":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","blowout_checkbox":true,"blowout_flowRate":94,"blowout_location":"dest_well","blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dropTip_location":"trashbin-1","labware":"493d4361-5dad-4912-b8f2-c676cfbbb5da:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","pushOut_checkbox":true,"pushOut_volume":"20","times":"5","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"50","wells":["A11"],"stepType":"mix","stepName":"Col 11: ELUTE Sample","stepDetails":"","id":"7be3b7db-a489-4457-a391-8eaa36abb1bb"},"0a4fe1a4-d3f3-4263-bdad-d73e7ab720b5":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-1:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-3","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-3:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":true,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 12: Conditioning 1st","stepDetails":"","id":"0a4fe1a4-d3f3-4263-bdad-d73e7ab720b5","dispense_touchTip_mmfromTop":null},"b57b4d2a-db9f-4b20-8529-a960de6a7adf":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-1:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-3","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-3:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 12: Conditioning 2nd","stepDetails":"","id":"b57b4d2a-db9f-4b20-8529-a960de6a7adf","dispense_touchTip_mmfromTop":null},"f4b4268e-052c-4e4f-b738-bf49e2e17b3e":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"3","aspirate_flowRate":"30","aspirate_labware":"labware-2:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"dest_well","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-4:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 12: Equilibrate 1st","stepDetails":"","id":"f4b4268e-052c-4e4f-b738-bf49e2e17b3e","dispense_touchTip_mmfromTop":null},"edae5065-5107-442c-9d04-debf9921dc65":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"30","aspirate_labware":"labware-2:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"dest_well","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"10","dispense_labware":"labware-4:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0.5","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":"5","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-bottom","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":true,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 12: Equilibrate 2nd","stepDetails":"","id":"edae5065-5107-442c-9d04-debf9921dc65","dispense_touchTip_mmfromTop":null},"27ac5874-40f2-4e18-a4cb-87495c13bdc4":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dropTip_location":"trashbin-1","labware":"4a5d3464-21f9-4fb5-8a3f-552680c3c2bc:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","pushOut_checkbox":false,"pushOut_volume":0,"times":"5","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","wells":["A12"],"stepType":"mix","stepName":"Col 12: Load sample","stepDetails":"","id":"27ac5874-40f2-4e18-a4cb-87495c13bdc4"},"1268a8fd-447b-49a8-86bd-0be7d999e743":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-4","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 12: Rinse 1st","stepDetails":"","id":"1268a8fd-447b-49a8-86bd-0be7d999e743","dispense_touchTip_mmfromTop":null},"d07a9e78-e292-47bc-832f-e0d8071fe0bc":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"30","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","aspirate_labware":"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":92.86,"blowout_location":"labware-4","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"30","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dispense_labware":"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"30","dropTip_location":"trashbin-1","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"Col 12: Rinse 2nd","stepDetails":"","id":"d07a9e78-e292-47bc-832f-e0d8071fe0bc","dispense_touchTip_mmfromTop":null},"9e9d495f-726f-49c2-a5f3-e05d494fdfe6":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"5","blowout_checkbox":true,"blowout_flowRate":94,"blowout_location":"dest_well","blowout_z_offset":0,"changeTip":"never","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"5","dropTip_location":"trashbin-1","labware":"493d4361-5dad-4912-b8f2-c676cfbbb5da:custom_beta/thermo_kingfisher_96_deepwell_2ml/1","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":"ALL","pipette":"c1b2ebcc-dca9-4616-90f6-418886696aab","pushOut_checkbox":true,"pushOut_volume":"20","times":"5","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"50","wells":["A12"],"stepType":"mix","stepName":"Col 12: ELUTE Sample","stepDetails":"","id":"9e9d495f-726f-49c2-a5f3-e05d494fdfe6"}},"orderedStepIds":["step-1","step-2","step-3","step-4","step-5","step-6","step-7","17438349-9ef5-4b0a-86d1-c8c2035315b9","e2019c30-6b40-4bec-a4ca-0bceae952f3c","cad42a6d-a644-485b-b8b4-8a5b2d5ba8c1","e6781b49-8830-481f-be3a-7863d6990994","eafcf019-cce8-4d2a-b3c0-6d51c4bcbea8","b71c1767-e3f4-4608-af4c-6f0efea4cbd4","a383761a-d67e-4998-a06f-4380fe58de15","65c401ea-d280-4291-a07a-55756b3020a7","7d988df8-d34e-4964-bf38-99f34bc54b9c","37cd4644-cd6b-4a78-8c65-a49c85e54536","f8a43d4d-22f8-4508-a873-319c5b24c933","cfe5d147-7578-4d44-a9a9-36a7e67288d6","04d69dee-4c9d-42d2-914d-cb4cd1641ae2","4048742f-9b04-427d-bc3c-5e8352518f8f","d2cd7488-319c-4080-9d1f-cd1335b28ecf","8b107c8b-5c52-40e0-b404-acce6b2b7be7","62e8e9bc-3b45-4abc-8657-668d01e5d3a6","84316cf6-6e6e-4930-b8c4-d1d2f3752645","46166675-caf5-4acc-a4b7-6cd3534f42b2","27a33688-3613-4f1a-8dd4-d16537223d79","d6c14ede-3853-4612-9595-c45c6cdf3ca0","ea488171-e216-4d1d-96e5-081ea68c57a2","34f1e51a-8bfe-4c02-a37f-6015f53fe8d8","5266fa19-5e18-4d2f-a0b2-956ece4b3a61","8e52efcb-fe63-4982-85c7-682da86e4594","d66059e3-0a14-48b8-9206-9b361f436efa","1f33b65a-819d-47e9-b8ed-d7ab8bff4f26","0a380ebd-17d1-4477-bcf6-eb3fdbc70830","9786a59c-fcab-4bcc-9dbc-ca52cfcb98ea","08fb7dfd-592d-42cd-a443-85b4c2490aa2","283e211d-6029-4c97-a7c8-0cd6a0566cb2","8f1b269b-1d47-4c03-9fc7-ddf317c2d574","d74e8c9f-1731-48ce-b2de-fb04e7d1df6e","55b9c967-d3f6-47aa-8b90-4768be3de442","ffc40d81-aa4d-4eb9-8134-ccb2fcf9adce","f83b0adf-e818-4f55-88fd-a46b7c00ff56","196d0421-7782-46fd-870d-9526d0b95215","1575c014-f310-4226-b6d7-add708bc0528","46e68c97-1efe-4bcc-89cd-ffb620f85a42","8ae8e0c9-e3a3-49ea-b1c4-d8635c4db916","1a6a1e4d-1ecd-4307-b1f1-ca6e49d88077","01a4e84a-8b7f-4465-bba9-75a0f2c3adde","be272985-9dc4-4f3c-8f27-d437dfa7add7","31f2cc35-58a9-47a1-a0aa-e9282eda85b7","b77d48d5-c784-4c76-a29b-ba8cb046fe3a","d40b28e9-1b18-453c-8dc8-a0d5da06b93a","0188566c-fe07-498d-82c0-82f236fe5f5f","e0de49ae-cb28-4acd-a5d1-f284c74617e6","0eecdbeb-87ee-4fc2-b888-cb26bc3826e1","469c0be5-4522-4570-b23a-eb452211f908","21ffb8bd-fd30-4d9b-91d8-cb9329ae8fa3","f6de6060-641a-4693-9cb9-4331de7b6848","a9df697f-423e-4d44-b58d-d7ec6984a33b","2e02cb47-c933-483a-babc-5cfc3c0dc859","153dfdc1-d2e4-4020-933f-11631095a1f5","ec6d63a6-5842-4dea-bcef-fe0432947cab","482eb4e9-4e66-4b37-ac5f-eb2edec579a3","45d00abd-14bc-43ad-812c-2251d7dde4a9","93668514-bae4-4e8d-8070-cacb13c2800f","c553f2d1-1af7-4772-88ca-0e097b966e16","91ef7c07-a998-4bb2-9e23-025bd0e7d035","4cca2d6c-116e-4005-bae6-a32a16eb73fb","cce27324-4b9a-46a2-9acd-ab81abc6bf29","9087859c-8d3f-41ef-b2ea-e66a77b88956","e49c5df8-bbb8-415f-be8b-85d57127de61","29e047cf-60d8-4183-98af-816067b0bb77","842f3ace-0a5c-4dac-9b6b-0569548d2778","f86ec4dc-fcfc-4f68-a82f-13936544c5d4","cd876d26-e323-4225-8577-875195aaf950","7a913aea-6940-4dbc-b822-5a7fe3f48f25","8c62ea9c-d1e0-4d58-afd6-f7b4282b56f0","f54c7d9f-b442-44e1-9780-7549959fc684","cb54ba87-1174-4529-bc70-5a930d3893b0","97b45d40-94b6-4a98-9cf9-dc3fe8a307e1","6135a255-6613-4e5e-9bae-9e698c763b02","756bd338-0903-4d11-8fdb-e1537350e1df","022584de-ea25-46f6-afdc-73a371a5760a","818dac47-ac7f-441c-a078-833927f2ca3c","94f0de9c-68b9-4655-b943-f1ad2e325320","47be1698-e021-4c67-916c-52283a60990f","7be3b7db-a489-4457-a391-8eaa36abb1bb","0a4fe1a4-d3f3-4263-bdad-d73e7ab720b5","b57b4d2a-db9f-4b20-8529-a960de6a7adf","f4b4268e-052c-4e4f-b738-bf49e2e17b3e","edae5065-5107-442c-9d04-debf9921dc65","27ac5874-40f2-4e18-a4cb-87495c13bdc4","1268a8fd-447b-49a8-86bd-0be7d999e743","d07a9e78-e292-47bc-832f-e0d8071fe0bc","9e9d495f-726f-49c2-a5f3-e05d494fdfe6"],"pipettes":{"c1b2ebcc-dca9-4616-90f6-418886696aab":{"pipetteName":"p300_multi"}},"modules":{},"labware":{"labware-1:opentrons/nest_12_reservoir_15ml/3":{"displayName":"NEST 12 Well Reservoir 15 mL - 50% ACN","labwareDefURI":"opentrons/nest_12_reservoir_15ml/3"},"labware-2:opentrons/nest_12_reservoir_15ml/3":{"displayName":"NEST 12 Well Reservoir 15 mL - 0.1% TFA","labwareDefURI":"opentrons/nest_12_reservoir_15ml/3"},"labware-3:opentrons/nest_12_reservoir_15ml/3":{"displayName":"NEST 12 Well Reservoir 15 mL - ACN Waste","labwareDefURI":"opentrons/nest_12_reservoir_15ml/3"},"labware-4:opentrons/nest_12_reservoir_15ml/3":{"displayName":"NEST 12 Well Reservoir 15 mL - TFA Waste","labwareDefURI":"opentrons/nest_12_reservoir_15ml/3"},"labware-9:opentrons/opentrons_96_tiprack_300ul/1":{"displayName":"Opentrons OT-2 96 Tip Rack 300 µL","labwareDefURI":"opentrons/opentrons_96_tiprack_300ul/1"},"493d4361-5dad-4912-b8f2-c676cfbbb5da:custom_beta/thermo_kingfisher_96_deepwell_2ml/1":{"displayName":"thermo_kingfisher_96_deepwell_2ml","labwareDefURI":"custom_beta/thermo_kingfisher_96_deepwell_2ml/1"},"f6d0c8a8-ecb3-4dbb-84ad-9720acf85d42:custom_beta/thermo_kingfisher_96_deepwell_2ml/1":{"displayName":"thermo_kingfisher_96_deepwell_2ml","labwareDefURI":"custom_beta/thermo_kingfisher_96_deepwell_2ml/1"},"4a5d3464-21f9-4fb5-8a3f-552680c3c2bc:custom_beta/thermo_kingfisher_96_deepwell_2ml/1":{"displayName":"thermo_kingfisher_96_deepwell_2ml","labwareDefURI":"custom_beta/thermo_kingfisher_96_deepwell_2ml/1"},"b6da5463-a138-43dd-8678-d68a3e8a028f:custom_beta/thermo_kingfisher_96_deepwell_2ml/1":{"displayName":"thermo_kingfisher_96_deepwell_2ml","labwareDefURI":"custom_beta/thermo_kingfisher_96_deepwell_2ml/1"}}}},"metadata":{"protocolName":"C18 Peptide Purification - 96 Samples","author":"Saito Lab","description":"This Protocol Designer protocol automates the purification of 96 peptide samples from salts and organic impurities using Pierce C18 tips on the OT-2 with multichannel pipettes.","created":1765396074714,"lastModified":1773673007348,"source":"Protocol Designer","category":null,"subcategory":null,"tags":[]}}"""
