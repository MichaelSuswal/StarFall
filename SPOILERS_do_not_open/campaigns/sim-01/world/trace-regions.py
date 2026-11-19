import json, math, numpy as np, cv2
from scipy.spatial import cKDTree
S="/home/claude/starfall/SPOILERS_do_not_open/campaigns/sim-01"
N=1024
COAST=[(0,722),(40,728),(95,745),(140,775),(150,830),(135,870),(200,880),(300,888),(400,884),(500,884),(560,880),(640,872),(700,855),(760,838),(800,835),(850,810),(900,772),(960,762),(1024,757)]
def ell(cx,cy,rx,ry,n=28): return [(round(cx+rx*math.cos(2*math.pi*i/n)),round(cy+ry*math.sin(2*math.pi*i/n))) for i in range(n)]
ENNER=ell(527,490,128,68); SERE=ell(875,357,62,17); BRINE=ell(297,250,52,14)
# id: (name, terrain, notes, [seeds])
L={
"skarn-west":("the Wester Skarn","mountain, snow range","",[(60,70),(170,70)]),
"skarn-sallow":("the Sallow Skarn","mountain, snow range","",[(290,75)]),
"skarn-high":("the High Skarn","mountain, the highest of the range","",[(420,60),(500,50),(585,70)]),
"skarn-east":("the Easter Skarn","mountain, snow range","",[(690,80)]),
"vorn":("Vorn","mountain, one bare dry peak standing apart","No springs on it. The Abiders' mountain.",[(812,78)]),
"skarn-far":("the Far Skarn","mountain, snow range","",[(940,85)]),
"underskarn-west":("the Wester Underskarn","hill, brown foothills","",[(90,165),(190,165)]),
"underskarn":("the Underskarn","hill, brown foothills","The foothill track from the Sallow to Stair runs here.",[(320,170),(410,165)]),
"stair-heights":("the Stair Heights","mountain, bare rock and snow above a valley head","g1-stone lands here.",[(508,150)]),
"stair":("Stair","valley, steep and terraced, pine on the slopes","The Stairfolk.",[(532,200)]),
"hask":("Hask","valley, steep, empty","Dead since the Winter of the Shut Stair.",[(585,190)]),
"upper-ennvale":("Upper Ennvale","valley, widening, pine and meadow","",[(545,255)]),
"ennvale":("Ennvale","valley, broad river meadow","",[(505,340)]),
"skarnwood":("the Skarnwood","forest, conifer under the range","",[(660,170),(730,165)]),
"deep-dimmet":("the Deep Dimmet","forest, dense dark conifer","",[(850,180),(960,180)]),
"easter-dimmet":("the Easter Dimmet","forest, dense dark conifer","",[(985,268)]),
"hallwood":("Hallwood","forest, conifer with birch","",[(790,255)]),
"wester-dimmet":("the Wester Dimmet","forest, dense dark conifer","",[(680,245)]),
"edge":("the Edge","forest, birch and pine giving out onto grass","g7-beasts lands here. The Edgefolk.",[(800,303)]),
"wester-edge":("the Wester Edge","forest, forest edge","",[(735,318),(660,305)]),
"easter-edge":("the Easter Edge","forest, forest edge","",[(862,305),(935,312)]),
"sere-grass":("the Sere Grass","steppe, pale grass round a salt lake","Tarsk wintering ground.",[(875,395),(795,352),(968,358)]),
"wester-grass":("the Wester Grass","steppe, open grass","",[(690,360),(730,400)]),
"high-grass":("the High Grass","steppe, open rolling grass","",[(850,450),(950,440)]),
"far-grass":("the Far Grass","steppe, dry open grass","",[(990,500)]),
"south-grass":("the South Grass","steppe, grass going to scrub","",[(790,520),(845,505)]),
"north-moors":("the North Moors","highland, upland moor","",[(120,215),(55,230),(200,225)]),
"sallow":("the Sallow","highland, a pale salt basin with a brine mere","The Sallowmen.",[(297,250),(250,246),(345,254),(297,232),(297,268)]),
"sallowdown":("Sallowdown","plain, dry gold grassland","",[(345,305),(310,320)]),
"harrow-fell":("Harrow Fell","hill, a bare massif standing alone","",[(400,255)]),
"dun-levels":("the Dun Levels","plain, dun grass and scattered wood","",[(440,310),(470,262)]),
"pass-tops":("the Pass Tops","highland, bare tops and a notch","The Carrow Pass and the slab cairns.",[(248,271)]),
"carrow":("Carrow","valley, a long upland valley, birch on the floor","The player lands at its head. The Carrowfolk.",[(235,297)]),
"windlow":("Windlow Moor","highland, bare ridge moor","The High Road and the Shut House.",[(203,292)]),
"carrowfoot":("Carrowfoot","valley, the valley's lower end, opening south-east","",[(252,326)]),
"broken-hills":("the Broken Hills","hill, broken hills and long valleys","",[(150,320),(190,348)]),
"far-moors":("the Far Moors","highland, upland moor","",[(50,310),(105,280)]),
"wend-heads":("the Wend Heads","hill, stream heads and rough pasture","",[(278,362)]),
"wendvale":("Wendvale","valley, a river valley between wood and hill","",[(288,425),(284,398)]),
"moorfoot":("Moorfoot","hill, the moor's southern skirts","",[(130,372),(215,385)]),
"holt":("the Holt","forest, old dark wood","",[(180,440),(225,468)]),
"wester-holt":("the Wester Holt","forest, old dark wood","",[(55,440),(112,425)]),
"corr-gorge":("the Corr Gorge","hill, water-cut cliffs","",[(297,470)]),
"corrford":("Corrford","valley, a stony ford below a gorge","g2-law lands here. The Sworn.",[(298,520)]),
"rust-hills":("the Rust Hills","hill, red broken hills","",[(150,540),(230,545)]),
"wester-breaks":("the Wester Breaks","hill, red broken hills","",[(50,560),(60,650)]),
"low-breaks":("the Low Breaks","hill, red broken hills falling to the south","",[(170,640),(255,625)]),
"corr-plain":("the Corr Plain","plain, stony flood plain, shifting channels","",[(322,572),(338,615)]),
"wester-ennerwold":("the Wester Ennerwold","hill, old worn hills, the bowl's west rim","Ennermere.",[(362,465),(352,520)]),
"norther-ennerwold":("the Norther Ennerwold","hill, old worn hills, the bowl's north rim","Ennermere. The Sighting Stones and the Leaf Halls.",[(450,390),(600,335),(575,395)]),
"easter-ennerwold":("the Easter Ennerwold","hill, old worn hills, the bowl's east rim","Ennermere.",[(690,430),(705,520)]),
"lave-rim":("the Lave Rim","hill, old worn hills, the bowl's south-east rim","Ennermere. The Sworn Door.",[(640,585)]),
"sarn-rim":("the Sarn Rim","hill, old worn hills, the bowl's south-west rim","Ennermere. The Ringing Stair.",[(430,585)]),
"gap-of-enner":("the Gap of Enner","valley, the one low way through the south rim","Ennerhold.",[(541,582)]),
"murk-shore":("the Murk Shore","coast, low shore of a foggy bay","",[(60,700),(118,728)]),
"sarnvale":("Sarnvale","valley, a slow brown river in wet meadow","The Ribs.",[(300,685),(252,702)]),
"cuts":("the Cuts","marsh, raised islands, cuts and causeways","g3-song lands here. The Cutfolk.",[(230,746)]),
"sarnmoss":("the Sarnmoss","marsh, reed, alder and standing water","",[(205,802),(262,822)]),
"murk-strand":("the Murk Strand","coast, fogbound beach and dune","",[(162,828)]),
"sarnmouth":("Sarnmouth","coast, a river mouth among sandbars","The Three Havens.",[(312,862)]),
"westwild":("the Westwild","forest, uncut scrub and wood","",[(368,720),(378,800)]),
"scrub-coast":("the Scrub Coast","coast, low wooded shore","",[(395,862)]),
"maundhead":("the Maundhead","valley, springs and the young river below the Gap","",[(515,618)]),
"upper-plain":("the Upper Plain","plain, dark farmland","",[(445,665),(565,662)]),
"bankland":("the Bankland","plain, deep black soil on both banks of a broad river","g4-harvest lands here. The Bankfolk.",[(493,750)]),
"wester-plain":("the Wester Plain","plain, dark farmland going to scrub","",[(425,745)]),
"easter-plain":("the Easter Plain","plain, dark farmland","The Three Bins.",[(555,795),(640,800)]),
"barrow-down":("Barrow Down","hill, one great lone hill on the plain","",[(590,738)]),
"low-plain":("the Low Plain","plain, dark farmland, ditched","Maundsea's own land.",[(468,828),(532,838)]),
"maundsea":("Maundsea","coast, a river mouth and a city's shore","",[(502,868)]),
"wester-long-coast":("the Wester Long Coast","coast, long pale beaches","",[(640,850)]),
"midhills":("the Midhills","hill, low wild hills between two rivers","",[(640,722)]),
"lave-heads":("the Lave Heads","hill, stream heads under the rim","The Dry Loft.",[(682,650)]),
"lavedale":("Lavedale","valley, a quiet river in settled low country","g6-dreams lands here. The Lavefolk.",[(745,737)]),
"easter-lave-hills":("the Easter Lave Hills","hill, gentle hills","",[(795,712)]),
"wester-lave-hills":("the Wester Lave Hills","hill, gentle hills","",[(692,775)]),
"braidvale":("Braidvale","valley, a braided gravel river","",[(805,640),(862,700)]),
"lavemouths":("the Lavemouths","marsh, delta marsh of many mouths","",[(815,800),(868,772)]),
"pans-coast":("the Pans Coast","coast, long beaches and pale salt pans","Whitepans.",[(950,742)]),
"easter-marches":("the Easter Marches","plain, grass and thorn between steppe and river country","",[(760,598),(838,588)]),
"norther-folds":("the Norther Folds","hill, low rounded hills","The Debt Door.",[(900,552)]),
"folds":("the Folds","valley, a middling river folded round by low hills","g5-fate lands here. The River Households.",[(940,611)]),
"souther-folds":("the Souther Folds","hill, low rounded hills","",[(975,700),(912,655)]),
"ishe-reach":("Ishe Reach","valley, the lower river, widening eastward","",[(1005,640)]),
}
SEA={"murk":("the Murk","sea, a shallow fogbound bay","",[(50,820),(60,950)]),
"south-water-west":("the Wester South Water","sea","",[(250,960)]),
"south-water":("the South Water","sea","",[(520,960)]),
"south-water-east":("the Easter South Water","sea","",[(770,940)]),
"east-water":("the East Water","sea","",[(960,880)])}
ids=list(L)+list(SEA)+["lake-enner","lake-sere"]
def tree(d):
    pts=[];lab=[]
    for k,v in d.items():
        for s in v[3]: pts.append(s); lab.append(ids.index(k))
    return cKDTree(pts),np.array(lab)
