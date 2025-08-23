def minimumArea(grid):
    hs,he,ws,we = -1
    area = float("inf")
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                hs = min(hs,i)
                he = max(he,i)
                ws = min(ws,j)
                we = max(we,j)
        area =  min(area,((he-hs)+1)*((we-ws)+1)) 
    return area          
