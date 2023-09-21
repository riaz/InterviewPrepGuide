from  src import hello

def test_say_hello():
    text = hello.say_hello()
    assert text == "hello"