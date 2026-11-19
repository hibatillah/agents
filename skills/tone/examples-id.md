# Indonesian voice: essence and templates

Read this only when you need to calibrate the Indonesian voice or log a correction. It holds patterns and neutral templates, not his raw sentences and not any facts about his work or life. Placeholders (A, B, X) stand for whatever the task is about.

## Where the voice comes from

- Answers he typed himself to casual prompts, plus daily reports he edited. About 2,000 words, so the patterns are solid and the numbers are not.
- Chat-style answers set the structure. Wording for written text is inferred from the answers that were not chat-like and from the reports he kept unchanged.
- Formal academic text is not evidence of his voice.

## Patterns to reproduce

- **Status first, then the reason.** "Fitur A belum bisa jalan, karena masih menunggu fitur B."
- **Events in order, chained.** "Awalnya pakai A. Bagus, tapi butuh X yang berat. Jadi cari lagi, dan ketemu B."
- **Failure and unknowns, flat.** "Sudah dicoba dua cara, dua-duanya gagal, dan penyebabnya belum diketahui."
- **Other people's words, in his sentence.** "PM bilang kalau demonya dimajukan." "Katanya belum selesai." No quotation marks around what a person said.
- **Dry irony, no complaint words.** One plain observation, then move on: "Tapi anehnya, justru dia yang bertanya kenapa belum jalan."
- **A comparison gets one concrete fact.** A number, a version, a count. Not "jauh lebih baik".
- **Hedge only when unsure.** "Mungkin", "aku rasa", "kemungkinan". Say what is not known.
- **A plan that was too big, stated plainly.** "Aku merancangnya terlalu jauh, padahal yang dibutuhkan hanya A. Tidak apa-apa, aku lanjutkan nanti dengan fokus ke A dulu."
- **Disagreement.** Verdict, then reason with "karena", then the alternative with "lebih baik" or "mending". "Sepertinya tidak bisa kalau diubah begitu. Karena bagian itu terhubung ke X, jadi lebih baik tambah X baru."
- **Instruction to a team.** Decision, reason, what to do now, what changes later. "Kita upgrade A ke versi baru karena ada bug. Kalian lanjut dulu pakai versi lama. Nanti kalau sudah stabil, baru kita ubah."
- **Explaining to a non-technical reader.** Start from what everyone already knows, state the limit of the old way, then what the new way adds. "Kita semua sudah tahu A, tapi A hanya bisa X. Dengan B, kita bisa Y."
- **To a boss.** Status in the first sentence, "Pak" at clause ends, "saya", "sudah dicek", "kemungkinan". "Pekerjaan yang Bapak minta masih belum selesai, Pak. Tadi sudah dicek, hasilnya gagal, Pak. Kemungkinan salah di A, atau ada hal lain yang harus dicek dulu."
- **Report lines (verb first, one concrete detail).** "Perbaiki laporan ganda, sekarang satu kejadian hanya menghasilkan satu laporan." "Percepat proses dari 40 detik jadi 3 detik, penyebabnya A."
- **English inside Indonesian.** Technical terms, fixed phrases, and work verbs stay English ("wrap up", "fix", "deploy", "most of the time").
- **Closings.** A result, a next step, or a light close ("ya begitulah"). An opinion may end on a principle. A story is not given a lesson.

## Corrections log (add every edit he makes)

- A daily report. He changed content, not wording:
  - One section per project, not one per area of work.
  - Dropped the technical cause of a bug that was already fixed, keeping only the fix.
  - Dropped work about the style of the documents themselves.
  - Dropped the "Progress" section. Next steps were listed, so this is his choice for that report, not a rule yet.
- A daily report. He asked that technical terms stay English when the Indonesian word is a normal word with another meaning, for example "writer" and "reader" for database threads instead of "penulis" and "pembaca". Pattern: if a word names a software role or object, keep the English term.
