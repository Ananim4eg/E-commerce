def test_smartphone_init(smartphone):
    smart1 = smartphone
    assert smart1.efficiency == "high"
    assert smart1.memory == 512
    assert smart1.model == 14
    assert smart1.color == "grey"