import pickle
import neat
import os
from _MachiKoro import *
from _Players import *

def eval_genomes(genomes, config):
    """
    Run each genome against eachother one time to determine the fitness.
    """
    for i, (genome_id, genome) in enumerate(genomes):
        genome.fitness = 0 #if genome.fitness == None else genome.fitness
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        training_player = NEAT_Player("AI TRAINING", nn=net)
        AI_Game_1 = TossUp (players= [training_player])
        for i in range(100): 
            AI_Game_1.Play()

        genome.fitness += (25 - training_player.turns)



def run_neat(config):
    #p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-9')
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))

    winner = p.run(eval_genomes, 25)

    with open("NN_Best.pickle", "wb") as f:
        pickle.dump(winner, f)

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)

    run_neat(config)