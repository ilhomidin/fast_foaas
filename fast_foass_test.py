import fast_foaas


def test_operations_in_all():
    operations = [
        operation for operation in dir(fast_foaas) if "_" not in operation
    ]
    missed_operations = [
        operation
        for operation in operations
        if operation not in fast_foaas.__all__
    ]
    if missed_operations:
        raise AssertionError(f"Miss {missed_operations} in __all__")


def test_anyway():
    assert (
        fast_foaas.anyway("LM", "Sam")
        == "Who the fuck are you anyway, LM, why are you stirring up so much trouble, and, who pays you? - Sam"
    )


def test_ashole():
    assert fast_foaas.ashole("Sam") == "Fuck you, asshole. - Sam"


def test_awesome():
    assert fast_foaas.awesome("Sam") == "This is Fucking Awesome. - Sam"


def test_bag():
    assert fast_foaas.bag("Sam") == "Eat a bag of fucking dicks. - Sam"


def test_balmer():
    assert (
        fast_foaas.balmer("John", "LM", "Sam")
        == "Fucking John is a fucking pussy. I'm going to fucking bury that guy, I have done it before, and I will do it again. I'm going to fucking kill LM. - Sam"
    )


def test_back():
    assert fast_foaas.back("John", "Sam") == "John, back the fuck off. - Sam"


def test_bday():
    assert (
        fast_foaas.bday("John", "Sam") == "Happy Fucking Birthday, John. - Sam"
    )


def test_because():
    assert (
        fast_foaas.because("Sam") == "Why? Because fuck you, that's why. - Sam"
    )


def test_blackadder():
    assert (
        fast_foaas.blackadder("John", "Sam")
        == "John, your head is as empty as a eunuch’s underpants. Fuck off! - Sam"
    )


def test_bm():
    assert fast_foaas.bm("John", "Sam") == "Bravo mike, John. - Sam"


def test_bucket():
    assert (
        fast_foaas.bucket("Sam") == "Please choke on a bucket of cocks. - Sam"
    )


def test_bus():
    assert (
        fast_foaas.bus("John", "Sam")
        == "Christ on a bendy-bus, John, don't be such a fucking faff-arse. - Sam"
    )


def test_bye():
    assert fast_foaas.bye("Sam") == "Fuckity bye! - Sam"


def test_caniuse():
    assert (
        fast_foaas.caniuse("FOAAS", "Sam")
        == "Can you use FOAAS? Fuck no! - Sam"
    )


def test_chainsaw():
    assert (
        fast_foaas.chainsaw("John", "Sam")
        == "Fuck me gently with a chainsaw, John. Do I look like Mother Teresa? - Sam"
    )


def test_cocksplat():
    assert (
        fast_foaas.cocksplat("John", "Sam")
        == "Fuck off John, you worthless cocksplat - Sam"
    )


def test_cool():
    assert fast_foaas.cool("Sam") == "Cool story, bro. - Sam"


def test_cup():
    assert (
        fast_foaas.cup("Sam")
        == "How about a nice cup of shut the fuck up? - Sam"
    )
