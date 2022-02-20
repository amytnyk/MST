echo 'Running benchmark ...'
python benchmark.py --vertex_count 260 --vertex_count_interval 100 --iters 30 --no_cache
echo 'Testing finished. Plotting ...'
python utils/visualizer.py