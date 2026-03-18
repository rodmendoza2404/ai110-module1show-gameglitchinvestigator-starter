from logic_utils import check_guess, get_hint_message, get_range_for_difficulty, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_too_high_hint_is_lower_direction():
    # New targeted regression test for the reversed hint bug.
    assert get_hint_message("Too High") == "📉 Go LOWER!"


def test_parse_guess_rejects_decimal():
    ok, value, error = parse_guess("12.5")
    assert ok is False
    assert value is None
    assert error == "Use a whole number."


def test_range_for_hard_mode():
    assert get_range_for_difficulty("Hard") == (1, 50)
