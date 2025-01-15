# dfa-samplers

This repo implements samplers for Deterministic Finite Automata (DFA) represented in [mvc format](https://github.com/mvcisback/dfa).

## Installation

```
pip install dfa-samplers
```

## Usage

```
from dfa_samplers import RADSampler, ReachSampler, ReachAvoidSampler

if __name__ == "__main__":
    rad_sampler = RADSampler()
    reach_sampler = ReachSampler()
    reach_avoid_sampler = ReachAvoidSampler()
    rad_dfa = rad_sampler.sample() # Returns a reach-avoid derived DFA
    reach_dfa = reach_sampler.sample() # Returns a reach DFA
    reach_avoid_dfa = reach_avoid_sampler.sample() # Returns a reach-avoid DFA
```
