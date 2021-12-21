import os
from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.set_font('Times', '', 16)

texto = "A fé e a razão possuem seus ideais, e se complementam em várias questões, há situações em que a razão pode provar o que ocorreu, mas há também momentos em que apenas a fé explica, o que há em comum entre eles é que sempre buscam explicar a vida, e entender o íntimo do ser humano.Tem que ter discernimento e saber balancear, ponderar, para não virar um cético e nem um fanático. A fé e a razão podem, e até tendem a andar juntas, pelo fato de que a filosofia busca dar sentido as coisas da vida, separar uma da outra empobrece o conhecimento pois são duas asas pelas quais o espírito humano se eleva para a contemplação da verdade. Foi Deus que colocou em nosso coração o desejo de conhecê-lo, de conhecer a verdade, e, assim, de nos conhecermos."

pdf.multi_cell(w=0, h=8, txt=texto, align='J')

pdf.output("Fé e Razão.pdf")

print("O PDF foi criado com sucesso!")
os.system("pause")