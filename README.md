# Generate flamegraph from Game Maker Studio profiler

View profiler output as a flamegraph to gain insights into your game's performance.

### Input profile csv file:
```
name,time,calls,step %
A,273,1,0,001 %
      B,125,1,0,000 %
            C,102,1,0,000 %
                  D,16,10,0,000 %
                  E,5,1,0,000 %
                  F,3,1,0,000 %
                  G,3,1,0,000 %
                  H,2,1,0,000 %
                  I,2,1,0,000 %
J,101,1,0,000 %
      K,78,1,0,000 %
            L,11,1,0,000 %
                  M,6,1,0,000 %
            N,7,1,0,000 %
            O,4,1,0,000 %
            P,2,1,0,000 %
            Q,2,1,0,000 %
```

### Output flamegraph:
<img src="https://raw.githubusercontent.com/SolveEducation/gms-flamegraph/master/sample-profile.svg">

## Prerequisites

Docker is required to build and run the application.

Once installed, open a shell and check that the following command executes without error.
```
docker --version
```

## Building the application

Either git clone or download a zip of the repo by clicking on the 'Clone or download' button.

Open a shell and navigate to the local copy of the repo.

Execute the following command to build the application.

```
docker build -t gms-flamegraph .
```

This builds a docker image named gms-flamegraph.

## Running the application

The application reads a GMS profile csv from standard input and write a flamegraph svg to standard output.

Note that the profile csv should be generated using 'total time' and 'tree' view.

The following command generates the flamegraph from the sample-profile.csv provided in this repo.

```
docker run -i gms-flamegraph < sample-profile.csv > sample-profile.svg
```

## Viewing the flamegraph

The generated flamegraph svg can be viewed in a browser.

## Acknowledgment

* [FlameGraph](https://github.com/brendangregg/FlameGraph)
* [Solve Education!](https://solveeducation.org/)
