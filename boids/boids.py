"""
A deliberately bad implementation of 
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
This code simulates the swarming behaviour of bird-like objects ("boids").
"""

from matplotlib import pyplot as plt
from matplotlib import animation

import random

boids_x=[random.uniform(-450,50.0) for x in range(50)]
boids_y=[random.uniform(300.0,600.0) for x in range(50)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(50)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def update_boids(boids):

    x_coords,y_coords,x_velocities,y_velocities=boids
    
    move_away_range = 100 # If other boids fall within this range, move away from it
    match_speed_range  = 10000 # If other boids fall within this range, match speed with it

    for boid_1 in range(len(x_coords)):
        for boid_2 in range(len(x_coords)):

            # Fly towards the middle
            x_velocities[boid_1]=x_velocities[boid_1]+(x_coords[boid_2]-x_coords[boid_1])*0.01/len(x_coords)
            y_velocities[boid_1]=y_velocities[boid_1]+(y_coords[boid_2]-y_coords[boid_1])*0.01/len(x_coords)

            # Fly away from nearby boids
            if (x_coords[boid_2]-x_coords[boid_1])**2 + (y_coords[boid_2]-y_coords[boid_1])**2 < move_away_range:
                x_velocities[boid_1]=x_velocities[boid_1]+(x_coords[boid_1]-x_coords[boid_2])
                y_velocities[boid_1]=y_velocities[boid_1]+(y_coords[boid_1]-y_coords[boid_2])

            # Try to match speed with nearby boids
            if (x_coords[boid_2]-x_coords[boid_1])**2 + (y_coords[boid_2]-y_coords[boid_1])**2 < match_speed_range:
                x_velocities[boid_1]=x_velocities[boid_1]+(x_velocities[boid_2]-x_velocities[boid_1])*0.125/len(x_coords)
                y_velocities[boid_1]=y_velocities[boid_1]+(y_velocities[boid_2]-y_velocities[boid_1])*0.125/len(x_coords)

        # Move according to velocities
        x_coords[boid_1]=x_coords[boid_1]+x_velocities[boid_1]
        y_coords[boid_1]=y_coords[boid_1]+y_velocities[boid_1]

    new_boids = (x_coords, y_coords, x_velocities, y_velocities)

    return(new_boids)
