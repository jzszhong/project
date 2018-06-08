:: This should be run in cmd in the Terrier¡¯s bin directory which is outside the project folder, otherwise there would be errors

start trec_setup.bat ../../project/AP8889

pause

start trec_terrier.bat -i -Dtermpipelines=Stopwords

pause

start trec_terrier.bat --printstats