from escpos.printer import Usb
import time

def emitir_beep(printer, vezes=1):
    # ESC + (b) para beep
    printer._raw([27, 33, vezes])  # Código ESC para "beep" e número de repetições

def imprimir_com_beeps(printer):
    printer.text("Impressão com som..gsdjfghsdklfghsdklfjghsdklfgshdkfghsdlkjfghsdlkfgsdgf.\nImpressão com som..gsdjfghsdklfghsdklfjghsdklfgshdkfghsdlkjfghsdlkfgsdgf.\nImpressão com som..gsdjfghsdklfghsdklfjghsdklfgshdkfghsdlkjfghsdlkfgsdgf.\nImpressão com som..gsdjfghsdklfghsdklfjghsdklfgshdkfghsdlkjfghsdlkfgsdgf.\n")
    
    # Emitir um beep
    emitir_beep(printer, 1)  # Emitir 1 beep
    
    time.sleep(0.5)  # Pausar
    
    printer.text("Texto impresso após beep...\n")
    
    # Emitir mais beeps
    emitir_beep(printer, 3)  # Emitir 3 beeps
    
    time.sleep(0.5)  # Pausar
    
    printer.text("Texto final...\n")
    
    # Emitir outro beep
    emitir_beep(printer, 2)  # Emitir 2 beeps
    
    # Cortar o papel
    printer.cut()

# Conectar à impressora USB
printer = Usb(0xfe6, 0x811e)

# Imprimir com beeps
imprimir_com_beeps(printer)
