from ltp import LTP

_model = None

def get_model():
    global _model
    if _model is None:
        _model = LTP("D:/LTP/legacy")
    return _model