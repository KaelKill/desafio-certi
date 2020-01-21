from flask_babel import _

class Number_Handler:
    def __init__(self, number):
        self.number = number
        self.written_form = ''
        self.blocks = []
        self.written_blocks = []
        self.is_negative = False

        self.split_number(list(number))
        self.written_form = self.number_to_text()

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

    def number_to_text(self):
        units = ['', _('um'), _('dois'), _('tres'), _('quatro'), _('cinco'), _('seis'), _('sete'), _('oito'), _('nove')]
        teens = [_('dez'), _('onze'), _('doze'), _('treze'), _('quatorze'), _('quinze'), _('dezesseis'), _('dezessete'), _('dezoito'), _('dezenove')]
        tens  = ['', _('dez'), _('vinte'), _('trinta'), _('quarenta'), _('cinquenta'), _('sessenta'), _('setenta'), _('oitenta'), _('noventa')]
        cents = ['', _('cento'), _('duzentos'), _('trezentos'), _('quatrocentos'), _('quinhentos'), _('seiscentos'), _('setecentos'), _('oitocentos'), _('novecentos')]

        cnt = 0
        for block in self.blocks:
            pre_text = []
            if block == [1, 0, 0]:
                pre_text.append(_('cem'))
            elif self.blocks == [[0, 0, 0]]:
                pre_text.append('zero')
            else:
                pre_text.append(cents[block[0]]) if cents[block[0]] != '' else None
                if block[1] == 1:
                    pre_text.append(teens[block[2]])
                else:
                    pre_text.append(tens[block[1]]) if tens[block[1]] != '' else None
                    pre_text.append(units[block[2]]) if units[block[2]] != '' else None
                
            text = _(' e ').join(pre_text)
            text = text + _(' mil') if cnt == 1 else text
            self.written_blocks.append(text) if text != '' else None
            cnt = cnt + 1

        self.written_blocks.reverse()
        self.written_form = _(' e ').join(self.written_blocks)

        if self.is_negative:
            self.written_form = _("menos ") + self.written_form

        print(self.written_form)
        return self.written_form


if __name__ == "__main__":
    nh = Number_Handler('1234')
    nh = Number_Handler('100000')
    nh = Number_Handler('14015')
    nh = Number_Handler('0')
