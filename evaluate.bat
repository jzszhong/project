start trec_terrier.bat -r -Dtrec.model=TF_IDF -c 0.4 -Dtrec.topics=../../project/topics.trec
start trec_terrier.bat -r -Dtrec.model=BM25 -c 0.4 -Dtrec.topics=../../project/topics.trec

pause

start trec_eval.bat -m map ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_0.res
start trec_eval.bat -m map ../../project/trec123.51-200.ap8889.qrels ../var/results/BM25b0.4_0.res

pause

start trec_eval.bat -m gm_map ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_0.res
start trec_eval.bat -m gm_map ../../project/trec123.51-200.ap8889.qrels ../var/results/BM25b0.4_0.res

pause

start trec_eval.bat -m set_P -M 10 ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_0.res
start trec_eval.bat -m set_P -M 10 ../../project/trec123.51-200.ap8889.qrels ../var/results/BM25b0.4_0.res

pause

start trec_eval.bat -m ndcg -M 10 ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_0.res
start trec_eval.bat -m ndcg -M 10 ../../project/trec123.51-200.ap8889.qrels ../var/results/BM25b0.4_0.res

pause

start trec_eval.bat -m map -q ../../project/trec123.51-200.ap8889.qrels ../var/results/TF_IDF_0.res
start trec_eval.bat -m map -q ../../project/trec123.51-200.ap8889.qrels ../var/results/BM25b0.4_0.res