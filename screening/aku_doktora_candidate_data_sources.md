# AKU_Doktora Candidate Data Sources

Purpose

- This note records the most useful CSV data sources discovered under `AKU_Doktora`.
- The goal is not to recover a ready-made exclusion log.
- The goal is to identify usable upstream data pools from which a fresh include/exclude trail can be constructed.

## Main takeaway

Yes, there is enough upstream data in `AKU_Doktora` to work with.

The strongest candidate files are:

1. `included_studies_seed.csv`
2. `Elicit - screen-results-review-226c619b-1930-4d4f-b156-ad106a003375.csv`
3. `Elicit - gather-results-review-226c619b-1930-4d4f-b156-ad106a003375.csv`
4. `included_studies.csv`
5. `Screening_Log.csv`

## Recommended priority order

### 1) Broad seed universe

File:

- `C:\Users\fdonmez\OneDrive - ASKERİ FABRİKA VE TERSANE İŞLETME A.Ş (ASFAT)\kisiselAlan\AKU_Doktora\reivew_2\adım1\included_studies_seed.csv`

Observed record count:

- `20,383`

Why it matters:

- This is the largest accessible candidate pool.
- It contains title, authors, DOI, venue, year, plus many extracted/reasoning fields.
- It is suitable as the broadest upstream seed if we want to reconstruct a large candidate universe.

Warning:

- The contents are not O-ISAC-specific by default.
- It contains many non-optical and RF-domain items.
- It should be treated as a broad discovery pool, not as a final screened set.

### 2) Best screening-stage candidate

File:

- `C:\Users\fdonmez\OneDrive - ASKERİ FABRİKA VE TERSANE İŞLETME A.Ş (ASFAT)\kisiselAlan\AKU_Doktora\reivew_2\datalar\Elicit - screen-results-review-226c619b-1930-4d4f-b156-ad106a003375.csv`

Observed record count:

- `695`

Why it matters:

- This is the closest match to the user’s expectation of a `600+` screening-scale CSV.
- It contains explicit screening judgments and reasoning fields.
- It is likely the best upstream file for reconstructing a title/abstract screening layer.

Key columns observed:

- `Title`
- `Authors`
- `DOI`
- `Venue`
- `Year`
- many criteria-specific reasoning columns
- `Screening judgement`
- `Screening score`

### 3) Gather-stage candidate pool

File:

- `C:\Users\fdonmez\OneDrive - ASKERİ FABRİKA VE TERSANE İŞLETME A.Ş (ASFAT)\kisiselAlan\AKU_Doktora\reivew_2\adım1\Elicit - gather-results-review-226c619b-1930-4d4f-b156-ad106a003375.csv`

Observed record count:

- `578`

Why it matters:

- This looks like a pre-screen or gathered-candidates layer.
- It is useful if we want an earlier candidate set before explicit screening judgments.

Key columns observed:

- `Title`
- `Authors`
- `DOI`
- `DOI link`
- `Venue`
- `Citation count`
- `Year`
- `Filename`

### 4) Curated included-style working set

File:

- `C:\Users\fdonmez\OneDrive - ASKERİ FABRİKA VE TERSANE İŞLETME A.Ş (ASFAT)\kisiselAlan\AKU_Doktora\reivew_2\datalar\included_studies.csv`

Observed record count:

- `85`

Why it matters:

- This is a much smaller curated set.
- It looks like a downstream working include list rather than a discovery or screening universe.
- It may be useful for comparison against the current repo’s included corpus, but not as the main screening base.

### 5) Manual decision log in another branch

File:

- `C:\Users\fdonmez\OneDrive - ASKERİ FABRİKA VE TERSANE İŞLETME A.Ş (ASFAT)\kisiselAlan\AKU_Doktora\OWISAC_PRISMA_Review\03_Tarama\Screening_Log.csv`

Observed record count:

- `8`

Why it matters:

- This file includes explicit stage, decision, and exclusion code fields.
- It is too small to serve as the main upstream pool, but it shows a more manually curated screening-log format.

Key columns observed:

- `record_id`
- `title`
- `venue`
- `year`
- `stage`
- `decision`
- `exclusion_code`
- `notes`

## Practical recommendation

If we are going to rebuild a workable screening dataset ourselves, the best starting combination is:

1. `included_studies_seed.csv` as the broad universe
2. `Elicit - screen-results...csv` as the screening-decision layer
3. `Elicit - gather-results...csv` as the pre-screen candidate layer

Then we can derive:

- a candidate pool
- an include/exclude decision layer
- a final manually curated exclusion log tailored to the O-ISAC manuscript

## Important note

The fact that the excluded DOI/title pairs were not found in these CSVs is not a blocker.

What matters is that these CSVs provide enough upstream material to create:

- a new exclusion log
- a new screening ledger
- a defensible reconstruction narrative

