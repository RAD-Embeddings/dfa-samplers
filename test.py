from dfa_samplers import RADSampler, ReachSampler, ReachAvoidSampler

if __name__ == "__main__":
    rad_sampler = RADSampler()
    reach_sampler = ReachSampler()
    reach_avoid_sampler = ReachAvoidSampler()
    for _ in range(100):
        assert rad_sampler.sample().find_word() is not None
        assert reach_sampler.sample().find_word() is not None
        assert reach_avoid_sampler.sample().find_word() is not None

    a = 10
    b = 20
    rad_sampler = RADSampler(min_size=a, max_size=b)
    reach_sampler = ReachSampler(min_size=a, max_size=b)
    reach_avoid_sampler = ReachAvoidSampler(min_size=a, max_size=b)
    for _ in range(100):
        n_rad = len(rad_sampler.sample().states())
        n_reach = len(reach_sampler.sample().states())
        n_reach_avoid = len(reach_avoid_sampler.sample().states())
        assert n_rad >= a and n_rad <= b
        assert n_reach >= a and n_reach <= b
        assert n_reach_avoid >= a and n_reach_avoid <= b
