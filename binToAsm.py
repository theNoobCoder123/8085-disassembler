data = dict()

l = "1,ACI,Data,CE,2\n2,ADC,A,8F,1\n3,ADC,B,88,1\n4,ADC,C,89,1\n5,ADC,D,8A,1\n6,ADC,E,8B,1\n7,ADC,H,8C,1\n8,ADC,L,8D,1\n9,ADC,M,8E,1\n10,ADD,A,87,1\n11,ADD,B,80,1\n12,ADD,C,81,1\n13,ADD,D,82,1\n14,ADD,E,83,1\n15,ADD,H,84,1\n16,ADD,L,85,1\n17,ADD,M,86,1\n18,ADI,Data,C6,2\n19,ANA,A,A7,1\n20,ANA,B,A0,1\n21,ANA,C,A1,1\n22,ANA,D,A2,1\n23,ANA,E,A3,1\n24,ANA,H,A4,1\n25,ANA,L,A5,1\n26,ANA,M,A6,1\n27,ANI,Data,E6,2\n28,CALL,Address,CD,3\n29,CC,Address,DC,3\n30,CM,Address,FC,3\n31,CMA,-,2F,1\n32,CMC,-,3F,1\n33,CMP,A,BF,1\n34,CMP,B,B8,1\n35,CMP,C,B9,1\n36,CMP,D,BA,1\n37,CMP,E,BB,1\n38,CMP,H,BC,1\n39,CMP,L,BD,1\n40,CMP,M,BD,1\n41,CNC,Address,D4,3\n42,CNZ,Address,C4,3\n43,CP,Address,F4,3\n44,CPE,Address,EC,3\n45,CPI,Data,FE,2\n46,CPO,Address,E4,3\n47,CZ,Address,CC,3\n48,DAA,-,27,1\n49,DAD,B,09,1\n50,DAD,D,19,1\n51,DAD,H,29,1\n52,DAD,SP,39,1\n53,DCR,A,3D,1\n54,DCR,B,05,1\n55,DCR,C,0D,1\n56,DCR,D,15,1\n57,DCR,E,1D,1\n58,DCR,H,25,1\n59,DCR,L,2D,1\n60,DCR,M,35,1\n61,DCX,B,0B,1\n62,DCX,D,1B,1\n63,DCX,H,2B,1\n64,DCX,SP,3B,1\n65,DI,-,F3,1\n66,EI,-,FB,1\n67,HLT,-,76,1\n68,IN,Data,DB,2\n69,INR,A,3C,1\n70,INR,B,04,1\n71,INR,C,0C,1\n72,INR,D,14,1\n73,INR,E,1C,1\n74,INR,H,24,1\n75,INR,L,2C,1\n76,INR,M,34,1\n77,INX,B,03,1\n78,INX,D,13,1\n79,INX,H,23,1\n80,INX,SP,33,1\n81,JC,Address,DA,3\n82,JM,Address,FA,3\n83,JMP,Address,C3,3\n84,JNC,Address,D2,3\n85,JNZ,Address,C2,3\n86,JP,Address,F2,3\n87,JPE,Address,EA,3\n88,JPO,Address,E2,3\n89,JZ,Address,CA,3\n90,LDA,Address,3A,3\n91,LDAX,B,0A,1\n92,LDAX,D,1A,1\n93,LHLD,Address,2A,3\n94,LXI,B Address,01,3\n95,LXI,D Address,11,3\n96,LXI,H Address,21,3\n97,LXI,SP Address,31,3\n98,MOV,A A,7F,1\n99,MOV,A B,78,1\n100,MOV,A C,79,1\n101,MOV,A D,7A,1\n102,MOV,A E,7B,1\n103,MOV,A H,7C,1\n104,MOV,A L,7D,1\n105,MOV,A M,7E,1\n106,MOV,B A,47,1\n107,MOV,B B,40,1\n108,MOV,B C,41,1\n109,MOV,B D,42,1\n110,MOV,B E,43,1\n111,MOV,B H,44,1\n112,MOV,B L,45,1\n113,MOV,B M,46,1\n114,MOV,C A,4F,1\n115,MOV,C B,48,1\n116,MOV,C C,49,1\n117,MOV,C D,4A,1\n118,MOV,C E,4B,1\n119,MOV,C H,4C,1\n120,MOV,C L,4D,1\n121,MOV,C M,4E,1\n122,MOV,D A,57,1\n123,MOV,D B,50,1\n124,MOV,D C,51,1\n125,MOV,D D,52,1\n126,MOV,D E,53,1\n127,MOV,D H,54,1\n128,MOV,D L,55,1\n129,MOV,D M,56,1\n130,MOV,E A,5F,1\n131,MOV,E B,58,1\n132,MOV,E C,59,1\n133,MOV,E D,5A,1\n134,MOV,E E,5B,1\n135,MOV,E H,5C,1\n136,MOV,E L,5D,1\n137,MOV,E M,5E,1\n138,MOV,H A,67,1\n139,MOV,H B,60,1\n140,MOV,H C,61,1\n141,MOV,H D,62,1\n142,MOV,H E,63,1\n143,MOV,H H,64,1\n144,MOV,H L,65,1\n145,MOV,H M,66,1\n146,MOV,L A,6F,1\n147,MOV,L B,68,1\n148,MOV,L C,69,1\n149,MOV,L D,6A,1\n150,MOV,L E,6B,1\n151,MOV,L H,6C,1\n152,MOV,L L,6D,1\n153,MOV,L M,6E,1\n154,MOV,M A,77,1\n155,MOV,M B,70,1\n156,MOV,M C,71,1\n157,MOV,M D,72,1\n158,MOV,M E,73,1\n159,MOV,M H,74,1\n160,MOV,M L,75,1\n161,MVI,A Data,3E,2\n162,MVI,B Data,06,2\n163,MVI,C Data,0E,2\n164,MVI,D Data,16,2\n165,MVI,E Data,1E,2\n166,MVI,H Data,26,2\n167,MVI,L Data,2E,2\n168,MVI,M Data,36,2\n169,NOP,-,00,1\n170,ORA,A,B7,1\n171,ORA,B,B0,1\n172,ORA,C,B1,1\n173,ORA,D,B2,1\n174,ORA,E,B3,1\n175,ORA,H,B4,1\n176,ORA,L,B5,1\n177,ORA,M,B6,1\n178,ORI,Data,F6,2\n179,OUT,Data,D3,2\n180,PCHL,-,E9,1\n181,POP,B,C1,1\n182,POP,D,D1,1\n183,POP,H,E1,1\n184,POP,PSW,F1,1\n185,PUSH,B,C5,1\n186,PUSH,D,D5,1\n187,PUSH,H,E5,1\n188,PUSH,PSW,F5,1\n189,RAL,-,17,1\n190,RAR,-,1F,1\n191,RC,-,D8,1\n192,RET,-,C9,1\n193,RIM,-,20,1\n194,RLC,-,07,1\n195,RM,-,F8,1\n196,RNC,-,D0,1\n197,RNZ,-,C0,1\n198,RP,-,F0,1\n199,RPE,-,E8,1\n200,RPO,-,E0,1\n201,RRC,-,0F,1\n202,RST,0,C7,1\n203,RST,1,CF,1\n204,RST,2,D7,1\n205,RST,3,DF,1\n206,RST,4,E7,1\n207,RST,5,EF,1\n208,RST,6,F7,1\n209,RST,7,FF,1\n210,RZ,-,C8,1\n211,SBB,A,9F,1\n212,SBB,B,98,1\n213,SBB,C,99,1\n214,SBB,D,9A,1\n215,SBB,E,9B,1\n216,SBB,H,9C,1\n217,SBB,L,9D,1\n218,SBB,M,9E,1\n219,SBI,Data,DE,2\n220,SHLD,Address,22,3\n221,SIM,-,30,1\n222,SPHL,F9,1\n223,STA,Address,32,3\n224,STAX,B,02,1\n225,STAX,D,12,1\n226,STC,-,37,1\n227,SUB,A,97,1\n228,SUB,B,90,1\n229,SUB,C,91,1\n230,SUB,D,92,1\n231,SUB,E,93,1\n232,SUB,H,94,1\n233,SUB,L,95,1\n234,SUB,M,96,1\n235,SUI,Data,D6,2\n236,XCHG,-,EB,1\n237,XRA,A,AF,1\n238,XRA,B,A8,1\n239,XRA,C,A9,1\n240,XRA,D,AA,1\n241,XRA,E,AB,1\n242,XRA,H,AC,1\n243,XRA,L,AD,1\n244,XRA,M,AE,1\n245,XRI,Data,EE,2\n246,XTHL,-,E3,1"
lines = l.split('\n')
for line in lines:
	line = line.strip()
	words = line.split(",")
	for i in range(len(words)):
		words[i] = words[i].strip()

	data[words[3]] = words

