import hashlib

from planner.cbs_ext.plan import plan, generate_config
from planner.cbs_ext_test import get_data_random
from planner.eval.eval_comparison_test import get_map_str
from planner.eval.eval_scenarios import get_costs
from planner.milp.milp import plan_milp
from tools import load_map
from planner.eval.display import *
from mpl_toolkits.mplot3d import Axes3D

params = get_data_random(20,
                         map_res=8,
                         map_fill_perc=20,
                         agent_n=4,
                         job_n=4,
                         idle_goals_n=0)
agent_pos, grid, idle_goals, jobs = params

mapstr = get_map_str(grid)
maphash = str(hashlib.md5(mapstr.encode('utf-8')).hexdigest())[:8]
fname = "planner/eval/cache/" + str(maphash) + '.pkl'  # unique filename based on map
config = generate_config()
config['filename_pathsave'] = fname
#
# tcbs_agent_job, tcbs_agent_idle, tcbs_paths = plan(
#     agent_pos, jobs, [], [], grid, config, plot=False
# )
#
# minlp_agent_job, minlp_paths = plan_milp(agent_pos, jobs, grid, config)

# print((
#     tcbs_paths, tcbs_agent_job,
#     minlp_paths, minlp_agent_job,
#     agent_pos, jobs
# ))
# ([([(1, 3, 0), (1, 4, 1), (0, 4, 2), (0, 5, 3), (0, 6, 4), (1, 6, 5), (2, 6, 6)], [(2, 6, 7), (1, 6, 8), (0, 6, 9), (0, 5, 10), (0, 4, 11), (0, 3, 12), (0, 2, 13), (1, 2, 14)]), ([(3, 0, 0), (3, 1, 1), (2, 1, 2)], [(2, 1, 3), (2, 2, 4), (1, 2, 5), (1, 3, 6), (0, 3, 7), (0, 4, 8)], [(0, 4, 9), (0, 4, 10), (0, 4, 12), (0, 4, 13), (0, 4, 14)]), ([(3, 1, 0), (3, 2, 1), (3, 3, 2)], [(3, 3, 3), (3, 2, 4), (4, 2, 5)], [(4, 2, 6), (4, 2, 7), (4, 2, 8), (4, 2, 9), (4, 2, 10), (4, 2, 11), (4, 2, 12), (4, 2, 13), (4, 2, 14)]), ([(4, 4, 0), (4, 5, 1), (4, 6, 2), (4, 7, 3), (5, 7, 4)], [(5, 7, 5), (5, 6, 6), (4, 6, 7), (4, 5, 8), (4, 4, 9), (4, 3, 10), (5, 3, 11), (5, 2, 12), (6, 2, 13)], [(6, 2, 14)])], ((3,), (0,), (1,), (2,)), [([(1, 3, 0), (1, 4, 1), (0, 4, 2), (0, 5, 3), (0, 6, 4), (1, 6, 5), (2, 6, 6)], [(2, 6, 7), (1, 6, 8), (0, 6, 9), (0, 5, 10), (0, 4, 11), (0, 3, 12), (0, 2, 13), (1, 2, 14)]), ([(3, 0, 0), (3, 1, 1), (3, 2, 2), (3, 3, 3)], [(3, 3, 4), (3, 2, 5), (4, 2, 6)], [(4, 2, 7), (4, 2, 8), (4, 2, 9), (4, 2, 10), (4, 2, 11), (4, 2, 12), (4, 2, 13), (4, 2, 14)]), ([(3, 1, 0), (2, 1, 1)], [(2, 1, 2), (2, 2, 3), (1, 2, 4), (1, 3, 5), (0, 3, 6), (0, 4, 7)], [(0, 4, 8), (0, 4, 9), (0, 4, 10), (0, 4, 12), (0, 4, 13), (0, 4, 14)]), ([(4, 4, 0), (4, 5, 1), (4, 6, 2), (4, 7, 3), (5, 7, 4)], [(5, 7, 5), (5, 6, 6), (4, 6, 7), (4, 5, 8), (4, 4, 9), (4, 3, 10), (5, 3, 11), (5, 2, 12), (6, 2, 13)], [(6, 2, 14)])], [(3,), (1,), (0,), (2,)], [(1, 3), (3, 0), (3, 1), (4, 4)], [((2, 1), (0, 4), 4), ((3, 3), (4, 2), 4), ((5, 7), (6, 2), 2), ((2, 6), (1, 2), 1)])

