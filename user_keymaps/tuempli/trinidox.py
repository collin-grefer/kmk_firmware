import board

from kb import KMKKeyboard
from kmk.hid import HIDModes
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType
from kmk.modules.PMW3360 import PMW3360

keyboard = KMKKeyboard()


# keyboard.tap_time = 320
keyboard.debug_enabled = False

split = Split(split_type=SplitType.BLE)
layers = Layers()

keyboard.modules = [split, layers]

keyboard.modules.append(PMW3360(
    cs=board.GP0,
    sclk=board.GP2,
    miso=board.GP4,
    mosi=board.GP3,
    invert_x=False,
    invert_y=True,
    flip_xy=False,
    lift_config=0x04,
    on_move=lambda keyboard: None,
    scroll_layers=[2],
    volume_layers=[3],
))

_______ = KC.TRNS
XXXXXXX = KC.NO

LT1_SP = KC.MO(2)
LT2_SP = KC.LT(3, KC.SPC)
TAB_SB = KC.LT(5, KC.TAB)
SUPER_L = KC.LM(4, KC.LGUI)

keyboard.keymap = [
    # Main
    # ,------------------------------------.          ,------------------------------------.
    # |  Z   |   Y  |   U  |   A  |Q(CTRL) |          |P(CTRL) |   B  |   M  |   L  |ß(WIN)|
    # |------+------+------+------+--------|          |--------+------+------+------+------|
    # |  C   |   S  |   I  |   E  |   O    |          |   D    |   T  |   N  |   R  |   H  |
    # |------+------+------+------+--------|          |--------+------+------+------+------|
    # |  V   |   X  |   Ü  |   Ä  |TAB(ALT)|          |EN(ALT) |   G  |   F  |   J  |   K  |
    # |------+------+------+------+--------|          |--------+------+------+------+------|
    # |      |      |  ESC |   Ö  |SP(SH)  |          | BSP(SH)|   W  |  DEL |      |      |
    #  `----------------------------------´            `-----------------------------------´
    #
    [
        # MAIN
        KC.Y,    KC.Z,    KC.U,   KC.A,  KC.Q,           KC.P,    KC.B,    KC.M,    KC.L,    KC.ß, \
        KC.C,    KC.S,    KC.I,   KC.E,  KC.O,           KC.D,    KC.T,    KC.N,    KC.R,    KC.H, \
        KC.V,    KC.X,    KC.Ü,   KC.Ä,  KC.TAB,         KC.ENT,  KC.G,    KC.F,    KC.J,    KC.K, \
        _______, _______, KC.ESC, KC.Ö,  KC.SP,          KC.BSP,  KC.W,    KC.DEL,  _______, _______
    ],

    # MOUSE
    # ,------------------------------------.          ,------------------------------------.
    # |  Z   |   Y  |   U  |   A  |Q(CTRL) |          |P(CTRL) |   B  |   M  |   L  |ß(WIN)|
    # |------+------+------+------+--------|          |--------+------+------+------+------|
    # |  C   |   S  |   I  |   E  |   O    |          |   D    |   T  |   N  |   R  |   H  |
    # |------+------+------+------+--------|          |--------+------+------+------+------|
    # |  V   |   X  |   Ü  |   Ä  |TAB(ALT)|          |EN(ALT) |   G  |   F  |   J  |   K  |
    # |------+------+------+------+--------|          |--------+------+------+------+------|
    # |      |      |  ESC |   Ö  |SP(SH)  |          | BSP(SH)|   W  |  DEL |      |      |
    #  `----------------------------------´            `-----------------------------------´
]

if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.USB)
