opcodes = {
    'mov': 0b00000,
    'add': 0b00001, 'sub': 0b00010, 'mul': 0b00011, 'div': 0b00100, 'mod': 0b00101, 'cmp': 0b00110,
    'and': 0b00111, 'or': 0b01000, 'not': 0b01001,
    'isl': 0b01010, 'isr': 0b01011, 'asr': 0b01100,
    'ld': 0b01101, 'st': 0b01110,
    'b': 0b01111, 'call': 0b10000, 'ret': 0b10001,
    '.beg': 0b10010, '.bgt': 0b10011,
    'ncp': 0b10100
}

def parse_register(reg):
    if not reg.startswith('R') or not reg[1:].isdigit():
        raise ValueError(f"Invalid register format: {reg}")
    reg_num = int(reg[1:])
    if reg_num < 0 or reg_num > 15:
        raise ValueError(f"Register number out of range (0-15): {reg}")
    return reg_num

def parse_immediate(imm):
    try:
        
        if ' ' in imm:
            imm = imm.split(' ')[0].strip()
        return int(imm.replace('#', ''), 0) 
    except ValueError:
        raise ValueError(f"Invalid immediate value: {imm}")


class Assembler:
    def __init__(self):
        self.labels = {}
        self.code = []
    
    def first_pass(self, lines):
        address = 0
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            
            if ':' in line and not line.endswith(':'):
                parts = line.split(':', 1)
                label = parts[0].strip()
                self.labels[label] = address
                if parts[1].strip():  
                    address += 1
                continue
                
            if line.endswith(':'):
                label = line[:-1].strip()
                self.labels[label] = address
            else:
                address += 1
                
    def second_pass(self, lines):
        address = 0
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
                
            
            if ':' in line:
                parts = line.split(':', 1)
                instruction_part = parts[1].strip()
                if not instruction_part: 
                    continue
                line = instruction_part
            
            parts = line.split()
            instr = parts[0].lower()  
            operands = []
        
            if len(parts) > 1:
                operand_string = ' '.join(parts[1:])
                operands = [op.strip() for op in operand_string.split(',')]
            
            
            if instr not in opcodes:
                raise ValueError(f"Unknown instruction: {instr}")
                
            machine_code = 0
                
            if instr == 'mov':
                
                if len(operands) != 2:
                    raise ValueError(f"mov requires 2 operands, got {len(operands)}")
                    
                rd = parse_register(operands[0])
                if operands[1].startswith('R') or operands[1].startswith('r'):
                    rs = parse_register(operands[1])
                    machine_code = (opcodes[instr] << 11) | (rd << 7) | (rs << 3) | 0  # 
                else:
                    imm = parse_immediate(operands[1])
                    machine_code = (opcodes[instr] << 11) | (rd << 7) | (imm & 0x7F) | 1  
                    
            elif instr in ['add', 'sub', 'mul', 'div', 'mod', 'and', 'or']:
                
                if len(operands) != 3:
                    raise ValueError(f"{instr} requires 3 operands, got {len(operands)}")
                    
                rd = parse_register(operands[0])
                rs1 = parse_register(operands[1])
                
                if operands[2].startswith('R') or operands[2].startswith('r'):
                    rs2 = parse_register(operands[2])
                    machine_code = (opcodes[instr] << 11) | (rd << 7) | (rs1 << 3) | rs2 | 0  
                else:
                    imm = parse_immediate(operands[2])
                    machine_code = (opcodes[instr] << 11) | (rd << 7) | (rs1 << 3) | (imm & 0x7) | 1  
            
            elif instr == 'cmp':
                if len(operands) != 2:
                    raise ValueError(f"cmp requires 2 operands,got {len(operands)}")
                rd = parse_register(operands[0])
                
                if(operands[1].startswith('R') or operands[1].startswith('r')):
                    rs = parse_register(operands[1])
                    machine_code = (opcodes[instr] << 11) | (rd << 7) | (rs << 3) | 0
                else:
                    imm = parse_immediate(operands[1])
                    machine_code = (opcodes[instr] << 11) | (rd << 7) | (imm & 0x7F) | 1
                
            
                    
            elif instr == 'not':
                
                if len(operands) != 2:
                    raise ValueError(f"not requires 2 operands, got {len(operands)}")
                    
                rd = parse_register(operands[0])
                rs = parse_register(operands[1])
                machine_code = (opcodes[instr] << 11) | (rd << 7) | (rs << 3)
                
            elif instr in ['isl', 'isr', 'asr']:
                
                if len(operands) != 3:
                    raise ValueError(f"{instr} requires 3 operands, got {len(operands)}")
                    
                rd = parse_register(operands[0])
                rs = parse_register(operands[1])
                
                if operands[2].startswith('R') or operands[2].startswith('r'):
                    rt = parse_register(operands[2])
                    machine_code = (opcodes[instr] << 11) | (rd << 7) | (rs << 3) | rt | 0  
                else:
                    shamt = parse_immediate(operands[2])
                    if shamt < 0 or shamt > 7:
                        raise ValueError(f"Shift amount out of range (0-7): {shamt}")
                    machine_code = (opcodes[instr] << 11) | (rd << 7) | (rs << 3) | (shamt & 0x7) | 1  
                    
            elif instr in ['ld', 'st']:
                
                if len(operands) != 2:
                    raise ValueError(f"{instr} requires 2 operands, got {len(operands)}")
                    
                rd = parse_register(operands[0])
                
                
                addr = operands[1].strip()
                if not (addr.startswith('[') and addr.endswith(']')):
                    raise ValueError(f"Invalid memory address format: {addr}")
                    
                addr_content = addr[1:-1].strip()
                if ',' in addr_content:
                    rs_str, offset_str = [x.strip() for x in addr_content.split(',', 1)]
                    rs = parse_register(rs_str)
                    offset = parse_immediate(offset_str)
                    if offset < 0 or offset > 7:
                        raise ValueError(f"Address offset out of range (0-7): {offset}")
                    machine_code = (opcodes[instr] << 11) | (rd << 7) | (rs << 3) | (offset & 0x7) | 1  
                else:
                    rs = parse_register(addr_content)
                    machine_code = (opcodes[instr] << 11) | (rd << 7) | (rs << 3) | 0  
                    
            elif instr in ['b', 'call']:
                
                if len(operands) != 1:
                    raise ValueError(f"{instr} requires 1 operand, got {len(operands)}")
                    
                if operands[0].startswith('R') or operands[0].startswith('r'):
                    rs = parse_register(operands[0])
                    machine_code = (opcodes[instr] << 11) | (1 << 10) | (rs << 3)  # 
                elif operands[0] in self.labels:
                    target_addr = self.labels[operands[0]]
                    offset = target_addr - address - 1  
                    if offset < -1024 or offset > 1023:  
                        raise ValueError(f"Branch target out of range: {offset}")
                    machine_code = (opcodes[instr] << 11) | (0 << 10) | (offset & 0x3FF)  
                else:
                    raise ValueError(f"Unknown branch target: {operands[0]}")
                    
            elif instr in ['.beg', '.bgt']:
                
                if len(operands) != 3:
                    raise ValueError(f"{instr} requires 3 operands, got {len(operands)}")
                    
                rs1 = parse_register(operands[0])
                rs2 = parse_register(operands[1])
                
                if operands[2] in self.labels:
                    target_addr = self.labels[operands[2]]
                    offset = target_addr - address - 1  
                    if offset < -32 or offset > 31:  
                        raise ValueError(f"Branch target out of range: {offset}")
                    machine_code = (opcodes[instr] << 11) | (rs1 << 7) | (rs2 << 3) | (offset & 0x3F)
                else:
                    raise ValueError(f"Unknown branch target: {operands[2]}")
                    
            elif instr == 'ret':
                
                if operands:
                    raise ValueError(f"ret takes no operands, got {len(operands)}")
                machine_code = opcodes[instr] << 11
                
            elif instr == 'ncp':
                if len(operands) != 2:
                    raise ValueError(f"ncp requires 2 operands, got {len(operands)}")
                    
                rd = parse_register(operands[0])
                rs = parse_register(operands[1])
                machine_code = (opcodes[instr] << 11) | (rd << 7) | (rs << 3)
            
            self.code.append(machine_code)
            address += 1

    def assemble(self, src):
        lines = []
        
        for line in src.split('\n'):
            line = line.split('@')[0].strip()
            
            if line:
                lines.append(line)
        
        self.labels = {}
        self.code = []
        self.first_pass(lines)
        self.second_pass(lines)
        return self.code