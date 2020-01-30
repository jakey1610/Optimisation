import pulp as plp

n = 6
m = 1
xvars = ["x1","x2","x3","x4","x5","x6"]
a = [[6,7,4,9,3,8]]
setI = range(0,n)
setJ = range(0,m)
c = [60,70,40,70,16,100]
prob = plp.LpProblem(name = "q4a")
vars  = plp.LpVariable.dicts("Variables",xvars,lowBound=0,upBound=1,cat='Integer')
prob += plp.lpSum([c[i]*vars[xvars[i]] for i in setI])
prob += plp.lpSum([a[0][i]*vars[xvars[i]] for i in setI]) <= 20, "First"

prob.sense = plp.LpMaximize
prob.solve()
print([x.value() for x in prob.variables()])
print(prob.objective.value())
