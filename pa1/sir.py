'''
Epidemic modelling

YOUR NAME

Functions for running a simple epidemiological simulation
'''

import random
import click

# This seed should be used for debugging purposes only!  Do not refer
# to it in your code.
TEST_SEED = 20170217

def count_infected(city):
    '''
    Count the number of infected people

    Inputs:
      city (list of strings): the state of all people in the
        simulation at the start of the day
    Returns (int): count of the number of people who are
      currently infected
    '''
    num_infected = 0
    for i in range(0, len(city)):
      if city[i][0] == "I":
        num_infected +=1

    # REPLACE -1 WITH THE APPROPRIATE INTEGER
    return num_infected


def has_an_infected_neighbor(city, position):
    '''
    Determine whether a person has an infected neighbor

    Inputs:
      city (list): the state of all people in the simulation at the
        start of the day
      position (int): the position of the person to check

    Returns:
      True, if the person has an infected neighbor, False otherwise.
    '''

    # This function should only be called when the person at position
    # is susceptible to infection.
    assert city[position] == "S"

    infected_neighbor = None
    
    if len(city) >= 2:
      if (position >= 1) and (position < len(city)-1):
        neighbors = [city[position -1], city[position], city[position+1]]
      elif position == 0:
        neighbors = [city[position], city[position+1]]
      else:
        neighbors = [city[position -1], city[position]]

      if count_infected(neighbors) >= 1:
        infected_neighbor = True
      else:
        infected_neighbor = False
    else:
      neighbors = city
      if count_infected(neighbors) >= 1:
        infected_neighbor = True
      else:
        infected_neighbor = False
    
  
        
    # YOUR CODE HERE

    # REPLACE None WITH THE APPROPRIATE BOOLEAN VALUE
    return infected_neighbor


def advance_person_at_position(city, position, days_contagious):
    '''
    Compute the next state for the person at the specified position.

    Inputs:
      city (list): the state of all people in the simulation at the
        start of the day
      position (int): the position of the person to check
      days_contagious (int): the number of a days a person is infected

    Returns: (string) disease state of the person after one day
    '''
    # YOUR CODE HERE
    status = None
    if city[position] == "S":
      if has_an_infected_neighbor(city, position) == True :
        status = "I0"
      else:
        status = "S"
    elif city[position] == "R":
      status = "R"
    elif city[position] == "V":
      status = "V"
    else:
      days_infected = None
      if int(city[position][1:]) + 1 < days_contagious:
        days_infected = int(city[position][1:]) + 1
        status = "I{:1d}".format(days_infected)
      else:
        status = "R"
    # REPLACE None WITH THE APPROPRIATE STRING
    return status

def simulate_one_day(starting_city, days_contagious):
    '''
    Move the simulation forward a single day.

    Inputs:
      starting_city (list): the state of all people in the simulation at the
        start of the day
      days_contagious (int): the number of a days a person is infected

    Returns:
      new_city (list): disease state of the city after one day
    '''
    new_city = []
    for i in range(0,len(starting_city)):
      new_city.append(advance_person_at_position(starting_city, i, days_contagious))
    # YOUR CODE HERE

    # REPLACE None WITH THE APPROPRIATE LIST OF STRINGS
    return new_city


def run_simulation(starting_city, days_contagious,
                   random_seed=None, vaccine_effectiveness=0.0):
    '''
    Run the entire simulation
    
    Inputs:
      starting_city (list): the state of all people in the city at the
        start of the simulation
      days_contagious (int): the number of a days a person is infected
      random_seed (int): the random seed to use for the simulation
      vaccine_effectiveness (float): the chance that a vaccination will be
        effective

    Returns tuple (list of strings, int): the final state of the city
      and the number of days actually simulated.
    '''

    # YOUR CODE HERE
    days_passed = 0
    new_day = starting_city
    random.seed(TEST_SEED)
    new_day = vaccinate_city(starting_city, vaccine_effectiveness)

    while count_infected(new_day) > 0:
      new_day = vaccinate_city(new_day, vaccine_effectiveness)
      new_day = simulate_one_day(new_day, days_contagious)
      days_passed += 1

    # REPLACE (None, None) WITH THE APPROPRIATE TUPLE
    #  (city, number of days simulated)
    return (new_day, days_passed)


def vaccinate_city(starting_city, vaccine_effectiveness):
    '''
    Vaccinate everyone in a city

    Inputs:
      starting_city (list): the state of all people in the simulation at the
        start of the simulation
      vaccine_effectiveness (float): the chance that a vaccination will be
        effective

    Returns:
      new_city (list): state of the city after vaccinating everyone in the city
    '''
    
    # YOUR CODE HERE
    new_city =[]
    for i in range(0, len(starting_city)):
      if starting_city[i] == "S":
        rand = random.random()
        if rand < vaccine_effectiveness:
          new_city.append("V")
        else:
          new_city.append("S")
      else:
        new_city.append(starting_city[i])


    # REPLACE None WITH THE APPROPRIATE LIST OF STRINGS
    return new_city


def calc_avg_days_to_zero_infections(
        starting_city, days_contagious,
        random_seed, vaccine_effectiveness,
        num_trials):
    '''
    Conduct N trials with the specified vaccine effectiveness and
    calculate the average number of days for a city to reach zero
    infections

    Inputs:
      starting_city (list): the state of all people in the city at the
        start of the simulation
      days_contagious (int): the number of a days a person is infected
      random_seed (int): the starting random seed. Use this value for
        the FIRST simulation, and then increment it once for each
        subsequent run.
      vaccine_effectiveness (float): the chance that a vaccination will be
        effective
      num_trials (int): the number of trials to run

    Returns (float): the average number of days for a city to reach zero
      infections
    '''
    assert num_trials > 0

    # YOUR CODE HERE

    # REPLACE -1.0 WITH THE APPROPRIATE FLOATING POINT VALUE
    return -1.0


################ Do not change the code below this line #######################


@click.command()
@click.argument("city", type=str)
@click.option("--days-contagious", default=2, type=int)
@click.option("--random_seed", default=None, type=int)
@click.option("--vaccine-effectiveness", default=0.0, type=float)
@click.option("--num-trials", default=1, type=int)
@click.option("--task-type", default="single",
              type=click.Choice(['single', 'average']))
def cmd(city, days_contagious, random_seed, vaccine_effectiveness,
        num_trials, task_type):
    '''
    Process the command-line arguments and do the work.
    '''

    # Convert the city string into a city list.
    city = [p.strip() for p in city.split(",")]
    emsg = ("Error: people in the city must be susceptible ('S'),"
            " recovered ('R'), or infected ('Ix', where *x* is an integer")
    for p in city:
        if p[0] == "I":
            try:
                _ = int(p[1])
            except ValueError:
                print(emsg)
                return -1
        elif p not in {"S", "R"}:
            print(emsg)
            return -1

    if task_type == "single":
        print("Running one simulation...")
        final_city, num_days_simulated = run_simulation(
            city, days_contagious, random_seed, vaccine_effectiveness)
        print("Final city:", final_city)
        print("Days simulated:", num_days_simulated)
    else:
        print("Running multiple trials...")
        avg_days = calc_avg_days_to_zero_infections(
            city, days_contagious, random_seed, vaccine_effectiveness,
            num_trials)
        msg = ("Over {} trial(s), on average, it took {:3.1f} days for the "
               "number of infections to reach zero")
        print(msg.format(num_trials, avg_days))

    return 0


if __name__ == "__main__":
    cmd()  # pylint: disable=no-value-for-parameter