yy,xx=np.mgrid[0:N,0:N]; P=np.c_[xx.ravel(),yy.ravel()]
tl,ll=tree(L); ts,ls=tree(SEA)
lab=ll[tl.query(P)[1]].reshape(N,N)
seam=np.zeros((N,N),np.uint8); cv2.fillPoly(seam,[np.array(COAST+[(1024,1024),(0,1024)],np.int32)],1)
slab=ls[ts.query(P)[1]].reshape(N,N); lab[seam==1]=slab[seam==1]
for nm,poly in (("lake-enner",ENNER),("lake-sere",SERE)):
    m=np.zeros((N,N),np.uint8); cv2.fillPoly(m,[np.array(poly,np.int32)],1); lab[m==1]=ids.index(nm)
meta=dict(L); meta.update(SEA)
meta["lake-enner"]=("Lake Enner","sea, a great dark still lake in a bowl of hills","The point under the star. The hoarder.",[])
meta["lake-sere"]=("Lake Sere","sea, a white-rimmed salt lake","Held by the Tarsk.",[])
regions=[];bad=[]
# pad so contours on the border close on the frame
for i,k in enumerate(ids):
    m=(lab==i).astype(np.uint8)
    n,cc=cv2.connectedComponents(m)
    if n>2:
        sizes=[(cc==j).sum() for j in range(1,n)]; bad.append((k,sizes))
    big=cv2.copyMakeBorder(m,1,1,1,1,cv2.BORDER_CONSTANT,value=0)
    cs,_=cv2.findContours(big,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    c=max(cs,key=cv2.contourArea)
    a=cv2.approxPolyDP(c,1.2,True).reshape(-1,2)-1
    # contour runs through pixel centres; push the frame-touching vertices out to the frame
    poly=[[int(0 if x<=0 else (N if x>=N-1 else x)),int(0 if y<=0 else (N if y>=N-1 else y))] for x,y in a]
    nm,ter,notes,_=meta[k]
    r={"id":k,"name":nm,"terrain":ter,"polygon":poly}
    if notes: r["notes"]=notes
    regions.append(r)
print("regions",len(regions),"fragments",bad)
F=[]
def f(id,name,type,shape,coords,regs,notes=""):
    d={"id":id,"name":name,"type":type,"shape":shape,"coords":[list(c) for c in coords],"regions":regs}
    if notes: d["notes"]=notes
    F.append(d)
exec(open("features.py").read())
world={"campaign":"sim-01","painting":{"size":[N,N],"miles_per_pixel":1.6,"grid_cell_px":128},"regions":regions,"features":F,"layers":LAYERS,"landings":LANDINGS}
json.dump(world,open(S+"/map.json","w"),indent=1)
np.save("lab.npy",lab); json.dump(ids,open("ids.json","w"))
# check features against regions
rid={r["id"] for r in regions}
for x in F+[y for l in LAYERS for y in l["features"]]:
    for r in x["regions"]:
        if r not in rid: print("BAD REGION",x["id"],r)
    if x["shape"]=="point":
        px,py=x["coords"][0]; actual=ids[lab[min(py,N-1),min(px,N-1)]]
        if actual not in x["regions"]: print("POINT",x["id"],"is in",actual,"not",x["regions"])
print("features",len(F))