binFileName = input("Enter name of binary file :- ")
with open(binFileName, 'rb') as bin:
	binFile = bin.read()
	cnt = 0
	instCnt = -1
	instructions = []

	for byte in binFile:
		byteHex = (('0x{:02x}'.format(byte))[-2:]).upper()
		if cnt == 0:
			cnt = int(data[byteHex][4]) - 1
			instructions.append([data[byteHex]])
			instCnt += 1
		else:
			instructions[instCnt].append(byteHex)
			cnt -= 1

with open('output.asm', 'w') as out:
	address = int(input("Enter starting address :- "), 16)
	for inst in instructions:
		addr = (('0x{:04x}'.format(address))[-4:]).upper()
		address += int(inst[0][4])
		ops = inst[0][2]
		operands = ops.split()
		if ' Data' in ops:
			dat = inst[1]
			ops = ops.replace(' Data', "," + dat)
		elif 'Data' in ops:
			dat = inst[1]
			ops = ops.replace('Data', dat)
		elif ' Address' in ops:
			label = inst[2] + inst[1]
			ops = ops.replace(' Address', "," + label)
		elif 'Address' in ops:
			label = inst[2] + inst[1]
			ops = ops.replace('Address', label)
		elif '-' in ops:
			ops = str()
		else:
			ops = ops.strip().replace(' ', ',')

		outstr = (addr + " : " + inst[0][1] + " " + ops).strip()
		print(outstr)
		out.write(outstr + "\n")
