#THE TREE OF THE ROMANIA MAP
y <- 1:13
arad  <- c(0,1,1,1,0,0,0,0,0,0,0,0,0)
sibiu <- c(1,0,0,0,1,1,0,1,0,0,0,0,0)
ti    <- c(1,0,0,0,0,0,1,0,0,0,0,0,0)
z     <- c(1,0,0,0,0,0,0,1,0,0,0,0,0)
f     <- c(0,1,0,0,0,0,0,0,1,0,0,0,0)
r     <- c(0,1,0,0,0,0,0,0,0,1,1,0,0)
l     <- c(0,0,1,0,0,0,0,0,0,0,0,1,0)
o     <- c(0,1,0,1,0,0,0,0,0,0,0,0,0)
b     <- c(0,0,0,0,1,0,0,0,0,0,1,0,0)
c     <- c(0,0,0,0,0,0,0,1,0,0,1,0,1)
p     <- c(0,0,0,0,0,1,0,0,0,1,1,0,0)
m     <- c(0,0,0,0,0,0,1,0,0,0,0,0,1)
d     <- c(0,0,0,0,0,0,0,0,0,1,0,1,0)
x     <-data.frame(arad,sibiu,ti,z,f,r,l,o,b,c,p,m,d)
#THE VISITED NODE
v<-c(0,0,0,0,0,0,0,0,0,0,0,0,0)
#ADD THE START NODE TO THE QUEUE WHICH IS ARAD
queue<-(0)
#SET THE ARAD TO BE VISITED
v[1]<-(1)
#DEQUEUE ARAD
node<-queue(0)
print(node)
vec<-13
repeat{
  for (i in vec) {
    #check if route exists and the node isn't visited
    if (matrix[node][i] && v[i]==(0)  ) {
          #VISIT NODE
          v[i]<-(1)
          #ENQUEUE NODE
          queue<-v(i)
  #WHEN QUEUE IS EMPTY THAT'S MEANS ALL THE NODE ARE VISITED
  if (length(queue)==0)
          break
  else
    #DEQUEUE ELEMENT FROM QUEUE
    node<-queue(0)
    print(node)
    }
  }
}