from src import vote

def test_vote():
    assert vote.vote(17) == "Você não é obrigado a votar."
    assert vote.vote(18) == "Escolha em quem deseja votar."
    assert vote.vote(69) == "Escolha em quem deseja votar."
    assert vote.vote(70) == "Você não é obrigado a votar."   
    assert vote.vote(-1) == "Idade inválida. Por favor, insira um valor válido."    
    assert vote.vote("a") == "Formato de idade inválida. Por favor, insira um número inteiro."