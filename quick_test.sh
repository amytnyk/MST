echo 'Running quick test'
echo 'Validating ...'
python validator.py
echo 'Validating finished. Running benchmark ...'
python test.py --vertex_count 260 --vertex_count_interval 100 --iters 30
echo 'Testing finished. Plotting ...'
python visualizer.py