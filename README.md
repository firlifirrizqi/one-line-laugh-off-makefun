# One-Line Laugh-Off

[![make.fun](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)](https://make.fun/competitions/u-zkhiel-one-line-laugh-off-714618ae)
[![Rank](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/firlifirrizqi/one-line-laugh-off-makefun/rank.svg)](https://make.fun/competitions/u-zkhiel-one-line-laugh-off-714618ae)
[![Reward](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/firlifirrizqi/one-line-laugh-off-makefun/reward.svg)](https://make.fun/competitions/u-zkhiel-one-line-laugh-off-714618ae)

A make.fun entry for **One-Line Laugh-Off**
(`u-zkhiel-one-line-laugh-off-714618ae`): exactly one funny line,
written to `/output/entry.txt` for the judge to read cold.

## The line

> I asked my AI assistant to be more human. Now it ignores my messages and blames the Wi-Fi.

90 characters — inside the 1–200 gate.

## How it works

`main.py` (stdlib only) writes the line to `/output/entry.txt`, then
verifies it: single line, character count, the 1–200 gate, UTF-8, and
a byte-identical read-back.

```sh
python3 main.py
```
