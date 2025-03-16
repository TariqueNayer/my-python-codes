import copy
import random

class Hat:
    def __init__(self, **args):
        #taking arguments
        for k,v in args.items():
            setattr(self,k,v)
        
        #making contents
        self.contents = []
        for k,v in args.items():
            for _ in range(v):
                self.contents.append(k)

    def draw(self, no_ball):
        if no_ball > len(self.contents):
            all_balls = self.contents
            self.contents = []
            return all_balls
        all_balls = []
        #Drawing balls out
        for _ in range(no_ball):
            ball = random.choice(self.contents)
            self.contents.remove(ball)
            temp = getattr(self,ball) - 1
            setattr(self,ball,temp)
            all_balls.append(ball)
        
        return all_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    prob = 0
    

    
    for _ in range(num_experiments):
        success = False
        temphat = copy.deepcopy(hat)
        myballs = temphat.draw(num_balls_drawn)

        draw_count = {}
        for ball in myballs:
            draw_count[ball] = draw_count.get(ball,0) + 1
        
        if all([ball in draw_count and draw_count[ball] >= count for ball,count in expected_balls.items()]):
            prob += 1
        
    return prob/num_experiments

if __name__ == "__main__":
    hat = Hat(black=6, red=4, green=3)
    probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
    print(probability)
    
