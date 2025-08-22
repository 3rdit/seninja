from ..expr import And, Or
from .arch_abstract import Arch
from .arch_aarch64_sph import AArch64SPH


class AArch64Arch(Arch):
    REGS = {
        # General-purpose registers x0-x30
        'x0': {
            'size': 8,
            'sub': {
                'w0': {'offset': 4, 'size': 4}
            }
        },
        'x1': {
            'size': 8,
            'sub': {
                'w1': {'offset': 4, 'size': 4}
            }
        },
        'x2': {
            'size': 8,
            'sub': {
                'w2': {'offset': 4, 'size': 4}
            }
        },
        'x3': {
            'size': 8,
            'sub': {
                'w3': {'offset': 4, 'size': 4}
            }
        },
        'x4': {
            'size': 8,
            'sub': {
                'w4': {'offset': 4, 'size': 4}
            }
        },
        'x5': {
            'size': 8,
            'sub': {
                'w5': {'offset': 4, 'size': 4}
            }
        },
        'x6': {
            'size': 8,
            'sub': {
                'w6': {'offset': 4, 'size': 4}
            }
        },
        'x7': {
            'size': 8,
            'sub': {
                'w7': {'offset': 4, 'size': 4}
            }
        },
        'x8': {
            'size': 8,
            'sub': {
                'w8': {'offset': 4, 'size': 4}
            }
        },
        'x9': {
            'size': 8,
            'sub': {
                'w9': {'offset': 4, 'size': 4}
            }
        },
        'x10': {
            'size': 8,
            'sub': {
                'w10': {'offset': 4, 'size': 4}
            }
        },
        'x11': {
            'size': 8,
            'sub': {
                'w11': {'offset': 4, 'size': 4}
            }
        },
        'x12': {
            'size': 8,
            'sub': {
                'w12': {'offset': 4, 'size': 4}
            }
        },
        'x13': {
            'size': 8,
            'sub': {
                'w13': {'offset': 4, 'size': 4}
            }
        },
        'x14': {
            'size': 8,
            'sub': {
                'w14': {'offset': 4, 'size': 4}
            }
        },
        'x15': {
            'size': 8,
            'sub': {
                'w15': {'offset': 4, 'size': 4}
            }
        },
        'x16': {
            'size': 8,
            'sub': {
                'w16': {'offset': 4, 'size': 4}
            }
        },
        'x17': {
            'size': 8,
            'sub': {
                'w17': {'offset': 4, 'size': 4}
            }
        },
        'x18': {
            'size': 8,
            'sub': {
                'w18': {'offset': 4, 'size': 4}
            }
        },
        'x19': {
            'size': 8,
            'sub': {
                'w19': {'offset': 4, 'size': 4}
            }
        },
        'x20': {
            'size': 8,
            'sub': {
                'w20': {'offset': 4, 'size': 4}
            }
        },
        'x21': {
            'size': 8,
            'sub': {
                'w21': {'offset': 4, 'size': 4}
            }
        },
        'x22': {
            'size': 8,
            'sub': {
                'w22': {'offset': 4, 'size': 4}
            }
        },
        'x23': {
            'size': 8,
            'sub': {
                'w23': {'offset': 4, 'size': 4}
            }
        },
        'x24': {
            'size': 8,
            'sub': {
                'w24': {'offset': 4, 'size': 4}
            }
        },
        'x25': {
            'size': 8,
            'sub': {
                'w25': {'offset': 4, 'size': 4}
            }
        },
        'x26': {
            'size': 8,
            'sub': {
                'w26': {'offset': 4, 'size': 4}
            }
        },
        'x27': {
            'size': 8,
            'sub': {
                'w27': {'offset': 4, 'size': 4}
            }
        },
        'x28': {
            'size': 8,
            'sub': {
                'w28': {'offset': 4, 'size': 4}
            }
        },
        'fp': {  # Frame pointer (x29)
            'size': 8,
            'sub': {
                'w29': {'offset': 4, 'size': 4}
            }
        },
        'lr': {  # Link register (x30)
            'size': 8,
            'sub': {
                'w30': {'offset': 4, 'size': 4}
            }
        },
        # Stack pointer
        'sp': {
            'size': 8,
            'sub': {
                'wsp': {'offset': 4, 'size': 4}
            }
        },
        # Program counter
        'pc': {
            'size': 8,
            'sub': {}
        },
        # Zero register
        'xzr': {
            'size': 8,
            'sub': {
                'wzr': {'offset': 4, 'size': 4}
            }
        },
        # SIMD/FP registers v0-v31
        'v0': {
            'size': 16,
            'sub': {
                'q0': {'offset': 0, 'size': 16},
                'd0': {'offset': 8, 'size': 8},
                's0': {'offset': 12, 'size': 4},
                'h0': {'offset': 14, 'size': 2},
                'b0': {'offset': 15, 'size': 1}
            }
        },
        'v1': {
            'size': 16,
            'sub': {
                'q1': {'offset': 0, 'size': 16},
                'd1': {'offset': 8, 'size': 8},
                's1': {'offset': 12, 'size': 4},
                'h1': {'offset': 14, 'size': 2},
                'b1': {'offset': 15, 'size': 1}
            }
        },
        'v2': {
            'size': 16,
            'sub': {
                'q2': {'offset': 0, 'size': 16},
                'd2': {'offset': 8, 'size': 8},
                's2': {'offset': 12, 'size': 4},
                'h2': {'offset': 14, 'size': 2},
                'b2': {'offset': 15, 'size': 1}
            }
        },
        'v3': {
            'size': 16,
            'sub': {
                'q3': {'offset': 0, 'size': 16},
                'd3': {'offset': 8, 'size': 8},
                's3': {'offset': 12, 'size': 4},
                'h3': {'offset': 14, 'size': 2},
                'b3': {'offset': 15, 'size': 1}
            }
        },
        'v4': {
            'size': 16,
            'sub': {
                'q4': {'offset': 0, 'size': 16},
                'd4': {'offset': 8, 'size': 8},
                's4': {'offset': 12, 'size': 4},
                'h4': {'offset': 14, 'size': 2},
                'b4': {'offset': 15, 'size': 1}
            }
        },
        'v5': {
            'size': 16,
            'sub': {
                'q5': {'offset': 0, 'size': 16},
                'd5': {'offset': 8, 'size': 8},
                's5': {'offset': 12, 'size': 4},
                'h5': {'offset': 14, 'size': 2},
                'b5': {'offset': 15, 'size': 1}
            }
        },
        'v6': {
            'size': 16,
            'sub': {
                'q6': {'offset': 0, 'size': 16},
                'd6': {'offset': 8, 'size': 8},
                's6': {'offset': 12, 'size': 4},
                'h6': {'offset': 14, 'size': 2},
                'b6': {'offset': 15, 'size': 1}
            }
        },
        'v7': {
            'size': 16,
            'sub': {
                'q7': {'offset': 0, 'size': 16},
                'd7': {'offset': 8, 'size': 8},
                's7': {'offset': 12, 'size': 4},
                'h7': {'offset': 14, 'size': 2},
                'b7': {'offset': 15, 'size': 1}
            }
        },
        'v8': {
            'size': 16,
            'sub': {
                'q8': {'offset': 0, 'size': 16},
                'd8': {'offset': 8, 'size': 8},
                's8': {'offset': 12, 'size': 4},
                'h8': {'offset': 14, 'size': 2},
                'b8': {'offset': 15, 'size': 1}
            }
        },
        'v9': {
            'size': 16,
            'sub': {
                'q9': {'offset': 0, 'size': 16},
                'd9': {'offset': 8, 'size': 8},
                's9': {'offset': 12, 'size': 4},
                'h9': {'offset': 14, 'size': 2},
                'b9': {'offset': 15, 'size': 1}
            }
        },
        'v10': {
            'size': 16,
            'sub': {
                'q10': {'offset': 0, 'size': 16},
                'd10': {'offset': 8, 'size': 8},
                's10': {'offset': 12, 'size': 4},
                'h10': {'offset': 14, 'size': 2},
                'b10': {'offset': 15, 'size': 1}
            }
        },
        'v11': {
            'size': 16,
            'sub': {
                'q11': {'offset': 0, 'size': 16},
                'd11': {'offset': 8, 'size': 8},
                's11': {'offset': 12, 'size': 4},
                'h11': {'offset': 14, 'size': 2},
                'b11': {'offset': 15, 'size': 1}
            }
        },
        'v12': {
            'size': 16,
            'sub': {
                'q12': {'offset': 0, 'size': 16},
                'd12': {'offset': 8, 'size': 8},
                's12': {'offset': 12, 'size': 4},
                'h12': {'offset': 14, 'size': 2},
                'b12': {'offset': 15, 'size': 1}
            }
        },
        'v13': {
            'size': 16,
            'sub': {
                'q13': {'offset': 0, 'size': 16},
                'd13': {'offset': 8, 'size': 8},
                's13': {'offset': 12, 'size': 4},
                'h13': {'offset': 14, 'size': 2},
                'b13': {'offset': 15, 'size': 1}
            }
        },
        'v14': {
            'size': 16,
            'sub': {
                'q14': {'offset': 0, 'size': 16},
                'd14': {'offset': 8, 'size': 8},
                's14': {'offset': 12, 'size': 4},
                'h14': {'offset': 14, 'size': 2},
                'b14': {'offset': 15, 'size': 1}
            }
        },
        'v15': {
            'size': 16,
            'sub': {
                'q15': {'offset': 0, 'size': 16},
                'd15': {'offset': 8, 'size': 8},
                's15': {'offset': 12, 'size': 4},
                'h15': {'offset': 14, 'size': 2},
                'b15': {'offset': 15, 'size': 1}
            }
        },
        'v16': {
            'size': 16,
            'sub': {
                'q16': {'offset': 0, 'size': 16},
                'd16': {'offset': 8, 'size': 8},
                's16': {'offset': 12, 'size': 4},
                'h16': {'offset': 14, 'size': 2},
                'b16': {'offset': 15, 'size': 1}
            }
        },
        'v17': {
            'size': 16,
            'sub': {
                'q17': {'offset': 0, 'size': 16},
                'd17': {'offset': 8, 'size': 8},
                's17': {'offset': 12, 'size': 4},
                'h17': {'offset': 14, 'size': 2},
                'b17': {'offset': 15, 'size': 1}
            }
        },
        'v18': {
            'size': 16,
            'sub': {
                'q18': {'offset': 0, 'size': 16},
                'd18': {'offset': 8, 'size': 8},
                's18': {'offset': 12, 'size': 4},
                'h18': {'offset': 14, 'size': 2},
                'b18': {'offset': 15, 'size': 1}
            }
        },
        'v19': {
            'size': 16,
            'sub': {
                'q19': {'offset': 0, 'size': 16},
                'd19': {'offset': 8, 'size': 8},
                's19': {'offset': 12, 'size': 4},
                'h19': {'offset': 14, 'size': 2},
                'b19': {'offset': 15, 'size': 1}
            }
        },
        'v20': {
            'size': 16,
            'sub': {
                'q20': {'offset': 0, 'size': 16},
                'd20': {'offset': 8, 'size': 8},
                's20': {'offset': 12, 'size': 4},
                'h20': {'offset': 14, 'size': 2},
                'b20': {'offset': 15, 'size': 1}
            }
        },
        'v21': {
            'size': 16,
            'sub': {
                'q21': {'offset': 0, 'size': 16},
                'd21': {'offset': 8, 'size': 8},
                's21': {'offset': 12, 'size': 4},
                'h21': {'offset': 14, 'size': 2},
                'b21': {'offset': 15, 'size': 1}
            }
        },
        'v22': {
            'size': 16,
            'sub': {
                'q22': {'offset': 0, 'size': 16},
                'd22': {'offset': 8, 'size': 8},
                's22': {'offset': 12, 'size': 4},
                'h22': {'offset': 14, 'size': 2},
                'b22': {'offset': 15, 'size': 1}
            }
        },
        'v23': {
            'size': 16,
            'sub': {
                'q23': {'offset': 0, 'size': 16},
                'd23': {'offset': 8, 'size': 8},
                's23': {'offset': 12, 'size': 4},
                'h23': {'offset': 14, 'size': 2},
                'b23': {'offset': 15, 'size': 1}
            }
        },
        'v24': {
            'size': 16,
            'sub': {
                'q24': {'offset': 0, 'size': 16},
                'd24': {'offset': 8, 'size': 8},
                's24': {'offset': 12, 'size': 4},
                'h24': {'offset': 14, 'size': 2},
                'b24': {'offset': 15, 'size': 1}
            }
        },
        'v25': {
            'size': 16,
            'sub': {
                'q25': {'offset': 0, 'size': 16},
                'd25': {'offset': 8, 'size': 8},
                's25': {'offset': 12, 'size': 4},
                'h25': {'offset': 14, 'size': 2},
                'b25': {'offset': 15, 'size': 1}
            }
        },
        'v26': {
            'size': 16,
            'sub': {
                'q26': {'offset': 0, 'size': 16},
                'd26': {'offset': 8, 'size': 8},
                's26': {'offset': 12, 'size': 4},
                'h26': {'offset': 14, 'size': 2},
                'b26': {'offset': 15, 'size': 1}
            }
        },
        'v27': {
            'size': 16,
            'sub': {
                'q27': {'offset': 0, 'size': 16},
                'd27': {'offset': 8, 'size': 8},
                's27': {'offset': 12, 'size': 4},
                'h27': {'offset': 14, 'size': 2},
                'b27': {'offset': 15, 'size': 1}
            }
        },
        'v28': {
            'size': 16,
            'sub': {
                'q28': {'offset': 0, 'size': 16},
                'd28': {'offset': 8, 'size': 8},
                's28': {'offset': 12, 'size': 4},
                'h28': {'offset': 14, 'size': 2},
                'b28': {'offset': 15, 'size': 1}
            }
        },
        'v29': {
            'size': 16,
            'sub': {
                'q29': {'offset': 0, 'size': 16},
                'd29': {'offset': 8, 'size': 8},
                's29': {'offset': 12, 'size': 4},
                'h29': {'offset': 14, 'size': 2},
                'b29': {'offset': 15, 'size': 1}
            }
        },
        'v30': {
            'size': 16,
            'sub': {
                'q30': {'offset': 0, 'size': 16},
                'd30': {'offset': 8, 'size': 8},
                's30': {'offset': 12, 'size': 4},
                'h30': {'offset': 14, 'size': 2},
                'b30': {'offset': 15, 'size': 1}
            }
        },
        'v31': {
            'size': 16,
            'sub': {
                'q31': {'offset': 0, 'size': 16},
                'd31': {'offset': 8, 'size': 8},
                's31': {'offset': 12, 'size': 4},
                'h31': {'offset': 14, 'size': 2},
                'b31': {'offset': 15, 'size': 1}
            }
        }
    }

    # Condition flags - N (negative), Z (zero), C (carry), V (overflow)
    FLAGS = {'n': 31, 'z': 30, 'c': 29, 'v': 28}

    REG_NAMES = [
        "pc", "sp", "fp", "lr",  # Program counter, stack pointer, frame pointer, link register
        "x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9", "x10", "x11",
        "x12", "x13", "x14", "x15", "x16", "x17", "x18", "x19", "x20", "x21", "x22",
        "x23", "x24", "x25", "x26", "x27", "x28", "xzr",
        "v0", "v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9", "v10", "v11",
        "v12", "v13", "v14", "v15", "v16", "v17", "v18", "v19", "v20", "v21", "v22",
        "v23", "v24", "v25", "v26", "v27", "v28", "v29", "v30", "v31"
    ]

    # AArch64 condition codes
    FLAGS_CONDS = {
        'EQ': lambda s: s.regs.flags['z'] == 1,  # Equal
        'NE': lambda s: s.regs.flags['z'] == 0,  # Not equal
        'CS': lambda s: s.regs.flags['c'] == 1,  # Carry set (unsigned higher or same)
        'HS': lambda s: s.regs.flags['c'] == 1,  # Unsigned higher or same (alias for CS)
        'CC': lambda s: s.regs.flags['c'] == 0,  # Carry clear (unsigned lower)
        'LO': lambda s: s.regs.flags['c'] == 0,  # Unsigned lower (alias for CC)
        'MI': lambda s: s.regs.flags['n'] == 1,  # Minus (negative)
        'PL': lambda s: s.regs.flags['n'] == 0,  # Plus (positive or zero)
        'VS': lambda s: s.regs.flags['v'] == 1,  # Overflow
        'VC': lambda s: s.regs.flags['v'] == 0,  # No overflow
        'HI': lambda s: And(                     # Unsigned higher
            s.regs.flags['c'] == 1,
            s.regs.flags['z'] == 0
        ),
        'LS': lambda s: Or(                      # Unsigned lower or same
            s.regs.flags['c'] == 0,
            s.regs.flags['z'] == 1
        ),
        'GE': lambda s: s.regs.flags['n'] == s.regs.flags['v'],  # Signed greater or equal
        'LT': lambda s: s.regs.flags['n'] != s.regs.flags['v'],  # Signed less than
        'GT': lambda s: And(                     # Signed greater than
            s.regs.flags['z'] == 0,
            s.regs.flags['n'] == s.regs.flags['v']
        ),
        'LE': lambda s: Or(                      # Signed less than or equal
            s.regs.flags['z'] == 1,
            s.regs.flags['n'] != s.regs.flags['v']
        ),
        'AL': lambda s: True                     # Always (unconditional)
    }

    sph = AArch64SPH()

    def __init__(self):
        self._bits = 64

    def bits(self):
        return self._bits

    def regs_data(self):
        return AArch64Arch.REGS

    def reg_names(self):
        return AArch64Arch.REG_NAMES

    def flags_data(self):
        return AArch64Arch.FLAGS

    def flags_default(self, flag):
        return None

    def endness(self):
        return 'little'

    def getip_reg(self):
        return 'pc'

    def get_base_pointer_reg(self):
        return 'fp'  # Frame pointer in AArch64

    def get_stack_pointer_reg(self):
        return 'sp'

    def save_return_address(self, state, return_address):
        state.regs.lr = return_address  # Link register

    def get_return_address(self, state):
        return state.regs.lr

    def get_argument_regs(self, calling_convention):
        # Standard AArch64 calling convention uses x0-x7 for arguments
        return ['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7']

    def save_result_value(self, state, calling_convention, value):
        if value.size == 8:
            state.regs.x0 = value.ZeroExt(56)
        elif value.size == 16:
            state.regs.x0 = value.ZeroExt(48)
        elif value.size == 32:
            state.regs.x0 = value.ZeroExt(32)
        elif value.size == 64:
            state.regs.x0 = value
        else:
            raise Exception("Wrong size in save_result_value")

    def get_flag_cond_lambda(self, cond: str, state):
        assert cond in AArch64Arch.FLAGS_CONDS
        return AArch64Arch.FLAGS_CONDS[cond]

    def execute_special_handler(self, disasm_str, sv):
        res = AArch64Arch.sph.handle_instruction(disasm_str, sv)
        return res

    def is_synthetic_reg(self, reg_name):
        # pc and xzr aren't queryable via binja
        return reg_name in ['pc', 'xzr']

    def is_zero_reg(self, reg_name):
        return reg_name == 'xzr'


Arch.fix_reg_addressess(AArch64Arch)