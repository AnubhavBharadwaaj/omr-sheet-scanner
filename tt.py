import cv2
import numpy as np
import imutils
img = cv2.imread('New Doc 2018-03-24 \(1\)_1.jpg',0)
height,width=img.shape
if(height>width):
    M = cv2.getRotationMatrix2D((width/2,height/2),90,1)
    img = cv2.warpAffine(img,M,(width,height))

l_ver=[]
di=0
st_ver=0
f=0
for i in range(img.shape[1]):
	for j in range(img.shape[0]):
		l_ver=[]
		if f==0 and img[j][i]!=255:
			f=1-f
			st_ver=j
		if(img[j][i]!=255):
			l_ver.append(j)
	for k in range(0,len(l_ver),2):
		if(di<=l_ver[k+1]-l_ver[k]):
			di=l_ver[k+1]-l_ver[k]
di2=0
st_hor=0
f=0
l_hor=[]
for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		if f==0 and img[i][j]!=255:
			f=1-f
			st_hor=j
		if img[i][j]!=255:
			l_hor.append(j)
	for k in range(0,len(l_hor),2):
		if(di2<=l_hor[k+1]-l_hor[k]):
			di2=l_hor[k+1]-l_hor[k]
f=0
en_hor=0
for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		if f==0 and img[i][img.shape[1]-1-j]!=255:
			 f=1-f
			 en_hor=img.shape[1]-1-j
			 break
	if f==1:
		break
f=0
en_ver=0
for i in range(img.shape[1]):
	for j in range(img.shape[0]):
		if f==0 and img[img.shape[0]-j-1][i]!=255:
			en_ver=img.shape[0]-j-1
			f=1-f
			break	
	if f==1:
		break
co=[]
res=[]
for i in range(st_hor,en_hor-di+1,di*1.5):
	ar=[]
	ke=1
	mi=0
	ans=-1
	for j in range(st_ver,en_ver-di2+1,di2*1.5):
		f=0
		a1=st_hor
		a2=st_ver
		a3=0
		a4=0
		for k1 in range(i,i+di):
			for k2 in range(j,j+di2):
				if(img[k1][k2]!=255):
					f=1
					a3=k1
					a4=k2
		if mi>=((a4-a2)*(a3-a1)):
			mi=(a4-a2)*(a3-a1)
			ans=ke
		ke++;
	res.append(ans)

print(res)
