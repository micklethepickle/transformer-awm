from ml_collections import ConfigDict


def get_config():
    config = ConfigDict()
    
    config.alg = 'arm'
    config.chunk_length = -1
    config.unroll_length = -1
    config.num_steps = 5000
    config.warmup_steps = 500
    config.update_every = 2
    config.batch_size = 32
    config.policy_batch_size = 8
    config.eval_every = 5
    config.action_repeat = 1
    config.network_sizes = (64, 64)
    config.epsilon = 0.9
    config.bp_discount = 0.99
    config.discount = 0.99
    config.bootstrap = 0
    config.entropy_init = 0.001
    config.entropy_decay_rate = 1
    config.entropy_transition_steps = 100
    config.dynamics_lr = 0.001
    config.policy_lr = 0.001
    config.critic_lr = 0.001
    config.tau = 0.005
    config.grad_clip = 10
    config.buffer_max = int(1e6)
    config.embd_dim = 48
    config.reset_every = 0
    config.input_observations = False
    config.sequence_model_name = 'lstm'
    
    return config

