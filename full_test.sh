echo 'Running benchmark ...'
python benchmark.py --vertex_count 1000 --vertex_count_interval 10 --iters 100
echo 'Testing finished. Plotting ...'
python utils/visualizer.py