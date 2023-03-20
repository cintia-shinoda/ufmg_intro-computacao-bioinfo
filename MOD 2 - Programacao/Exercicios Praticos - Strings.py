# Exercicio 1

tnf =  'VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL'

## A
len(tnf)

## B
tnf.count('LL')

## C
tnf.find('GG')

tnf.find('RR')

## D
tnf[:100]

## E
tnf = tnf.replace('SSSR', 'AAAA')

## F
tnf.split('AAAA')


# Exercicio 2

texto = "As proteínas são cadeias polipeptídicas formadas pela ligação peptídica entre resíduos de aminoácidos. Existem 20 tipos de aminoácidos comumente encontrados nos seres vivos. A esses aminoácidos, foram atribuídas abreviações de 3 letras e símbolos de 1 letra. As abreviações de 3 letras são bastante evidentes consistindo nas três primeiras letras do se nome."

## A
texto.upper()

## B
texto.lower()

## C
texto.title()

## D
texto.swapcase()


# Exercicio 3
insulin_signal = 'MALWMRLLPLLALLALWGPDPAAA'

## A
len(insulin_signal)

## B
insulin_signal.split('LLALLALWG')

## C
''.join(insulin_signal)

## D
insulin_signal.replace('DPAAA', 'LLALL')


# Exercicio 4
seq_dna = 'GATGGAACTTGACGTAAACCTATATT'
seq_dna.replace('T', 'U')