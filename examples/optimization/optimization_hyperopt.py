import argparse
import json
import logging
import time

from hyperopt import hp, fmin, tpe, space_eval, STATUS_OK, Trials
import hyperopt.pyll.stochastic

LOG = logging.getLogger("examples")


def hyperopt_example0(args: argparse.Namespace) -> None:
    space = hp.choice('a',
                      [
                          ('case 1', 1 + hp.lognormal('c1', 0, 1)),
                          ('case 2', hp.uniform('c2', -10, 10))
                      ])
    for i in range(5):
        LOG.info(f"Space sample {i + 1}: {hyperopt.pyll.stochastic.sample(space)}")


# define an objective function
def objective_1(args):
    case, val = args
    if case == 'case 1':
        return val
    else:
        return val ** 2


def hyperopt_example1(args: argparse.Namespace) -> None:
    LOG.info("Running hyperopt_example1")

    # define a search space
    space = hp.choice('a',
                      [
                          ('case 1', 1 + hp.lognormal('c1', 0, 1)),
                          ('case 2', hp.uniform('c2', -10, 10))
                      ])

    # minimize the objective over the space
    best = fmin(objective_1, space, algo=tpe.suggest, max_evals=100)

    LOG.info(f"Best value: {best}")
    LOG.info(f"Space val: {space_eval(space, best)}")
    return


def hyperopt_example2(args: argparse.Namespace) -> None:
    LOG.info("Running hyperopt_example2")

    best = fmin(fn=lambda x: x ** 2,
                space=hp.uniform('x', -10, 10),
                algo=tpe.suggest,
                max_evals=100)
    LOG.info(f"Best value: {best}")


def objective_3(x):
    loss = x ** 2
    LOG.info(f"objective_3: x={x} => loss={loss}")
    return {
        'loss': loss,
        'status': STATUS_OK,
        # -- store other results like this
        'eval_time': time.time(),
        'other_stuff': {'type': None, 'value': [0, 1, 2]},
    }


def hyperopt_example3(args: argparse.Namespace) -> None:
    LOG.info("Running hyperopt_example3")

    trials = Trials()
    best = fmin(objective_3,
                space=hp.uniform('x', -10, 10),
                algo=tpe.suggest,
                max_evals=10,
                trials=trials)

    LOG.info(f"Best value: {best}")
    for trial in trials.trials:
        print(trial)
    for i, loss in enumerate(trials.losses()):
        print(f"Itr. {i}: loss={loss}")
