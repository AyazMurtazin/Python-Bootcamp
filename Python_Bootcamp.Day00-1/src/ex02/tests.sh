#!/bin/sh

echo "Вариант True:"
python3 mfinder.py < test_files/mfile.txt

echo "Вариант Ошибка:"
python3 mfinder.py < test_files/empty.txt

echo "Вариант False:"
python3 mfinder.py < test_files/notmfile.txt

echo "Вариант False:"
python3 mfinder.py < test_files/notmfile2.txt