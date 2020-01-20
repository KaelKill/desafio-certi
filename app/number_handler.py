class Number_Handler:
    def __init__(self, number):
        self.number = number
        self.written_form = ''
        self.blocks = []
        self.written_blocks = []
        self.is_negative = False

        self.split_number(list(number))
        self.number_to_text()

    def split_number(self, number):
        
        if not number[0].isdigit():
            self.is_negative = True
            number.pop(0)
        
        number.reverse()
        
        number = [int(num) for num in number]
            

        for num in range(0, len(number), 3):
            num_block = number[num:num+3]
            
            while len(num_block) < 3:
                num_block.append(0)

            num_block.reverse()
            self.blocks.append(num_block)
        
        # self.blocks.reverse()
        # print(number)

    def number_to_text(self):
        units = ['', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
        teens = ['', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
        tens  = ['', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
        cents = ['', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']

        for block in self.blocks:
            pre_text = []
            # pre_text = [cents[block[0]], tens[block[1]], units[block[2]]]
            
            if block == [1, 0, 0]:
                pre_text.append('cem')
            else:
                pre_text.append(cents[block[0]]) if cents[block[0]] != '' else None
                if block[1] == 1:
                    pre_text.append(teens[block[2]])
                else:
                    pre_text.append(tens[block[1]]) if tens[block[1]] != '' else None
                    pre_text.append(units[block[2]]) if units[block[2]] != '' else None
                
            text = ' e '.join(pre_text)
            text = text + ' mil' if self.blocks.index(block) == 1 else text
            # print(text)
            self.written_blocks.append(text) if text != '' else None
        self.written_blocks.reverse()
        self.written_form = ' e '.join(self.written_blocks)

        if self.is_negative:
            self.written_form = "menos {}".format(self.written_form)

        print(self.written_form)
        return self.written_form


if __name__ == "__main__":
    nh = Number_Handler('-1234')
    nh = Number_Handler('100000')
    nh = Number_Handler('14015')
