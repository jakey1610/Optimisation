import pulp as plp

n = 7
m = 7
xvars = ["x1","x2","x3","x4","x5","x6","x7"]
a = [[6,7,4,9,3,8,-1],[1,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0]]
setI = range(0,n)
setJ = range(0,m)
c = [60,70,40,70,16,100,-15]
prob = plp.LpProblem(name = "q4a")
vars  = plp.LpVariable.dicts("Variables",xvars,lowBound=0,cat='Integer')
prob += plp.lpSum([c[i]*vars[xvars[i]] for i in setI])
prob += plp.lpSum([a[0][i]*vars[xvars[i]] for i in setI]) <= 20, "First"
prob += plp.lpSum([a[1][i]*vars[xvars[i]] for i in setI]) <= 1, "Second"
prob += plp.lpSum([a[2][i]*vars[xvars[i]] for i in setI]) <= 1, "Third"
prob += plp.lpSum([a[3][i]*vars[xvars[i]] for i in setI]) <= 1, "Fourth"
prob += plp.lpSum([a[4][i]*vars[xvars[i]] for i in setI]) <= 1, "Fifth"
prob += plp.lpSum([a[5][i]*vars[xvars[i]] for i in setI]) <= 1, "Sixth"
prob += plp.lpSum([a[6][i]*vars[xvars[i]] for i in setI]) <= 1, "Seventh"
prob.sense = plp.LpMaximize
prob.solve()
print([x.value() for x in prob.variables()])
print(prob.objective.value())
