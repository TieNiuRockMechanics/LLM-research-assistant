# Wiki Log

Record major ingest/update runs here.

- 2026-04-27T18:22:21 - ingested 5 paper records; wrote 40 pages; problems=0

- 2026-04-27T21:09:02 - ingested 43 paper records; wrote 78 pages; problems=0

- 2026-04-27T23:33:25 - ingested 245 paper records; wrote 130 pages; problems=0

- 2026-04-28T00:04:04 - ingested 245 paper records; wrote 180 pages; problems=0

- 2026-04-28T00:36:49 - ingested 245 paper records; wrote 230 pages; problems=0

- 2026-04-28T01:08:10 - ingested 245 paper records; wrote 276 pages; problems=0

- 2026-04-28T01:12:34 - ingested 245 paper records; wrote 279 pages; problems=0

- 2026-04-28T15:29:49 - ingested 10 paper records; wrote 10 pages; problems=0; warnings=71

- 2026-04-28T15:30:22 - ingested 10 paper records; wrote 10 pages; problems=0; warnings=71

- 2026-04-29T20:49:53 - ingested 155 paper records; wrote 155 pages; problems=0; warnings=71

- 2026-04-30T00:39:06 - ingested 255 paper records; wrote 255 pages; problems=0; warnings=71

- 2026-04-30T16:07:12 - ingested 508 paper records; wrote 508 pages; problems=1; warnings=71

- 2026-04-30T17:38:25 - archived 193 old aggregate pages before Pro aggregate rebuild to wiki/.archive/aggregates-manual-clear-20260430-173825


- 2026-04-30T17:45:15 - aggregate: ingest start index=papers aggregate_only=True no_aggregate=False force=False resume=True

- 2026-04-30T17:45:26 - aggregate: loaded index records raw=513

- 2026-04-30T17:45:26 - aggregate: deduplicated records count=508

- 2026-04-30T17:48:42 - aggregate: ingest start index=papers aggregate_only=True no_aggregate=False force=False resume=True

- 2026-04-30T17:48:54 - aggregate: loaded index records raw=513

- 2026-04-30T17:48:54 - aggregate: deduplicated records count=508

- 2026-04-30T17:48:54 - aggregate: loaded paper pages for aggregate count=508 active_ids=508

- 2026-04-30T17:48:55 - aggregate: prepared paper_pages=508 cards=508 batches=10 card_budget=2600 batch_budget=140000 checkpoint=wiki/.staging/aggregate-checkpoints/20260430-174842

- 2026-04-30T17:48:55 - aggregate: start stage=batch aggregation 1/10 final=False cards=54 chars=137510 timeout=300s

- 2026-04-30T17:56:20 - aggregate: response stage=batch aggregation 1/10 elapsed=444.9s raw_chars=40805 usage={'prompt_tokens': 67651, 'completion_tokens': 16326, 'total_tokens': 83977, 'prompt_tokens_details': {'cached_tokens': 67584}, 'completion_tokens_details': {'reasoning_tokens': 498}, 'prompt_cache_hit_tokens': 67584, 'prompt_cache_miss_tokens': 67}

- 2026-04-30T17:56:20 - aggregate: parsed stage=batch aggregation 1/10 counts={'concepts': 19, 'methods': 10, 'claims': 21, 'syntheses': 6, 'open_questions': 5}

- 2026-04-30T17:56:20 - aggregate: saved checkpoint stage=batch aggregation 1/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-001-of-010.json

- 2026-04-30T17:56:20 - aggregate: completed batch 1/10

- 2026-04-30T17:56:20 - aggregate: start stage=batch aggregation 2/10 final=False cards=54 chars=137944 timeout=300s

- 2026-04-30T18:08:37 - aggregate: response stage=batch aggregation 2/10 elapsed=737.6s raw_chars=56210 usage={'prompt_tokens': 67417, 'completion_tokens': 27385, 'total_tokens': 94802, 'prompt_tokens_details': {'cached_tokens': 67328}, 'completion_tokens_details': {'reasoning_tokens': 5693}, 'prompt_cache_hit_tokens': 67328, 'prompt_cache_miss_tokens': 89}

- 2026-04-30T18:08:37 - aggregate: parsed stage=batch aggregation 2/10 counts={'concepts': 19, 'methods': 19, 'claims': 23, 'syntheses': 8, 'open_questions': 9}

- 2026-04-30T18:08:37 - aggregate: saved checkpoint stage=batch aggregation 2/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-002-of-010.json

- 2026-04-30T18:08:37 - aggregate: completed batch 2/10

- 2026-04-30T18:08:37 - aggregate: start stage=batch aggregation 3/10 final=False cards=54 chars=138201 timeout=300s

- 2026-04-30T18:21:37 - aggregate: response stage=batch aggregation 3/10 elapsed=779.5s raw_chars=108535 usage={'prompt_tokens': 65443, 'completion_tokens': 29421, 'total_tokens': 94864, 'prompt_tokens_details': {'cached_tokens': 65408}, 'completion_tokens_details': {'reasoning_tokens': 4282}, 'prompt_cache_hit_tokens': 65408, 'prompt_cache_miss_tokens': 35}

- 2026-04-30T18:21:37 - aggregate: parsed stage=batch aggregation 3/10 counts={'concepts': 20, 'methods': 20, 'claims': 31, 'syntheses': 6, 'open_questions': 10}

- 2026-04-30T18:21:37 - aggregate: saved checkpoint stage=batch aggregation 3/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-003-of-010.json

- 2026-04-30T18:21:37 - aggregate: completed batch 3/10

- 2026-04-30T18:21:37 - aggregate: start stage=batch aggregation 4/10 final=False cards=55 chars=139274 timeout=300s

- 2026-04-30T18:38:00 - aggregate: response stage=batch aggregation 4/10 elapsed=982.9s raw_chars=68274 usage={'prompt_tokens': 65806, 'completion_tokens': 32512, 'total_tokens': 98318, 'prompt_tokens_details': {'cached_tokens': 65792}, 'completion_tokens_details': {'reasoning_tokens': 6552}, 'prompt_cache_hit_tokens': 65792, 'prompt_cache_miss_tokens': 14}

- 2026-04-30T18:38:00 - aggregate: failed stage=batch aggregation 4/10 elapsed=982.9s error=Expecting ',' delimiter: line 738 column 128 (char 43434)

- 2026-04-30T18:43:37 - aggregate: ingest start index=papers aggregate_only=True no_aggregate=False force=False resume=True

- 2026-04-30T18:43:49 - aggregate: loaded index records raw=513

- 2026-04-30T18:43:49 - aggregate: deduplicated records count=508

- 2026-04-30T18:43:49 - aggregate: loaded paper pages for aggregate count=508 active_ids=508

- 2026-04-30T18:43:50 - aggregate: prepared paper_pages=508 cards=508 batches=10 card_budget=2600 batch_budget=140000 checkpoint=wiki/.staging/aggregate-checkpoints/20260430-174842

- 2026-04-30T18:43:50 - aggregate: reuse checkpoint stage=batch aggregation 1/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-001-of-010.json counts={'concepts': 19, 'methods': 10, 'claims': 21, 'syntheses': 6, 'open_questions': 5}

- 2026-04-30T18:43:50 - aggregate: completed batch 1/10

- 2026-04-30T18:43:50 - aggregate: reuse checkpoint stage=batch aggregation 2/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-002-of-010.json counts={'concepts': 19, 'methods': 19, 'claims': 23, 'syntheses': 8, 'open_questions': 9}

- 2026-04-30T18:43:50 - aggregate: completed batch 2/10

- 2026-04-30T18:43:50 - aggregate: reuse checkpoint stage=batch aggregation 3/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-003-of-010.json counts={'concepts': 20, 'methods': 20, 'claims': 31, 'syntheses': 6, 'open_questions': 10}

- 2026-04-30T18:43:50 - aggregate: completed batch 3/10

- 2026-04-30T18:43:50 - aggregate: start stage=batch aggregation 4/10 final=False cards=55 chars=139274 timeout=300s

- 2026-04-30T18:57:19 - aggregate: response stage=batch aggregation 4/10 elapsed=809.1s raw_chars=89334 usage={'prompt_tokens': 65806, 'completion_tokens': 26744, 'total_tokens': 92550, 'prompt_tokens_details': {'cached_tokens': 65792}, 'completion_tokens_details': {'reasoning_tokens': 6186}, 'prompt_cache_hit_tokens': 65792, 'prompt_cache_miss_tokens': 14}

