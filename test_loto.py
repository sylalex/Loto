import pytest
from loto import Ticket


class TestLoto:
    def test_name(self):
        ticket = Ticket()
        assert ticket.name == 'User'

    def test_game(self):
        ticket = Ticket()
        assert ticket.is_game == True

    def test_tck(self):
        ticket = Ticket()
        assert len(ticket.tck) == 3