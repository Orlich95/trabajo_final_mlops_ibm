from src.predict import predict_close


def test_predict_close_returns_float():
    prediction = predict_close(
        open_price=180,
        high=185,
        low=178,
        volume=10000000,
    )

    assert isinstance(prediction, float)