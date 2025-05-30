if __name__ == "__main__":
    class Pessoa:
        def __init__(self, nome, email, cpf, rg, telefone, anonascimento):
            self.nome = nome
            self.email = email
            self.cpf = cpf
            self.rg = rg
            self.telefone = telefone
            self.anonascimento = anonascimento

    pacientes_sem_risco = []
    cont = 0
    contador = 0
    confirmacao = "s"
    while confirmacao == "s":
        cont += 1
        confirmacao = input("'s' para adcionar paciente e 'n' se nao quiser: ")
        if confirmacao == "s":
            pessoa = Pessoa(input("Nome: "), input("Email: "),
                            int(input("CPF: ")), input("RG: "),
                            input("Telefone: "), int(input("Ano de Nascimento: ")))

            def calcular_Idade():
                idade = 2025 - pessoa.anonascimento
                return idade

            if calcular_Idade() >= 65:
                with open(r"./risco/pacientes.txt", "a", encoding="UTF-8") as arquivo:
                    arquivo.write(f"""
    Paciente {cont}:
    Nome: {pessoa.nome}
    email: {pessoa.email}
    CPF: {pessoa.cpf}
    RG: {pessoa.rg}
    Telefone: {pessoa.telefone}
    Idade:{calcular_Idade()}

                """)
                    arquivo.close()
            else:
                contador += 1
                paciente = {"nome": pessoa.nome,
                            "email": pessoa.email,
                            "CPF": pessoa.cpf,
                            "RG": pessoa.rg,
                            "Telefone": pessoa.telefone,
                            "Idade": calcular_Idade()}
                pacientes_sem_risco.append(paciente)
                paciente = {}
        else:
            print("Sistema cancelado!")
            break
