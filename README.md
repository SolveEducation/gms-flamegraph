# Generate flamegraph from Game Maker Studio profiler

View profiler output as a flamegraph to gain insights into your game's performance.

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
