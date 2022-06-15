%   generating part
1 { move(D,P,T) : disk(D), peg(P) } 1 :- T = 1..moves.

%   defining part
move(D,T)           :- move(D,_,T).
on(D,P,0)           :- init_on(D,P).
on(D,P,T)           :- move(D,P,T).
on(D,P,T+1)         :- on(D,P,T), not move(D,T+1), T < moves.
blocked(D-1,P,T+1)  :- on(D,P,T), T < moves.
blocked(D-1,P,T)    :- blocked(D,P,T), disk(D).


%   testing part
:- move(D,P,T), blocked(D-1,P,T).
:- move(D,T), on(D,P,T-1), blocked(D,P,T).
:- not 1 { on(D,P,T) } 1, disk(D), T = 1..moves.

:- goal_on(D,P), not on(D,P,moves).

%   displaying part
#show move/3.
