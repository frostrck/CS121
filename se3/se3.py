"""
Short Exercises #3
"""

    

def find_candidates_from_city(candidates, office_loc):
    """
    Given a list of candidates, construct a list of the candidate IDs
    for candidates with a campaign headquartered in the specified location.

    Inputs:
      candidates: list of candidates
      office_loc (string, string): a tuple of the form (city name, state abbreviation)

    Returns: list of candidate IDs (strings)
    """

    ID = []

    city, state = office_loc
    for candidate in candidates:
      if candidate["City"] == city and candidate["State"] == state:
        ID.append(candidate["Candidate_ID"])
    return ID


def construct_dict_from_lists(keys, values):
    """
    Given a list of keys and a list of values of equal length,
    construct a dictionary that maps the ith key to the ith value.

    Inputs:
      keys: a list of (unique) immutable values (strings, ints, etc)
      values: a list of values

    Returns: dictionary
    """
    assert len(keys) == len(values)
    # check for repeats in the keys
    assert len(keys) == len(set(keys))

    dictionary = {}
    val = 0
    for key in keys:
      dictionary[key] = values[val]
      val += 1

    ### EXERCISE 2 -- Replace pass with your code
    return dictionary


def construct_homestate_dict(candidates):
    """
    Construct a dictionary that maps a candidate ID to the candidate's
    home state.

    Inputs:
      candidates: list of candidates

    Returns: dictionary that maps each candidate id (string) to a state
      abbreviation (string)
    """

    states = {}
    for candidate in candidates:
      states[candidate["Candidate_ID"]] = candidate["State"]
    return states


def find_unsuccessful_fund_raisers(cand_to_count, threshold):
    """
    Given a dictionary that maps candidate IDs to the number
    of donations received by the campaigns, compute a
    list of the candidates who have received strictly fewer than
    the threshold number of contributions.

    Inputs:
      cand_to_count: dictionary that maps Candidate IDs to integers
      threshold (int): the threshold for labelling a candidate as a unsuccessful.

    Returns: list of Candidate IDs.
    """
    ### EXERCISE 4 -- Replace pass with your code
    unsuccessful = []
    for cand in cand_to_count:
      if cand_to_count[cand] < threshold:
        unsuccessful.append(cand)
    return unsuccessful


def construct_cands_by_state(candidates):
    """
    Construct a mapping from states to the candidates from that state.

    Inputs:
      candidates: list of candidate dictionaries

    Returns: dictionary that maps a state abbreviation (string) to a
     list of dictionaries for candidates from that state.
    """

    states = []
    for candidate in candidates:
      if candidate["State"] not in states:
        states.append(candidate["State"])

    dictionary = {}
    for state in states:
      lst = []
      for candidate in candidates:
        if candidate["State"] == state:
          lst.append(candidate)
      dictionary[state] = lst

    
    return dictionary
