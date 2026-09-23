# Lab 01 - Reproducibility log

This file records the commands and results used in the submitted report.

## Environment and source

- Upstream repository: <https://github.com/unreal-kz/lab-01-AI-course>
- Upstream commit: `4ef3eafb077ddbeff3b0232cdb36d4b5502af8ad`
- Python used for this run: `3.12.14`
- Dependencies were installed from the repository's `requirements.txt`.

Setup:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Part 0 - tokenizer counts

Command:

```bash
python3 part0_tokenizers.py
```

Recorded output (token counts):

| Corpus item | Tokenizer | EN | RU | KK | RU/EN | KK/EN |
|---|---|---:|---:|---:|---:|---:|
| sentence | o200k_base | 12 | 18 | 21 | 1.50x | 1.75x |
| sentence | cl100k_base | 12 | 35 | 58 | 2.92x | 4.83x |
| complaint | o200k_base | 59 | 80 | 118 | 1.36x | 2.00x |
| complaint | cl100k_base | 59 | 146 | 265 | 2.47x | 4.49x |
| system_prompt | o200k_base | 40 | 49 | 67 | 1.23x | 1.68x |
| system_prompt | cl100k_base | 40 | 77 | 157 | 1.93x | 3.92x |
| own_complaint | o200k_base | 45 | 55 | 70 | 1.22x | 1.56x |
| own_complaint | cl100k_base | 45 | 94 | 149 | 2.09x | 3.31x |
| kk_shared_letters | o200k_base | 13 | 14 | 16 | 1.08x | 1.23x |
| kk_shared_letters | cl100k_base | 13 | 31 | 30 | 2.38x | 2.31x |
| kk_specific_letters | o200k_base | 12 | 18 | 21 | 1.50x | 1.75x |
| kk_specific_letters | cl100k_base | 13 | 30 | 46 | 2.31x | 3.54x |
| complaint_json | o200k_base | 96 | 115 | 156 | 1.20x | 1.62x |
| complaint_json | cl100k_base | 95 | 184 | 301 | 1.94x | 3.17x |

## Part 1 - offline measurements and prediction

Command:

```bash
python3 part1_offline.py
```

Relevant recorded output:

| Corpus item / language | Characters | UTF-8 bytes | Words | Bytes/character |
|---|---:|---:|---:|---:|
| complaint / EN | 300 | 300 | 54 | 1.00 |
| complaint / RU | 315 | 576 | 45 | 1.83 |
| complaint / KK | 344 | 640 | 42 | 1.86 |
| own_complaint / EN | 213 | 213 | 36 | 1.00 |
| own_complaint / RU | 210 | 379 | 30 | 1.80 |
| own_complaint / KK | 194 | 353 | 25 | 1.82 |
| kk_shared_letters / KK | 49 | 89 | 9 | 1.82 |
| kk_specific_letters / KK | 44 | 81 | 7 | 1.84 |

The pre-measurement heuristic used the complaint's UTF-8 byte ratios:

```text
RU/EN prediction = 576 / 300 = 1.92x
KK/EN prediction = 640 / 300 = 2.13x
```

The official Claude reference measurement for the complaint was:

```text
RU/EN measured = 134 / 92 = 1.46x
KK/EN measured = 198 / 92 = 2.15x
```

## Part 2 - official reference fallback

No classroom/projector API key was available, so `part2_measure.py` was not
called. The fallback explicitly documented in the repository README was used:

```bash
cp measurements.example.json measurements.json
```

The reference file is dated 2026-09-12 and reports Claude Opus 5 request usage:

| Language | Input tokens | Output tokens |
|---|---:|---:|
| EN | 145 | 955 |
| RU | 209 | 1,226 |
| KK | 317 | 1,337 |

These values are the repository's reference measurements, not a new API run.

## Part 3 - annual cost

Command:

```bash
python3 part3_cost.py --requests-per-day 2000
```

Recorded annual cost in US dollars:

| Model | EN | RU | KK |
|---|---:|---:|---:|
| haiku-4.5 | 3,592 | 4,627 | 5,111 |
| sonnet-5 | 7,183 | 9,255 | 10,223 |
| opus-5 | 17,958 | 23,137 | 25,557 |
| fable-5.1 | 35,916 | 46,275 | 51,115 |

For each language and model, the repository script applies:

```text
one request = (input_tokens * input_price + output_tokens * output_price) / 1,000,000
annual cost = one_request * 2,000 * 365
```

The script also reported, for Opus 5:

```text
Input-token ratios: EN 1.00x, RU 1.44x, KK 2.19x
Total-bill ratios:  EN 1.00x, RU 1.29x, KK 1.42x
```

## Core extension checks

1. `OWN_COMPLAINT` was added as a semantically parallel EN/RU/KK support case.
2. The KK version of `KK_SHARED_LETTERS` contains none of the nine
   Kazakh-specific letters. The KK version of `KK_SPECIFIC_LETTERS` contains
   all nine: `ә ғ қ ң ө ұ ү һ і`.
3. Before running Part 0, the predicted direction for `COMPLAINT_JSON` was an
   increase in every language. The measured increases over prose were:

| Tokenizer | EN increase | RU increase | KK increase |
|---|---:|---:|---:|
| o200k_base | +37 | +35 | +38 |
| cl100k_base | +36 | +38 | +36 |

