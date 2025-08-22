from collections import namedtuple
import re

AArch64Mnemonic = namedtuple("AArch64Mnemonic", ["mnemonic", "cond"])
AArch64ShiftExtend = namedtuple("AArch64ShiftExtend", ["type", "amount"])

conds = {
    'EQ', 'NE', 'CS', 'HS', 'CC', 'LO', 'MI', 'PL',
    'VS', 'VC', 'HI', 'LS', 'GE', 'LT', 'GT', 'LE', 'AL', 'NV'
}

shift_extend = {
    'LSL', 'LSR', 'ASR', 'ROR',  # Shifts
    'UXTB', 'UXTH', 'UXTW', 'UXTX',  # Unsigned extends
    'SXTB', 'SXTH', 'SXTW', 'SXTX'   # Signed extends
}

conds_regex = '|'.join(map(lambda x: x.lower(), conds))
shift_extend_regex = '|'.join(map(lambda x: x.lower(), shift_extend))


def parse_mnemonic(instr):
    """Parse AArch64 instruction mnemonic and condition code.
    
    In AArch64, condition codes are typically suffixed to the instruction.
    Examples: b.eq, csel.ne, etc.
    """
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
    """Parse AArch64 shift/extend operations with their amounts.
    
    Examples: lsl #2, uxtw #4, asr #0x10
    """
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
    """Parse AArch64 immediate values.
    
    Supports both hexadecimal (#0x...) and decimal (#...) formats.
    """
    regex_imm = r"\#(0x[0-9a-fA-F]+|[0-9]+)"
    tokens = re.match(regex_imm, par)
    assert tokens is not None  # parse failed
    tokens = tokens.groups()

    return int(tokens[0], 16) if tokens[0][:2] == '0x' else int(tokens[0])


def get_src(state, param):
    """Helper to get source value from register or immediate.
    
    Args:
        state: Current execution state
        param: Parameter string (register name or immediate value)
        
    Returns:
        Value from register or parsed immediate
    """
    if param.startswith('#'):
        return parse_immediate(param)
    else:
        # Assume it's a register name
        return state.regs[param]


def store_to_dst(state, param, value):
    """Helper to store value to destination register.
    
    Args:
        state: Current execution state
        param: Destination parameter (register name)
        value: Value to store
    """
    # Store to register
    state.regs[param] = value