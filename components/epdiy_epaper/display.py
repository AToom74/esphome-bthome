import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import display
from esphome.components.esp32 import add_idf_component
from esphome.const import (
    CONF_ID,
    CONF_LAMBDA,
    CONF_PAGES,
)

DEPENDENCIES = ["esp32"]
CODEOWNERS = ["@esphome-bthome"]

CONF_DISPLAY_TYPE = "display_type"
CONF_BOARD = "board"

epdiy_epaper_ns = cg.esphome_ns.namespace("epdiy_epaper")
EpdiyEpaper = epdiy_epaper_ns.class_(
    "EpdiyEpaper", display.DisplayBuffer
)

DISPLAY_TYPES = {
    "ED047TC1": "ED047TC1",
    "ED047TC2": "ED047TC2",
    "ED060SC4": "ED060SC4",
    "ED060XC3": "ED060XC3",
    "ED097OC4": "ED097OC4",
    "ED097TC2": "ED097TC2",
    "ED133UT2": "ED133UT2",
}

BOARD_TYPES = {
    "LILYGO_T5_47": "LILYGO_T5_47",
    "V2_V3": "V2_V3",
    "V4": "V4",
    "V5": "V5",
    "V6": "V6",
    "V7": "V7",
}

CONFIG_SCHEMA = cv.All(
    display.FULL_DISPLAY_SCHEMA.extend(
        {
            cv.GenerateID(): cv.declare_id(EpdiyEpaper),
            cv.Optional(CONF_DISPLAY_TYPE, default="ED047TC1"): cv.one_of(
                *DISPLAY_TYPES.keys(), upper=True
            ),
            cv.Optional(CONF_BOARD, default="LILYGO_T5_47"): cv.one_of(
                *BOARD_TYPES.keys(), upper=True
            ),
        }
    )
    .extend(cv.polling_component_schema("never")),
    cv.has_at_most_one_key(CONF_PAGES, CONF_LAMBDA),
    cv.only_with_framework("esp-idf"),
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await display.register_display(var, config)

    if CONF_LAMBDA in config:
        lambda_ = await cg.process_lambda(
            config[CONF_LAMBDA], [(display.DisplayRef, "it")], return_type=cg.void
        )
        cg.add(var.set_writer(lambda_))

    display_type = config[CONF_DISPLAY_TYPE]
    board_type = config[CONF_BOARD]
    cg.add(var.set_display_type(display_type))
    cg.add(var.set_board_type(board_type))

    # Add epdiy as ESP-IDF component
    add_idf_component(
        name="epdiy",
        repo="https://github.com/vroland/epdiy.git",
        ref="main",
    )

    # epdiy build configuration
    cg.add_build_flag("-DBOARD_HAS_PSRAM")
    cg.add_build_flag(f"-DCONFIG_EPD_DISPLAY_TYPE_{display_type}")
    cg.add_build_flag(f"-DCONFIG_EPD_BOARD_REVISION_{board_type}")
