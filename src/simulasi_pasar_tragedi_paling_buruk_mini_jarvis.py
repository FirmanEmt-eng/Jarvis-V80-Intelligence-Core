import numpy as np
import pandas as pd
import time
import random

# ==========================================================
# THE MATRIX V4: RAGNAROK PROTOCOL (BEYOND LOGIC)
# ==========================================================
STARTING_EQUITY = 214.0
DAILY_PROFIT_TARGET = 25.0
MAX_DAILY_LOSS = 15.0  # PERISAI TERAKHIR SEBELUM KIAMAT
BASE_LOT = 0.12
COMMISSION_FIXED = 7.0 
RECOVERY_FACTOR = 1.35

print("🌋 MENGAKTIFKAN PROTOKOL RAGNAROK: Menggabungkan Tragedi SNB 2015 & Brexit 2016...")
time.sleep(2)

class RagnarokSimulator:
    def __init__(self):
        self.equity = STARTING_EQUITY
        self.is_trading = False
        self.entry_price = 0
        self.current_lot = 0
        self.trade_type = ""
        self.is_recovery_active = False

    def generate_ragnarok_market(self):
        """Menciptakan 1.000 menit pasar paling manipulatif dan berdarah dalam sejarah."""
        prices = [1.08000]
        atrs = []; spreads = []
        
        for i in range(1000):
            # Jebakan Ketenangan Palsu (Setiap 30 menit, pasar tenang memancing bot masuk)
            if i % 30 == 0:
                volatility = random.uniform(-0.0002, 0.0002)
                spread = random.uniform(0.5, 2.5) # Spread mengecoh
            else:
                # RAGNAROK MODE: Harga melompat liar dan gergaji (Whipsaw)
                volatility = random.uniform(-0.0030, 0.0030) # 30 pips lompatan dalam 1 menit!
                spread = random.uniform(5.0, 30.0) # Spread broker panik (5 hingga 30 pips!)
            
            prices.append(prices[-1] + volatility)
            spreads.append(spread)
            atrs.append(abs(volatility) * 10000)

        return pd.DataFrame({'price': prices[1:], 'atr': atrs, 'spread': spreads})

    def run_matrix(self):
        market_data = self.generate_ragnarok_market()
        print(f"📊 {len(market_data)} Menit Sejarah Tergelap Forex Dimulai. Menguji Perisai -$15...\n")
        time.sleep(1)

        for index, row in market_data.iterrows():
            profit_today = self.equity - STARTING_EQUITY
            
            # PERISAI TERAKHIR: MAX DAILY LOSS CHECK
            if profit_today <= -MAX_DAILY_LOSS:
                print(f"\n🛡️ SYSTEM HALT! PERISAI -$15 PECAH! Jarvis Menghentikan Perdagangan!")
                print(f"💀 Hasil: Rugi -${abs(profit_today):.2f}. Tapi Saldo Tuan TERSELAMATKAN: ${self.equity:.2f} (TIDAK MC!)")
                return
                
            if profit_today >= DAILY_PROFIT_TARGET:
                print(f"\n👑 IMPOSSIBLE! Jarvis Mengalahkan Ragnarok! Profit: +${profit_today:.2f} | Saldo Akhir: ${self.equity:.2f}")
                return

            # STATUS: MENCARI MANGSA
            if not self.is_trading:
                # Jarvis tertipu oleh Ketenangan Palsu (Spread <= 3.0)
                if row['spread'] <= 3.0:
                    self.trade_type = random.choice(["BUY", "SELL"])
                    
                    # Chaos Defense Aktif (ATR tinggi, lot otomatis dipotong)
                    self.current_lot = BASE_LOT * 0.5 if row['atr'] > 3.5 else BASE_LOT
                    
                    # 🌋 SIKSAAN 1: MASSIVE SLIPPAGE (Terpeleset 3 hingga 8 Pips!)
                    slippage = random.uniform(3.0, 8.0) / 10000
                    self.entry_price = row['price'] + slippage if self.trade_type == "BUY" else row['price'] - slippage
                    
                    self.is_trading = True
                    self.is_recovery_active = False
                    
                    slippage_pips = slippage * 10000
                    print(f"[{index}] ⚠️ JEBAKAN BROKER! Menembak ({self.trade_type}): Lot {self.current_lot:.2f} | (Slippage Gila: {slippage_pips:.1f} Pips!)")

            # STATUS: BERTAHAN HIDUP DI NERAKA
            else:
                if self.trade_type == "BUY": pips = (row['price'] - self.entry_price) * 10000
                else: pips = (self.entry_price - row['price']) * 10000

                gross_profit = pips * self.current_lot * 10 
                net_profit = gross_profit - (self.current_lot * COMMISSION_FIXED)

                # Coba Keluar jika kebetulan selamat
                if net_profit >= 1.50:
                    self.equity += net_profit
                    print(f"[{index}] 🎯 KEAJAIBAN EXIT ({self.trade_type}): Menang +${net_profit:.2f}. Saldo: ${self.equity:.2f}")
                    self.is_trading = False

                # ZERO LOSS RECOVERY (Disiksa oleh Likuiditas Kosong)
                elif pips <= -4.0 and not self.is_recovery_active:
                    recovery_lot = round(self.current_lot * RECOVERY_FACTOR, 2)
                    print(f"[{index}] 🩸 RAGNAROK (-4 Pips). Membuka Hedging {recovery_lot} Lot!")
                    self.is_recovery_active = True
                    
                    # 🌋 SIKSAAN 2: BIAYA RECOVERY MELEDAK
                    # Karena spread sedang 30 pips, menutup posisi hedging sangat mahal!
                    spread_penalty = random.uniform(2.0, 5.0) # Broker merampok komisi ekstra
                    recovery_cost = -((self.current_lot + recovery_lot) * COMMISSION_FIXED * spread_penalty) 
                    
                    self.equity += recovery_cost
                    print(f"[{index}] 💀 HEDGING HANCUR OLEH SPREAD BROKER! Kerugian Fatal: -${abs(recovery_cost):.2f}. Saldo: ${self.equity:.2f}")
                    self.is_trading = False

        print(f"\n⏱️ Kiamat Selesai. Saldo Akhir: ${self.equity:.2f}")

if __name__ == "__main__":
    matrix = RagnarokSimulator()
    matrix.run_matrix()