- 2026-04-30T18:57:19 - aggregate: saved raw response stage=batch aggregation 4/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-004-of-010.json.raw.txt

- 2026-04-30T18:57:19 - aggregate: parsed stage=batch aggregation 4/10 counts={'concepts': 20, 'methods': 18, 'claims': 31, 'syntheses': 3, 'open_questions': 5}

- 2026-04-30T18:57:19 - aggregate: saved checkpoint stage=batch aggregation 4/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-004-of-010.json

- 2026-04-30T18:57:19 - aggregate: completed batch 4/10

- 2026-04-30T18:57:19 - aggregate: start stage=batch aggregation 5/10 final=False cards=54 chars=138632 timeout=300s

- 2026-04-30T19:10:42 - aggregate: response stage=batch aggregation 5/10 elapsed=802.2s raw_chars=58553 usage={'prompt_tokens': 67892, 'completion_tokens': 26857, 'total_tokens': 94749, 'prompt_tokens_details': {'cached_tokens': 67840}, 'completion_tokens_details': {'reasoning_tokens': 5453}, 'prompt_cache_hit_tokens': 67840, 'prompt_cache_miss_tokens': 52}

- 2026-04-30T19:10:42 - aggregate: saved raw response stage=batch aggregation 5/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-005-of-010.json.raw.txt

- 2026-04-30T19:10:42 - aggregate: parsed stage=batch aggregation 5/10 counts={'concepts': 18, 'methods': 18, 'claims': 33, 'syntheses': 6, 'open_questions': 8}

- 2026-04-30T19:10:42 - aggregate: saved checkpoint stage=batch aggregation 5/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-005-of-010.json

- 2026-04-30T19:10:42 - aggregate: completed batch 5/10

- 2026-04-30T19:10:42 - aggregate: start stage=batch aggregation 6/10 final=False cards=54 chars=137821 timeout=300s

