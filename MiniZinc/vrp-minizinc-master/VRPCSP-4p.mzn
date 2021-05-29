%------------------------------------------------------------------------------%
% vrp.mzn
% Jakob Puchinger
% July 2009
% vim: ft=zinc ts=4 sw=4 et tw=0
%------------------------------------------------------------------------------%

    % The number of Nodes, Node 0 corresponds to the depot
int: N;
    % Maximum number of vehicles
int: K;    
    % Distances between the nodes
array[1..N+1, 1..N+1] of int: Distance;
    % is arc ij part of a route and if so what route?
array[0..N, 0..N] of var 0..K: x;
    % Wether a node has a route from a depot
array[1..N] of var 0..N: attached;
    % a node is attached if it has an arc from the depot to it.
constraint
   forall(j in 1..N)(
       x[0,j]>0 -> attached[j] = 1);
     % A node is attached if there is an arc from an attached node to it.    
constraint
  forall(j in 1..N, i in 1..N)(
    x[i,j]>0 /\ attached[i]>0 -> attached[j] = attached[i] + 1);
    % A node is not attached if it is not connected to the depot, nor to another connected arc.
constraint
  forall(j in 1..N)(
      count(i in 1..N)(x[i,j]>0 /\ attached[i]>0) = 0 /\ x[0,j]=0 -> attached[j]=0);
    % All nodes need to be attached.
constraint
   forall(i in 1..N)(
       attached[i] > 0);
    %if a node has an inbound arc, the outbound arc must be of the same route.
constraint
   forall(i in 0..N, j in 1..N, l in 0..N)(
       x[i,j]>0 -> x[j,l] = x[i,j] \/ x[j,l] = 0);
    % arcs from a node to the same node are not possible.
constraint
   forall(i in 0..N)(
       x[i,i]=0);
   
    % Indegree constraints
constraint
    forall(j in 1..N)(
        count(i in 0..N)(x[i,j]!=0) = 1
    );
    
    % Outdegree constraints
constraint
    forall(i in 1..N)(
        count(j in 0..N)(x[i,j]!=0) = 1
    );

    % Indegree Depot
constraint
    M <= K;

    % Outdegree Depot
constraint
    count(j in 1..N)(x[0, j]!=0) <= K;
    
    % as many routes enter as leave from the depot
 constraint
    M = count(j in 1..N)(x[0, j]!=0);
   
    %remove symetry (solutions with the same routes driven by different vehicles are no longer possible) 
constraint
    forall(i in 1..N)(
        x[0, i] > 1 -> count(j in 1..i)(x[0, j] = x[0, i]-1)=1); 
         
    % Amount of vehicles used = amount of arcs leaving the depot 
var int: M =
    count(i in 1..N)(x[i, 0]!=0);
    
    % Longest route
var opt int: maxL =
    max(k in 1..M)(sum(i,j in 0..N)(if x[i,j]=k then Distance[i+1,j+1] else 0 endif));

var float: objective =
    0.5*M*maxL; 
    
solve 
    minimize objective;

output [
    "x = ", show(x), "\n",
    "objective = ", show(objective),"\n"
];