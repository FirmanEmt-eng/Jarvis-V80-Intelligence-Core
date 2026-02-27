# Jarvis V80: Comprehensive Data Dictionary
> Scale:2.95M+ Synchronized Points | Focus: AI Safety & High-Fidelity Execution

This directory contains samples of the datasets used to train, validate, and audit the Zenith Core framework and its **8-General Ensemble Logic.

---

# 1. Synthetic Market Intelligence (`synthetic_market_sample.csv`)
Used for baseline price action analysis and initial "Danger" metric correlation.

| Column | Description |
| :--- | :--- |
| `Price` | Current market quote (normalized). |
| `Danger` | Proprietary anomaly score based on tick volume and price gaps. |
| `Result` | Success/Failure binary outcome for pattern recognition. |
| `high` / `low` | Periodic extremes for range calculation. |
| `tick_volume` | Real-time market activity density. |

---

# 2. Daily Memory Dataset (`daily_memory_sample.csv`)
The "Feature Space" used for training the 8 Generals. This represents the system's memory of market states.

| Column | Technical Definition | Purpose |
| :--- | :--- | :--- |
| `u_bb` / `l_bb` | Bollinger Bands (Upper/Lower) | Volatility envelope mapping. |
| `macd` | Moving Average Convergence Divergence | Trend momentum identification. |
| `atr` | Average True Range | Noise-to-signal ratio adjustment. |
| `roc` | Rate of Change | Speed of price acceleration. |
| `dist_bb` | Distance to BB Extremes | Market overextension monitoring. |
| `target` | Supervised Label | Ground truth for 97% accuracy training. |

---

# 3. Jarvis Execution Logic (`jarvis_execution_log.csv`)
Real-time audit logs of the AI's decision-making process, highlighting the AI Safety protocols.

| Column | Description |
| :--- | :--- |
| `confidence_score` | Percentage of consensus between the 8 Generals. |
| `signal` | Decision output (BUY/SELL or BLOCKED_BY_DANGER). |
| `danger_count` | Number of risk triggers detected in real-time. |
| `fundamental_bias` | Integration of high-level market sentiment. |

---

# 4. Failure Post-Mortem Logs (`death_log_sample.csv`)
Crucial diagnostic data used for Continuous Learning Loop and Stress Testing.

| Column | Description |
| :--- | :--- |
| `death_reason` | Automated diagnosis of trade failure (e.g., SLAIN_BY_FUNDAMENTAL_STORM). |
| `loss_pips` | Quantitative measure of the prediction error. |
| `market_state` | Contextual environment during the failure (Normal vs. Volatile). |

---
Note: These files are structural samples provided for technical review. The full 2.95M+ production dataset is managed within a private secure environment to maintain IP integrity and operational security.
