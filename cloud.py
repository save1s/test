import leancloud

engine = leancloud.Engine()


@engine.define
def test(**params):
    return 123
