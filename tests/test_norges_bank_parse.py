from terra_terminal.clients.norges_bank import NorgesBankClient


def test_parse_sdmx_minimal() -> None:
    payload = {
        "data": {
            "structure": {
                "dimensions": {
                    "observation": [
                        {
                            "values": [
                                {"id": "2024-01-01"},
                                {"id": "2024-01-02"},
                            ]
                        }
                    ]
                }
            },
            "dataSets": [
                {
                    "series": {
                        "0:0:0:0": {
                            "observations": {
                                "0": ["4.5"],
                                "1": ["4.25"],
                            }
                        }
                    }
                }
            ],
        }
    }
    rows = NorgesBankClient.parse_sdmx_observations(payload)
    assert len(rows) == 2
    assert rows[0].period == "2024-01-01"
    assert rows[0].value == 4.5
    assert rows[1].value == 4.25
