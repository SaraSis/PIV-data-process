# PIV-data-process
Some codes used to process the fluid experiments data aquried by PIV(Particle Image Velocimetry) sysytem

**Input file**:

the .mat file exported from the PIVlab on MATLAB

**Output results**:
1. the time-avereaged velocity
2. the turbulent velocity
3. the turbulent kinetic energy dissipation rate

**---to be continued---**


## Source Code Description

*Velocity.py*:  

            load mat file and calculate the velocity

*Smooth.py*:  
            
            define a moving average function

            the median average algorithm is used here
            
            require input as 1-d array and the output is a 1-d array, too 
            
*DissipationRate.py*:  
                     
            define a function to compute the turbulent kinetic energy dissipation rate
              
            need the turbulent velocity as input (a 3-d array here)
                     
            the output is a 3-d array of the dissipation rate
