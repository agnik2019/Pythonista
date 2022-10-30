# Function to swap a value from
# big Endian to little Endian and
# vice versa.
def swap_Endians(value):

	leftmost_byte = (value & eval('0x000000FF')) >> 0
	left_middle_byle = (value & eval('0x0000FF00')) >> 8
	right_middle_byte = (value & eval('0x00FF0000'))>> 16
	rightmost_byte = (value & eval('0xFF000000'))>> 24

	leftmost_byte <<= 24
	left_middle_byle <<= 16
	right_middle_byte <<= 8
	rightmost_byte <<= 0
    
	result = (leftmost_byte | left_middle_byle
				| right_middle_byte | rightmost_byte)


	return result



# main function
if __name__ == '__main__':
	big_Endian = eval('0x12345678')
	little_Endian = eval('0x78563412')
	
	result1 = swap_Endians(big_Endian)

	result2 = swap_Endians(little_Endian)

	print("big Endian to little: % s\nlittle Endian
			to big: % s" %(hex(result1), hex(result2)))
