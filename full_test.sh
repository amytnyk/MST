echo 'Running full test'
echo 'Validating ...'
python validator.py
echo 'Validating finished. Running benchmark ...'
python test.py --vertex_count 1000 --vertex_count_interval 10 --iters 100
echo 'Testing finished. Plotting ...'
python visualizer.py