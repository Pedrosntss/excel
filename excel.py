def se(condicao, valor_se_verdadeiro, valor_se_falso):
    return (valor_se_verdadeiro if condicao else valor_se_falso)

alunos = [
    ("João", 40),
    ("Maria", 60),
    ("jose", 94),
    ("Pedro", 70),
    ("Ricardo", 91),
    ("Bruno", 56),
    ("Silas", 51),
    ("Patrícia", 36),
    ("Tatiana", 82),
    ("Roseane", 36),
    ("Rebeca", 66),
    ("Carlos", 65),
    ("Marcos", 73),
    ("Adriana", 91),
    ("Adriano", 32),
]
print(f"{'Aluno':^15} {'Nota':^6} {'Situação':^12}")
print("-"*38)

for nome, nota in alunos:
    situacao = se(nota >=70, "APROVADO", se(nota >=50, "RECUPERAÇÃO","REPROVADO"))

    print(f"{nome} {nota} {situacao}")



print("\n --- Boletim Escolar ---")

aprovados = 0
recuperacao = 0
reprovados = 0

for nome, nota in alunos:
    if nota >= 70:
        aprovados += 1
    elif nota >= 50:
        recuperacao += 1
    elif nota < 50:
        reprovados += 1

print(f"Aprovados: {aprovados}  Recuperação: {recuperacao}  Reprovados: {reprovados}" )