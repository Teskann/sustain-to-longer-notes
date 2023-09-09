import sustain_to_longer_notes.core as sus


def test_SustainRange_contains():
    # Inside
    assert sus.SustainRange(0, 10).contains(3)
    assert sus.SustainRange(0, 10).contains(5)

    # Bounds should be included
    assert sus.SustainRange(1, 4).contains(1)
    assert sus.SustainRange(1, 4).contains(4)

    # Greater
    assert not sus.SustainRange(70.2, 103.0).contains(103.1)
    assert not sus.SustainRange(70.2, 103.0).contains(1000.0)

    # Lower
    assert not sus.SustainRange(11.0, 23.3).contains(10.9)
    assert not sus.SustainRange(11.0, 23.3).contains(0.0)


def test_SustainRange_eq():
    assert sus.SustainRange(0, 1) == sus.SustainRange(0, 1)
    assert sus.SustainRange(10, 20) == sus.SustainRange(10, 20.0)
    assert not sus.SustainRange(10, 21) == sus.SustainRange(10, 20.0)
    assert not sus.SustainRange(10, 20) == sus.SustainRange(3, 20.0)

    assert [sus.SustainRange(10, 10), sus.SustainRange(23, 24)] == [sus.SustainRange(10, 10), sus.SustainRange(23, 24)]


def test_SustainRange_str():
    assert str(sus.SustainRange(0, 1)) == "(0, 1)"
    assert str(sus.SustainRange(5.32, 12.3)) == "(5.32, 12.3)"
