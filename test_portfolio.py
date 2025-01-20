from portfolio import Portfolio

def test_update_holdings():
    p = Portfolio()

    # sell before buy
    assert p.update_holdings("MSFT", -20) == False
    assert p.get_holdings() == {}

    # buy stock for first time
    assert p.update_holdings("MSFT", 20) == True
    assert p.get_holdings() == {"MSFT": 20}

    # normal buy
    assert p.update_holdings("MSFT", 30) == True
    assert p.get_holdings() == {"MSFT" : 50}

    # normal sell
    assert p.update_holdings("MSFT", -30) == True
    assert p.get_holdings() == {"MSFT" : 20}

    #sell all
    assert p.update_holdings("MSFT", -50) == True
    assert p.get_holdings() == {}
