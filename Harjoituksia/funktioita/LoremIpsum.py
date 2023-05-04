def tulostaLoremIpsum():
    LoremIpsum = "Lorem Ipsum dolor sit amet, consectetur adipiscing elit."
    print(LoremIpsum)

def tulostaLoremIpsumLauseKymmenesti():
    tulostuskerrat = 0
    while tulostuskerrat < 10:
        tulostaLoremIpsum()
        tulostuskerrat += 1

tulostaLoremIpsumLauseKymmenesti()