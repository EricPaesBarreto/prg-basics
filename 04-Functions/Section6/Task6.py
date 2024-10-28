def hide_card_number(card_number):
    str_card_number = str(card_number)
    if len(str_card_number) != 16:
        return 'N/A'
    else:
        return f'{str_card_number[0:2]}**********{str_card_number[12:16]}'
    
print(hide_card_number(5290312400019022))