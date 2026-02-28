import MetaTrader5 as mt5
import pandas as pd
import numpy as np

# ==========================================================
# JARVIS MEGA-MINER V80: THE 3 MILLION LIMIT-BREAKER
# ==========================================================
SYMBOL = "EURUSD.m"
FILE_NAME = "synthetic_market_data.csv"
TARGET_BARS = 3000000 

print(f"🚀 MEMULAI OPERASI PENAMBANGAN RAKSASA (3 JUTA DATA)...")

if not mt5.initialize():
    print("❌ Gagal terhubung ke MT5"); quit()

# 1. SEDOT DATA M1 DARI SERVER
print(f"📡 Menarik {TARGET_BARS:,} candle M1... (Proses ini butuh 2-5 menit)")
rates = mt5.copy_rates_from_pos(SYMBOL, mt5.TIMEFRAME_M1, 0, TARGET_BARS)

# Perbaikan Logika Pengecekan (is not None)
if rates is None or len(rates) < 1:
    print(f"⚠️ Peringatan: Gagal mengambil data. Cek koneksi atau 'Max bars in chart'.")
    mt5.shutdown(); quit()
else:
    print(f"✅ Berhasil menyedot {len(rates):,} data asli dari server.")

# 2. PROSES & MAPPING (Price, Danger, Result)
df = pd.DataFrame(rates)
df['Price'] = df['close']
df['Danger'] = df['tick_volume']
# Result: 1 jika naik 3 pips dalam 10 menit
df['Result'] = (df['close'].shift(-10) > df['close'] + 0.0003).astype(int)

# Simpan kolom dasar saja agar RAM tidak sesak
df_final = df[['Price', 'Danger', 'Result', 'high', 'low', 'tick_volume']]

# 3. LOCK DATA KE CSV
print(f"💾 Menyimpan 3 Juta data ke {FILE_NAME}... (Sabar, file akan besar)")
df_final.to_csv(FILE_NAME, index=False)

print(f"🏁 OPERASI SELESAI!")
print(f"📊 File '{FILE_NAME}' kini berisi {len(df_final):,} baris amunisi.")
mt5.shutdown()