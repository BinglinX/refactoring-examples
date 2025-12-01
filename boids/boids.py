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
    
    for i in range(len(x_coords)):
        for j in range(len(x_coords)):

            # Fly towards the middle
            x_velocities[i]=x_velocities[i]+(x_coords[j]-x_coords[i])*0.01/len(x_coords)
            y_velocities[i]=y_velocities[i]+(y_coords[j]-y_coords[i])*0.01/len(x_coords)

            # Fly away from nearby boids
            if (x_coords[j]-x_coords[i])**2 + (y_coords[j]-y_coords[i])**2 < 100:
                x_velocities[i]=x_velocities[i]+(x_coords[i]-x_coords[j])
                y_velocities[i]=y_velocities[i]+(y_coords[i]-y_coords[j])

            # Try to match speed with nearby boids
            if (x_coords[j]-x_coords[i])**2 + (y_coords[j]-y_coords[i])**2 < 10000:
                x_velocities[i]=x_velocities[i]+(x_velocities[j]-x_velocities[i])*0.125/len(x_coords)
                y_velocities[i]=y_velocities[i]+(y_velocities[j]-y_velocities[i])*0.125/len(x_coords)

        # Move according to velocities
        x_coords[i]=x_coords[i]+x_velocities[i]
        y_coords[i]=y_coords[i]+y_velocities[i]

    new_boids = (x_coords, y_coords, x_velocities, y_velocities)

    return(new_boids)