(
    tcbs_paths, tcbs_agent_job,
    minlp_paths, minlp_agent_job,
    agent_pos, jobs
) = ([([(1, 3, 0), (1, 4, 1), (0, 4, 2), (0, 5, 3), (0, 6, 4), (1, 6, 5), (2, 6, 6)],
       [(2, 6, 7), (1, 6, 8), (0, 6, 9), (0, 5, 10), (0, 4, 11), (0, 3, 12), (0, 2, 13), (1, 2, 14)]), (
      [(3, 0, 0), (3, 1, 1), (2, 1, 2)], [(2, 1, 3), (2, 2, 4), (1, 2, 5), (1, 3, 6), (0, 3, 7), (0, 4, 8)],
      [(0, 4, 9), (0, 4, 10), (0, 4, 12), (0, 4, 13), (0, 4, 14)]), (
      [(3, 1, 0), (3, 2, 1), (3, 3, 2)], [(3, 3, 3), (3, 2, 4), (4, 2, 5)],
      [(4, 2, 6), (4, 2, 7), (4, 2, 8), (4, 2, 9), (4, 2, 10), (4, 2, 11), (4, 2, 12), (4, 2, 13), (4, 2, 14)]), (
      [(4, 4, 0), (4, 5, 1), (4, 6, 2), (4, 7, 3), (5, 7, 4)],
      [(5, 7, 5), (5, 6, 6), (4, 6, 7), (4, 5, 8), (4, 4, 9), (4, 3, 10), (5, 3, 11), (5, 2, 12), (6, 2, 13)],
      [(6, 2, 14)])], ((3,), (0,), (1,), (2,)), [([(1, 3, 0), (1, 4, 1), (0, 4, 2), (0, 5, 3), (0, 6, 4), (1, 6, 5),
                                                   (2, 6, 6)],
                                                  [(2, 6, 7), (1, 6, 8), (0, 6, 9), (0, 5, 10), (0, 4, 11), (0, 3, 12),
                                                   (0, 2, 13), (1, 2, 14)]), (
                                                 [(3, 0, 0), (3, 1, 1), (3, 2, 2), (3, 3, 3)],
                                                 [(3, 3, 4), (3, 2, 5), (4, 2, 6)],
                                                 [(4, 2, 7), (4, 2, 8), (4, 2, 9), (4, 2, 10), (4, 2, 11), (4, 2, 12),
                                                  (4, 2, 13), (4, 2, 14)]), ([(3, 1, 0), (2, 1, 1)],
                                                                             [(2, 1, 2), (2, 2, 3), (1, 2, 4),
                                                                              (1, 3, 5), (0, 3, 6), (0, 4, 7)],
                                                                             [(0, 4, 8), (0, 4, 9), (0, 4, 10),
                                                                              (0, 4, 12), (0, 4, 13), (0, 4, 14)]), (
                                                 [(4, 4, 0), (4, 5, 1), (4, 6, 2), (4, 7, 3), (5, 7, 4)],
                                                 [(5, 7, 5), (5, 6, 6), (4, 6, 7), (4, 5, 8), (4, 4, 9), (4, 3, 10),
                                                  (5, 3, 11), (5, 2, 12), (6, 2, 13)], [(6, 2, 14)])],
     [(3,), (1,), (0,), (2,)], [(1, 3), (3, 0), (3, 1), (4, 4)],
     [((2, 1), (0, 4), 4), ((3, 3), (4, 2), 4), ((5, 7), (6, 2), 2), ((2, 6), (1, 2), 1)])

get_costs(tcbs_paths, jobs, tcbs_agent_job, True)
get_costs(minlp_paths, jobs, minlp_agent_job, True)

f = plt.figure()
f.set_size_inches(8, 4.5)
ani = animate_results(
    f, [], tcbs_paths, tcbs_agent_job, agent_pos, grid, [], jobs, 'TCBS'
)
ani.save("planner/eval/random_tcbs.mp4", writer="ffmpeg", fps=10)

f = plt.figure()
f.set_size_inches(8, 4.5)
ani = animate_results(
    f, [], minlp_paths, minlp_agent_job, agent_pos, grid, [], jobs, 'MINLP'
)
ani.save("planner/eval/random_minlp.mp4", writer="ffmpeg", fps=10)
