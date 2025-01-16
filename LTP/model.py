from ltp import LTP

_model = None

def get_model():
    global _model
    if _model is None:
        _model = LTP("D:/LTP/small")
        _model.add_words(["不敢", "点心", "是因为", "是由于", "归因于", "得益于", "归功于", "归咎于"])
    return _model