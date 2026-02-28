import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import joblib
import os
import xgboost as xgb
import psutil

# ==========================================================
# JARVIS V80.13: OMNI-GOD ULTRA-DEEP (5000 PASUKAN)
# ==========================================================
SYMBOL = "EURUSD.m"
BRAIN_FILE = "jarvis_brain_v60.pkl"
SYNTHETIC_FILE = "synthetic_market_data.csv" 

def cek_ram():
    mem = psutil.virtual_memory()
    print(f"📊 MONITOR RAM: {mem.used / (1024**3):.2f} GB / {mem.total / (1024**3):.2f} GB")

def get_rsi(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def enrich_data(df):
    if 'Price' in df.columns: df['close'] = df['Price']
    if 'Danger' in df.columns: df['tick_volume'] = df['Danger']
    df.columns = [c.lower() for c in df.columns]

    print("🧪 Mengaktifkan 8 Jendral (RSI, BB, MACD, ATR, ROC, VOL)...")
    df['rsi'] = get_rsi(df['close'])
    ma20 = df['close'].rolling(20).mean()
    std20 = df['close'].rolling(20).std()
    df['u_bb'] = ma20 + (2 * std20)
    df['l_bb'] = ma20 - (2 * std20)
    df['macd'] = df['close'] - df['close'].shift(12).rolling(14).mean()
    df['atr'] = (df['high'] - df['low']).rolling(100).mean() * 10000 
    df['roc'] = (df['close'] - df['close'].shift(5)) / df['close'].shift(5) * 100
    df['vol'] = df['tick_volume']
    
    df['target'] = (df['close'].shift(-10) > df['close'] + 0.0003).astype(int)
    return df.dropna()

print("⚡ MENGAKTIFKAN MODE PREDATOR ULTRA-DEEP RTX 3050...")
cek_ram()

if not mt5.initialize(): quit()
rates = mt5.copy_rates_from_pos(SYMBOL, mt5.TIMEFRAME_M1, 0, 50000)
df_fresh = enrich_data(pd.DataFrame(rates))
mt5.shutdown()

if os.path.exists(SYNTHETIC_FILE):
    print(f"📚 Menelan 2.9jt Data Sejarah...")
    df_old = pd.read_csv(SYNTHETIC_FILE)
    df_old = enrich_data(df_old)
    final_df = pd.concat([df_old, df_fresh], ignore_index=True)
else:
    print("❌ FILE TIDAK DITEMUKAN!"); quit()

features = ['close', 'rsi', 'u_bb', 'l_bb', 'macd', 'atr', 'roc', 'vol']
X = final_df[features].values.astype('float32')
y = final_df['target'].values.astype('int8')

print(f"🔥 TOTAL PASUKAN BERLATIH: {len(final_df):,} baris.")
cek_ram()

model = xgb.XGBClassifier(
    n_estimators=5000,      # Pasukan ditambah untuk data 3jt
    max_depth=25,           # Pikiran lebih dalam
    learning_rate=0.03,     # Belajar lebih teliti
    tree_method='hist',
    device='cuda',          # Paksa GPU RTX 3050
    random_state=42,
    verbosity=1
)

print("🏗️ MEMULAI PERANG DATA PADA GPU (5000 TREES)...")
model.fit(X, y)

joblib.dump(model, BRAIN_FILE)
print(f"✅ JARVIS V80.13 BERHASIL MENERAPKAN KEKUATAN GPU RTX 3050!")
cek_ram()