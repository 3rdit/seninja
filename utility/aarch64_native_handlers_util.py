from collections import namedtuple
import re

AArch64Mnemonic = namedtuple("AArch64Mnemonic", ["mnemonic", "cond"])
AArch64ShiftExtend = namedtuple("AArch64ShiftExtend", ["type", "amount"])

conds = {
    'EQ', 'NE', 'CS', 'HS', 'CC', 'LO', 'MI', 'PL',
    'VS', 'VC', 'HI', 'LS', 'GE', 'LT', 'GT', 'LE', 'AL', 'NV'
}

shift_extend = {
    'LSL', 'LSR', 'ASR', 'ROR',      # shifts
    'UXTB', 'UXTH', 'UXTW', 'UXTX',  # unsigned extends
    'SXTB', 'SXTH', 'SXTW', 'SXTX'   # signed extends
}

conds_regex = '|'.join(map(lambda x: x.lower(), conds))
shift_extend_regex = '|'.join(map(lambda x: x.lower(), shift_extend))


def parse_mnemonic(instr):
    regex_mnemonic = \
        r"^([a-z]+)" + \
        r"(?:\.({conds_regex}))?\b" \
        .format(conds_regex=conds_regex)

    res = re.match(regex_mnemonic, instr)
    assert res is not None  # parse failed
    res = res.groups()

    return AArch64Mnemonic(
        mnemonic=res[0],
        cond=res[1]
    )


def parse_shift_extend(par):
    regex_shift_extend = r"({shift_extend_regex})\s*\#(0x[0-9a-fA-F]+|[0-9]+)".format(
        shift_extend_regex=shift_extend_regex
    )
    tokens = re.match(regex_shift_extend, par)
    assert tokens is not None  # parse failed
    tokens = tokens.groups()

    return AArch64ShiftExtend(
        type=tokens[0].upper(),
        amount=int(tokens[1], 16) if tokens[1][:2] == '0x' else int(tokens[1])
    )


def parse_immediate(par):
    regex_imm = r"\#(0x[0-9a-fA-F]+|[0-9]+)"
    tokens = re.match(regex_imm, par)
    assert tokens is not None  # parse failed
    tokens = tokens.groups()

    return int(tokens[0], 16) if tokens[0][:2] == '0x' else int(tokens[0])


def get_src(state, param):
    if param.startswith('#'):
        return parse_immediate(param)
    else:
        # assume it's a register name
        return state.regs[param]


def store_to_dst(state, param, value):
    # store to register
    state.regs[param] = value
