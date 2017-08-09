DIC_FOLDER=./dic

init:
	./cfg.py

clean: 
	rm -f $(DIR_FOLDER)/*

.PHONY: init
