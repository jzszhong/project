start trec_terrier.bat -r -Dtrec.model=TF_IDF -c 0.4 -Dtrec.topics=../../project/expanded_topics/expanded_topics_cbow_s100.trec
pause
start trec_terrier.bat -r -Dtrec.model=TF_IDF -c 0.4 -Dtrec.topics=../../project/expanded_topics/expanded_topics_cbow_s300.trec
pause
start trec_terrier.bat -r -Dtrec.model=TF_IDF -c 0.4 -Dtrec.topics=../../project/expanded_topics/expanded_topics_cbow_s700.trec
pause
start trec_terrier.bat -r -Dtrec.model=TF_IDF -c 0.4 -Dtrec.topics=../../project/expanded_topics/expanded_topics_skipgram_s100.trec
pause
start trec_terrier.bat -r -Dtrec.model=TF_IDF -c 0.4 -Dtrec.topics=../../project/expanded_topics/expanded_topics_skipgram_s300.trec
pause
start trec_terrier.bat -r -Dtrec.model=TF_IDF -c 0.4 -Dtrec.topics=../../project/expanded_topics/expanded_topics_skipgram_s700.trec
pause
start trec_terrier.bat -r -Dtrec.model=TF_IDF -c 0.4 -Dtrec.topics=../../project/expanded_topics/expanded_topics_glove_s100.trec
pause
start trec_terrier.bat -r -Dtrec.model=TF_IDF -c 0.4 -Dtrec.topics=../../project/expanded_topics/expanded_topics_glove_s300.trec
pause
start trec_terrier.bat -r -Dtrec.model=TF_IDF -c 0.4 -Dtrec.topics=../../project/expanded_topics/expanded_topics_glove_s700.trec

pause

:: The sequence of result files are: cbow_s100: TF_IDF_1, cbow_s300: TF_IDF_2, ..., glove_s700: TF_IDF_9
:: The actual numbers may need to be changed in different computer according to the current counter of Terrier

start trec_eval.bat -m map ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_1.res
start trec_eval.bat -m map ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_2.res
start trec_eval.bat -m map ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_3.res
pause
start trec_eval.bat -m map ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_4.res
start trec_eval.bat -m map ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_5.res
start trec_eval.bat -m map ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_6.res
pause
start trec_eval.bat -m map ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_7.res
start trec_eval.bat -m map ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_8.res
start trec_eval.bat -m map ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_9.res

pause

start trec_eval.bat -m gm_map ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_1.res
start trec_eval.bat -m gm_map ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_2.res
start trec_eval.bat -m gm_map ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_3.res
pause
start trec_eval.bat -m gm_map ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_4.res
start trec_eval.bat -m gm_map ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_5.res
start trec_eval.bat -m gm_map ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_6.res
pause
start trec_eval.bat -m gm_map ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_7.res
start trec_eval.bat -m gm_map ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_8.res
start trec_eval.bat -m gm_map ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_9.res

pause

start trec_eval.bat -m set_P -M 10 ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_1.res
start trec_eval.bat -m set_P -M 10 ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_2.res
start trec_eval.bat -m set_P -M 10 ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_3.res
pause
start trec_eval.bat -m set_P -M 10 ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_4.res
start trec_eval.bat -m set_P -M 10 ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_5.res
start trec_eval.bat -m set_P -M 10 ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_6.res
pause
start trec_eval.bat -m set_P -M 10 ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_7.res
start trec_eval.bat -m set_P -M 10 ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_8.res
start trec_eval.bat -m set_P -M 10 ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_9.res

pause

start trec_eval.bat -m ndcg -M 10 ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_1.res
start trec_eval.bat -m ndcg -M 10 ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_2.res
start trec_eval.bat -m ndcg -M 10 ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_3.res
pause
start trec_eval.bat -m ndcg -M 10 ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_4.res
start trec_eval.bat -m ndcg -M 10 ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_5.res
start trec_eval.bat -m ndcg -M 10 ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_6.res
pause
start trec_eval.bat -m ndcg -M 10 ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_7.res
start trec_eval.bat -m ndcg -M 10 ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_8.res
start trec_eval.bat -m ndcg -M 10 ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_9.res

pause

:: The BEST run is the result from Skipgram with 700 hidden layers

start trec_eval.bat -m map -q ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_6.res