import time
from escpos.printer import Usb

# 30 caracteres no max por linha
# printer.textln('@'*30) -> som mais grosso

def print_range(printer, n, text='\n', multiply_text=1):
    # max 30 chars per line in multiply_text
    for _ in range(n):
        printer.text(text * multiply_text)
        
        
def imprimir_com_tempo(printer):
    print_range(printer, 1)
    time.sleep(.5)
    print_range(printer, 4)
    time.sleep(.5)
    print_range(printer, 10)

    time.sleep(1)
    
    print_range(printer, 1)
    time.sleep(.5)
    print_range(printer, 4)
    time.sleep(.5)
    print_range(printer, 10)
    
    time.sleep(1)
    
    print_range(printer, 1)
    time.sleep(.5)
    print_range(printer, 4)
    time.sleep(.5)
    print_range(printer, 10)
    time.sleep(.5)
    print_range(printer, 4)
    time.sleep(.7)
    print_range(printer, 4, '&', 30)
    time.sleep(1)

printer = Usb(0xfe6, 0x811e)
printer.line_spacing(10)
# Imprimir com pausa
imprimir_com_tempo(printer)
