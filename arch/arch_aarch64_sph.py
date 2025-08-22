from .arch_abstract import SpecialInstructionHandler


class AArch64SPH(SpecialInstructionHandler):
    def __init__(self):
        pass

    # override
    def handle_instruction(self, disasm_str: str, sv):
        inst_name = disasm_str.split(" ")[0]
        parameters = ''.join(disasm_str.split(" ")[1:]).split(",")

        # Basic instruction handling can be extended here
        # For now, return False to indicate no special handling
        return False