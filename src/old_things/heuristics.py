from collections import Counter, defaultdict
from random import choice


def graphs(vnames, vals, depots, g):
    res = []
    dsol = {vnames[i]: vals[i] for i in range(len(vals))}
    for bn in depots:
        res.append(defaultdict(lambda: []))
        for v1 in g:
            for v2 in g[v1]:
                if dsol["bus_edge_" + str(bn) + "_" + str(v1) + "_" + str(v2)] > 0.5:
                    res[-1][v1].append(v2)
    return res


def alternative_graphs(vnames, vals, depots, g):
    res = defaultdict(lambda: {})
    dsol = {vnames[i]: vals[i] for i in range(len(vals))}
    for v1 in g:
        for v2 in g[v1]:
            if dsol["edge_" + str(v1) + "_" + str(v2)] > 0.5:
                res[v1][v2] = g[v1][v2][1]
    return res


def heuristic_sbrp(g, bs, sp):
    paths = [[b] for b in bs]
            
    not_seen = set([v for v in g if v not in bs + [sp]])
    while len(not_seen) > 0:
        min_dist = float('inf')
        for path in paths:
            for v in not_seen:
                if g[path[-1]][v] < min_dist:
                    min_dist = g[path[-1]][v]
                    min_dist_pair = (path[-1], v)
        for path in paths:
            if min_dist_pair[0] == path[-1]:
                path.append(min_dist_pair[1])
                not_seen.remove(min_dist_pair[1])
    print(paths)

    onvars = []

    for path in paths:
        for i in range(len(path) - 1):
            onvars.append(
                "bus_edge_" + str(path[0]) + "_" + str(path[i]) + "_" + str(path[i + 1]))
        onvars.append(
            "bus_edge_" + str(path[0]) + "_" + str(path[-1]) + "_" + str(sp))

    varsnames = ["bus_edge_" + str(bn) + "_" + str(v1) + "_" + str(v2)
                 for bn in bs for v1 in g for v2 in g]
    varsvals = [1 if varsnames[i]
                in onvars else 0 for i in range(len(varsnames))]

    return [varsnames, varsvals]


def heuristic_alternative(stops, students, maxw, std_stp,
                          stp_std, depots, capacity, g):

    student_stop_res = {i: choice(std_stp[i]) for i in range(len(students))}
    # print(student_stop_res)
    stops_load_res = {v: len([y for x, y in student_stop_res.items(
    ) if y == v]) for k, v in student_stop_res.items()}

    paths = [[b] for b in depots]
    path_loads = [stops_load_res[b] for b in depots]
    not_seen = set([v for v in stops_load_res if v not in depots])
    while len(not_seen) > 0:
        min_dist = float('inf')
        for path_i in range(len(paths)):
            for v in not_seen:
                if g[paths[path_i][-1]][v] < min_dist and path_loads[path_i] + stops_load_res[v] <= capacity:
                    min_dist = g[paths[path_i][-1]][v]
                    min_dist_pair = (paths[path_i][-1], v)
        for path_i in range(len(paths)):
            if min_dist_pair[0] == paths[path_i][-1]:
                path_loads[path_i] += stops_load_res[min_dist_pair[1]]
                paths[path_i].append(min_dist_pair[1])
                not_seen.remove(min_dist_pair[1])
    print(paths)

    onvars = ["student_stop_" + str(i) + '_' + str(student_stop_res[i])
              for i in range(len(students))]

    for path in paths:
        for i in range(len(path) - 1):
            onvars.append(
                "edge_" + str(path[i]) + "_" + str(path[i + 1]))
        onvars.append(
            "edge_" + str(path[-1]) + "_" + str(0))

    varsnames = ["student_stop_" + str(i) + '_' + str(st)
                 for i in range(len(students)) for st in std_stp[i]] + \
        ["edge_" + str(v1) + "_" + str(v2)
         for v1 in g for v2 in g]
    varsvals = [1 if varsnames[i]
                in onvars else 0 for i in range(len(varsnames))]

    # print(onvars)
    return [varsnames, varsvals]


def heuristic_alternative_2(stops, students, max_walk_dist, std_stp, stp_std,
                            clusters, stop_to_stop_cluster, depots, capacity, g):

    stop_load = {k: 0 for k in g}
    varsnames = []
    varsvals = []

    # print(stop_to_stop_cluster)
    # print(clusters)
    vars = {'students_stop_cluster_' +
            str(v) + '_' + str(c): 0 for v in g for c in stop_to_stop_cluster[v]}
    # vars.update({'stopload_' + str(v):0 for v in g})
    for c in clusters:
        distribution = Counter([choice(c) for i in range(clusters[c])])
        for v, k in distribution.items():
            stop_load[v] += k
            # vars['stopload_' + str(v)] += k
            vars['students_stop_cluster_' + str(v) + '_' + str(c)] += k

    paths = [[b] for b in depots]
    path_loads = [stop_load[b] for b in depots]
    not_seen = set([v for v in stop_load if v not in depots + [0]])
    while len(not_seen) > 0:
        # print(paths)
        min_dist = float('inf')
        for path_i in range(len(paths)):
            for v in not_seen:
                if g[paths[path_i][-1]][v][0] < min_dist and path_loads[path_i] + stop_load[v] <= capacity:
                    min_dist = g[paths[path_i][-1]][v][0]
                    min_dist_pair = (paths[path_i][-1], v)
        for path_i in range(len(paths)):
            if min_dist_pair[0] == paths[path_i][-1]:
                path_loads[path_i] += stop_load[min_dist_pair[1]]
                paths[path_i].append(min_dist_pair[1])
                not_seen.remove(min_dist_pair[1])
    paths = [p + [0] for p in paths]
    # print(paths)
    # print(path_loads)
    # print(not_seen)

    vars.update({'edge_' + str(v) + '_' + str(v2): 0 for v in g for v2 in g})
    for path in paths:
        for i in range(1, len(path)):
            vars['edge_' + str(path[i - 1]) + '_' + str(path[i])] = 1

    # for v in vars:
    #     if vars[v] > 0.5:
    #         print(v, vars[v])

    return [[k for k, v in vars.items()], [v for k, v in vars.items()]]



def insertion_heuristic(stops, students, max_walk_dist, std_stp, stp_std,
                        clusters, stop_to_stop_cluster, depots, capacity, g):
    paths = [[d, 0] for d in depots]
    not_added = set([s for s in range(len(stops)) if s not in depots + [0]])
    print(paths)

    while len(not_added) > 0:
        min_cost = (float('inf'),)
        for v in not_added:
            # print("INSERTANDO",v)
            for pi in range(len(paths)):
                p = paths[pi]
                # print("EN CAMINO",p)
                for i in range(1, len(p)):
                    c = g[p[i - 1]][v] + g[v][p[i]] - g[p[i - 1]][p[i]]
                    min_cost = min((c, v, pi, i), min_cost)
                    # print(p, i, v, c)
        c, v, pi, i = min_cost
        paths[pi] = paths[pi][:i] + [v] + paths[pi][i:]
        not_added.remove(v)

    vars = {'edge_' + str(v1) + '_' + str(v2)}
