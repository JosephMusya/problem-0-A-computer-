class Assembler:
    '''
        Assembler for encoding the assembler code
    '''
    def __init__(self) -> None:
        # A dictionary that maps instruction mnemonics to instruction numbers
        self.instruction_map = {
            'halt': 0x00,
            'nop': 0x01,
            'li': 0x02,
            'lw': 0x03,
            'sw': 0x04,
            'add': 0x05,
            'sub': 0x06,
            'mult': 0x07,
            'div': 0x08,
            'j': 0x09,
            'jr': 0x0A,
            'beq': 0x0B,
            'bne': 0x0C,
            'inc': 0x0D,
            'dec': 0x0E
        }
        # Create a list to store the encoded bytecode
        self.bytecode = []
        # Symbol table for labels and variables
        self.symbol_table = {}
    def assemble(self,assembly_code)->list: 
        '''
            This method takes an assembler code and returns a machine language which
            is encoded. 
            The return value is in list form.
        '''       
        # Split the assembly code into lines
        lines = assembly_code.split('\n')
        print("\nAssembly Lines List: {}\n".format(lines))
        
        # First iteration find and store labels
        for line in lines:
            if ':' in line:
                label = line.split(':')[0].strip()
                self.symbol_table[label] = len(self.bytecode)
                print("Label: ",label)
                print("Symbol table: ",self.symbol_table)
            else:
                # Cleaning the code by removing whitespace and comments
                line = line.split(',')[0].strip()
                print("Line: ",line)
                if line:
                    instruction = line.split()[0]
                    if instruction in self.instruction_map:
                        self.bytecode.append(instruction)
                    print("Instruction {}".format(instruction,))
        # Second iteration to encode the instruction into machine code
        pc = 0
        for line in lines:
            # Remove whitespace and comments
            line = line.split('#')[0].strip()
            if line:
                instruction = line.split()[0]
                if instruction in self.instruction_map:
                    instr_num = self.instruction_map[instruction]
                    # Get the registers or immediate value after the li
                    if instruction == 'li':
                        # Extract register number and immediate value passed with li
                        reg_num, imm_val = line.split()[1:]
                        print("Register {} and Immediateval {}".format(reg_num,imm_val))
                        reg_num = int(reg_num[1:])
                        imm_val = int(imm_val, 0)
                        instr = (instr_num << 12) | (reg_num << 8) | imm_val
                    elif instruction in ['j', 'jr']:
                        if instruction == 'j':
                            address = int(line.split()[1], 0)
                            print("Skip to address: ".format(address))
                        else:
                            reg_num = int(line.split()[1][1:])
                            address = self.symbol_table[self.bytecode[pc-1 + reg_num]]
                        instr = (instr_num << 12) | address
                    else:
                        # Extract register numbers for other instruction apart from the li
                        reg1, reg2, reg3 = line.split()[1:]
                        reg1 = int(reg1[1:])
                        reg2 = int(reg2[1:])
                        reg3 = int(reg3[1:])
                        instr = (instr_num << 12) | (reg1 << 8) | (reg2 << 4) | reg3
                    self.bytecode[pc] = (instr)
                    
                    #increment the program counter
                    pc += 1

        return self.bytecode

#initialize the assembler class
assembler = Assembler()


#This script can be ran as a module.
#When imported this section wont ran
if __name__ == "__main__":
    assembly_program = "; a simple counter program.\nli R1 0x00000000\n; end\nli R2 0x0000FFFF\nadd R3 R1 R2\nbne R1 R2 R3"
    output_int = (assembler.assemble(assembly_program))

    output_hex = [hex(vals) for vals in (output_int)]
    print("\nOutput in integer form: {}".format(output_int))
    print("Output in hex for {}".format(output_hex))
