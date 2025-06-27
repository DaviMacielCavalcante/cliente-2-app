def vote(idade):
    try:
        if isinstance(idade, str):
            raise ValueError("Formato de idade inválida. Por favor, insira um número inteiro.")
        if isinstance(idade, int):
            if idade < 0:
                raise ValueError("Idade inválida. Por favor, insira um valor válido.")
            elif idade < 18 or idade >= 70:
                return "Você não é obrigado a votar."
            elif 18 <= idade < 70:
                return "Escolha em quem deseja votar."
        else:
            raise ValueError("Formato inválido. Por favor, insira um número inteiro.")
    except ValueError as e:
        return str(e)