- 2026-04-30T19:24:11 - aggregate: response stage=batch aggregation 6/10 elapsed=809.2s raw_chars=55387 usage={'prompt_tokens': 65583, 'completion_tokens': 26831, 'total_tokens': 92414, 'prompt_tokens_details': {'cached_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 6223}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 65583}

- 2026-04-30T19:24:11 - aggregate: saved raw response stage=batch aggregation 6/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-006-of-010.json.raw.txt

- 2026-04-30T19:24:11 - aggregate: parsed stage=batch aggregation 6/10 counts={'concepts': 16, 'methods': 20, 'claims': 29, 'syntheses': 6, 'open_questions': 7}

- 2026-04-30T19:24:11 - aggregate: saved checkpoint stage=batch aggregation 6/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-006-of-010.json

- 2026-04-30T19:24:11 - aggregate: completed batch 6/10

- 2026-04-30T19:24:11 - aggregate: start stage=batch aggregation 7/10 final=False cards=54 chars=137948 timeout=300s

- 2026-04-30T19:31:41 - aggregate: response stage=batch aggregation 7/10 elapsed=450.5s raw_chars=29913 usage={'prompt_tokens': 64163, 'completion_tokens': 17320, 'total_tokens': 81483, 'prompt_tokens_details': {'cached_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 6340}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 64163}

- 2026-04-30T19:31:41 - aggregate: saved raw response stage=batch aggregation 7/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-007-of-010.json.raw.txt

- 2026-04-30T19:31:41 - aggregate: parsed stage=batch aggregation 7/10 counts={'concepts': 12, 'methods': 12, 'claims': 14, 'syntheses': 3, 'open_questions': 4}

- 2026-04-30T19:31:41 - aggregate: saved checkpoint stage=batch aggregation 7/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-007-of-010.json

- 2026-04-30T19:31:41 - aggregate: completed batch 7/10

- 2026-04-30T19:31:41 - aggregate: start stage=batch aggregation 8/10 final=False cards=54 chars=137878 timeout=300s

- 2026-04-30T19:42:26 - aggregate: response stage=batch aggregation 8/10 elapsed=644.7s raw_chars=52109 usage={'prompt_tokens': 65084, 'completion_tokens': 24307, 'total_tokens': 89391, 'prompt_tokens_details': {'cached_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 4003}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 65084}

- 2026-04-30T19:42:26 - aggregate: saved raw response stage=batch aggregation 8/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-008-of-010.json.raw.txt

- 2026-04-30T19:42:26 - aggregate: parsed stage=batch aggregation 8/10 counts={'concepts': 20, 'methods': 19, 'claims': 34, 'syntheses': 12, 'open_questions': 10}

- 2026-04-30T19:42:26 - aggregate: saved checkpoint stage=batch aggregation 8/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-008-of-010.json

- 2026-04-30T19:42:26 - aggregate: completed batch 8/10

- 2026-04-30T19:42:26 - aggregate: start stage=batch aggregation 9/10 final=False cards=54 chars=138167 timeout=300s

- 2026-04-30T19:53:28 - aggregate: response stage=batch aggregation 9/10 elapsed=662.0s raw_chars=86067 usage={'prompt_tokens': 67644, 'completion_tokens': 21442, 'total_tokens': 89086, 'prompt_tokens_details': {'cached_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 1170}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 67644}

- 2026-04-30T19:53:28 - aggregate: saved raw response stage=batch aggregation 9/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-009-of-010.json.raw.txt

- 2026-04-30T19:53:28 - aggregate: parsed stage=batch aggregation 9/10 counts={'concepts': 20, 'methods': 18, 'claims': 19, 'syntheses': 4, 'open_questions': 7}

- 2026-04-30T19:53:28 - aggregate: saved checkpoint stage=batch aggregation 9/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-009-of-010.json

- 2026-04-30T19:53:28 - aggregate: completed batch 9/10

- 2026-04-30T19:53:28 - aggregate: start stage=batch aggregation 10/10 final=False cards=21 chars=53563 timeout=300s

- 2026-04-30T20:05:20 - aggregate: response stage=batch aggregation 10/10 elapsed=712.5s raw_chars=49268 usage={'prompt_tokens': 25837, 'completion_tokens': 23293, 'total_tokens': 49130, 'prompt_tokens_details': {'cached_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 4469}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 25837}

- 2026-04-30T20:05:20 - aggregate: saved raw response stage=batch aggregation 10/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-010-of-010.json.raw.txt

- 2026-04-30T20:05:20 - aggregate: parsed stage=batch aggregation 10/10 counts={'concepts': 20, 'methods': 20, 'claims': 23, 'syntheses': 6, 'open_questions': 9}

- 2026-04-30T20:05:20 - aggregate: saved checkpoint stage=batch aggregation 10/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-010-of-010.json

- 2026-04-30T20:05:20 - aggregate: completed batch 10/10

- 2026-04-30T20:05:21 - aggregate: start stage=final merge and deduplication final=True cards=1 chars=140000 timeout=300s

- 2026-04-30T20:28:21 - aggregate: ingest start index=papers aggregate_only=True no_aggregate=False force=False resume=True

- 2026-04-30T20:28:33 - aggregate: loaded index records raw=513

- 2026-04-30T20:28:33 - aggregate: deduplicated records count=508

- 2026-04-30T20:28:34 - aggregate: loaded paper pages for aggregate count=508 active_ids=508

- 2026-04-30T20:28:34 - aggregate: prepared paper_pages=508 cards=508 batches=10 card_budget=2600 batch_budget=140000 checkpoint=wiki/.staging/aggregate-checkpoints/20260430-174842

- 2026-04-30T20:28:34 - aggregate: reuse checkpoint stage=batch aggregation 1/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-001-of-010.json counts={'concepts': 19, 'methods': 10, 'claims': 21, 'syntheses': 6, 'open_questions': 5}

- 2026-04-30T20:28:34 - aggregate: completed batch 1/10

- 2026-04-30T20:28:34 - aggregate: reuse checkpoint stage=batch aggregation 2/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-002-of-010.json counts={'concepts': 19, 'methods': 19, 'claims': 23, 'syntheses': 8, 'open_questions': 9}

- 2026-04-30T20:28:34 - aggregate: completed batch 2/10

- 2026-04-30T20:28:34 - aggregate: reuse checkpoint stage=batch aggregation 3/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-003-of-010.json counts={'concepts': 20, 'methods': 20, 'claims': 31, 'syntheses': 6, 'open_questions': 10}

- 2026-04-30T20:28:34 - aggregate: completed batch 3/10

- 2026-04-30T20:28:34 - aggregate: reuse checkpoint stage=batch aggregation 4/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-004-of-010.json counts={'concepts': 20, 'methods': 18, 'claims': 31, 'syntheses': 3, 'open_questions': 5}

- 2026-04-30T20:28:35 - aggregate: completed batch 4/10

- 2026-04-30T20:28:35 - aggregate: reuse checkpoint stage=batch aggregation 5/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-005-of-010.json counts={'concepts': 18, 'methods': 18, 'claims': 33, 'syntheses': 6, 'open_questions': 8}

- 2026-04-30T20:28:35 - aggregate: completed batch 5/10

- 2026-04-30T20:28:35 - aggregate: reuse checkpoint stage=batch aggregation 6/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-006-of-010.json counts={'concepts': 16, 'methods': 20, 'claims': 29, 'syntheses': 6, 'open_questions': 7}

- 2026-04-30T20:28:35 - aggregate: completed batch 6/10

- 2026-04-30T20:28:35 - aggregate: reuse checkpoint stage=batch aggregation 7/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-007-of-010.json counts={'concepts': 12, 'methods': 12, 'claims': 14, 'syntheses': 3, 'open_questions': 4}

- 2026-04-30T20:28:35 - aggregate: completed batch 7/10

- 2026-04-30T20:28:35 - aggregate: reuse checkpoint stage=batch aggregation 8/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-008-of-010.json counts={'concepts': 20, 'methods': 19, 'claims': 34, 'syntheses': 12, 'open_questions': 10}

- 2026-04-30T20:28:35 - aggregate: completed batch 8/10

- 2026-04-30T20:28:35 - aggregate: reuse checkpoint stage=batch aggregation 9/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-009-of-010.json counts={'concepts': 20, 'methods': 18, 'claims': 19, 'syntheses': 4, 'open_questions': 7}

- 2026-04-30T20:28:35 - aggregate: completed batch 9/10

- 2026-04-30T20:28:35 - aggregate: reuse checkpoint stage=batch aggregation 10/10 path=wiki/.staging/aggregate-checkpoints/20260430-174842/batch-010-of-010.json counts={'concepts': 20, 'methods': 20, 'claims': 23, 'syntheses': 6, 'open_questions': 9}

- 2026-04-30T20:28:35 - aggregate: completed batch 10/10

- 2026-04-30T20:28:35 - aggregate: merge input partials=10 chars=684857 merge_budget=140000

- 2026-04-30T20:28:35 - aggregate: merge round 1 chunks=7 input_chars=684857 merge_budget=140000

- 2026-04-30T20:28:35 - aggregate: start stage=merge round 1 batch 1/7 final=False cards=2 chars=109972 timeout=300s

- 2026-04-30T21:20:23 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=False force=False resume=True

- 2026-04-30T21:20:36 - aggregate: loaded index records raw=513

- 2026-04-30T21:20:36 - aggregate: deduplicated records count=508

- 2026-04-30T21:20:36 - aggregate: applied limit=3 remaining=3

- 2026-04-30T21:54:58 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=False force=False resume=True

- 2026-04-30T21:55:10 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-04-30T21:55:10 - aggregate: indexed records with unknown Zotero item type kept for review: 3

- 2026-04-30T21:55:10 - aggregate: loaded index records raw=492

- 2026-04-30T21:55:10 - aggregate: deduplicated records count=487

- 2026-04-30T21:55:10 - aggregate: applied limit=10 remaining=10

- 2026-04-30T21:55:42 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=True resume=True

- 2026-04-30T21:55:54 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-04-30T21:55:54 - aggregate: indexed records with unknown Zotero item type kept for review: 3

- 2026-04-30T21:55:54 - aggregate: loaded index records raw=492

- 2026-04-30T21:55:54 - aggregate: deduplicated records count=487

- 2026-04-30T21:55:54 - aggregate: applied limit=10 remaining=10

- 2026-04-30T23:01:50 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=False force=False resume=True run_id=20260430-230150

- 2026-04-30T23:02:06 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-04-30T23:02:06 - aggregate: indexed records with unknown Zotero item type kept for review: 3

- 2026-04-30T23:02:06 - aggregate: loaded index records raw=492

- 2026-04-30T23:02:06 - aggregate: deduplicated records count=487

- 2026-04-30T23:02:06 - aggregate: applied limit=10 remaining=10

- 2026-04-30T23:06:11 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=True resume=True run_id=paper-pro-smoke

- 2026-04-30T23:06:27 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-04-30T23:06:27 - aggregate: indexed records with unknown Zotero item type kept for review: 3

- 2026-04-30T23:06:27 - aggregate: loaded index records raw=492

- 2026-04-30T23:06:27 - aggregate: deduplicated records count=487

- 2026-04-30T23:06:27 - aggregate: applied limit=1 remaining=1

- 2026-04-30T23:22:34 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=True resume=True run_id=paper-pro-debug-20260430-232233

- 2026-05-01T10:20:21 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=True resume=True run_id=paper-pro-smoke-v4-20260501-1020

- 2026-05-01T10:20:33 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-01T10:20:33 - aggregate: indexed records with unknown Zotero item type kept for review: 3

- 2026-05-01T10:20:33 - aggregate: loaded index records raw=492

- 2026-05-01T10:20:33 - aggregate: deduplicated records count=487

- 2026-05-01T10:20:33 - aggregate: applied limit=1 remaining=1

- 2026-05-01T10:24:36 - ingested 1 paper records; wrote 1 pages; skipped_over_budget=0; failed=0; problems=1; warnings=0

- 2026-05-01T10:35:45 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260501-103545

- 2026-05-01T10:36:01 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-01T10:36:01 - aggregate: indexed records with unknown Zotero item type kept for review: 3

- 2026-05-01T10:36:01 - aggregate: loaded index records raw=492

- 2026-05-01T10:36:01 - aggregate: deduplicated records count=487

- 2026-05-01T10:36:01 - aggregate: applied limit=3 remaining=3

- 2026-05-01T10:39:09 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=foreground-dryrun-debug

- 2026-05-01T10:39:21 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-01T10:39:21 - aggregate: indexed records with unknown Zotero item type kept for review: 3

- 2026-05-01T10:39:21 - aggregate: loaded index records raw=492

- 2026-05-01T10:39:21 - aggregate: deduplicated records count=487

- 2026-05-01T10:39:21 - aggregate: applied limit=1 remaining=1

- 2026-05-01T10:39:44 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=start-process-dryrun-debug

- 2026-05-01T10:39:56 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-01T10:39:56 - aggregate: indexed records with unknown Zotero item type kept for review: 3

- 2026-05-01T10:39:56 - aggregate: loaded index records raw=492

- 2026-05-01T10:39:56 - aggregate: deduplicated records count=487

- 2026-05-01T10:39:56 - aggregate: applied limit=1 remaining=1

- 2026-05-01T10:40:23 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=True resume=True run_id=start-process-limit1-debug-104023

- 2026-05-01T10:40:35 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-01T10:40:35 - aggregate: indexed records with unknown Zotero item type kept for review: 3

- 2026-05-01T10:40:35 - aggregate: loaded index records raw=492

- 2026-05-01T10:40:35 - aggregate: deduplicated records count=487

- 2026-05-01T10:40:35 - aggregate: applied limit=1 remaining=1

- 2026-05-01T10:40:35 - ingested 1 paper records; wrote 1 pages; skipped_over_budget=0; failed=0; problems=0; warnings=0

- 2026-05-01T10:42:57 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=start-process-dryrun-full-104256

- 2026-05-01T10:43:09 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-01T10:43:09 - aggregate: indexed records with unknown Zotero item type kept for review: 3

- 2026-05-01T10:43:09 - aggregate: loaded index records raw=492

- 2026-05-01T10:43:09 - aggregate: deduplicated records count=487

- 2026-05-01T10:44:16 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=True resume=True run_id=paper-pro-20260501-104416

- 2026-05-01T10:44:29 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-01T10:44:29 - aggregate: indexed records with unknown Zotero item type kept for review: 3

- 2026-05-01T10:44:29 - aggregate: loaded index records raw=492

- 2026-05-01T10:44:29 - aggregate: deduplicated records count=487

- 2026-05-01T17:56:55 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=True resume=True run_id=paper-pro-resume-20260501-175654

- 2026-05-01T17:57:14 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-01T17:57:14 - aggregate: indexed records with unknown Zotero item type kept for review: 3

- 2026-05-01T17:57:14 - aggregate: loaded index records raw=492

- 2026-05-01T17:57:14 - aggregate: deduplicated records count=487

- 2026-05-01T22:44:47 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=True resume=True run_id=paper-pro-resume-20260501-224447

- 2026-05-01T22:45:06 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-01T22:45:06 - aggregate: indexed records with unknown Zotero item type kept for review: 3

- 2026-05-01T22:45:06 - aggregate: loaded index records raw=492

- 2026-05-01T22:45:06 - aggregate: deduplicated records count=487

- 2026-05-02T00:22:11 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=True resume=True run_id=paper-pro-resume-20260502-002211

- 2026-05-02T00:22:30 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-02T00:22:30 - aggregate: indexed records with unknown Zotero item type kept for review: 3

- 2026-05-02T00:22:30 - aggregate: loaded index records raw=492

- 2026-05-02T00:22:30 - aggregate: deduplicated records count=487

- 2026-05-02T01:13:37 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=True resume=True run_id=paper-pro-resume-20260502-011337

- 2026-05-02T01:13:50 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-02T01:13:50 - aggregate: indexed records with unknown Zotero item type kept for review: 3

- 2026-05-02T01:13:50 - aggregate: loaded index records raw=492

- 2026-05-02T01:13:50 - aggregate: deduplicated records count=487

- 2026-05-02T03:14:21 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=True resume=True run_id=20260502-031421 shard=0/2

- 2026-05-02T03:14:21 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=True resume=True run_id=20260502-031421 shard=1/2

- 2026-05-02T03:14:39 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-02T03:14:39 - aggregate: indexed records with unknown Zotero item type kept for review: 3

- 2026-05-02T03:14:39 - aggregate: loaded index records raw=492

- 2026-05-02T03:14:39 - aggregate: deduplicated records count=487

- 2026-05-02T03:14:39 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-02T03:14:39 - aggregate: indexed records with unknown Zotero item type kept for review: 3

- 2026-05-02T03:14:39 - aggregate: applied limit=10 remaining=10

- 2026-05-02T03:14:39 - aggregate: applied shard index=0 count=2 global_records=10 shard_records=5

- 2026-05-02T03:14:39 - aggregate: loaded index records raw=492

- 2026-05-02T03:14:39 - aggregate: deduplicated records count=487

- 2026-05-02T03:14:39 - aggregate: applied limit=10 remaining=10

- 2026-05-02T03:14:39 - aggregate: applied shard index=1 count=2 global_records=10 shard_records=5

- 2026-05-02T03:18:17 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=True resume=True run_id=test-shard-syntax-shard0-of-2 shard=0/2

- 2026-05-02T03:20:48 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=True resume=True run_id=paper-pro-sharded-manual-20260502-shard0-of-2 shard=0/2

- 2026-05-02T03:21:01 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-02T03:21:01 - aggregate: indexed records with unknown Zotero item type kept for review: 3

- 2026-05-02T03:21:01 - aggregate: loaded index records raw=492

- 2026-05-02T03:21:01 - aggregate: deduplicated records count=487

- 2026-05-02T03:21:01 - aggregate: applied shard index=0 count=2 global_records=487 shard_records=244

- 2026-05-02T03:21:14 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=True resume=True run_id=paper-pro-sharded-manual-20260502-shard1-of-2 shard=1/2

- 2026-05-02T03:21:26 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-02T03:21:26 - aggregate: indexed records with unknown Zotero item type kept for review: 3

- 2026-05-02T03:21:26 - aggregate: loaded index records raw=492

- 2026-05-02T03:21:26 - aggregate: deduplicated records count=487

- 2026-05-02T03:21:26 - aggregate: applied shard index=1 count=2 global_records=487 shard_records=243

- 2026-05-02T08:35:21 - ingested 244 paper records; wrote 244 pages; skipped_over_budget=0; failed=0; problems=0; warnings=0

- 2026-05-02T08:57:34 - ingested 243 paper records; wrote 242 pages; skipped_over_budget=1; failed=0; problems=0; warnings=0

- 2026-05-02T09:15:39 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=True resume=True run_id=paper-pro-repair-20260502 shard=0/1

- 2026-05-02T09:16:01 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-02T09:16:01 - aggregate: indexed records with unknown Zotero item type kept for review: 3

- 2026-05-02T09:16:01 - aggregate: loaded index records raw=492

- 2026-05-02T09:16:01 - aggregate: deduplicated records count=487

- 2026-05-02T09:28:14 - ingested 487 paper records; wrote 487 pages; skipped_over_budget=0; failed=0; problems=0; warnings=0

- 2026-05-02T10:16:40 - aggregate: ingest start index=papers aggregate_only=True no_aggregate=False force=False resume=True run_id=20260502-101640 shard=0/1

- 2026-05-02T10:16:53 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-02T10:16:53 - aggregate: indexed records with unknown Zotero item type kept for review: 3

- 2026-05-02T10:16:53 - aggregate: loaded index records raw=492

- 2026-05-02T10:16:53 - aggregate: deduplicated records count=487

- 2026-05-02T10:16:54 - aggregate: loaded paper pages for aggregate count=487 complete_ids=487 over_budget_skips=0

- 2026-05-02T10:16:57 - aggregate: prepared paper_pages=487 cards=487 batches=7 card_budget=70000 batch_budget=700000 checkpoint=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502

- 2026-05-02T10:16:57 - aggregate: start stage=batch aggregation 1/7 final=False cards=70 chars=692638 timeout=1800s

- 2026-05-02T10:25:20 - aggregate: response stage=batch aggregation 1/7 elapsed=503.0s raw_chars=39353 usage={'prompt_tokens': 269822, 'completion_tokens': 20048, 'total_tokens': 289870, 'prompt_tokens_details': {'cached_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 5447}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 269822}

- 2026-05-02T10:25:20 - aggregate: saved raw response stage=batch aggregation 1/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-001-of-007.json.raw.txt

- 2026-05-02T10:25:20 - aggregate: parsed stage=batch aggregation 1/7 counts={'concepts': 14, 'methods': 8, 'claims': 30, 'syntheses': 3, 'open_questions': 4}

- 2026-05-02T10:25:20 - aggregate: saved checkpoint stage=batch aggregation 1/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-001-of-007.json

- 2026-05-02T10:25:20 - aggregate: completed batch 1/7

- 2026-05-02T10:25:20 - aggregate: start stage=batch aggregation 2/7 final=False cards=66 chars=699210 timeout=1800s

- 2026-05-02T10:46:47 - aggregate: response stage=batch aggregation 2/7 elapsed=1287.0s raw_chars=123578 usage={'prompt_tokens': 271262, 'completion_tokens': 49984, 'total_tokens': 321246, 'prompt_tokens_details': {'cached_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 694}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 271262}

- 2026-05-02T10:46:47 - aggregate: saved raw response stage=batch aggregation 2/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-002-of-007.json.raw.txt

- 2026-05-02T10:46:47 - aggregate: parsed stage=batch aggregation 2/7 counts={'concepts': 41, 'methods': 37, 'claims': 41, 'syntheses': 6, 'open_questions': 8}

- 2026-05-02T10:46:47 - aggregate: saved checkpoint stage=batch aggregation 2/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-002-of-007.json

- 2026-05-02T10:46:47 - aggregate: completed batch 2/7

- 2026-05-02T10:46:47 - aggregate: start stage=batch aggregation 3/7 final=False cards=84 chars=696546 timeout=1800s

- 2026-05-02T10:57:50 - aggregate: response stage=batch aggregation 3/7 elapsed=663.9s raw_chars=41506 usage={'prompt_tokens': 323784, 'completion_tokens': 21653, 'total_tokens': 345437, 'prompt_tokens_details': {'cached_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 6706}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 323784}

- 2026-05-02T10:57:50 - aggregate: saved raw response stage=batch aggregation 3/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-003-of-007.json.raw.txt

- 2026-05-02T10:57:50 - aggregate: parsed stage=batch aggregation 3/7 counts={'concepts': 25, 'methods': 19, 'claims': 10, 'syntheses': 3, 'open_questions': 4}

- 2026-05-02T10:57:50 - aggregate: saved checkpoint stage=batch aggregation 3/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-003-of-007.json

- 2026-05-02T10:57:50 - aggregate: completed batch 3/7

- 2026-05-02T10:57:50 - aggregate: start stage=batch aggregation 4/7 final=False cards=91 chars=694085 timeout=1800s

- 2026-05-02T11:05:11 - aggregate: response stage=batch aggregation 4/7 elapsed=440.1s raw_chars=33837 usage={'prompt_tokens': 351781, 'completion_tokens': 14681, 'total_tokens': 366462, 'prompt_tokens_details': {'cached_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 1911}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 351781}

- 2026-05-02T11:05:11 - aggregate: saved raw response stage=batch aggregation 4/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-004-of-007.json.raw.txt

- 2026-05-02T11:05:11 - aggregate: parsed stage=batch aggregation 4/7 counts={'concepts': 14, 'methods': 7, 'claims': 10, 'syntheses': 5, 'open_questions': 6}

- 2026-05-02T11:05:11 - aggregate: saved checkpoint stage=batch aggregation 4/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-004-of-007.json

- 2026-05-02T11:05:11 - aggregate: completed batch 4/7

- 2026-05-02T11:05:11 - aggregate: start stage=batch aggregation 5/7 final=False cards=82 chars=694376 timeout=1800s

- 2026-05-02T11:13:49 - aggregate: response stage=batch aggregation 5/7 elapsed=518.4s raw_chars=42508 usage={'prompt_tokens': 318249, 'completion_tokens': 18289, 'total_tokens': 336538, 'prompt_tokens_details': {'cached_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 688}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 318249}

- 2026-05-02T11:13:49 - aggregate: saved raw response stage=batch aggregation 5/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-005-of-007.json.raw.txt

- 2026-05-02T11:13:49 - aggregate: parsed stage=batch aggregation 5/7 counts={'concepts': 20, 'methods': 13, 'claims': 20, 'syntheses': 4, 'open_questions': 3}

- 2026-05-02T11:13:49 - aggregate: saved checkpoint stage=batch aggregation 5/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-005-of-007.json

- 2026-05-02T11:13:49 - aggregate: completed batch 5/7

- 2026-05-02T11:13:49 - aggregate: start stage=batch aggregation 6/7 final=False cards=83 chars=699052 timeout=1800s

- 2026-05-02T11:23:23 - aggregate: response stage=batch aggregation 6/7 elapsed=573.9s raw_chars=44564 usage={'prompt_tokens': 330719, 'completion_tokens': 20814, 'total_tokens': 351533, 'prompt_tokens_details': {'cached_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 4363}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 330719}

- 2026-05-02T11:23:23 - aggregate: saved raw response stage=batch aggregation 6/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-006-of-007.json.raw.txt

- 2026-05-02T11:23:23 - aggregate: parsed stage=batch aggregation 6/7 counts={'concepts': 22, 'methods': 15, 'claims': 10, 'syntheses': 6, 'open_questions': 7}

- 2026-05-02T11:23:23 - aggregate: saved checkpoint stage=batch aggregation 6/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-006-of-007.json

- 2026-05-02T11:23:23 - aggregate: completed batch 6/7

- 2026-05-02T11:23:23 - aggregate: start stage=batch aggregation 7/7 final=False cards=11 chars=91212 timeout=1800s

- 2026-05-02T11:46:01 - aggregate: response stage=batch aggregation 7/7 elapsed=1358.5s raw_chars=116926 usage={'prompt_tokens': 45593, 'completion_tokens': 44942, 'total_tokens': 90535, 'prompt_tokens_details': {'cached_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 4359}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 45593}

- 2026-05-02T11:46:01 - aggregate: saved raw response stage=batch aggregation 7/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-007-of-007.json.raw.txt

- 2026-05-02T11:46:01 - aggregate: parsed stage=batch aggregation 7/7 counts={'concepts': 78, 'methods': 48, 'claims': 40, 'syntheses': 4, 'open_questions': 9}

- 2026-05-02T11:46:01 - aggregate: saved checkpoint stage=batch aggregation 7/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-007-of-007.json

- 2026-05-02T11:46:01 - aggregate: completed batch 7/7

- 2026-05-02T11:46:01 - aggregate: merge input partials=7 chars=470034 merge_budget=700000

- 2026-05-02T11:46:01 - aggregate: final merge input cards=7 chars=470034 merge_budget=700000

- 2026-05-02T11:46:01 - aggregate: start stage=final merge and deduplication final=True cards=7 chars=470034 timeout=1800s

- 2026-05-02T12:16:23 - aggregate: response stage=final merge and deduplication elapsed=1821.0s raw_chars=187360 usage={'prompt_tokens': 172900, 'completion_tokens': 65536, 'total_tokens': 238436, 'prompt_tokens_details': {'cached_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 2155}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 172900}

- 2026-05-02T12:16:23 - aggregate: saved raw response stage=final merge and deduplication path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/final-merge.json.raw.txt

- 2026-05-02T12:16:23 - aggregate: parse failed stage=final merge and deduplication; attempting json repair error=Expecting ',' delimiter: line 5465 column 6 (char 187034)

- 2026-05-02T12:43:35 - aggregate: failed stage=final merge and deduplication elapsed=3453.1s error=Expecting ',' delimiter: line 3146 column 6 (char 109222)

- 2026-05-02T13:25:58 - aggregate: ingest start index=papers aggregate_only=True no_aggregate=False force=False resume=True run_id=20260502-132558 shard=0/1

- 2026-05-02T13:26:17 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-02T13:26:17 - aggregate: indexed records with unknown Zotero item type kept for review: 3

- 2026-05-02T13:26:17 - aggregate: loaded index records raw=492

- 2026-05-02T13:26:17 - aggregate: deduplicated records count=487

- 2026-05-02T13:26:21 - aggregate: loaded paper pages for aggregate count=487 complete_ids=487 over_budget_skips=0

- 2026-05-02T13:26:24 - aggregate: prepared paper_pages=487 cards=487 batches=7 card_budget=70000 batch_budget=700000 checkpoint=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502

- 2026-05-02T13:26:24 - aggregate: reuse checkpoint stage=batch aggregation 1/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-001-of-007.json counts={'concepts': 14, 'methods': 8, 'claims': 30, 'syntheses': 3, 'open_questions': 4}

- 2026-05-02T13:26:24 - aggregate: completed batch 1/7

- 2026-05-02T13:26:24 - aggregate: reuse checkpoint stage=batch aggregation 2/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-002-of-007.json counts={'concepts': 41, 'methods': 37, 'claims': 41, 'syntheses': 6, 'open_questions': 8}

- 2026-05-02T13:26:24 - aggregate: completed batch 2/7

- 2026-05-02T13:26:24 - aggregate: reuse checkpoint stage=batch aggregation 3/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-003-of-007.json counts={'concepts': 25, 'methods': 19, 'claims': 10, 'syntheses': 3, 'open_questions': 4}

- 2026-05-02T13:26:24 - aggregate: completed batch 3/7

- 2026-05-02T13:26:24 - aggregate: reuse checkpoint stage=batch aggregation 4/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-004-of-007.json counts={'concepts': 14, 'methods': 7, 'claims': 10, 'syntheses': 5, 'open_questions': 6}

- 2026-05-02T13:26:24 - aggregate: completed batch 4/7

- 2026-05-02T13:26:24 - aggregate: reuse checkpoint stage=batch aggregation 5/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-005-of-007.json counts={'concepts': 20, 'methods': 13, 'claims': 20, 'syntheses': 4, 'open_questions': 3}

- 2026-05-02T13:26:24 - aggregate: completed batch 5/7

- 2026-05-02T13:26:24 - aggregate: reuse checkpoint stage=batch aggregation 6/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-006-of-007.json counts={'concepts': 22, 'methods': 15, 'claims': 10, 'syntheses': 6, 'open_questions': 7}

- 2026-05-02T13:26:24 - aggregate: completed batch 6/7

- 2026-05-02T13:26:24 - aggregate: reuse checkpoint stage=batch aggregation 7/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-007-of-007.json counts={'concepts': 78, 'methods': 48, 'claims': 40, 'syntheses': 4, 'open_questions': 9}

- 2026-05-02T13:26:24 - aggregate: completed batch 7/7

- 2026-05-02T13:26:24 - aggregate: category final merge start partials=7 counts={'concepts': 214, 'methods': 147, 'claims': 161, 'syntheses': 31, 'open_questions': 41}

- 2026-05-02T13:26:24 - aggregate: category merge input category=concepts partials=7 chars=151537 merge_budget=700000

- 2026-05-02T13:26:24 - aggregate: category final merge input category=concepts cards=7 chars=151537 merge_budget=700000

- 2026-05-02T13:26:24 - aggregate: start stage=final concepts merge and deduplication category=concepts final=True cards=7 chars=151537 timeout=1800s thinking=True reasoning_effort=max max_tokens=65536

- 2026-05-02T13:48:06 - aggregate: response stage=final concepts merge and deduplication category=concepts elapsed=1301.9s raw_chars=112690 usage={'prompt_tokens': 49918, 'completion_tokens': 53371, 'total_tokens': 103289, 'prompt_tokens_details': {'cached_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 18652}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 49918}

- 2026-05-02T13:48:06 - aggregate: saved raw response stage=final concepts merge and deduplication category=concepts path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/final-concepts.json.raw.txt

- 2026-05-02T13:48:06 - aggregate: parsed stage=final concepts merge and deduplication category=concepts count=131

- 2026-05-02T13:48:06 - aggregate: saved checkpoint stage=final concepts merge and deduplication category=concepts path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/final-concepts.json

- 2026-05-02T13:48:06 - aggregate: category final merge done category=concepts count=131

- 2026-05-02T13:48:06 - aggregate: category merge input category=methods partials=7 chars=138231 merge_budget=700000

- 2026-05-02T13:48:06 - aggregate: category final merge input category=methods cards=7 chars=138231 merge_budget=700000

- 2026-05-02T13:48:06 - aggregate: start stage=final methods merge and deduplication category=methods final=True cards=7 chars=138231 timeout=1800s thinking=True reasoning_effort=max max_tokens=65536

- 2026-05-02T14:10:58 - aggregate: failed stage=final methods merge and deduplication category=methods elapsed=1372.3s error=IncompleteRead(22 bytes read)

- 2026-05-02T14:31:50 - aggregate: ingest start index=papers aggregate_only=True no_aggregate=False force=False resume=True run_id=20260502-143150 shard=0/1

- 2026-05-02T14:32:03 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-02T14:32:03 - aggregate: indexed records with unknown Zotero item type kept for review: 3

- 2026-05-02T14:32:03 - aggregate: loaded index records raw=492

- 2026-05-02T14:32:03 - aggregate: deduplicated records count=487

- 2026-05-02T14:32:03 - aggregate: loaded paper pages for aggregate count=487 complete_ids=487 over_budget_skips=0

- 2026-05-02T14:32:06 - aggregate: prepared paper_pages=487 cards=487 batches=7 card_budget=70000 batch_budget=700000 checkpoint=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502

- 2026-05-02T14:32:06 - aggregate: reuse checkpoint stage=batch aggregation 1/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-001-of-007.json counts={'concepts': 14, 'methods': 8, 'claims': 30, 'syntheses': 3, 'open_questions': 4}

- 2026-05-02T14:32:06 - aggregate: completed batch 1/7

- 2026-05-02T14:32:06 - aggregate: reuse checkpoint stage=batch aggregation 2/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-002-of-007.json counts={'concepts': 41, 'methods': 37, 'claims': 41, 'syntheses': 6, 'open_questions': 8}

- 2026-05-02T14:32:06 - aggregate: completed batch 2/7

- 2026-05-02T14:32:06 - aggregate: reuse checkpoint stage=batch aggregation 3/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-003-of-007.json counts={'concepts': 25, 'methods': 19, 'claims': 10, 'syntheses': 3, 'open_questions': 4}

- 2026-05-02T14:32:06 - aggregate: completed batch 3/7

- 2026-05-02T14:32:06 - aggregate: reuse checkpoint stage=batch aggregation 4/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-004-of-007.json counts={'concepts': 14, 'methods': 7, 'claims': 10, 'syntheses': 5, 'open_questions': 6}

- 2026-05-02T14:32:06 - aggregate: completed batch 4/7

- 2026-05-02T14:32:06 - aggregate: reuse checkpoint stage=batch aggregation 5/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-005-of-007.json counts={'concepts': 20, 'methods': 13, 'claims': 20, 'syntheses': 4, 'open_questions': 3}

- 2026-05-02T14:32:06 - aggregate: completed batch 5/7

- 2026-05-02T14:32:06 - aggregate: reuse checkpoint stage=batch aggregation 6/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-006-of-007.json counts={'concepts': 22, 'methods': 15, 'claims': 10, 'syntheses': 6, 'open_questions': 7}

- 2026-05-02T14:32:06 - aggregate: completed batch 6/7

- 2026-05-02T14:32:06 - aggregate: reuse checkpoint stage=batch aggregation 7/7 path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/batch-007-of-007.json counts={'concepts': 78, 'methods': 48, 'claims': 40, 'syntheses': 4, 'open_questions': 9}

- 2026-05-02T14:32:06 - aggregate: completed batch 7/7

- 2026-05-02T14:32:06 - aggregate: category final merge start partials=7 counts={'concepts': 214, 'methods': 147, 'claims': 161, 'syntheses': 31, 'open_questions': 41}

- 2026-05-02T14:32:06 - aggregate: category merge input category=concepts partials=7 chars=151537 merge_budget=700000

- 2026-05-02T14:32:06 - aggregate: category final merge input category=concepts cards=7 chars=151537 merge_budget=700000

- 2026-05-02T14:32:06 - aggregate: reuse checkpoint stage=final concepts merge and deduplication category=concepts path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/final-concepts.json count=131

- 2026-05-02T14:32:06 - aggregate: category final merge done category=concepts count=131

- 2026-05-02T14:32:06 - aggregate: category merge input category=methods partials=7 chars=138231 merge_budget=700000

- 2026-05-02T14:32:06 - aggregate: category final merge input category=methods cards=7 chars=138231 merge_budget=700000

- 2026-05-02T14:32:06 - aggregate: start stage=final methods merge and deduplication category=methods final=True cards=7 chars=138231 timeout=1800s thinking=True reasoning_effort=max max_tokens=65536

- 2026-05-02T14:55:47 - aggregate: response stage=final methods merge and deduplication category=methods elapsed=1421.2s raw_chars=77833 usage={'prompt_tokens': 51270, 'completion_tokens': 48537, 'total_tokens': 99807, 'prompt_tokens_details': {'cached_tokens': 51200}, 'completion_tokens_details': {'reasoning_tokens': 18309}, 'prompt_cache_hit_tokens': 51200, 'prompt_cache_miss_tokens': 70}

- 2026-05-02T14:55:47 - aggregate: saved raw response stage=final methods merge and deduplication category=methods path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/final-methods.json.raw.txt

- 2026-05-02T14:55:47 - aggregate: parsed stage=final methods merge and deduplication category=methods count=88

- 2026-05-02T14:55:47 - aggregate: saved checkpoint stage=final methods merge and deduplication category=methods path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/final-methods.json

- 2026-05-02T14:55:47 - aggregate: category final merge done category=methods count=88

- 2026-05-02T14:55:47 - aggregate: category merge input category=claims partials=7 chars=107349 merge_budget=700000

- 2026-05-02T14:55:47 - aggregate: category final merge input category=claims cards=7 chars=107349 merge_budget=700000

- 2026-05-02T14:55:47 - aggregate: start stage=final claims merge and deduplication category=claims final=True cards=7 chars=107349 timeout=1800s thinking=True reasoning_effort=max max_tokens=65536

- 2026-05-02T15:15:43 - aggregate: response stage=final claims merge and deduplication category=claims elapsed=1195.9s raw_chars=84917 usage={'prompt_tokens': 41695, 'completion_tokens': 48140, 'total_tokens': 89835, 'prompt_tokens_details': {'cached_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 15690}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 41695}

- 2026-05-02T15:15:43 - aggregate: saved raw response stage=final claims merge and deduplication category=claims path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/final-claims.json.raw.txt

- 2026-05-02T15:15:43 - aggregate: parsed stage=final claims merge and deduplication category=claims count=127

- 2026-05-02T15:15:43 - aggregate: saved checkpoint stage=final claims merge and deduplication category=claims path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/final-claims.json

- 2026-05-02T15:15:43 - aggregate: category final merge done category=claims count=127

- 2026-05-02T15:15:43 - aggregate: category merge input category=syntheses partials=7 chars=48633 merge_budget=700000

- 2026-05-02T15:15:43 - aggregate: category final merge input category=syntheses cards=7 chars=48633 merge_budget=700000

- 2026-05-02T15:15:43 - aggregate: start stage=final syntheses merge and deduplication category=syntheses final=True cards=7 chars=48633 timeout=1800s thinking=True reasoning_effort=max max_tokens=65536

- 2026-05-02T15:45:46 - aggregate: response stage=final syntheses merge and deduplication category=syntheses elapsed=1802.9s raw_chars=35829 usage={'prompt_tokens': 21037, 'completion_tokens': 61753, 'total_tokens': 82790, 'prompt_tokens_details': {'cached_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 47124}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 21037}

- 2026-05-02T15:45:46 - aggregate: saved raw response stage=final syntheses merge and deduplication category=syntheses path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/final-syntheses.json.raw.txt

- 2026-05-02T15:45:46 - aggregate: parsed stage=final syntheses merge and deduplication category=syntheses count=16

- 2026-05-02T15:45:46 - aggregate: saved checkpoint stage=final syntheses merge and deduplication category=syntheses path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/final-syntheses.json

- 2026-05-02T15:45:46 - aggregate: category final merge done category=syntheses count=16

- 2026-05-02T15:45:46 - aggregate: category merge input category=open_questions partials=7 chars=25446 merge_budget=700000

- 2026-05-02T15:45:46 - aggregate: category final merge input category=open_questions cards=7 chars=25446 merge_budget=700000

- 2026-05-02T15:45:46 - aggregate: start stage=final open_questions merge and deduplication category=open_questions final=True cards=7 chars=25446 timeout=1800s thinking=True reasoning_effort=max max_tokens=65536

- 2026-05-02T16:02:46 - aggregate: response stage=final open_questions merge and deduplication category=open_questions elapsed=1019.7s raw_chars=22017 usage={'prompt_tokens': 10732, 'completion_tokens': 34496, 'total_tokens': 45228, 'prompt_tokens_details': {'cached_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 25599}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 10732}

- 2026-05-02T16:02:46 - aggregate: saved raw response stage=final open_questions merge and deduplication category=open_questions path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/final-open_questions.json.raw.txt

- 2026-05-02T16:02:46 - aggregate: parsed stage=final open_questions merge and deduplication category=open_questions count=31

- 2026-05-02T16:02:46 - aggregate: saved checkpoint stage=final open_questions merge and deduplication category=open_questions path=wiki/.staging/aggregate-checkpoints/aggregate-pro-20260502/final-open_questions.json

- 2026-05-02T16:02:46 - aggregate: category final merge done category=open_questions count=31

- 2026-05-02T16:02:46 - aggregate: category final merge all done counts={'concepts': 131, 'methods': 88, 'claims': 127, 'syntheses': 16, 'open_questions': 31}

- 2026-05-02T16:02:46 - aggregate: aggregate payload ready; write pages

- 2026-05-02T16:02:46 - aggregate: write aggregate pages start staging=wiki/.staging/aggregates/20260502-160246 counts={'concepts': 131, 'methods': 88, 'claims': 127, 'syntheses': 16, 'open_questions': 31}

- 2026-05-02T16:02:46 - aggregate: archive existing aggregate pages start target=wiki/.archive/aggregates/20260502-160246

- 2026-05-02T16:02:46 - aggregate: archive existing aggregate pages done moved=0

- 2026-05-02T16:02:46 - aggregate: write aggregate pages done promoted=363

- 2026-05-02T16:02:49 - ingested 487 paper records; wrote 363 pages; skipped_over_budget=0; failed=0; problems=0; warnings=106

- 2026-05-04T14:30:02 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-143002 shard=0/2

- 2026-05-04T14:30:02 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-143002 shard=1/2

- 2026-05-04T14:30:24 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T14:30:24 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T14:30:24 - aggregate: loaded index records raw=821

- 2026-05-04T14:30:24 - aggregate: deduplicated records count=801

- 2026-05-04T14:30:24 - aggregate: deduplicated records count=801

- 2026-05-04T14:30:24 - aggregate: applied limit=10 remaining=10

- 2026-05-04T14:30:24 - aggregate: applied limit=10 remaining=10

- 2026-05-04T14:30:24 - aggregate: applied shard index=0 count=2 global_records=10 shard_records=5

- 2026-05-04T14:30:24 - aggregate: applied shard index=1 count=2 global_records=10 shard_records=5

- 2026-05-04T14:34:40 - ingested 5 paper records; wrote 5 pages; skipped_over_budget=0; failed=0; problems=0; warnings=2

- 2026-05-04T14:34:42 - ingested 5 paper records; wrote 5 pages; skipped_over_budget=0; failed=0; problems=0; warnings=2

- 2026-05-04T14:44:13 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-144413 shard=0/1

- 2026-05-04T14:44:27 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T14:44:27 - aggregate: loaded index records raw=821

- 2026-05-04T14:46:00 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-144600 shard=0/1

- 2026-05-04T14:46:15 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T14:46:15 - aggregate: loaded index records raw=821

- 2026-05-04T14:46:15 - aggregate: deduplicated records count=801

- 2026-05-04T14:46:15 - aggregate: applied limit=20 remaining=20

- 2026-05-04T14:49:37 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-144937 shard=0/1

- 2026-05-04T14:49:52 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T14:49:52 - aggregate: loaded index records raw=821

- 2026-05-04T14:49:52 - aggregate: deduplicated records count=801

- 2026-05-04T14:49:52 - aggregate: applied limit=0 remaining=0

- 2026-05-04T14:49:52 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T14:49:52 - aggregate: loaded index records raw=821

- 2026-05-04T14:49:52 - aggregate: deduplicated records count=801

- 2026-05-04T14:49:52 - aggregate: applied limit=0 remaining=0

- 2026-05-04T14:49:52 - ingested 0 paper records; wrote 0 pages; skipped_over_budget=0; failed=0; problems=0; warnings=2

- 2026-05-04T14:49:52 - ingested 0 paper records; wrote 0 pages; skipped_over_budget=0; failed=0; problems=0; warnings=2

- 2026-05-04T14:53:27 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-145327 shard=0/1

- 2026-05-04T14:53:42 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T14:53:42 - aggregate: loaded index records raw=821

- 2026-05-04T14:53:42 - aggregate: deduplicated records count=801

- 2026-05-04T14:56:41 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-145641 shard=0/1

- 2026-05-04T14:56:55 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T14:56:55 - aggregate: loaded index records raw=821

- 2026-05-04T14:56:55 - aggregate: deduplicated records count=801

- 2026-05-04T15:02:03 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-150203 shard=0/1

- 2026-05-04T15:02:16 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T15:02:16 - aggregate: loaded index records raw=821

- 2026-05-04T15:02:17 - aggregate: deduplicated records count=801

- 2026-05-04T15:02:17 - aggregate: applied limit=0 remaining=0

- 2026-05-04T15:02:17 - ingested 0 paper records; wrote 0 pages; skipped_over_budget=0; failed=0; problems=0; warnings=2

- 2026-05-04T15:05:47 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-150547 shard=0/1

- 2026-05-04T15:06:01 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T15:06:01 - aggregate: loaded index records raw=821

- 2026-05-04T15:06:01 - aggregate: deduplicated records count=801

- 2026-05-04T15:12:35 - ingested 801 paper records; wrote 492 pages; skipped_over_budget=0; failed=0; problems=0; warnings=2

- 2026-05-04T15:22:37 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-04T15:22:37 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T15:23:40 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-04T15:23:40 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T15:25:01 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-04T15:25:01 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T15:26:09 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-04T15:26:09 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T15:41:22 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-154122 shard=0/1

- 2026-05-04T15:41:22 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-154122 shard=0/1

- 2026-05-04T15:41:37 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T15:41:37 - aggregate: loaded index records raw=821
otero item type kept for review: 317

- 2026-05-04T15:41:37 - aggregate: loaded index records raw=821

- 2026-05-04T15:41:37 - aggregate: deduplicated records count=801

- 2026-05-04T15:41:37 - aggregate: deduplicated records count=801

- 2026-05-04T15:47:44 - ingested 801 paper records; wrote 492 pages; skipped_over_budget=0; failed=0; problems=0; warnings=2

- 2026-05-04T15:47:54 - ingested 801 paper records; wrote 492 pages; skipped_over_budget=0; failed=0; problems=0; warnings=2

- 2026-05-04T16:02:04 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-04T16:02:04 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T16:02:59 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-04T16:02:59 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T16:13:56 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-161356 shard=0/1

- 2026-05-04T16:13:56 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-161356 shard=0/1

- 2026-05-04T16:14:10 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-04T16:14:10 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T16:14:10 - aggregate: loaded index records raw=800

- 2026-05-04T16:14:10 - aggregate: deduplicated records count=780

- 2026-05-04T16:14:10 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-04T16:14:10 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T16:14:10 - aggregate: loaded index records raw=800

- 2026-05-04T16:14:10 - aggregate: deduplicated records count=780

- 2026-05-04T16:17:58 - ingested 780 paper records; wrote 492 pages; skipped_over_budget=0; failed=0; problems=0; warnings=2

- 2026-05-04T16:18:22 - ingested 780 paper records; wrote 492 pages; skipped_over_budget=0; failed=0; problems=0; warnings=2

- 2026-05-04T16:25:47 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-162547 shard=0/1

- 2026-05-04T16:25:47 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-162547 shard=0/1

- 2026-05-04T16:26:02 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-04T16:26:02 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T16:26:02 - aggregate: loaded index records raw=800

- 2026-05-04T16:26:02 - aggregate: deduplicated records count=780

- 2026-05-04T16:26:02 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-04T16:26:02 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T16:26:02 - aggregate: loaded index records raw=800

- 2026-05-04T16:26:02 - aggregate: deduplicated records count=780

- 2026-05-04T16:31:54 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-163154 shard=0/1

- 2026-05-04T16:31:54 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-163154 shard=0/1

- 2026-05-04T16:32:08 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-04T16:32:08 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T16:32:08 - aggregate: loaded index records raw=800

- 2026-05-04T16:32:08 - aggregate: deduplicated records count=780

- 2026-05-04T16:32:08 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-04T16:32:08 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T16:32:08 - aggregate: loaded index records raw=800

- 2026-05-04T16:32:08 - aggregate: deduplicated records count=780

- 2026-05-04T16:42:06 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-164206 shard=0/1

- 2026-05-04T16:42:20 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-04T16:42:20 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T16:42:20 - aggregate: loaded index records raw=800

- 2026-05-04T16:42:20 - aggregate: deduplicated records count=780

- 2026-05-04T16:42:20 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-04T16:42:20 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T16:42:20 - aggregate: loaded index records raw=800

- 2026-05-04T16:42:20 - aggregate: deduplicated records count=780

- 2026-05-04T16:43:42 - ingested 780 paper records; wrote 512 pages; skipped_over_budget=0; failed=0; problems=0; warnings=2

- 2026-05-04T16:44:11 - ingested 780 paper records; wrote 512 pages; skipped_over_budget=0; failed=0; problems=0; warnings=2

- 2026-05-04T16:45:22 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-164522 shard=0/1

- 2026-05-04T16:45:22 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-164522 shard=0/1

- 2026-05-04T16:45:37 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T16:45:37 - aggregate: loaded index records raw=821

- 2026-05-04T16:45:37 - aggregate: deduplicated records count=801

- 2026-05-04T16:45:37 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T16:45:37 - aggregate: loaded index records raw=821

- 2026-05-04T16:45:37 - aggregate: deduplicated records count=801

- 2026-05-04T16:52:39 - aggregate: skipped non-allowed Zotero item types: {'book': 3, 'thesis': 18}

- 2026-05-04T16:52:39 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T16:53:16 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-165316 shard=0/1

- 2026-05-04T16:53:30 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T16:53:30 - aggregate: loaded index records raw=821

- 2026-05-04T16:53:30 - aggregate: deduplicated records count=801

- 2026-05-04T16:54:18 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T16:55:17 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T17:10:52 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-171052 shard=0/1

- 2026-05-04T17:10:52 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-171052 shard=0/1

- 2026-05-04T17:11:07 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T17:11:07 - aggregate: loaded index records raw=821

- 2026-05-04T17:11:07 - aggregate: deduplicated records count=801

- 2026-05-04T17:11:10 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T17:11:10 - aggregate: loaded index records raw=821

- 2026-05-04T17:11:10 - aggregate: deduplicated records count=801

- 2026-05-04T17:16:12 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-171612 shard=0/1

- 2026-05-04T17:16:27 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T17:16:27 - aggregate: loaded index records raw=821

- 2026-05-04T17:16:27 - aggregate: deduplicated records count=801

- 2026-05-04T17:17:04 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T17:22:49 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T17:27:16 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-172716 shard=0/1

- 2026-05-04T17:27:30 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T17:27:30 - aggregate: loaded index records raw=821

- 2026-05-04T17:27:30 - aggregate: deduplicated records count=801

- 2026-05-04T17:28:49 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-172849 shard=0/2

- 2026-05-04T17:28:49 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-172849 shard=1/2

- 2026-05-04T17:29:04 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T17:29:04 - aggregate: loaded index records raw=821

- 2026-05-04T17:29:04 - aggregate: deduplicated records count=801

- 2026-05-04T17:29:04 - aggregate: applied shard index=1 count=2 global_records=801 shard_records=400

- 2026-05-04T17:29:04 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T17:29:04 - aggregate: loaded index records raw=821

- 2026-05-04T17:29:04 - aggregate: deduplicated records count=801

- 2026-05-04T17:29:04 - aggregate: applied shard index=0 count=2 global_records=801 shard_records=401

- 2026-05-04T22:53:27 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-225327 shard=0/2

- 2026-05-04T22:53:50 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260504-225350 shard=1/2

- 2026-05-04T22:53:50 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T22:53:50 - aggregate: loaded index records raw=821

- 2026-05-04T22:53:50 - aggregate: deduplicated records count=802

- 2026-05-04T22:53:50 - aggregate: applied shard index=0 count=2 global_records=802 shard_records=401

- 2026-05-04T22:54:05 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-04T22:54:05 - aggregate: loaded index records raw=821

- 2026-05-04T22:54:05 - aggregate: deduplicated records count=802

- 2026-05-04T22:54:05 - aggregate: applied shard index=1 count=2 global_records=802 shard_records=401

- 2026-05-05T00:45:57 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260505-004557 shard=0/2

- 2026-05-05T00:45:57 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260505-004557 shard=1/2

- 2026-05-05T00:46:11 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-05T00:46:11 - aggregate: loaded index records raw=821

- 2026-05-05T00:46:11 - aggregate: deduplicated records count=802

- 2026-05-05T00:46:11 - aggregate: applied shard index=0 count=2 global_records=802 shard_records=401

- 2026-05-05T00:46:11 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-05T00:46:11 - aggregate: loaded index records raw=821

- 2026-05-05T00:46:11 - aggregate: deduplicated records count=802

- 2026-05-05T00:46:11 - aggregate: applied shard index=1 count=2 global_records=802 shard_records=401

- 2026-05-05T00:47:21 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260505-004721 shard=0/2

- 2026-05-05T00:47:35 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-05T00:47:35 - aggregate: loaded index records raw=821

- 2026-05-05T00:47:35 - aggregate: deduplicated records count=802

- 2026-05-05T00:47:35 - aggregate: applied shard index=0 count=2 global_records=802 shard_records=401

- 2026-05-05T00:48:21 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260505-004821 shard=1/2

- 2026-05-05T00:48:39 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-05T00:48:39 - aggregate: loaded index records raw=821

- 2026-05-05T00:48:39 - aggregate: deduplicated records count=802

- 2026-05-05T00:48:39 - aggregate: applied shard index=1 count=2 global_records=802 shard_records=401

- 2026-05-05T10:20:24 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260505-102024 shard=0/2

- 2026-05-05T10:20:38 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-05T10:20:38 - aggregate: loaded index records raw=821

- 2026-05-05T10:20:38 - aggregate: deduplicated records count=802

- 2026-05-05T10:20:38 - aggregate: applied shard index=0 count=2 global_records=802 shard_records=401

- 2026-05-05T10:21:48 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260505-102148 shard=1/2

- 2026-05-05T10:22:02 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-05T10:22:02 - aggregate: loaded index records raw=821

- 2026-05-05T10:22:02 - aggregate: deduplicated records count=802

- 2026-05-05T10:22:02 - aggregate: applied shard index=1 count=2 global_records=802 shard_records=401

- 2026-05-05T11:25:03 - ingested 401 paper records; wrote 400 pages; skipped_over_budget=1; failed=0; problems=0; warnings=2

- 2026-05-05T11:40:15 - ingested 401 paper records; wrote 399 pages; skipped_over_budget=2; failed=0; problems=0; warnings=2

- 2026-05-05T11:52:35 - aggregate: ingest start index=papers aggregate_only=False no_aggregate=True force=False resume=True run_id=20260505-115235 shard=0/1

- 2026-05-05T11:52:57 - aggregate: indexed records with unknown Zotero item type kept for review: 317

- 2026-05-05T11:52:57 - aggregate: loaded index records raw=821

- 2026-05-05T11:52:57 - aggregate: deduplicated records count=802

- 2026-05-05T11:59:00 - ingested 802 paper records; wrote 802 pages; skipped_over_budget=0; failed=0; problems=0; warnings=2
