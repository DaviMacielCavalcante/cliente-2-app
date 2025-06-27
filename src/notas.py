def calcular_media(n1: float, n2: float) -> str:

    try:
        if not isinstance(n1, float) or isinstance(n2, float):
            try:
                n1 = float(n1)
                n2 = float(n2)
            except ValueError:
                raise ValueError("Formato de nota inválida. Por favor, insira um número.")
        if n1 < 0 or n2 < 0:
            raise ValueError("Nota inválida. Por favor, insira valores positivos.")
        if n1 > 10 or n2 > 10:
            raise ValueError("Nota inválida. Por favor, insira notas entre 0 e 10.")
        media = (n1 + n2) / 2
        return f"A média é: {media:.2f}"
    except ValueError as e:
        return e
    