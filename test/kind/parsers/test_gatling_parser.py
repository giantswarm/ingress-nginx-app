from parsers.gatling_parser import GatlingParser


def test_gatling_parser():
    text: str = ""
    with open("sample.log", "r") as f:
        text = f.read()

    parser = GatlingParser(text)
