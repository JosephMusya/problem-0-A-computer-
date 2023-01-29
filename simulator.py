#Import our custom module(Class) which converts assembler code to machine code

from assemble import Assembler

class Simulator:
    #Initializer the simulator with the specified number if registers and memory size
    def __init__(self):
        self.registers = [0] * 32
        self.memory = [0] * 0x10000
        self.pc = 0

    #load the machine code as program
    def load_program(self, program)->list:
        '''
            This method loads the machine code into the respective memories allocated
            It returns a list the memory that carry data
        '''
        self.memory[:len(program)] = program
        memory_with_data = (self.memory[:7])
        self.pc = 0
        
        return memory_with_data        


    def run(self,memory_with_data):
        '''
            This method executes the machine code that is stored in the 
            respective memory locations
        '''
        for i,instruction in enumerate(memory_with_data):
            instruction = self.memory[i]
            opcode = instruction >> 26
            print("OPCODE ",opcode)
            if opcode == 0:
                # li instruction
                print("li operation performing")
                rt = (instruction >> 16) & 0x1F
                immediate = instruction & 0xFFFF
                self.registers[rt] = immediate
            elif opcode == 43:
                # sw instruction
                print("sw operation performing")
                rt = (instruction >> 16) & 0x1F
                offset = instruction & 0xFFFF
                self.memory[self.registers[rt] + offset] = self.registers[rt]
            elif opcode == 8:
                # inc instruction
                print("inc operation performing")
                rt = (instruction >> 16) & 0x1F
                self.registers[rt] += 1
            elif opcode == 5:
                # bne instruction
                print("bne operation performing")
                rs = (instruction >> 21) & 0x1F
                rt = (instruction >> 16) & 0x1F
                offset = instruction & 0xFFFF
                if self.registers[rs] != self.registers[rt]:
                    self.pc += offset
                    continue
            elif opcode == 63:
                print("Exiting program on HALT!")
                # halt instruction
                break
            self.pc += 1
            print("Program counter incremented")
            print("\n")
            

#Example of machine code
machine_program = [0x20000000,0x201FFFFF,0x20000003,0xAC110000,0x40880001,0x1489FFFC,0x00000000]

#Example of an assembler code
assembly_code = "; a simple counter program.\nli R1 0x00000000\n; end\nli R2 0x0000FFFF\nadd R3 R1 R2\nbne R1 R2 R3"

#initialize the assembler and the simulator
assember = Assembler()
sim = Simulator()

encoded_machine_code = assember.assemble(assembly_code=assembly_code)
memory_with_data = sim.load_program(program=encoded_machine_code)
sim.run(memory_with_data)
