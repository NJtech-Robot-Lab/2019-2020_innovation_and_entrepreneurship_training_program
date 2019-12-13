import math
#本地图使用一个装着点的列表来表示整张地图
points=[]

tree=[]#用这个列表装最终的查询结果

#运动方向的元组
direct=([1,0],[0,1],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1])

#初始化地图函数
def ini(points,x,y):
    for i in range(1,x+1):
        for j in range(1,y+1):
            new_point={'x':i,'y':j,'value':1}
            points.append(new_point)
            
#设置地图障碍物的函数
def setbound(points,x,y):
    for point in points:
        if point['x']==x and point['y']==y:
            point['value']=0

#查询某个点的周围的点
def checkpoint(Bpoints,x,y,Apoints):
    global direct
    centerpoint={'x':x,'y':y,'value':1}
    if centerpoint in Bpoints:
        for i in range(0,8):#遍历8个方向
            ex=x+direct[i][0]
            ey=y+direct[i][1]
            temp={'x':ex,'y':ey,'value':1}
            if temp in Bpoints:#如果这个方向有这个点，并且填入
                    insert(x,y,ex,ey,Apoints)

#将某个点插入到Apoint当中去
def insert(x,y,ex,ey,Apoints):
    global endx
    global endy
    newpoint={'x':ex,'y':ey,'H':math.sqrt(abs((x-ex)*10.0)**2+abs((y-ey)*10.0)**2),'P':abs(ex-endx)*10.0+abs(ey-endy)*10.0,'use':1}
    if len(Apoints)==0:
        Apoints.append(newpoint)
    fla=0
    for i in range(0,len(Apoints)):
        if(Apoints[i]['x']==ex and Apoints[i]['y']==ey):
            #如果存在这个点的话
            fla=1#不需要插入
            if(math.sqrt(abs((x-ex)*10.0)**2+abs((y-ey)*10.0)**2)+abs(ex-endx)*10.0+abs(ey-endy)*10.0<Apoints[i]['H']+Apoints[i]['P']):
                   Apoints[i]['H']=math.sqrt(abs((x-ex)*10.0)**2+abs((y-ey)*10.0)**2)
                   Apoints[i]['P']=abs(ex-endx)*10.0+abs(ey-endy)*10.0
                   Apoints[i]['use']=1
    
    if(fla==0):#如果没找到
        Apoints.append(newpoint)
                   
   
    
#输入地图的宽度和长度
x=input('请输入地图宽度')
x=int(x)
y=input('请输入地图长度')
y=int(y)

#初始化地图
ini(points,x,y)

#输入障碍点
while 1:
    print('请输入障碍点，如果想结束输入，则xy都为-1')
    xi=input('输入障碍点的x')
    xi=int(xi)
    yi=input('输入障碍点的y')
    yi=int(yi)
    if xi==-1 and yi==-1:
        break
    setbound(points,xi,yi)#将那个点设置为障碍物

#输入起点
startx=input('请输入你的起点的x')
starty=input('请输入你的起点的y')
startx=int(startx)
starty=int(starty)

#输入终点
endx=input('请输入你的终点的x')
endy=input('请输入你的终点的y')
endx=int(endx)
endy=int(endy)

#表示已经搜索过的点集
Apoints=[]

#表示等待搜索的点集
Bpoints=points
flag=1


checkpoint(Bpoints,startx,starty,Apoints)#查询第一个点
setbound(Bpoints,startx,starty)
lastx=startx
lasty=starty

end_point={'x':endx,'y':endy,'value':1}
cnt1=0
while end_point in Bpoints:#如果终点还没有被走过,就进行循环
    #print('dosomething')
    if len(Apoints)==0:#如果没有带测点，就结束
        flag=0
        break
    cnt1=cnt1+1
    #无线循环保护器
    if cnt1==1000:
        break
    #默认最好的点是Apoint中的第一个
    minH=1000000000.000
    minx=-1
    miny=-1

    for point in Apoints:#遍历所有的A中的点，找出最好的点
        if minH>point['H']+point['P']and point['use']==1:
            minx=point['x']
            miny=point['y']
            minH=point['H']+point['P']

    print(Apoints)
    print(minx)
    print(miny)
    print(minH)
    
    #从A中去掉这个点
    cnt=len(Apoints)
    for i in range(0,cnt):
        if Apoints[i]['x']==minx and Apoints[i]['y']==miny:
            Apoints[i]['use']=0
            break
        
    checkpoint(Bpoints,minx,miny,Apoints)#查询最优点的周围的点

    #接着把minx,miny从B点去掉,并且令这个点的父节点为上一次的最佳节点
    setbound(Bpoints,minx,miny)
    new_point={'x':minx,'y':miny,'fx':lastx,'fy':lasty}
    las=0
    if(len(tree)==0):
        tree.append(new_point)
        las=1
    else:
        for i in range(0,len(tree)):
            if(tree[i]['x']==minx and tree[i]['y']==miny):
                #print('进行了覆盖')
                tree[i]['fx']=lastx
                tree[i]['fy']=lasty
                las=1
                break
    if(las==0):
        tree.append(new_point)
    lastx=minx
    lasty=miny
    
        
        
if flag==0:
    print('并不存在路径')
for i in range(1,len(tree)):
    if tree[i]['x']==4 and tree[i]['y']==4:
        print(tree[i])

print(tree)
print('成功运行')
