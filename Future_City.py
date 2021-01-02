INF = int(1e9)

n, m = map(int,input().split())

graph =[[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
  a,b = map(int,input().split())
  graph[a][b] = graph[b][a] = 1

# k 먼저, x 최종 
x, k = map(int,input().split())

# 자기 자신 
for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
      graph[a][b]=graph[b][a]=0

for c in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = graph[b][a] = min(graph[a][b],graph[a][c]+graph[c][b]) 
    

# for i in range(1,n+1):
#   for j in range(1,n+1):
#     print(graph[i][j],end=' ')
#   print()

if graph[1][k]!=INF and graph[k][x]!=INF:  
  print(graph[1][k]+graph[k][x])
else:
  print("-1")