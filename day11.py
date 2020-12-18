#!/usr/bin/env python3

rows = list(map(lambda x: list(x),open("11test.in", "r").read().split("\n")[:-1]))
changed = False
for i in range(7):
    new_rows = rows.copy()
    for idx, row in enumerate(rows):
        for sidx, seat in enumerate(row):
            if(seat == "#"):
                adjacent_seats = 0
                adj_dy1 = False
                adj_dy2 = False
                adj_dy3 = False
                adj_dy4 = False
                adj_y1 = False
                adj_x1 = False
                adj_y2 = False
                adj_x2 = False

                if(idx == 0):
                    adj_y2 = rows[idx+1][sidx] == "#"
                    if(sidx == 0):
                        adj_x2 = row[sidx+1] == "#"
                        adj_dy2 = rows[idx+1][sidx+1] == "#"
                    elif(sidx == len(row)-1):
                        adj_x1 = row[sidx-1] == "#"
                        adj_dy1 = rows[idx+1][sidx-1] == "#"
                    else:
                        adj_x1 = row[sidx-1] == "#"
                        adj_x2 = row[sidx+1] == "#"
                        adj_dy1 = rows[idx+1][sidx-1] == "#"
                        adj_dy2 = rows[idx+1][sidx+1] == "#"
                elif(idx == len(rows)-1):
                    adj_y1 = rows[idx-1][sidx] == "#"
                    if(sidx == 0):
                        adj_x2 = row[sidx+1] == "#"
                        adj_dy4 = rows[idx-1][sidx+1] == "#"
                    elif(sidx == len(row)-1):
                        adj_x1 = row[sidx-1] == "#"
                        adj_dy3 = rows[idx-1][sidx-1] == "#"
                    else:
                        adj_x1 = row[sidx-1] == "#"
                        adj_x2 = row[sidx+1] == "#"
                        adj_dy3 = rows[idx-1][sidx-1] == "#"
                        adj_dy4 = rows[idx-1][sidx+1] == "#"
                elif(sidx == 0):
                    adj_x2 = row[sidx+1] == "#"
                    adj_y1 = rows[idx-1][sidx] == "#"
                    adj_y2 = rows[idx+1][sidx] == "#"
                    adj_dy4 = rows[idx-1][sidx+1] == "#"
                    adj_dy2 = rows[idx+1][sidx+1] == "#"
                elif(sidx == len(row)-1):
                    adj_x1 = row[sidx-1] == "#"
                    adj_y1 = rows[idx-1][sidx] == "#"
                    adj_y2 = rows[idx+1][sidx] == "#"
                    adj_dy3 = rows[idx-1][sidx-1] == "#"
                    adj_dy1 = rows[idx+1][sidx-1] == "#"
                else:
                    adj_x1 = row[sidx-1] == "#"
                    adj_x2 = row[sidx+1] == "#"
                    adj_y1 = rows[idx-1][sidx] == "#"
                    adj_y2 = rows[idx+1][sidx] == "#"
                    adj_dy1 = rows[idx-1][sidx-1] == "#"
                    adj_dy2 = rows[idx-1][sidx+1] == "#"
                    adj_dy3 = rows[idx+1][sidx-1] == "#"
                    adj_dy4 = rows[idx+1][sidx+1] == "#"

                list_of_bools = [adj_dy1,adj_dy2,adj_dy3,adj_dy4,adj_y1,adj_y2,adj_x1,adj_x2]
                adjacent_seats = list_of_bools.count(True)
                if(adjacent_seats >= 4):
                    new_rows[idx][sidx] = "L"
            elif(seat == "L"):
                adj_dy1 = None
                adj_dy2 = None
                adj_y = None
                adj_x = None

                if(idx == 0):
                    adj_y = rows[idx+1][sidx] != "#"
                    if(sidx == 0):
                        adj_x = row[sidx+1] != "#"
                        adj_dy1 = rows[idx+1][sidx+1] != "#"
                        adj_dy2 = True
                    elif(sidx == len(row)-1):
                        adj_x = row[sidx-1] != "#"
                        adj_dy1 = rows[idx+1][sidx-1] != "#"
                        adj_dy2 = True
                    else:
                        adj_dy1 = rows[idx+1][sidx-1] != "#" and rows[idx+1][sidx+1] != "#"
                        adj_dy2 = True
                elif(idx == len(rows)-1):
                    adj_y = rows[idx-1][sidx] != "#"
                    if(sidx == 0):
                        adj_x = row[sidx+1] != "#"
                        adj_dy1 = True
                        adj_dy2 = rows[idx-1][sidx+1] != "#"
                    elif(sidx == len(row)-1):
                        adj_x = row[sidx-1] != "#"
                        adj_dy1 = True
                        adj_dy2 = rows[idx-1][sidx-1] != "#"
                    else:
                        adj_dy1 = True
                        adj_dy2 = rows[idx-1][sidx-1] != "#" and rows[idx-1][sidx+1] != "#"
                elif(sidx == 0):
                    adj_x = row[sidx+1] != "#"
                    adj_y = rows[idx-1][sidx] != "#" and rows[idx+1][sidx] != "#"
                    adj_dy1 = rows[idx-1][sidx+1] != "#"
                    adj_dy2 = rows[idx+1][sidx+1] != "#"
                elif(sidx == len(row)-1):
                    adj_x = row[sidx-1] != "#"
                    adj_y = rows[idx-1][sidx] != "#" and rows[idx+1][sidx] != "#"
                    adj_dy1 = rows[idx-1][sidx-1] != "#"
                    adj_dy2 = rows[idx+1][sidx-1] != "#"
                else:
                    adj_x = row[sidx-1] != "#" and row[sidx+1] != "#"
                    adj_y = rows[idx-1][sidx] != "#" and rows[idx+1][sidx] != "#"
                    adj_dy1 = rows[idx-1][sidx-1] != "#" and rows[idx-1][sidx+1] != "#"
                    adj_dy2 = rows[idx+1][sidx-1] != "#" and rows[idx+1][sidx+1] != "#"

                if(adj_x and adj_y and adj_dy1 and adj_dy2):
                    new_rows[idx][sidx] = "#"
            else:
                pass
    rows = new_rows.copy()
print(rows)
