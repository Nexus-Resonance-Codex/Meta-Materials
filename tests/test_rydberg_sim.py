from rydberg_sim import RydbergSimulator


def test_rydberg_simulation():
    sim = RydbergSimulator(50)
    result = sim.execute_simulation(5.0, 1.2090419, 0.4653555)

    assert "delta_r_hz" in result
    assert "lqg_index" in result
    assert "ttt7_status" in result
