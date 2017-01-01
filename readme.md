# Download and extraction

1. Downloaded Siddhanta Kaumudi - Text only.zip file from mail of Dr. H. N. Bhat dated 26 Dec 2016.
2. Extracted and copy pasted in siddhantakaumudi.txt (This is base copy in which there will not be any change.)
3. Created a copy of it in sk0.txt.

# Step 0 - Manual corrections

1. There are misorders in this file. So created a list of misordered sUtra numbers by step0.py in step0_notes.txt and made corrections in sk0.txt.
2. Added missing 2139-2150 sUtras manually in sk0.txt. 
3. sarvasamAsazeSaprakaraNam is missing.  - Added manually.
4. prakaraNa headings were missing. - Added manually.
5. तिङन्तप्रत्ययमालाप्रकरणम्‌ is missing. - Added manually.
6. Last one portion of svaraprakaraNam page 775 is missing. Added manually.
8. Correct verb number errors. They should be in chronologic order. When not, it means it is wrong. e.g. 157 वगि -> 147 वगि
9. 1209 verb number are missing in original. Made adjustment in step1.py logic.
10. Some missing data for verbs was also incorporated. The diff file is logged in sk0_manual.txt file. (by `diff siddhantakaumudi.txt sk0.txt > sk0_manual.txt`).
11. sUtra 3158 is missing in original SK text also (uNAdi sUtras are there in its place.) Therefore only 3977 sUtras are present instead of 3978 as in printed text.

# Step 1 - Mechanical changes and add markup

1. Add space after the sUtra number. (2264)धात्वादेः षः सः -> (2264) धात्वादेः षः सः
2. Add space after the sentence हल्संज्ञायाम्।। -> हल्संज्ञायाम् ।।
3. Change ।। -> ॥
4. (अ) -> ॒ and (स्व) -> ॑
5. ।शकन्ध्वादिषु पररूपं वाच्यम् (वा)।। depicts a vArtika. Try to preserve this information while correcting the spaces after and before ॥ and ।.
	5.1. {%...%} for vArtika.
	5.2. {%?...?%} Questionable vArtikas. There is a small subset 251 items following regex `'।[^ ।]([^।]+)।।'` which also has vArtikas (without (वा) at the end). See ।पितुर्भ्रातरि व्यत्।।. They are marked with {%?...?%}. Question mark shows that it needs to be verified whether they actually are vArtikas or not.
	5.3. {%??...??%} Very doubtful vArtikas. 143 such cases `'।([^ ।][^।0-9]+)।'` regex.
	5b and 5c need manual examination and confirmation whether they are actually vArtikas or not.
	Ideal is to make them uniformly in format of 5a in sk0.txt itself manually, so that it is consistent throughout.
6. Figures in bracket is SK rule number `(2264)`. Figures with two dashes are AS rule number `6-1-64`. Figures without bracktes are reference to SK rule.
There is a slight issue with the rule without bracket referring to only SK rules. They may also refer to verb number or something else too.
"""
(2264)धात्वादेः षः सः    6-1-64 
धातोरादेः षस्य सः स्यात्। सात्पदाद्योः 2123 इति षत्वनिषेधः। अनुस्वदते। सस्वदे। स्वर्दते। सस्वर्दे । 20 उर्द माने क्रीडायां च।।
"""
In the present example 2123 refers to SK rule, whereas 20 refers to the 20th verb under examination.
There is a possibility of identifying SK rule reference by regex `X इति` or `X इत्‍`or `X इती`.
Another check is - verb numbers will be in chronologic order. If there is some number which is not chronologic, it is highly probable that it is rule number.
Suggested approach - 
	6.1. {#...#} encoding for SK rule.
	6.2. {@...@} encoding for AS rule.
	6.3. {*...*} encoding for internal reference to SK rule.
	6.4. {$...$} encoding for verb number or other stuff (if they are found out).
7. ःढ़द्य; -> ऊ
8. After all corrections, change >1 space to 1 space and remove trailing space.