from src import notas

def test_calcular_media():
    assert isinstance(notas.calcular_media(10.0, 10.0), str)  
    assert isinstance(notas.calcular_media(0, 0), str)     
    assert isinstance(notas.calcular_media(-1, 5), ValueError)
    assert isinstance(notas.calcular_media(5, -1), ValueError)
    assert isinstance(notas.calcular_media(-1,-1), ValueError)
    assert isinstance(notas.calcular_media(10, 11), ValueError)
    assert isinstance(notas.calcular_media(11, 11), ValueError)
    assert isinstance(notas.calcular_media("a", 5), ValueError)
    assert isinstance(notas.calcular_media("a", "a"), ValueError)
    assert isinstance(notas.calcular_media(0, -1), ValueError)