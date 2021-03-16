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


def test_dalton():
    assert (
        fast_foaas.dalton("John", "Sam")
        == "John: A fucking problem solving super-hero. - Sam"
    )


def test_dense():
    assert (
        fast_foaas.dense("Sam") == "You disingenuous dense motherfucker! - Sam"
    )


def test_deraadt():
    assert (
        fast_foaas.deraadt("John", "Sam")
        == "John you are being the usual slimy hypocritical asshole... You may have had value ten years ago, but people will see that you don't anymore. - Sam"
    )


def test_diabetes():
    assert (
        fast_foaas.diabetes("Sam")
        == "I'd love to stop and chat to you but I'd rather have type 2 diabetes. - Sam"
    )


def test_donut():
    assert (
        fast_foaas.donut("John", "Sam")
        == "John, go and take a flying fuck at a rolling donut. - Sam"
    )


def test_dosomething():
    assert (
        fast_foaas.dosomething("Write", "test", "Sam")
        == "Write the fucking test! - Sam"
    )


def test_dumbledore():
    assert (
        fast_foaas.dumbledore("Sam")
        == "Happiness can be found, even in the darkest of times, if one only remembers to fuck off. - Sam"
    )


def test_equity():
    assert (
        fast_foaas.equity("John", "Sam")
        == "Equity only? Long hours? Zero Pay? Well John, just sign me right the fuck up. - Sam"
    )


def test_even():
    assert fast_foaas.even("Sam") == "I can't fuckin' even. - Sam"


def test_everyone():
    assert fast_foaas.everyone("Sam") == "Everyone can go and fuck off. - Sam"


def test_everything():
    assert fast_foaas.everything("Sam") == "Fuck everything. - Sam"


def test_family():
    assert (
        fast_foaas.family("Sam")
        == "Fuck you, your whole family, your pets, and your feces. - Sam"
    )


def test_fascinating():
    assert (
        fast_foaas.fascinating("Sam")
        == "Fascinating story, in what chapter do you shut the fuck up? - Sam"
    )


def test_fewer():
    assert (
        fast_foaas.fewer("John", "Sam")
        == "Go fuck yourself John, you'll disappoint fewer people. - Sam"
    )


def test_field():
    assert (
        fast_foaas.field("John", "Sam", "Lui")
        == "And John said unto Sam, 'Verily, cast thine eyes upon the field in which I grow my fucks', and Sam gave witness unto the field, and saw that it was barren. - Lui"
    )


def test_flying():
    assert fast_foaas.flying("Sam") == "I don't give a flying fuck. - Sam"


def test_ftfy():
    assert fast_foaas.ftfy("Sam") == "Fuck That, Fuck You - Sam"


def test_fts():
    assert fast_foaas.fts("John", "Sam") == "Fuck that shit, John. - Sam"


def test_fyyff():
    assert fast_foaas.fyyff("Sam") == "Fuck you, you fucking fuck. - Sam"
