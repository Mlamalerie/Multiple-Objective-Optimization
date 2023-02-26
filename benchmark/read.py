import ast
import numpy as np
import os

#  [http://home.ku.edu.tr/~moolibrary/](http://home.ku.edu.tr/~moolibrary/)
PATH = os.path.dirname(os.path.abspath(__file__))


def list_benchmarks(name, benchmarks_path=PATH):
    """List all benchmarks in a directory.
    Args:
        name (str): Name of the benchmark. E.g. "kp" for knapsack.
        benchmarks_path (str): Path to the benchmarks directory.
    Returns:
        list: List of benchmarks.
    """
    return os.listdir(os.path.join(benchmarks_path, name))


def read_kp_benchmark(p: int, n: int, instance: int = 1, verbose: bool = True):
    # set file name
    file_path = f"{PATH}/kp/KP_p-{p}_n-{n}_ins-{instance}.dat"
    # verify if file exists
    if not os.path.exists(file_path):
        # get list of files in directory
        files = os.listdir("kp")
        # filter files with the same p and n
        files = [file for file in files if f"p-{p}" in file]
        # raise error message, list of available files
        raise FileNotFoundError(f"File {file_path} not found. \nAvailable files with p={p} are: {files}")

    with open(file_path, "r") as f:
        n_objective_functions, n_objects, max_weight_constraint, *goals_values, objects_weights = f.read().splitlines()

    n_objective_functions: int = int(n_objective_functions)
    n_objects: int = int(n_objects)
    max_weight_constraint: int = int(max_weight_constraint)
    profits_matrix: np.ndarray = np.array(ast.literal_eval("".join(goals_values)))
    objects_weights: np.ndarray = np.array(ast.literal_eval(objects_weights))
    if verbose:
        print("Number of objective functions (p) :", n_objective_functions)
        print("Number of objects (n) :", n_objects)
        print("Capacity of the knapsack (W) :", max_weight_constraint)
        print("Profits of the objects in each objective function :", profits_matrix)
        print("Weights of the objects (w)", objects_weights)
    return {"n_objective_functions": n_objective_functions, "n_objects": n_objects,
            "max_weight_constraint": max_weight_constraint, "profits_matrix": profits_matrix,
            "objects_weights": objects_weights}


data = read_kp_benchmark(4, 10, 1)
