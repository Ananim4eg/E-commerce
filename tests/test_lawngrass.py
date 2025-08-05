def test_lawngrass_init(lawngrass):
    lg = lawngrass
    assert lg.country == "Germany"
    assert lg.germination_period == 0.5
    assert lg.color == "green"
