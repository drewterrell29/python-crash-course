import city_functions
def test_city_country():
    response = city_functions.place("Dallas", "Texas")

    assert response == "Dallas, Texas"
