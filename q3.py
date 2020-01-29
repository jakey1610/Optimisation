import pulp as plp
n = 7
m = 8
xvars = ["x1","x2","x3","x4","x5","x6","x7"]
a = [[0,-1,-1,2,0,0,0],[-1,0,-1,0,2,0,0],[-1,-1,0,0,0,2,0],[-1,-1,-1,0,0,0,3],[-1,-1,-1,2,2,2,3],[1,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0]]
setI = range(1,n+1)
setJ = range(1,m+1)
c = [0,0,0,10,15,25,25]

prob = plp.LpProblem(name = "q3")
vars  = plp.LpVariable.dicts("Variables",xvars,lowBound=0,cat='Integer')
prob += plp.lpSum([c[i-1]*vars[xvars[i-1]] for i in setI])
prob += plp.lpSum([a[0][i-1]*vars[xvars[i-1]] for i in setI]) <= 2, "First"
prob += plp.lpSum([a[1][i-1]*vars[xvars[i-1]] for i in setI]) <= 2, "Second"
prob += plp.lpSum([a[2][i-1]*vars[xvars[i-1]] for i in setI]) <= 2, "Third"
prob += plp.lpSum([a[3][i-1]*vars[xvars[i-1]] for i in setI]) <= 3, "Fourth"
prob += plp.lpSum([a[4][i-1]*vars[xvars[i-1]] for i in setI]) == 0, "Correct Units"
prob += plp.lpSum([a[5][i-1]*vars[xvars[i-1]] for i in setI]) <= 10, "Max Cyan"
prob += plp.lpSum([a[6][i-1]*vars[xvars[i-1]] for i in setI]) <= 5, "Max Magenta"
prob += plp.lpSum([a[7][i-1]*vars[xvars[i-1]] for i in setI]) <= 11, "Max Yellow"

prob.sense = plp.LpMaximize
prob.solve()
print(prob.objective.value())
print([vars[xvars[i-1]].value() for i in setI])
