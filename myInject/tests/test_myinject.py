import pytest

from myInject import Injection as INJ

def add(x,y): return x+y
def sub(x,y): return x-y
def mul(x,y): return x*y
def exp(x,y): return x**y

ADD=INJ(fn=add)
SUB=INJ(fn=sub)
EXP=INJ(fn=exp)

def binop(x,y,inj=ADD): return inj.fn(x,y)

@pytest.fixture
def wrapped():
    class Namespace: pass
    xx=Namespace()
    xx.binop = lambda x,y : binop( x, y, inj=EXP )
    return xx

def test_add(): assert binop(3,2) == 3 + 2
def test_sub(): assert binop(3,2,inj=SUB) == 3 - 2
def test_mul(): assert binop(3,2,inj=INJ(fn=lambda x,y: x*y)) == 3 * 2
def test_exp(wrapped): assert wrapped.binop(3,2) == 3 ** 2
