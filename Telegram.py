n,m,c = map(int,input().split())
INF = int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]

hour =[]

count =0

for _ in range(m):
  x,y,z = map(int,input().split())
  graph[x][y]=z

for c in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b],graph[a][c]+graph[c][b]) 


# print()
for i in range(1,n+1):
  for j in range(1,n+1):
    # print(graph[i][j],end=' ')
    if graph[i][j]!=INF:
      count+=1
      hour.append(graph[i][j])
  # print()

print(count,max(hour))