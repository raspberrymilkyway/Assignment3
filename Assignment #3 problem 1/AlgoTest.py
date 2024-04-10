import time
import matplotlib.pyplot as plt
from problem_2 import generate_graph

def algorithm_problem_2(n, m):
    generate_graph(n, m)
    pass

n_values = range(3, 100, 5)
m_values = range(3, 100, 5)


n_times = []
m_times = []
n_m_times = []

for n in n_values:
    start_time = time.perf_counter()
    algorithm_problem_2(n, 3)
    end_time = time.perf_counter()
    n_times.append(end_time - start_time)

for m in m_values:
    start_time = time.perf_counter()
    algorithm_problem_2(3, m)
    end_time = time.perf_counter()
    m_times.append(end_time - start_time)

for n, m in zip(n_values, m_values):
    start_time = time.perf_counter()
    algorithm_problem_2(n, m)
    end_time = time.perf_counter()
    n_m_times.append(end_time - start_time)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)
fig.suptitle('Algorithm Running Time Analysis')

ax1.plot(n_values, n_times, label='RunningTime')
ax1.set_title('Increasing "n"')
ax2.plot(m_values, m_times, label='RunningTime')
ax2.set_title('Increasing "m"')
ax3.plot(n_values, n_m_times, label='Running Time')
ax3.set_title('Increasing "n" and "m"')
ax4.set_axis_off()

for ax in fig.get_axes():
    ax.set(xlabel='Variable Size', ylabel='Time (seconds)')
    ax.label_outer()
fig.set_size_inches(19.2, 10.8)
fig.show()
