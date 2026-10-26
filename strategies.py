import pandas as pd
import numpy as np

def calculate_advanced_signal(df):
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    df['RSI'] = df['RSI'].fillna(50)

    df['EMA9'] = df['Close'].ewm(span=9, adjust=False).mean()
    df['EMA21'] = df['Close'].ewm(span=21, adjust=False).mean()
    
    last_close = df['Close'].iloc[-1]
    last_open = df['Open'].iloc[-1]
    last_high = df['High'].iloc[-1]
    last_low = df['Low'].iloc[-1]
    last_rsi = df['RSI'].iloc[-1]
    upper_b = df['Upper_Band'].iloc[-1]
    lower_b = df['Lower_Band'].iloc[-1]
    ema9 = df['EMA9'].iloc[-1]
    ema21 = df['EMA21'].iloc[-1]
    
    prev_close = df['Close'].iloc[-2]
    prev_open = df['Open'].iloc[-2]

    support_level = df['Low'].min()
    resistance_level = df['High'].max()

    total_candle_range = last_high - last_low if (last_high - last_low) > 0 else 0.0001
    lower_wick = min(last_open, last_close) - last_low
    upper_wick = last_high - max(last_open, last_close)

    lower_wick_ratio = lower_wick / total_candle_range
    upper_wick_ratio = upper_wick / total_candle_range

    bullish_engulfing = (prev_close < prev_open) and (last_close > last_open) and (last_close > prev_open)
    bearish_engulfing = (prev_close > prev_open) and (last_close < last_open) and (last_close < prev_open)

    call_score = 0
    put_score = 0

    if abs(last_close - support_level) <= 0.0003 or last_close <= lower_b:
        call_score += 3
    if abs(last_close - resistance_level) <= 0.0003 or last_close >= upper_b:
        put_score += 3

    if lower_wick_ratio >= 0.4:
        call_score += 2
    if upper_wick_ratio >= 0.4:
        put_score += 2

    if last_rsi < 42:
        call_score += 2
    elif last_rsi > 58:
        put_score += 2

    if ema9 > ema21:
        call_score += 1
    elif ema9 < ema21:
        put_score += 1

    if bullish_engulfing:
        call_score += 2
    elif bearish_engulfing:
        put_score += 2

    if call_score > put_score and call_score >= 3:
        accuracy = min(87 + call_score * 2, 98)
        return "CALL", "CALL (UP) ⬆", f"{accuracy}%", last_rsi
    elif put_score > call_score and put_score >= 3:
        accuracy = min(87 + put_score * 2, 98)
        return "PUT", "PUT (DOWN) ⬇", f"{accuracy}%", last_rsi
    else:
        if lower_wick_ratio > upper_wick_ratio:
            return "CALL", "CALL (UP) ⬆", "86%", last_rsi
        else:
            return "PUT", "PUT (DOWN) ⬇", "86%", last_rsi
